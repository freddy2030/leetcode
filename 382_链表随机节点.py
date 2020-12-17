# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random

class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        v = None
        n = 0
        p = self.head
        while p.val!=None:
            n += 1
            if random.random() < 1/n:
                v = p.val
            p = p.next
        return v




# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()