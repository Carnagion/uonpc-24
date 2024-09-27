n = int(input())

spies = []
houses = []

for i in range(n):
    line = input()
    for j in range(len(line)):
        if line[j] == 'S':
            spies.append([i, j])
        elif line[j] == 'H':
            houses.append([i, j])

largest = -1

for s in spies:
    lowest = 10000000

    for h in houses:
        d = abs(s[0] - h[0]) + abs(s[1] - h[1])
        if d < lowest:
            lowest = d

    if lowest > largest:
        largest = lowest

print(largest)
