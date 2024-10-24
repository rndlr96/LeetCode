# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [(root, 1)]
        depth_total = collections.defaultdict(int)
        while stack:
            cur, level = stack.pop()
            depth_total[level] += cur.val
            stack.append((cur.left, level+1)) if cur.left is not None else None
            stack.append((cur.right, level+1)) if cur.right is not None else None
        
        if root is not None:
            root.val = 0
            
        stack = [(root, 1)]
        while stack:
            cur, level = stack.pop()
            
            left_value = cur.left.val if cur.left is not None else 0
            right_value = cur.right.val if cur.right is not None else 0
            
            if cur.left is not None:
                cur.left.val = depth_total[level+1] - right_value - cur.left.val
                stack.append((cur.left, level+1))
            if cur.right is not None:
                cur.right.val = depth_total[level+1] - left_value - cur.right.val
                stack.append((cur.right, level+1))
                
        return root