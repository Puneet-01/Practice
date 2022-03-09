# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left: int, right: int) :
        if head==None or head.next==None:
            return head
        
        
        prev=None
        curr=head
        while left>1:
            prev=curr
            curr=curr.next
            left,right=left-1,right-1
            
        tail,con=curr,prev
        while right:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            right-=1
        if con:
            con.next=prev
        else:
            head=prev
        tail.next=curr
        return head