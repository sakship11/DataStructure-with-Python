#delete Node:DLL
class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
class DLL:
    def __init__(self):
        self.head=None
    def insert_end(self,newnode):
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
    def delete_node(self,key):
        if self.head is None:
            print("empty list")
            return
        if self.head is not None:
            if self.head.data==key:
                self.head=self.head.next
                return
        tmp=self.head
        while(tmp):
            if tmp.data==key:
                break
            prv=tmp
            tmp=tmp.next
        prv.next=tmp.next
    def display(self):
        tmp=self.head
        while(tmp is not None):
            print(tmp.data)
            tmp=tmp.next
        return              
list1=DLL()                            
n1=Node(data="A")                            
list1.insert_end(n1)                    
n2=Node(data="B")
list1.insert_end(n2)

n3=Node(data="C")
list1.insert_end(n3)
print("list before deletion")
list1.display()                  

list1.delete_node("B")
print("list After deletion")
list1.display()
