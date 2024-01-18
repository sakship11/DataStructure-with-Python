#Searching element In SLL
class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next
class SLL:
    def __init__(self):
        self.head=None

    def insert_e(self,newnode):
        if self.head is None:
            self.head=newnode
            return
        if self.head is not None:
            last=self.head
            while(last.next is not None):
                last=last.next
            last.next=newnode
            return
    def search(self,key):
        #check whether list is empty
        if self.head is None:
            print("List is Empty")
            return
        #check whether element is present or not
        tmp=self.head
        while(tmp is not None):
            if tmp.data==key:
                print("Element Found!")
            tmp=tmp.next
    def display(self):
        tmp=self.head
        while(tmp):
            print(tmp.data)
            tmp=tmp.next
        return
list1=SLL()
n1=Node("M")
list1.insert_e(n1)
n2=Node("N")
list1.insert_e(n2)
n3=Node("O")
list1.insert_e(n3)
list1.display()

list1.search("N")
