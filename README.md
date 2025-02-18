# Design_and_Analyze_Algorithms
 TP in DAA
**Data Structured covered:**
    LinkedList (Singly,Doubly,Cicular)
    Queues/Stack/Heap
    Graphs
    Trees

**Singly Linked list:**
A Singly Linked List is a data structure that consists of a sequence of elements called nodes. Each node contains:

Data: The actual value stored in the node.
Next: A pointer/reference to the next node in the sequence.
In a singly linked list, each node points only to the next node, and the last node's next reference is set to null.
![alt text](image.png)

**Advantages:**
Dynamic size: It can grow or shrink as needed without pre-allocating space.
Efficient insertion/deletion at the beginning or middle (compared to arrays).
**Disadvantages:**
No direct access to elements (sequential access).
More memory used because each node stores a pointer.

Code Snippet:
class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node (initially None)

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Head of the list (initially None, empty list)

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:  # If the list is empty
            self.head = new_node  # The new node becomes the head
            return  # Exit the function

        last = self.head  # Start from the head to find the last node
        while last.next:  # Traverse the list until the next node is None
            last = last.next  # Move to the next node
        last.next = new_node  # The last node's next pointer points to the new node

    def display(self):
        current = self.head  # Start from the head
        while current:  # Traverse the list until the current node is None
            print(current.data, end=" -> ")  # Print the data of the current node
            current = current.next  # Move to the next node
        print("None")  # Print "None" to indicate the end of the list

# Example Usage (explained below):
linklist = SinglyLinkedList()
linklist.append("Fool")
linklist.append("Manila Bay")
linklist.append("Feel so good")
linklist.display()  # Output: Fool -> Manila Bay -> Feel so good -> None

Use case:
A song playlist, you can easily add or remove a song in the playlist. Each song points to the next one just like the output on the code.

Doubly Linked List:
A Doubly Linked List is a data structure similar to a singly linked list, but with an additional feature:

Each node contains two pointers:
Next: Points to the next node in the list.
Prev: Points to the previous node in the list.
This allows traversal in both directions (forward and backward).
![alt text](image-1.png)

Advantages:
Bidirectional traversal: Can easily traverse both forward and backward.
Efficient deletion/insertion: Easy to insert or delete nodes from both ends or in the middle, without needing to traverse the list.
Disadvantages:
Extra memory: Each node uses extra memory to store the Prev pointer.
Slightly more complex operations due to handling two pointers.

Code snippet:

class Node:
    def __init__(self, data):
        self.data = data      # Data stored in the node
        self.next = None      # Pointer to the next node (initially None)
        self.prev = None      # Pointer to the previous node (initially None)

class DoublyLinkedList:
    def __init__(self):
        self.head = None      # Head of the list (initially None)

    def append(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:      # If the list is empty
            self.head = new_node  # New node is both head and tail
            return

        last = self.head      # Start from the head to find the last node
        while last.next:      # Traverse until the next node is None
            last = last.next  # Move to the next node
        last.next = new_node  # Link the last node to the new node
        new_node.prev = last  # Link the new node back to the last node

    def prepend(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # New node's next points to the current head
        if self.head:          # If the list is not empty
            self.head.prev = new_node  # Current head's prev points to the new node
        self.head = new_node      # New node becomes the new head

    def display(self):
        current = self.head      # Start from the head
        while current:          # Traverse until the current node is None
            print(current.data, end=" <-> ")  # Print the data
            current = current.next  # Move to the next node
        print("None")          # Mark the end of the list

    def display_reverse(self):
        if not self.head:
            return

        current = self.head      # Start from the head
        while current.next:      # Traverse to the end of the list
            current = current.next

        while current:          # Traverse backwards
            print(current.data, end=" <-> ")
            current = current.prev  # Move to the previous node
        print("None")          # Mark the end of the list

Use case:
A song or a playlist you can play the next song or the previous song. A web browser history you can go to the next url or the previous url.
