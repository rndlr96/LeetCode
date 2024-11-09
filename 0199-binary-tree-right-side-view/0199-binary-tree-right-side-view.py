# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        results = {}
        stack = [(root, 0)]
        
        while stack:
            cur, depth = stack.pop()
            if depth not in results:
                results[depth] = cur.val
                
            stack.append((cur.left, depth+1)) if cur.left else None
            stack.append((cur.right, depth+1)) if cur.right else None
            
        return list(results.values())