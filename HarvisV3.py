import tkinter as tk
from PIL import Image, ImageTk
import vlc  # VLC module for video playback
import threading
import os
from playsound import playsound
import speech_recognition as sr
import webbrowser
from datetime import datetime
import sys  # For exiting the program
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import math
import screen_brightness_control as sbc

# === Voice Assistant Logic ===
def play_audio(file_path):
    """Function to play an MP3 file."""
    if os.path.exists(file_path):
        playsound(file_path)
    else:
        print(f"Error: {file_path} not found!")

def get_greeting():
    """Determine the greeting based on the current time and return the corresponding audio file."""
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "good_morning.mp3"
    elif 12 <= current_hour < 17:
        return "good_afternoon.mp3"
    elif 17 <= current_hour < 21:
        return "good_evening.mp3"
    else:
        return "hello sir.mp3"

def set_brightness(level):
    """Set screen brightness to the specified level (0-100)."""
    try:
        sbc.set_brightness(level)
    except Exception as e:
        print(f"Error setting brightness: {e}")

def get_volume_interface():
    """Get the audio volume interface."""
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None
    )
    return interface.QueryInterface(IAudioEndpointVolume)

def set_volume(level):
    """Set the system volume to the specified level (0-100)."""
    level = max(0, min(100, level))  # Ensure level is within 0-100
    volume_interface = get_volume_interface()
    scalar_value = level / 100
    volume_interface.SetMasterVolumeLevelScalar(scalar_value, None)

def mute_volume():
    """Mute the system volume."""
    volume_interface = get_volume_interface()
    volume_interface.SetMasterVolumeLevelScalar(0, None)

def listen():
    """Function to listen to user's voice and convert to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            play_audio("Sorry, I didn't catch that.mp3")
            return None
        except sr.RequestError:
            play_audio("Unable to connect to the service.mp3")
            return None

def execute_command(command, root):
    """Execute tasks based on the command."""
    if "open youtube" in command:
        play_audio("Sure sir.mp3")
        webbrowser.open("https://www.youtube.com")
    elif "search for" in command:
        query = command.replace("search for", "").strip()
        play_audio("Command acknowledged.mp3")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif "open chat gpt" in command:
        play_audio("Command acknowledged.mp3")
        webbrowser.open("https://chat.openai.com")
    elif "hello" in command:
        play_audio("hello sir.mp3")
    elif "exit" in command or "bye" in command:
        play_audio("good bye.mp3")
        root.quit()  # Stop the Tkinter event loop
        sys.exit()   # Exit the program
    elif "max volume" in command:
        play_audio("maximum.mp3")
        set_volume(100)
    elif "mute volume" in command:
        play_audio("Mutingvolume.mp3")
        mute_volume()
    elif "bright" in command:
        play_audio("Adjusting brightness.mp3")
        if "brighter" in command:
            set_brightness(80)
        elif "brightest" in command:
            set_brightness(100)
        else:
            set_brightness(60)
    elif "dim" in command:
        play_audio("Adjusting brightness.mp3")
        if "dimmer" in command:
            set_brightness(20)
        elif "dimmest" in command:
            set_brightness(0)
        else:
            set_brightness(40)
    else:
        play_audio("Command acknowledged.mp3")
    return False

def voice_assistant(root):
    """Voice assistant main loop."""
    greeting_file = get_greeting()
    play_audio(greeting_file)
    while True:
        command = listen()
        if command:
            if execute_command(command, root):
                break

# === GUI Logic ===
def play_intro_video(video_path, root):
    """Play the intro video with VLC."""
    player = vlc.MediaPlayer(video_path)
    player.play()

    # Wait until the video finishes playing
    while True:
        state = player.get_state()
        if state in [vlc.State.Ended, vlc.State.Stopped, vlc.State.Error]:
            break
        root.update()

    player.stop()

def create_jarvis_gui(root):
    """Switch to Jarvis GUI after intro video."""
    for widget in root.winfo_children():
        widget.destroy()

    # Jarvis running GUI
    background = tk.Label(root, text="Jarvis is now active", font=("Helvetica", 24), bg="black", fg="cyan")
    background.pack(fill="both", expand=True)

    # Start the voice assistant in a thread
    threading.Thread(target=voice_assistant, args=(root,), daemon=True).start()

def main():
    # Initialize the main window
    root = tk.Tk()
    root.title("Jarvis Assistant")
    root.geometry("800x600")

    # Play the intro video
    play_intro_video("jarvistest.mp4", root)

    # Switch to Jarvis GUI
    create_jarvis_gui(root)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
