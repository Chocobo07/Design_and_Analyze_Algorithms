class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ->")
            current = current.next
        print("None")

linklist = SinglyLinkedList()
linklist.append("Fool")
linklist.append("Manila Bay")
linklist.append("Feel so good")
linklist.display()