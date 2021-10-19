from collections import Counter


def looks_like_english(text: str) -> bool:
    counts: Counter[str] = Counter()
    for char in text.lower():
        if char.isalpha():
            counts[char] += 1

    # https://en.wikipedia.org/wiki/Letter_frequency
    count_letter = [(count, letter) for letter, count in counts.items()]
    count_letter.sort(reverse=True)
    top_letters = [letter for count, letter in count_letter][:3]
    return top_letters == ["e", "t", "a"]
