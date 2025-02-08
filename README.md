Live Speech Translator

Description

This program captures live speech, converts it into text, translates it into a target language, and then converts the translated text into speech using SpeechRecognition, Google Translate, and gTTS.

Features

Live speech recognition from the microphone.

Supports multiple languages for input and output.

Text translation using Google Translate.

Converts translated text to speech.

User-friendly interface with an option to continue or exit.

Prerequisites

Ensure you have Python 3.x installed on your system.

Installation

Clone this repository or download the script:

git clone https://github.com/your-username/live-speech-translator.git
cd live-speech-translator

Install required dependencies:

pip install SpeechRecognition googletrans==4.0.0-rc1 gTTS pyaudio

Note: If you encounter issues with pyaudio, install it using:

Windows:

pip install pipwin
pipwin install pyaudio

macOS:

brew install portaudio
pip install pyaudio

Linux:

sudo apt-get install portaudio19-dev
pip install pyaudio

Usage

Run the script using:

python main.py

Steps:

Choose the source language (the language you will speak).

Choose the target language (the language to translate into).

Speak into the microphone.

The program will:

Convert speech to text.

Translate the text.

Convert the translation into speech.

Listen to the translated speech.

Choose whether to continue or exit.

Supported Languages

Arabic (ar)

Bengali (bn)

Chinese (zh-cn)

English (en)

French (fr)

German (de)

Gujarati (gu)

Hindi (hi)

Japanese (ja)

Kannada (kn)

Korean (ko)

Malayalam (ml)

Marathi (mr)

Odia (or)

Punjabi (pa)

Russian (ru)

Spanish (es)

Tamil (ta)

Telugu (te)

Urdu (ur)

Troubleshooting

Microphone Not Detected: Ensure your microphone is connected and set as the default recording device.

No Speech Detected: Speak clearly and check your microphone sensitivity.

Translation Issues: Ensure you are connected to the internet.

Audio Playback Issues: Try opening output.mp3 manually in a media player.

License

This project is licensed under the MIT License.

Contributing

Feel free to contribute by submitting issues or pull requests!

Author

Your Name

GitHub: your-username

