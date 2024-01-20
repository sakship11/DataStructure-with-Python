class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_e(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def insert_m(self, prev_node, data):
        new_node = Node(data)
        if not self.head:
            print("Cannot insert after a previous node. List is empty.")
            return
        temp = self.head
        while temp.next != self.head and temp.data != prev_node:
            temp = temp.next

        if temp.data != prev_node:
            print(f"Node with data {prev_node} not found.")
        else:
            new_node.next = temp.next
            temp.next = new_node

    def display(self):
        if self.head is None:
            print("Circular Linked List is empty.")
            return
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

c1 = CLL()

c1.insert_e(1)
c1.insert_e(2)
c1.insert_e(3)

print("Circular Linked List after inserting at the end:")
c1.display()


c1.insert_m(2, 4)

print("\nCircular Linked List after inserting after a previous node:")
c1.display()
