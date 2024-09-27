t = int(input())


def f():
    n = int(input())
    home = ([int(x) for x in input().split()], "home", set())
    stores = []
    for i in range(n):
        stores.append(([int(x) for x in input().split()], "store", set()))
    dest = ([int(x) for x in input().split()], "dest", set())

    nodes = [home] + stores + [dest]

    # Build graph adjacency

    for i in range(len(nodes)):
        node = nodes[i]
        pos = node[0]

        for j in range(len(nodes)):
            if i == j:
                continue

            node2 = nodes[j]
            pos2 = node2[0]

            d = abs(pos[0] - pos2[0]) + abs(pos[1] - pos2[1])

            if d <= 1000:
                node[2].add(j)
                node2[2].add(i)

    # Search graph

    queue = [0]
    visited = set()

    while len(queue) > 0:
        i = queue.pop()
        node = nodes[i]
        if node[1] == "dest":
            return "happy"
        for a in node[2]:
            if a not in visited:
                visited.add(a)
                queue.append(a)

    return "sad"


for _ in range(t):
    print(f())
