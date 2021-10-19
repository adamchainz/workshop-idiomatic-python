def list_has_suffix(items: list[str], suffix: str) -> bool:
    return all(i.endswith(suffix) for i in items)


all_counties = [
    "Bedfordshire",
    "Berkshire",
    "Bristol",
    "Buckinghamshire",
    "Hampshire",
    "Herefordshire",
    "Hertfordshire",
    "Lancashire",
    "Leicestershire",
    "Lincolnshire",
]

counties_by_letter: dict[str, list[str]] = {}  # Can also use defaultdict(list)
for county in all_counties:
    first_letter = county[0]
    counties_by_letter.setdefault(first_letter, []).append(county)

for letter, counties in counties_by_letter.items():
    all_shires = list_has_suffix(counties, "shire")
    if all_shires:
        verb = "do"
    else:
        verb = "do not"
    print("All", letter, "counties", verb, "end with 'shire'.")
