#FLICKERING ISSUEEEEEEEEEE


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

# === GUI Logic with Video Background ===
def play_video(video_path, label):
    """Function to play video on a tkinter label."""
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:  # Restart video if it ends
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        # Convert frame to ImageTk format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (800, 600))  # Adjust size to fit the window
        img = ImageTk.PhotoImage(image=Image.fromarray(frame))

        # Display the frame on the label
        label.imgtk = img
        label.configure(image=img)

        # Break loop on GUI close
        if not label.winfo_exists():
            break

    cap.release()

def create_gui_with_video():
    # Initialize the main window
    root = tk.Tk()
    root.title("Jarvis Assistant")
    root.geometry("800x600")

    # Create a label to display the video
    video_label = tk.Label(root)
    video_label.pack(fill="both", expand=True)

    # Start the video playback in a separate thread
    video_thread = threading.Thread(target=play_video, args=("jarvistest.mp4", video_label), daemon=True)
    video_thread.start()

    # Add a status label
    status_label = tk.Label(root, text="Jarvis is running...", font=("Helvetica", 16), bg="black", fg="cyan")
    status_label.pack(pady=10)

    # Start the voice assistant in another thread
    threading.Thread(target=voice_assistant, daemon=True).start()

    # Start the GUI event loop
    root.mainloop()

# Run the application
if __name__ == "__main__":
    create_gui_with_video()
