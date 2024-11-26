class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        def _is_winner(team: int, maps: List[List[int]]) -> bool:
            visited = [0] * len(maps)
            stack = [team]
            while stack:
                cur = stack.pop()
                if visited[cur]:
                    continue
                visited[cur] = 1
                for idx in range(n):
                    if maps[cur][idx]:
                        stack.append(idx)
            if sum(visited) == len(maps):
                return True
            return False
        
        maps = [[0] * n for _ in range(n)]
        for edge in edges:
            maps[edge[0]][edge[1]] = 1
        
        for idx in range(n):
            if _is_winner(idx, maps):
                return idx
            
        return -1