class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Stack:
    def __init__(self):
        self.top=None
        
    def push(self,data):      #Push element(insert)
        if self.top is None:
            self.top=Node(data)
            
        else:
            newnode=Node(data)
            newnode.next=self.top
            self.top=newnode
            
    def pop(self):           #Remove element
        if self.top is None:
            print("Empty stack")
            
        else:
            poped=self.top
            self.top=self.top.next
            poped.next=None
            print("poped element is",poped.data) 
            
    def isempty(self):  #check whether stack is empty or not
        if self.top is None:
            print("stack is empty")
        else:
            return
            
    def top_element(self):   #find topmost element
        if self.top is None:
            print("stack is empty")
        else:
            top_ele=self.top.data
            print("top element is ",top_ele)
        
    def display(self):  
 
        temp = self.top
        if self.isempty():
            print("Stack Underflow")
 
        else:
 
            while(temp != None):
 
                print(temp.data, end = "")
                temp = temp.next
                if(temp != None):
                    print(" -> ", end = "")
            return
        
stck=Stack()
stck.push(10)
stck.push(20)
stck.push(30)
stck.push(40)

print("original stack is ")
stck.display()

print("\npop an element")
stck.pop()

print("top of stack is  ")
stck.top_element()
