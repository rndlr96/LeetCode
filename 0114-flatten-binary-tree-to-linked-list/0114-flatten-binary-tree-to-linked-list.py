# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None

        def get_right_left(root: Optional[TreeNode]) -> TreeNode:
            while root.right is not None:
                root = root.right
            return root
        
        if root.left is not None:
            right = root.right
            right_leaf = get_right_left(root.left)
            right_leaf.right = right
            root.right = root.left
            root.left = None
            
        self.flatten(root.right)