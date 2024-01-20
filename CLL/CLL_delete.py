  
class Node:  
      def __init__(self,data):
            self.data = data  
            self.next = None  
            
class CLL:
    def __init__(self):
        self.head = Node(None)  
        self.tail = Node(None)  
        self.head.next = self.tail  
        self.tail.next = self.head 
        
    def add(self,data):
        newnode=Node(data)
        if self.head.data is None:
            self.head=newnode
            self.tail=newnode
            newnode.next = self.head
            
        else:
            self.tail.next =newnode
            self.tail = newnode
            self.tail.next = self.head 
            
    def delete_node(self,key):
        #check wether the list is empty
        if self.head is None:
            print("empty list")
            return
        #if list is not empty and key is matched with first node
        if self.head is not None:
            if self.head.data==key:
               
                self.tail.next=self.head.next
                self.head=self.head.next
                return
        #if key is not matched with head node
        tmp=self.head
        while(tmp.next is not self.head):
            if tmp.data==key:
                prv.next=tmp.next
                tmp=None
                break
            
    def display(self):
        temp=self.head
        if self.head is None:
            print("Empty list")
            return
        
        else:
            print(temp.data)
            while(temp.next is not self.head):
                temp=temp.next
                print(temp.data)
                
list1=CLL()
list1.add(1)
list1.add(2)
list1.add(3)
list1.add(4)

list1.delete_node(2)

list1.display()
     
