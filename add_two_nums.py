# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        strnum1 = ""
        strnum2 = ""
        addlist = []
        addnums = 0
        while(l1!=None):
            strnum1+=str(l1.val)
            l1=l1.next
        strrev1 = int(strnum1[::-1])
        while(l2!=None):
            strnum2+=str(l2.val)
            l2=l2.next
        strrev2 = int(strnum2[::-1])
        addnums = str(strrev1+strrev2)
        addlist = [int(x) for x in addnums[::-1]]
        cur = dummy = ListNode(0)
        for i in addlist:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next
           