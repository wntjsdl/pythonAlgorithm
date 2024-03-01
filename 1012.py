"""
I
- graph[][] 먼저 생성해준 뒤, 이중 for 돌면서
값이 1일 때 count += 1 한뒤, dx + 1, dy + 1 값이 1인 곳 0 만들어줌
T
- O(M*N)
V
- 
"""

import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    queue = [(x, y)]
    graph[x][y] = 0

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * (N) for _ in range(M)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(M):
        for b in range(N):
            if graph[a][b] == 1:
                bfs(a, b)
                cnt += 1

    print(cnt)
