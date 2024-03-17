from collections import deque

# BFS로 가장 가까운 먹을 수 있는 물고기 찾기
def find_fish(start, size):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = set([start])
    fish = []
    time = 0

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            if 0 < grid[x][y] < size:  # 먹을 수 있는 물고기 발견
                fish.append((time, x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                    if grid[nx][ny] <= size:  # 이동 가능한 칸
                        queue.append((nx, ny))
                        visited.add((nx, ny))
        if fish:
            return sorted(fish)[0]  # 가장 가까운 물고기 반환
        time += 1

    return None

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 아기 상어 위치 찾기 및 초기화
for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            shark = (i, j)
            grid[i][j] = 0

shark_size = 2
eat_count = 0
time_spent = 0

while True:
    result = find_fish(shark, shark_size)
    if result is None:  # 먹을 수 있는 물고기가 더 이상 없음
        break
    time, x, y = result
    time_spent += time  # 이동 시간 더하기
    eat_count += 1
    if eat_count == shark_size:  # 성장
        shark_size += 1
        eat_count = 0
    grid[x][y] = 0  # 물고기 먹기
    shark = (x, y)  # 상어 위치 업데이트

print(time_spent)
