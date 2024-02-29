"""
I
- 그리디
- 배열 정렬 후 (count - index)을 곱한 값을 더해줌
T
- O(N)
V
- timeList []
"""

import sys

N = int(sys.stdin.readline())
timeList = list(map(int, sys.stdin.readline().split()))
timeList.sort()

answer = 0
for idx, val in enumerate(timeList):
    answer += val * (N - idx)

print(answer)
