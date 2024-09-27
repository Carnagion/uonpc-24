n = int(input())
animals = int(
    "".join(['0' if input() == 'Z' else '1' for i in range(n)]),
    base=2)
print(animals)
