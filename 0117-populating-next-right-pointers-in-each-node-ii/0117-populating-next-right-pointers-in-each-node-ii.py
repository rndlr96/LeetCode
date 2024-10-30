"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

import collections

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
            
        stack = collections.deque([root])
        while stack:
            stack_len = len(stack)
            for idx in range(stack_len):
                cur = stack.popleft()
                cur.next = stack[0] if idx < stack_len - 1 else None
                stack.append(cur.left) if cur.left is not None else None
                stack.append(cur.right) if cur.right is not None else None
            
        return root