def cmp(i, j, k):
    ai, bi = i
    aj, bj = j

    jgei = ai + k < aj or bi + k < bj
    igej = aj + k < ai or bj + k < bi

    if jgei and igej:
        return 0
    elif igej:
        return 1
    elif jgei:
        return -1


n, k = [int(x) for x in input().split()]
assistants = [(int(a), int(b))
              for a, b in zip(input().split(), input().split())]

distinct = 0
for i in range(len(assistants)):
    for j in range(i + 1, len(assistants)):
        if cmp(assistants[i], assistants[j], k) != 0:
            distinct += 1

print(distinct)
