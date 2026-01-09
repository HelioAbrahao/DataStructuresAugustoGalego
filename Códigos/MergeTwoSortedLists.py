# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        p1 = list1
        p2 = list2
        
        if not p1:
            return p2
        
        if not p2:
            return p1
        
        if p1.val <= p2.val:
            newHead = p1
            p1 = p1.next
            
        else:
            newHead = p2
            p2 = p2.next 
            
        answer = newHead
        
        while p1 is not None and p2 is not None:     
            if p1.val <= p2.val:
                newHead.next = p1
                p1 = p1.next
                newHead = newHead.next
            else: 
                newHead.next = p2
                p2 = p2.next 
                newHead = newHead.next
                
        if p1 is not None:
            newHead.next = p1
        else:
            newHead.next = p2
                
        return answer
           
        
        