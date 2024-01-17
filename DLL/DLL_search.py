#searching of node
class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.next=next
        self.prev=prev
class DLL:
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
            newnode.prev=last
            return
    def search(self,key):
        if self.head is None:
            print("Empty List")
            return
        tmp=self.head
        while (tmp is not None):
            if tmp.data==key:
                print("Element found")
            tmp=tmp.next
    def display(self):
        tmp=self.head
        while(tmp):
            print(tmp.data)
            tmp=tmp.next
        return
list1=DLL()
n1=Node("A")
list1.add(n1)
n2=Node("B")
list1.add(n2)
n3=Node("C")
list1.add(n3)
list1.display()
list1.search("B")
