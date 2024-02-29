"""
I
- dp[n] = dp[n-1] + dp[n-2] + dp[n-3] 
T
- 
V
- arr []
"""

import sys

n = int(sys.stdin.readline())

arr = [0] * 11
arr[1] = 1
arr[2] = 2
arr[3] = 4
for i in range(4, 11):
    arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]

for _ in range(n):
    input = int(sys.stdin.readline())
    print(arr[input])
