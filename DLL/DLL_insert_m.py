#Insertion of node after given node(Previous node)
class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.data=data
        self.next=next
        self.prev=prev
class DLL:
    def __init__(self):
        self.head=None
    def add(self,newnode):
        #if list is empty then newnode will be headnode
        if self.head is None:
            self.head=newnode
            return
        #if headnode is present then newnode will add at end of DLL
        if self.head is not None:
            last=self.head
            while(last.next is not None):
                last=last.next
            last.next=newnode
            newnode.prv=last
            return
    def insert_m(self,prev_node,newnode):
        if prev_node is None:
            print("Previous node is not present")
            return
       
        newnode.next=prev_node.next
        newnode.prev=prev_node
        prev_node.next=newnode
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
list1.insert_m(n2,n5)
list1.display()
