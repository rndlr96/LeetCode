class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(matrix, target, row=-1):
            start = 0
            end = len(matrix[-1])-1 if row > -1 else len(matrix)-1
            while start <= end:
                mid = (start+end) // 2
                mid_num = matrix[row][mid] if row > -1 else matrix[mid][0]
                if mid_num == target:
                    return mid
                elif mid_num < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return end
        
        row = binary_search(matrix, target, -1)
        col = binary_search(matrix, target, row)
        return matrix[row][col] == target