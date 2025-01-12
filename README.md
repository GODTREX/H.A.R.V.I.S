# Jarvis: Voice-Controlled Personal Assistant

## 📝 Summary
Jarvis is a Python-based voice-controlled personal assistant inspired by the AI assistant from Iron Man. It greets the user based on the time of day and executes voice commands such as opening websites, performing Google searches, and more. Jarvis can also be extended with additional features as needed.

---

## 🔍 Features
- **Greeting**: Plays a greeting based on the current time (e.g., "Good Morning," "Good Evening").
- **Voice Commands**:
  - Open websites like YouTube.
  - Perform Google searches.
  - Exit the application with a voice command.
- **Custom Voice Responses**: Plays pre-recorded MP3 files for responses.
- **Easily Extendable**: Add more commands and functionality as desired.

---

## 📋 Prerequisites
1. **Python**: Ensure Python 3.10+ is installed on your system. Download it from [python.org](https://www.python.org/).
2. **Required Libraries**: Install the following Python libraries:
   - `speech_recognition`
   - `playsound==1.2.2`
   - `datetime`
   - `webbrowser`
   - `os`

---

## 🔧 Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/jarvis.git
   cd jarvis
   ```

2. **Install Dependencies**:
   Run the following command to install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
   *(Create a `requirements.txt` file with the following content for easy setup)*:
   ```
   speechrecognition
   playsound==1.2.2
   ```

3. **Prepare Audio Files**:
   - Place your custom MP3 files in the project directory.
   - Ensure the file names match:
     - `good_morning.mp3`
     - `good_afternoon.mp3`
     - `good_evening.mp3`
     - `hello sir.mp3`
     - `Sorry, I didn't catch that.mp3`
     - `Unable to connect to the service.mp3`
     - `Command acknowledged.mp3`
     - `good bye.mp3`

4. **Run the Application**:
   Execute the following command in the terminal:
   ```bash
   python jarvis.py
   ```

---

## 🛠️ How to Use
1. Launch the application.
2. Speak clearly into your microphone.
3. Use commands such as:
   - "Open YouTube" to open YouTube in your browser.
   - "Search for Python tutorials" to perform a Google search.
   - "Exit" or "Bye" to stop the program.

---

## 🚀 Extending Jarvis
You can add more commands by modifying the `execute_command()` function in `jarvis.py`. For example:
```python
elif "open github" in command:
    webbrowser.open("https://github.com")
```

---

## 🖋️ Synopsis
Jarvis is a beginner-friendly project designed to help users explore voice recognition, audio playback, and basic Python automation. It's an ideal starting point for anyone interested in AI-powered personal assistants.

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request with your enhancements.

---

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

