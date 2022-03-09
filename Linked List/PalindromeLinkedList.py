# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        
        if head == None:
            return False
        if head.next == None:
            return True
        
        slow = head
        fast=head
        
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            
            
            
        rev=self.reverse(slow)
        
        curr=head
        
        while(rev!=None):
            if curr.val != rev.val:
                
                return False
            print("Curr",curr.val)
            print("Rev",rev.val)
            curr=curr.next
            rev=rev.next
        return True
    
    
    def reverse(self,head):
        
        curr=head
        prev=None
        
        while curr!=None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        return prev