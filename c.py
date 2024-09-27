n = int(input())
ks = [int(k) for k in input().split(" ")]

correct = len([k for k, i in zip(ks, range(len(ks))) if k == i + 1])
print(len(ks) + 2 - correct)
