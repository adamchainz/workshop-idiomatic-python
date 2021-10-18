fruits = ["Apple", "Banana", "Cherry"]

for i in range(len(fruits)):
    fruit = fruits[i]
    print(f"fruits[{i}] = {fruit!r}")
print()

vegetables = ["Squash", "Celeriac", "Potato"]
print("My favourite vegetables:")
i = 1
while i < len(vegetables) + 1:
    vegetable = vegetables[i - 1]
    print(f"{i}. {vegetable}")
    i += 1
print()

languages = ["Python", "Java", "JavaScript"]
print("Top three programming languages, in reverse order:")
for i in range(len(languages), 0, -1):
    language = languages[i - 1]
    print(f"{i}. {language}")
