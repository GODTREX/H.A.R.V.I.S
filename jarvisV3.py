import speech_recognition as sr
from datetime import datetime
import os
from playsound import playsound  # To play your MP3 files
import webbrowser  # To handle web browsing

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
        webbrowser.open("https://chat.openai.com/")  # Correct URL for ChatGPT
    elif "hello" in command:
        play_audio("hello sir.mp3")
    elif "exit" in command or "bye" in command:
        play_audio("good bye.mp3")
        return True
    else:
        play_audio("Command acknowledged.mp3")
    return False

# Start the assistant
if __name__ == "__main__":
    greeting_file = get_greeting()
    play_audio(greeting_file)
    while True:
        command = listen()
        if command:
            if execute_command(command):
                break