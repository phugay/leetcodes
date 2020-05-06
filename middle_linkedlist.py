# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        
        ll_length = 0
        if head == None:
            return head
        
        curr = head
        while(curr!=None):
            curr = curr.next      
            ll_length+=1               
        print("total nodes ",ll_length)
        
        mid = 0
        if ll_length%2==0:
            mid = ll_length/2
        else:
            mid = int(floor(ll_length/2))
        print("middle of linked list ",mid)
                        
        i=0
        curr = head
        while(curr!=None and i<mid):
            print(curr.val)
            curr = curr.next
            i+=1

        return curr
      
        