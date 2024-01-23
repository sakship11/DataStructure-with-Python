#Queue
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,data): #Insert an element
        if self.rear is None:
            self.front=self.rear=Node(data)
        else:
            self.rear.next=Node(data)
            self.rear=self.rear.next
            
    def dequeue(self):       #Remove element
        if self.front is None:
            print("Empty Queue")
        else:
            deleted=self.front.data
            self.front=self.front.next
            print("Deleted element:",deleted)
            return  
            
    def isempty(self):  #check whether queue is empty or not
        if self.front is None:
            print("Queue is an empty")
        else:
            print("Queue is not empty")

    def size(self): #size of the queue
        count=0
        tmp=self.front
        while(tmp):
            count+=1
            tmp=tmp.next
        print("Size of Queue:",count) 

    def display(self):
        temp=self.front
        if self.front is None:
            print("Empty Queue")
        
        while(temp!=None):
            print(temp.data)
            temp=temp.next
        return
            
q=Queue()
print("Enqueue elements")
q.enqueue(12)
q.enqueue(24)
q.enqueue(36)
q.display()

print("Deueue element:")
q.dequeue()
q.display()

q.isempty()

q.size()
