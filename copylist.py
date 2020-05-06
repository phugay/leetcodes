"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        d = {}
        curr = head

        while curr:
            d[curr] = Node(curr.val, None, None)
            curr = curr.next


        curr = head

        while curr:
            if curr.next != None:
                d[curr].next = d[curr.next]
            if curr.random != None:
                d[curr].random = d[curr.random]
            curr = curr.next



        return d[head]