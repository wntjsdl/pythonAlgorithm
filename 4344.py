'''
I
- python sum, len 함수 + for문 이용하여 하나씩 출력해줌
T
- 이중 for문 O(n^2)
V
tempList[]
'''
import sys
import math

n = int(sys.stdin.readline())
for _ in range(n):
    inputList = list(map(float, sys.stdin.readline().split()))
    N = inputList.pop(0)
    avg = sum(inputList) / N
    temp = 0
    for score in inputList:
        if score > avg:
            temp += 1
    answer = round(temp / N * 100, 3)
    print(f"{answer}%")