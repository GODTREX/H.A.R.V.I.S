import speech_recognition as sr
from datetime import datetime
import os
from playsound import playsound  # To play your MP3 files

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
        return "good_morning.mp3"  # Replace with your Good Morning audio file
    elif 12 <= current_hour < 17:
        return "good_afternoon.mp3"  # Replace with your Good Afternoon audio file
    elif 17 <= current_hour < 21:
        return "good_evening.mp3"  # Replace with your Good Evening audio file
    else:
        return "hello sir.mp3"  # Replace with your Good Night audio file

def listen():
    """Function to listen to user's voice and convert to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust to ambient noise
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            play_audio("Sorry, I didn't catch that.mp3")  # Replace with your error audio file
            return None
        except sr.RequestError:
            play_audio("Unable to connect to the service.mp3")  # Replace with your error audio file
            return None

# Start the assistant
if __name__ == "__main__":
    greeting_file = get_greeting()
    play_audio(greeting_file)
    while True:
        command = listen()
        if command:
            if "exit" in command or "bye" in command:
                play_audio("good bye.mp3")  # Replace with your Goodbye audio file
                break
            else:
                play_audio("Command acknowledged.mp3")  # Replace with a generic response audio file
