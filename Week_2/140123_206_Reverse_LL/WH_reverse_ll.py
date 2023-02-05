# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        temp = head.next
        head.next = None
        r = self.reverseList(temp)
        temp.next = head
        return r
