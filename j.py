n = int(input())

shortest = None
strings = []
for i in range(n):
    string = input()
    strings.append(string)
    if not shortest or len(string) < len(shortest):
        shortest = string
strings.remove(shortest)

shortN = len(shortest)
for length in range(shortN - 1, 0 - 1, -1):
    found = False
    for start in range(shortN - length + 1):
        substr = shortest[start:start + length]
        if all(substr in s for s in strings):
            found = True
            print(len(substr))
            break
    if found:
        break


# substrings = []
# for start in range(len(shortest)):
#     for end in range(start + 1, len(shortest)):
#         substrings.append(shortest[start:end + 1])
# substrings.sort(key=len, reverse=True)


# longest = 0
# for substring in substrings:
#     skip = False
#     for string in strings:
#         if substring not in string:
#             skip = True
#             break
#     if skip:
#         continue
#     longest = max(longest, len(substring))

# print(longest)
