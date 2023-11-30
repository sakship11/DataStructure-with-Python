#insertion of node after a given node(Previous)
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class SLL:
    def __init__(self):
        self.head=None
    def add(self,newnode):
        if self.head is None:
            self.head=newnode
            return
        if self.head is not None:
            last=self.head
            while(last.next is not None):
                last=last.next
            last.next=newnode
            return
    #Function to insert node after a given node
    def insert_m(self, prv_node,newnode):
        #if prv_node is empty then node will not insert
        if prv_node is None:
            print("Previous node is not present")
            return
        newnode.next=prv_node.next
        prv_node.next=newnode
    def display(self):
        tmp=self.head
        while(tmp):
            print(tmp.data)
            tmp=tmp.next
        return
list1=SLL()
n1=Node("A")
list1.add(n1)

n2=Node("B")
list1.add(n2)

n3=Node("C")
list1.add(n3)

n5=Node("X")
list1.insert_m(n2,n5)
list1.display()
