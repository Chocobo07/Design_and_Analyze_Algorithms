class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = new_node
        new_node.prev = last

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_reverse(self):
        if not self.head:
            return
        
        current = self.head
        while current.next:
            current = current.next

        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

doubly = DoublyLinkedList()
doubly.append("Fool")
doubly.append("Manila Bay")
doubly.append("Feel so good")

doubly.prepend(0)
doubly.display()
doubly.display_reverse()