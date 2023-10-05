import sys

first = list(map(str, input()))
second = list(map(str, input()))

firstLen, secondLen = len(first), len(second)
cache = [0] * 12

print(firstLen)
print(secondLen)
print(cache)

for i in range(firstLen):
    cnt = 0
    for j in range(secondLen):
        if cnt < cache[j]:
            cnt = cache[j]
        elif first[i] == second[j]:
            cache[j] = cnt + 1


print(cache)
print(max(cache))
