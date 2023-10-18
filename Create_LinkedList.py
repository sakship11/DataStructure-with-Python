class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next

class SLlist:
    def __init__(self):
        self.head=None

    def display(self):
        current=list1.head
        while(current):
            print(current.data)
            current=current.next

list1= SLlist()

n1=Node("Sun")
list1.head=n1

n2=Node("Mon")
n1.next=n2

n3=Node("Tue")
n2.next=n3

list1.display()
