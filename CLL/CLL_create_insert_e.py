#Circular Linked List and insret element at end
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.next=self.head
    def add(self,data):
        newnode=Node(data)

        if self.head.data is None:
            self.head=newnode
            self.tail=newnode
            newnode.next=self.head
        else:
            self.tail.next=newnode
            self.tail=newnode
            self.tail.next=self.head
    def display(self):
        current=self.head
        if self.head is None:
            print("List is Empty")
            return
        else:
            print(current.data)
            while(current.next != self.head):
                current=current.next
                print(current.data)
cl=CLL()
cl.add(1)
cl.add(2)
cl.add(3)
cl.add(4)
cl.display()
