#Insertion of node at the end(DLL)
class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next       
class SLL:
    def __init__(self):
        self.head=None        
    #function to add node at the end in doubly linked list
    def insert_end(self,newnode):       
        #if list is empty then newnode will be the head node
        if self.head is None:
            self.head=newnode
            return
        #if head node is present then new node will be added at the end
        if self.head is not None:
            last=self.head
            while(last.next is not None):
                last=last.next
            last.next=newnode
            newnode.prev=last
            return              
    #function to traverse DLL and display elements
    def display(self):
        tmp=self.head
        while(tmp is not None):
            print(tmp.data)
            tmp=tmp.next
        return              
list1=SLL()                             #creation of empty doubly linked list
n1=Node(data="A")                            #creation of node
list1.insert_end(n1)                    #insert node at the end in SLL
n2=Node(data="B")
list1.insert_end(n2)
n3=Node(data="C")
list1.insert_end(n3)
list1.display()
