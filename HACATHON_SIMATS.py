import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Initialize recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

# Function to capture live speech and convert it to text
def live_speech_to_text(language='en'):
    with sr.Microphone() as source:
        print("Listening... Please speak.")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        try:
            audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds
            print("Stopped listening.")
            text = recognizer.recognize_google(audio, language=language)
            print(f"You said: {text}")
            return text
        except sr.WaitTimeoutError:
            print("No speech detected. Please try again.")
            return None
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio. Please try again.")
            return None
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
            return None

# Function to translate text to a target language
def translate_text(text, target_language='en'):
    translation = translator.translate(text, dest=target_language)
    print(f"Translated text: {translation.text}")
    return translation.text

# Function to convert text to speech
def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language)
    tts.save("output.mp3")
    print("Playing translated speech...")
    os.system("start output.mp3")  # Play the audio file (Windows)
    # For macOS/Linux, use: os.system("afplay output.mp3")

# Function to get language code from user input
def get_language_code(prompt):
    # Alphabetical list of supported languages
    language_map = {
        "arabic": "ar",
        "bengali": "bn",
        "chinese": "zh-cn",
        "english": "en",
        "french": "fr",
        "german": "de",
        "gujarati": "gu",
        "hindi": "hi",
        "japanese": "ja",
        "kannada": "kn",
        "korean": "ko",
        "malayalam": "ml",
        "marathi": "mr",
        "odia": "or",
        "punjabi": "pa",
        "russian": "ru",
        "spanish": "es",
        "tamil": "ta",
        "telugu": "te",
        "urdu": "ur",
    }
    while True:
        language = input(prompt).strip().lower()
        if language in language_map:
            return language_map[language]
        else:
            print("Unsupported language. Please try again.")

# Main function
def main():
    # Step 1: Get source and target languages from the user
    print("Supported languages:")
    print("Arabic, Bengali, Chinese, English, French, German, Gujarati, Hindi, Japanese, Kannada, Korean, Malayalam, Marathi, Odia, Punjabi, Russian, Spanish, Tamil, Telugu, Urdu")
    
    source_language = get_language_code("Enter the language you will speak (e.g., Hindi): ")
    target_language = get_language_code("Enter the language you want the translation in (e.g., French): ")

    while True:
        # Step 2: Convert live speech to text in the source language
        text = live_speech_to_text(language=source_language)
        if text:
            # Step 3: Translate the text to the target language
            translated_text = translate_text(text, target_language=target_language)
            # Step 4: Convert translated text to speech
            text_to_speech(translated_text, language=target_language)

        # Step 5: Ask the user if they want to continue
        user_input = input("\nPress 1 to continue or any other key to stop: ")
        if user_input != "1":
            print("Stopping the program. Goodbye!")
            break

if __name__ == "__main__":
    main()