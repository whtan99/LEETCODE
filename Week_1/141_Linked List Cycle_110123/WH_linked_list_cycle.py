# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        p2 = head.next
        if not p2:
            return False
        while head and p2:
            if head == p2:
                return True
            head = head.next
            p2 = p2.next
            if not p2:
                return False
            p2 = p2.next
        return False
