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

# Trick is to invert condition
red_fruits = [f for f in fruits if f.colour == "red"]

print("Found these red fruits:")
for fruit in red_fruits:
    print("*", fruit.name)
print()


favourite_cheeses = [
    "Stilton",
    "Wensleydale",
    "Cheddar",
]

cheese_to_rank = {
    cheese: rank for rank, cheese in enumerate(favourite_cheeses, start=1)
}

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

# unique_names = {n for n in names}
unique_names = set(names)

print(f"Found {len(unique_names)} unique names.")
