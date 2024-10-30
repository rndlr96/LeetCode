class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[-1])
        visited = [[0] * n for _ in range(m)]
        stack, max_move = [], 0
        for start_row in range(m):
            stack.append((start_row, 0))
        
        dx = [-1, 0, 1]
        dy = [1, 1, 1]
        while stack:
            x, y = stack.pop()
            max_move = max(max_move, visited[x][y])
            for idx in range(3):
                nx, ny = x + dx[idx], y + dy[idx]
                if nx < 0 or ny < 0 or nx >= m or ny >= n or visited[nx][ny] > visited[x][y] or grid[x][y] >= grid[nx][ny]:
                    continue
                visited[nx][ny] = visited[x][y] + 1
                stack.append((nx, ny))

        return max_move
