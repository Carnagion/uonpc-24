n, a0, b0, c0 = [int(x) for x in input().split()]

a = a0
b = b0
c = c0

for i in range(n - 1):
    a2 = a0 * (b + c)
    b2 = b0 * (a + c)
    c2 = c0 * (a + b)

    a = a2
    b = b2
    c = c2

print((a + b + c) % (10**9+7))
