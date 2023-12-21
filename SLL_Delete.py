#Deleteion of node in Singly Linked List
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
class SLL:
    def __init__(self):
        self.head=None
        
    #function to add node at the end in singly linked list
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
            return
        
    def delete_node(self,key):
        #check wether the list is empty
        if self.head is None:
            print("empty list")
            return
        #if list is not empty and key is matched with first node
        if self.head is not None:
            if self.head.data==key:
                self.head=self.head.next
                return
        #if key is not matched with head node
        tmp=self.head
        while(tmp):
            if tmp.data==key:
                prv.next=tmp.next
                tmp=None
                break
                  
    #function to traverse SLL and display elements
    def display(self):
        tmp=self.head
        while(tmp):
            print(tmp.data)
            tmp=tmp.next
        return
        
              
list1=SLL()                             #creation of empty singly linked list
n1=Node("A")                            #creation of node
list1.insert_end(n1)                    #insert node at the end in SLL

n2=Node("B")
list1.insert_end(n2)

n3=Node("C")
list1.insert_end(n3)
print("list before deletion")
list1.display()                  #call to display()to display elements.

list1.delete_node("A")
print("list After deletion")
list1.display()
