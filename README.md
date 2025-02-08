# **Live Speech Translator**

## Description
The **Live Speech Translator** is a real-time speech-to-text translation tool that captures spoken language, converts it into text, translates it into a target language, and then converts it back into speech. This project uses **SpeechRecognition**, **Google Translate API**, and **gTTS** for seamless language translation.

## Features
- **Real-time speech recognition.**
- **Supports multiple languages for translation.**
- **Text-to-speech conversion for translated output.**
- **User-friendly interface with voice input.**

## Technologies Used
- **Speech Recognition:** `speechrecognition`
- **Translation:** `googletrans`
- **Text-to-Speech:** `gtts`
- **Python Version:** 3.x

## Requirements
- **Python 3.x**
- **speechrecognition**
- **googletrans**
- **gtts**
- **pyaudio** (for microphone input)


Install dependencies:
bash
Copy
Edit
pip install speechrecognition googletrans==4.0.0-rc1 gtts pyaudio
Usage
Run the program:

bash
Copy
Edit
python translator.py
Select input and output languages:

The program prompts you to choose a language for speech input.
Choose the target language for translation.
Start speaking:

The application will listen to your voice, convert it to text, and translate it.
The translated text is then spoken aloud using gTTS.
Supported Languages
English, Hindi, French, Spanish, German, Chinese, Japanese, Korean, Arabic, Tamil, Telugu, and more.
Troubleshooting
If the microphone is not working, ensure pyaudio is installed correctly.
If translation fails, check your internet connection as googletrans requires an active connection.
Use:
bash
Copy
Edit
pip install --upgrade googletrans
if translation issues persist.
License
This project is licensed under the MIT License.

Author
Jhanesh V
📧 jhaneshvanka@gmail.com
🌐 GitHub Profile

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/live-speech-translator.git
   cd live-speech-translator
