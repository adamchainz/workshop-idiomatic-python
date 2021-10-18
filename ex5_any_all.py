def list_has_suffix(items: list[str], suffix: str) -> bool:
    result = True
    for item in items:
        if not item.endswith(suffix):
            result = False
            break
    return result


# Bonus task: change this code so there is a single list of counties, which is
# then converted into this data structure.
counties_by_letter = {
    "B": [
        "Bedfordshire",
        "Berkshire",
        "Bristol",
        "Buckinghamshire",
    ],
    "H": [
        "Hampshire",
        "Herefordshire",
        "Hertfordshire",
    ],
    "L": [
        "Lancashire",
        "Leicestershire",
        "Lincolnshire",
    ],
}

for letter, counties in counties_by_letter.items():
    all_shires = list_has_suffix(counties, "shire")
    if all_shires:
        verb = "do"
    else:
        verb = "do not"
    print("All", letter, "counties", verb, "end with 'shire'.")
