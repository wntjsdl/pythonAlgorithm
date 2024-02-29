'''
I
- M개 중 N개 선택하는 경우의 수나 마찬가지
- itertools combinations(조합) 사용하여 구하기
T
- 
V
'''
import math
import sys

n = int(sys.stdin.readline())
for _ in range(n):
    N, M = map(int, sys.stdin.readline().split())
    print(math.comb(M,N))
    

