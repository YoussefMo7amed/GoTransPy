import argparse
import json
import os
import sys


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


# get arguments from JSON file
def get_arguments():
    try:
        with open(os.path.join(sys.path[0], "arguments.json"), "r") as file:
            data = json.load(file)
    except:
        print("Error: JSON file not found.")
        data = None
    return data["argument"], data["description"]


def get_examples():
    examples = dict()
    # arguments
    arguments = get_arguments()[0]
    text_examples = arguments["text"]["examples"]
    examples["text"] = text_examples
    source_language_examples = arguments["source"]["examples"]
    examples["source"] = source_language_examples
    target_language_examples = arguments["target"]["examples"]
    examples["target"] = target_language_examples

    ls = ["Examples:\n"]
    for example in examples:
        ls.append(example + "\n")
        for item in examples[example]:
            ls.append("\t" + item + "\n")
        ls.append("\n")
    return "".join(ls)


ARGUMENTS, DESCRIPTION = get_arguments()
SETTINGS = get_settings()


class ArgumentReader:
    def __init__(self):
        self.arguments, self.description = ARGUMENTS, DESCRIPTION
        self.parser = argparse.ArgumentParser(
            description=self.description,
            formatter_class=argparse.RawTextHelpFormatter,
            epilog=get_examples(),
        )

    # read from files

    # Intialize the parser console arguments
    def init_parser(self):
        version = self.arguments["version"]
        self.parser.add_argument(
            version["name"], version["flag"], action="version", version=version["value"]
        )

        # mandatory argument
        text_arg = self.arguments["text"]
        self.parser.add_argument("text", help=text_arg["help"])

        # optional arguments
        source_language_arg = self.arguments["source"]
        self.parser.add_argument(
            source_language_arg["name"],
            source_language_arg["flag"],
            help=source_language_arg["help"],
        )

        target_language_arg = self.arguments["target"]
        self.parser.add_argument(
            target_language_arg["name"],
            target_language_arg["flag"],
            help=target_language_arg["help"],
            default=SETTINGS["primary_langauge"],
        )

    def get_arguments(self):
        self.init_parser()
        args = self.parser.parse_args()
        return args
