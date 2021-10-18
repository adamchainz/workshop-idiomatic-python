"""
Use letter frequency heuristics to check if a file could be in English.
"""
import sys
from collections import Counter

# Bonus task: refactor sys.argv code to use argparse and its FileType class
if len(sys.argv) < 2:
    print("You must pass at least one filename")
    raise SystemExit(1)

exit_code = 0
for filename in sys.argv[1:]:
    counts: Counter[str] = Counter()
    text = open(filename).read().lower()
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
    print(filename, verb, "English.")
raise SystemExit(exit_code)
