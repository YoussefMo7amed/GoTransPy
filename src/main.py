import argparse
import json
import os
import urllib.request
from google_translator import GoogleTranslator
import sys
from argument_reader import ArgumentReader


def check_internet_connection(host="https://www.google.com"):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


if __name__ == "__main__":
    if not check_internet_connection():
        print("No Internet Connection.\nplease check your connection and try again.")
        exit()

    Translator = GoogleTranslator()
    argumentReader = ArgumentReader()
    args = argumentReader.get_arguments()
    text, target_language, source_language = args.text, args.target, args.source
    print(
        Translator.translate(
            text, target_language, source_language if source_language else "auto"
        )
    )
