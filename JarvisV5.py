#NO SOUND PLAYBACK IN INTRO

import tkinter as tk
from PIL import Image, ImageTk
import cv2  # OpenCV for video handling
import threading
from playsound import playsound
import speech_recognition as sr
import webbrowser
import os

# === Voice Assistant Logic ===
def play_audio(file_path):
    """Function to play an MP3 file."""
    if os.path.exists(file_path):
        playsound(file_path)
    else:
        print(f"Error: {file_path} not found!")

def get_greeting():
    """Determine the greeting based on the current time and return the corresponding audio file."""
    from datetime import datetime
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "good_morning.mp3"
    elif 12 <= current_hour < 17:
        return "good_afternoon.mp3"
    elif 17 <= current_hour < 21:
        return "good_evening.mp3"
    else:
        return "hello sir.mp3"

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

def execute_command(command):
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
        return True
    else:
        play_audio("Command acknowledged.mp3")
    return False

def voice_assistant():
    """Voice assistant main loop."""
    greeting_file = get_greeting()
    play_audio(greeting_file)
    while True:
        command = listen()
        if command:
            if execute_command(command):
                break

# === GUI Logic ===
def play_intro_video(video_path, root):
    """Function to play an intro video with sound."""
    cap = cv2.VideoCapture(video_path)
    video_window = tk.Toplevel(root)
    video_window.geometry("800x600")
    video_label = tk.Label(video_window)
    video_label.pack()

    # Play video and sound
    threading.Thread(target=playsound, args=(video_path,), daemon=True).start()

    while True:
        ret, frame = cap.read()
        if not ret:  # Video ended
            break

        # Convert frame to ImageTk format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (800, 600))  # Resize frame to fit window
        img = ImageTk.PhotoImage(image=Image.fromarray(frame))

        video_label.imgtk = img
        video_label.configure(image=img)
        video_window.update()

    cap.release()
    video_window.destroy()  # Close video window

def create_gui():
    """Create main GUI for Jarvis after intro video."""
    # Main GUI window
    root = tk.Tk()
    root.title("Jarvis Assistant")
    root.geometry("800x600")

    # Set background image for running Jarvis
    bg_image = ImageTk.PhotoImage(Image.open("jarvis.jpg"))  # Use a suitable background image
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    # Add a status label
    status_label = tk.Label(root, text="Jarvis is listening...", font=("Helvetica", 16), bg="black", fg="cyan")
    status_label.pack(pady=10)

    # Start voice assistant in a separate thread
    threading.Thread(target=voice_assistant, daemon=True).start()

    # Start the GUI event loop
    root.mainloop()

# Run the application
if __name__ == "__main__":
    # Main root
    main_root = tk.Tk()
    main_root.withdraw()  # Hide the main root window during intro

    # Play intro video
    play_intro_video("jarvistest.mp4", main_root)

    # Create the main Jarvis GUI
    create_gui()
