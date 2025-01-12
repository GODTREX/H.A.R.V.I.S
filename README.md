# HARVIS Voice-Controlled Assistant

hARVIS is a Python-based voice-controlled assistant that provides task automation features, including web browsing, system volume adjustment, and screen brightness control. It uses speech recognition and plays responses in real-time, coupled with a graphical user interface (GUI).

## Features

1. **Voice Commands**:

   - Open websites (e.g., YouTube, Google search).
   - Adjust system volume (mute, max volume, etc.).
   - Control screen brightness (increase, decrease, set maximum/minimum).
   - Custom greetings based on the time of day.
   - Quit the application with a command.

2. **GUI**:

   - Displays an interface that runs during the assistant’s operation.

3. **Introductory Video**:

   - Plays a customizable intro video before activating the assistant.

## Prerequisites

Before running JARVIS, ensure your system meets the following requirements:

1. **Python 3.7+**

   - [Download Python](https://www.python.org/downloads/)

2. **VLC Media Player**

   - Install VLC Media Player for video playback functionality.
   - [Download VLC](https://www.videolan.org/vlc/)

3. **Audio Drivers**

   - Ensure your system has proper audio drivers installed for volume adjustments.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/jarvis-assistant.git
   cd jarvis-assistant
   ```

2. Install the required Python libraries:

   ```bash
   pip install playsound speechrecognition pillow python-vlc pycaw screen-brightness-control comtypes
   ```

3. Ensure all necessary files are available:

   - **Audio Files**: Place the required audio files in the project directory (e.g., `good_morning.mp3`, `Adjusting brightness.mp3`).
   - **Video File**: Include `jarvistest.mp4` in the directory for the introductory video.

## Usage

1. Run the script:

   ```bash
   python harvis_fusion_code.py
   ```

2. Speak commands into the microphone as prompted by the assistant.

3. Available commands:

   - **"Open YouTube"**: Opens YouTube in a browser.
   - **"Search for [query]"**: Performs a Google search for the specified query.
   - **"Max volume" / "Mute volume"**: Adjusts system volume.
   - **"Bright" / "Brighter" / "Brightest"**: Increases brightness by varying levels.
   - **"Dim" / "Dimmer" / "Dimmest"**: Decreases brightness by varying levels.
   - **"Exit" or "Bye"**: Exits the application.

## File Structure

```
jarvis-assistant/
├── harvis_fusion_code.py      # Main Python script
├── jarvistest.mp4            # Intro video
├── good_morning.mp3          # Example audio file
├── Adjusting brightness.mp3  # Example audio file
└── README.md                 # Documentation
```

## Troubleshooting

1. **Missing Files**:

   - Ensure all referenced audio and video files are present in the project directory.

2. **Brightness Control Issues**:

   - Verify your system supports brightness adjustment via `screen-brightness-control`.

3. **VLC Errors**:

   - Ensure VLC Media Player is installed and accessible via your system's PATH.

## Contributing

Feel free to submit issues or contribute to the project by creating a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Thank you
