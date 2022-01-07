"""
#TODO
    * read a file 
        - get its extention
        - translate it
            - Default output with same name + "_language.extension"
            - if user added -o "name" or "path"
                - you can add convert output format
        
"""

import textract
import argparse
import json
import os

from google_translator import GoogleTranslator

Translator = GoogleTranslator()
language = "ar"
extenstion = "pdf"
input_format = {"language": "ar", "extenstion": "pdf"}
# file_path = "/home/youssef/Documents/programming/python/current projects/GoTransPy/test/{language}/test.{extenstion}"
output_format = {"language": "ar", "extenstion": "out"}

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()
file_path = args.filename
print(file_path)
text = textract.process(args.filename).decode("utf-8")
output_file = file_path.split(".")[0]
with open(output_file + ".out", "w", encoding="utf-8") as file:
    translated_text = Translator.translate(text)
    file.write(translated_text)
    print("done")
