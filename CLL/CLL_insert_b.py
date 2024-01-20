class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, make the new node the only node and point to itself
            new_node.next = new_node
            self.head = new_node
        else:
            # If the list is not empty, insert the new node at the end
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def insert_at_b(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def display(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

c1 = CircularLinkedList()

# Inserting elements at the end
c1.insert_at_end(1)
c1.insert_at_end(2)
c1.insert_at_end(3)

# Displaying the circular linked list
print("Circular Linked List after inserting at the end:")
c1.display()

c1.insert_at_b(0)
c1.insert_at_b(7)

print("\nCircular Linked List after inserting at the beginning:")
c1.display()
