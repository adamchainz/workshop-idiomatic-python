class Fruit:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour


fruits = [
    Fruit("Grape", "white"),
    Fruit("Dragonfruit", "red"),
    Fruit("Apple", "green"),
    Fruit("Apple", "red"),
    Fruit("Grape", "red"),
    Fruit("Melon", "yellow"),
]

red_fruits = []
for fruit in fruits:
    if fruit.colour != "red":
        continue
    red_fruits.append(fruit)

print("Found these red fruits:")
for fruit in red_fruits:
    print("*", fruit.name)
print()


favourite_cheeses = [
    "Stilton",
    "Wensleydale",
    "Cheddar",
]

cheese_to_rank = {}
for rank, cheese in enumerate(favourite_cheeses, start=1):
    cheese_to_rank[cheese] = rank

print("Cheddar has a rank of:", cheese_to_rank["Cheddar"])
print("...whilst Stilton has a rank of:", cheese_to_rank["Stilton"])
print()

names = [
    "Alice",
    "Matilda",
    "Agnes",
    "Margaret",
    "Alice",
    "Alice",
    "Agnes",
    "Joan",
    "Alice",
    "Agnes",
    "Matilda",
]

unique_names = []
for name in names:
    if name in unique_names:
        continue
    unique_names.append(name)

print(f"Found {len(unique_names)} unique names.")
