# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1, head)
        prev, nxt = head, head.next
        
        while nxt:
            while nxt.next and nxt.val == nxt.next.val:
                nxt = nxt.next
            
            if prev.next != nxt:
                prev.next = nxt.next
            else:
                prev = nxt
            nxt = nxt.next
            
        return head.next