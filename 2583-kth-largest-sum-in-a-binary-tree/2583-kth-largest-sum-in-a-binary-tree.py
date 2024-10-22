# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        stack = [(root, 1)]
        levels = {}
        while stack:
            cur, level = stack.pop()
            levels[level] = levels[level] + cur.val if levels.get(level, 0) else cur.val

            stack.append((cur.left, level+1)) if cur.left is not None else None
            stack.append((cur.right, level+1)) if cur.right is not None else None

        return sorted(levels.values(), reverse=True)[k-1] if len(levels) >= k else -1