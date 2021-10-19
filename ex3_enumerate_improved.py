fruits = ["Apple", "Banana", "Cherry"]

for i, fruit in enumerate(fruits):
    print(f"fruits[{i}] = {fruit!r}")
print()

vegetables = ["Squash", "Celeriac", "Potato"]
print("My favourite vegetables:")
for i, vegetable in enumerate(vegetables, start=1):
    print(f"{i}. {vegetable}")
print()

languages = ["Python", "Java", "JavaScript"]
print("Top three programming languages, in reverse order:")
reverse_numbered_languages = reversed(
    list(enumerate(languages, start=1)),
)
for i, language in reverse_numbered_languages:
    print(f"{i}. {language}")
