from email import header


class Node:
    def __init__(self,data) -> None:
        self.val=data
        self.next=None
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def insert(self,n):
        if self.head == None:
            self.head=n
            return self.head
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=n
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.val,end="->")
            temp=temp.next

if __name__== '__main__':
    llist = LinkedList()

    n=int(input("Enter The number of values\n"))

    for i in range(n):
        val=int(input())
        node=Node(val)
        llist.insert(node)
    llist.display()




    