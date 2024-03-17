from googletrans import Translator

import pyttsx3

engine = pyttsx3.init()

def translate_to_hindi(text):
    translator = Translator()
    translated_text = translator.translate(text, dest='hi').text
    return translated_text

if __name__ == "__main__":
    text_to_translate = input("Enter text in English: ")
    engine.say(text_to_translate)
    engine.runAndWait()


    translated_text = translate_to_hindi(text_to_translate)
    print("Translated text in Hindi:", translated_text)
    engine.say(translated_text)
    engine.runAndWait()
