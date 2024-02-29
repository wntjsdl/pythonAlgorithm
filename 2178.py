'''
I
- BFS 이용
T
V
- graph list []
'''
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):

    dq = deque()
    dq.append((x, y))

    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                dq.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[N-1][M-1]

print(bfs(0,0))