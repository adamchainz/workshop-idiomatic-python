import argparse

from ex9.algorithm import looks_like_english


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=argparse.FileType("r"), nargs="+")

    args = parser.parse_args(argv)
    files = args.file

    exit_code = 0
    for file in files:
        text = file.read()
        if looks_like_english(text):
            verb = "looks like"
        else:
            verb = "does not look like"
            exit_code = 1
        print(file.name, verb, "English.")

    return exit_code
