#Creation and traversing of Doubly Linked List
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def append(self, data):
        new_node = Node(data) #Create a New Node:
        if not self.head:     #Check if the List is Empty:
            self.head = new_node
        else:    #Traverse to the End of the List:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display(self):
        tmp=list1.head
        while(tmp is not None):
            print(tmp.data)
            tmp=tmp.next
        
list1=DLL()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)

list1.display()
