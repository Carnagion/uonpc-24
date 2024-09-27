from itertools import combinations
import sys

m, n, k = [int(x) for x in input().split()]

rows = []

for i in range(m):
    rows += [input().split()]


def f(zeros, remaining_rows, l):
    if l == 0:
        return False

    for i in range(len(remaining_rows)):
        r = remaining_rows[i]
        zeros2 = [x for x in zeros]
        for j in range(n):
            zeros2[j] |= r[j] == '0'

        if all(zeros2):
            return True

        remaining_rows2 = [x for (j, x) in enumerate(remaining_rows) if j != i]
        if f(zeros2, remaining_rows2, l - 1):
            return True

    return False


if f([False] * n, rows, k):
    print("yes")
else:
    print("no")

# for c in combinations(rows, k):
#     zeros = [False] * n

#     for r in c:
#         for i in range(n):
#             zeros[i] |= r[i] == '0'

#     if all(zeros):
#         print("yes")
#         sys.exit(0)

# print("no")
