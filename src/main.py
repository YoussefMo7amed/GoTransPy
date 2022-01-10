import json
import os
import urllib.request
from google_translator import GoogleTranslator
import sys
from argument_reader import ArgumentReader


def get_settings():
    try:
        with open(os.path.join(sys.path[0], "settings.json"), "r") as file:
            settings = json.load(file)
    except:
        print("settings file not found!\nloading default settings....")
        try:
            with open(os.path.join(sys.path[0], "defaultSettings.json"), "r") as file:
                settings = json.load(file)
            print("creating settings file.....")
            with open(os.path.join(sys.path[0], "settings.json"), "w") as file:
                json.dump(settings, file)
            print("done creating settings file")
        except:
            print("ERROR: settings file not found!\ncant't open the app.")
            return None
    return settings


def check_internet_connection(host="https://www.google.com"):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


SETTINGS = get_settings()

if __name__ == "__main__":
    if not check_internet_connection():
        print("No Internet Connection.\nplease check your connection and try again.")
        exit()

    Translator = GoogleTranslator()
    argumentReader = ArgumentReader()

    args = argumentReader.get_arguments()
    text, target_language, source_language = args.text, args.target, args.source
    if not target_language:
        target_language = SETTINGS["primary_langauge"]

    print(
        Translator.translate(
            text,
            target_language if target_language else "auto",
            source_language if source_language else "auto",
        )
    )
    # print(text, target_language, source_language)
