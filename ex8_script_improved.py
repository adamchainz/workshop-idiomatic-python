#!/usr/bin/env python
"""
Use letter frequency heuristics to check if a file could be in English.
"""
import argparse
from collections import Counter


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="determine if files are english")
    parser.add_argument(
        "file", type=argparse.FileType("r"), nargs="+", help="a real filename"
    )

    args = parser.parse_args(argv)
    files = args.file

    exit_code = 0
    for file in files:
        counts: Counter[str] = Counter()
        text = file.read().lower()
        for char in text:
            if char.isalpha():
                counts[char] += 1

        # https://en.wikipedia.org/wiki/Letter_frequency
        count_letter = [(count, letter) for letter, count in counts.items()]
        count_letter.sort(reverse=True)
        top_letters = [letter for count, letter in count_letter][:3]
        if top_letters == ["e", "t", "a"]:
            verb = "looks like"
        else:
            verb = "does not look like"
            exit_code = 1
        print(file.name, verb, "English.")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
