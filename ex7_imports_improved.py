import statistics
from collections import Counter
from math import sqrt

fruits = [
    "Apple",
    "Apple",
    "Apple",
    "Banana",
    "Banana",
    "Banana",
    "Cherry",
    "Cherry",
    "Cherry",
    "Cherry",
]
fruit_counter = Counter(fruits)
for fruit, count in fruit_counter.items():
    print(f"{fruit}: {count}")
print()

square_numbers = []
for number in range(101):
    root = sqrt(number)
    if int(root) == root:
        square_numbers.append(number)
        print(number, "is a square number")
print()

print("The mean square number is", statistics.mean(square_numbers))
