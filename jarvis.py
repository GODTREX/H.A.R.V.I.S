import pyttsx3
import speech_recognition as sr
from datetime import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Configure voice settings
voices = engine.getProperty('voices')
for voice in voices:
    if "en-US" in voice.id and "David" in voice.name:  # Choose a Jarvis-like voice
        engine.setProperty('voice', voice.id)
        break
engine.setProperty('rate', 150)  # Adjust speed

def speak(text):
    """Function to make the assistant speak."""
    engine.say(text)
    engine.runAndWait()

def get_greeting():
    """Determine the greeting based on the current time."""
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 17:
        return "Good afternoon"
    elif 17 <= current_hour < 21:
        return "Good evening"
    else:
        return "Good night"

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
            speak("Sorry, I didn't catch that. Please repeat.")
            return None
        except sr.RequestError:
            speak("I'm unable to connect to the speech recognition service.")
            return None

# Start the assistant
if __name__ == "__main__":
    greeting = get_greeting()
    speak(f"{greeting}, Sir. How can I assist you today?")
    while True:
        command = listen()
        if command:
            if "exit" in command or "bye" in command:
                speak("Goodbye, Sir. Have a great day!")
                break
            else:
                speak(f"You said: {command}. I am still learning to perform tasks.")
