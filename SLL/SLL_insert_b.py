#insert a node at g bginning in Linked list
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class SLList:
    def __init__(self):
        self.head=None
    def display(self):  #traverse the Linked List
        current=self.head
        while(current):
            print(current.data)
            current=current.next
    def insert_beginning(self,newnode):  #insert node at beginning
        newnode.next=self.head
        self.head=newnode

list1=SLList() #object created
n1=Node("Mon")
list1.head=n1
n2=Node("Tue")
n1.next=n2
n3=Node("Wed")
n2.next=n3
newnode=Node("Sun")
list1.insert_beginning(newnode)  #function calling

list1.display() #function calling
        
