import argparse
import json
import os
import sys


# get arguments from JSON file
def get_arguments():
    try:
        with open(os.path.join(sys.path[0], "arguments.json"), "r") as file:
            data = json.load(file)
    except:
        print("Error: JSON file not found.")
        data = None
    return data["version"], data["description"], data["argument"]


def get_examples():
    examples = dict()
    # arguments
    arguments = get_arguments()[2]

    for argument in arguments:
        examples[argument] = arguments[argument]["examples"]

    ls = ["Examples:\n"]
    for example in examples:
        ls.append(example + "\n")
        for item in examples[example]:
            ls.append("\t" + item + "\n")
        ls.append("\n")
    return "".join(ls)


VERSION, DESCRIPTION, ARGUMENTS = get_arguments()


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
        version = VERSION
        self.parser.add_argument(
            version["name"], version["flag"], action="version", version=version["value"]
        )

        # mandatory argument
        text_arg = self.arguments["text"]
        self.parser.add_argument("text", help=text_arg["help"], type=str)

        # text_arg = self.arguments["text"]
        # self.parser.add_argument("text", help=text_arg["help"], type=file)

        # optional arguments
        for argument in ARGUMENTS:
            if argument == "text":
                continue  # because it is a mandatory argument, and already added
            current_argument = ARGUMENTS[argument]
            self.parser.add_argument(
                current_argument["name"],
                current_argument["flag"],
                help=current_argument["help"],
            )

    def get_arguments(self):
        self.init_parser()
        args = self.parser.parse_args()
        return args
