#Insertion of node in beginning DLL
class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.next=next
        self.prev=prev
class DLL:
    def __init__(self):
        self.head=None
    #function to add(append )node in DLL
    def add(self,newnode):
        if self.head is None:
            self.head=newnode
            return
        #if headnode is present then new node will added at end of DLL

        if self.head is not None:
            last=self.head
            while(last.next is not None):
                last=last.next
            last.next=newnode
            newnode.prv=last
            return          
    def insert_b(self,newnode):
        #if list is empty then newnode will be head node
        if self.head is None:
            self.head=newnode
            return
        #if headnode is present then newnode will be added at beginning
        if self.head is not None:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def display(self):
        tmp=self.head
        while(tmp is not None):
            print(tmp.data)
            tmp=tmp.next
        return
list1=DLL()
n1=Node(data="A")
list1.add(n1)
n2=Node(data="B")
list1.add(n2)
n3=Node(data="C")
list1.add(n3)
n5=Node(data="X")
list1.insert_b(n5)
list1.display()
