import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
city = list(list(map(int, input().split())) for _ in range(n))
print("city", city)

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        if city[i][j] == 2:
            chicken.append([i, j])

print("house", house)
print("chicken", chicken)
chickenLen = 1000000
for chi in combinations(chicken, m):
    tmp = 0
    for h in house:
        leng = 1000000
        for i in range(m):
            leng = min(leng, abs(h[0] - chi[i][0]) + abs(h[1] - chi[i][1]))
        tmp += leng
    chickenLen = min(chickenLen, tmp)

print(chickenLen)
