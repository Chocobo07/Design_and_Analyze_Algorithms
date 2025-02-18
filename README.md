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

**Code Snippet:**
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

linklist = SinglyLinkedList()
linklist.append("Fool")
linklist.append("Manila Bay")
linklist.append("Feel so good")
linklist.display()  # Output: Fool -> Manila Bay -> Feel so good -> None

**Use case:**
A song playlist, you can easily add or remove a song in the playlist. Each song points to the next one just like the output on the code.

 -----------------------------------------------------------------------------------------------------------------------------------------------------------------
**Doubly Linked List:**
A Doubly Linked List is a data structure similar to a singly linked list, but with an additional feature:

Each node contains two pointers:
Next: Points to the next node in the list.
Prev: Points to the previous node in the list.
This allows traversal in both directions (forward and backward).
![alt text](image-1.png)

**Advantages:**
Bidirectional traversal: Can easily traverse both forward and backward.
Efficient deletion/insertion: Easy to insert or delete nodes from both ends or in the middle, without needing to traverse the list.
**Disadvantages:**
Extra memory: Each node uses extra memory to store the Prev pointer.
Slightly more complex operations due to handling two pointers.

**Code snippet:**

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

**Use case:**
A song or a playlist you can play the next song or the previous song. A web browser history you can go to the next url or the previous url.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

**Cirular Linked List**
A Circular Linked List is a variation of a linked list where:

The last node points back to the first node instead of having a null reference.
This creates a circular structure, where you can loop through the list continuously from any node.
Circular linked lists can be singly or doubly linked, depending on whether each node contains one or two pointers (next and/or prev).
![alt text](image-3.png)

**Advantages:**
Efficient circular traversal: You can easily traverse the list in a loop, which is useful in applications like round-robin scheduling.
No need for null pointers: The structure is self-referential, so no null pointers are required to mark the end.
Efficient for continuous operations: Especially useful for problems involving cycles or repeated operations.
**Disadvantages:**
Complexity: Slightly more complex to manage due to circular references.
Memory management: Can be tricky in cases of frequent insertion/deletion, especially when loops are involved.

class Node:
    def __init__(self, data):
        self.data = data      # Data stored in the node
        self.next = None      # Pointer to the next node (initially None)

class CircularLinkedList:
    def __init__(self):
        self.head = None      # Head of the list (initially None)

    def append(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:      # If the list is empty
            self.head = new_node  # New node is the head
            new_node.next = self.head  # Make it circular (points to itself)
            return

        current = self.head      # Start from the head to find the last node
        while current.next != self.head:  # Traverse until we reach the last node
            current = current.next  # Move to the next node
        current.next = new_node  # Link the last node to the new node
        new_node.next = self.head  # Link the new node back to the head (circular)

    def display(self):
        if not self.head:
            return

        current = self.head      # Start from the head
        while True:              # Loop indefinitely (until we break)
            print(current.data, end=" -> ")  # Print the data
            current = current.next  # Move to the next node
            if current == self.head:  # Check if we've come back to the head
                break              # Exit the loop
        print("None")          # Mark the end (although it's circular)


# Example Usage (explained below):
cll = CircularLinkedList()
cll.append("Fool")
cll.append("Manila Bay")
cll.append("Feel so good")
cll.display()  # Output: Fool -> Manila Bay -> Feel so good -> None


# Explanation of the example usage:

# 1. cll = CircularLinkedList():
#    - Creates an empty circular linked list.  self.head is None.

# 2. cll.append("Fool"):
#    - Creates a new node with data "Fool".
#    - Since the list is empty, this node becomes the head.
#    - Crucially, its next pointer is set to itself, making it circular.

# 3. cll.append("Manila Bay"):
#    - Creates a new node with data "Manila Bay".
#    - The code traverses from the head ("Fool") to find the last node (which is currently "Fool" itself).
#    - The "Fool" node's next pointer is set to the "Manila Bay" node.
#    - The "Manila Bay" node's next pointer is set back to the head ("Fool"), completing the circle.

# 4. cll.append("Feel so good"):
#    - Creates a new node with data "Feel so good".
#    - The code traverses from the head ("Fool") until it finds the last node ("Manila Bay").
#    - The "Manila Bay" node's next pointer is set to the "Feel so good" node.
#    - The "Feel so good" node's next pointer is set back to the head ("Fool"), maintaining the circular structure.

# 5. cll.display():
#    - Starts at the head ("Fool").
#    - Prints the data and moves to the next node.
#    - Continues until it comes back to the head ("Fool") again.  This is how it knows it has traversed the entire circular list.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Queue**
A Queue is a linear data structure that follows the First In, First Out (FIFO) principle. This means that the first element added to the queue will be the first one to be removed, similar to a queue in real life (like a line at a coffee shop).
![alt text](image-4.png)

**Advantages:**
Simple and efficient for managing sequential data.
Ensures fair processing with FIFO order.
Useful for handling tasks in various applications like IO buffering or task scheduling.
**Disadvantages:**
Limited access: Only the front element can be accessed directly.
Fixed size (in some implementations), which may require resizing or cause overflow.

**Code snippet:**
class Queue:
    def __init__(self):
        self.items = []  # Use a list to store queue elements

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)  # Add to the rear (end)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove from the front (beginning)
        else:
            return None  # Or raise an exception

    def peek(self):
        if not self.is_empty():
            return self.items[0]  # Return the front element without removing it
        else:
            return None

    def size(self):
        return len(self.items)

    def view_queue(self):
        return self.items  # Return the queue as a list

# Example usage (explained below):
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Current queue:", queue.view_queue())  # Output: Current queue: [1, 2, 3]

print("Queue size:", queue.size())  # Output: Queue size: 3
print("Front element:", queue.peek())  # Output: Front element: 1

print("Dequeued element:", queue.dequeue())  # Output: Dequeued element: 1
print("Dequeued element:", queue.dequeue())  # Output: Dequeued element: 2

print("Is queue empty?", queue.is_empty())  # Output: Is queue empty? False

print("Dequeued element:", queue.dequeue())  # Output: Dequeued element: 3
print("Is queue empty?", queue.is_empty())  # Output: Is queue empty? True

print("Dequeued Element:", queue.dequeue())  # Output: Dequeued Element: None


# Explanation of the example usage:

# 1. queue = Queue():
#    - Creates an empty queue.  self.items is initialized as an empty list [].

# 2. queue.enqueue(1), queue.enqueue(2), queue.enqueue(3):
#    - Adds elements to the *rear* of the queue.
#    - The queue now looks like this: [1, 2, 3] (1 is at the front, 3 is at the rear).

# 3. print("Current queue:", queue.view_queue()):
#    - Prints the current state of the queue.

# 4. print("Queue size:", queue.size()):
#    - Prints the number of elements in the queue (3 at this point).

# 5. print("Front element:", queue.peek()):
#    - Prints the element at the front of the queue *without* removing it (1).

# 6. print("Dequeued element:", queue.dequeue()):
#    - Removes and returns the element at the *front* of the queue (1).
#    - The queue is now: [2, 3]

# 7. print("Dequeued element:", queue.dequeue()):
#    - Removes and returns the element at the front of the queue (2).
#    - The queue is now: [3]

# 8. print("Is queue empty?", queue.is_empty()):
#    - Checks if the queue is empty (it's not, it has one element).

# 9. print("Dequeued element:", queue.dequeue()):
#    - Removes and returns the element at the front of the queue (3).
#    - The queue is now empty: []

# 10. print("Is queue empty?", queue.is_empty()):
#     - Checks if the queue is empty (it is now).

# 11. print("Dequeued Element:", queue.dequeue()):
#     - Tries to dequeue from an empty queue.  Returns None.

**Use case:**
A line of people ordering in a coffee shop, The first one in the line will be the first one to order and get out of the line, if a new customer will order he/she needs to be at the end of  the line becoming the tail.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Stack**
A Stack is a linear data structure that follows the Last In, First Out (LIFO) principle. This means the last element added to the stack is the first one to be removed, similar to a stack of plates where you take the top plate first.
![alt text](image-2.png)

**Advantages:**
Simple and efficient for operations like adding/removing from the top.
Useful for problems that need to track the order of operations in a reversible manner.
**Disadvantages:**
Limited access: You can only access the top element, not the ones below it.
Fixed size (in some implementations), leading to overflow when the stack is full.

**Code snippet:**
class Stack:
    def __init__(self):
        self.items = []  # Use a list to store stack elements

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):  # Corrected: parameter name should be 'item', not 'items'
        self.items.append(item)  # Add to the top

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove and return the top element
        else:
            return None  # Or raise an exception

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Return the top element without removing it
        else:
            return None

    def size(self):
        return len(self.items)

    def view_stack(self):
        return self.items  # Return the stack as a list


# Example usage (explained below):
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Current Stack:", stack.view_stack())  # Output: Current Stack: [1, 2, 3]

print("Stack size:", stack.size())  # Output: Stack size: 3
print("Top element:", stack.peek())  # Output: Top element: 3

print("Popped element:", stack.pop())  # Output: Popped element: 3
print("Popped element:", stack.pop())  # Output: Popped element: 2

print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False

print("Popped element:", stack.pop())  # Output: Popped element: 1
print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? True

print("Popped element:", stack.pop())  # Output: Popped element: None


# Explanation of the example usage:

# 1. stack = Stack():
#    - Creates an empty stack. self.items is initialized as an empty list [].

# 2. stack.push(1), stack.push(2), stack.push(3):
#    - Adds elements to the *top* of the stack.
#    - The stack now looks like this: [1, 2, 3] (3 is at the top).

# 3. print("Current Stack:", stack.view_stack()):
#    - Prints the current state of the stack.

# 4. print("Stack size:", stack.size()):
#    - Prints the number of elements in the stack (3 at this point).

# 5. print("Top element:", stack.peek()):
#    - Prints the element at the top of the stack *without* removing it (3).

# 6. print("Popped element:", stack.pop()):
#    - Removes and returns the element at the *top* of the stack (3).
#    - The stack is now: [1, 2]

# 7. print("Popped element:", stack.pop()):
#    - Removes and returns the element at the top of the stack (2).
#    - The stack is now: [1]

# 8. print("Is stack empty?", stack.is_empty()):
#    - Checks if the stack is empty (it's not, it has one element).

# 9. print("Popped element:", stack.pop()):
#    - Removes and returns the element at the top of the stack (1).
#    - The stack is now empty: []

# 10. print("Is stack empty?", stack.is_empty()):
#     - Checks if the stack is empty (it is now).

# 11. print("Popped element:", stack.pop()):
#     - Tries to pop from an empty stack. Returns None.

**Use case:**
A stack of books, to get the book at the bottom, you need to remove the books at the top first, otherwise the stack will collapse.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Heap**
A Heap is a special type of binary tree that satisfies the heap property. There are two main types of heaps:

Max Heap: The value of each node is greater than or equal to the values of its children. The largest value is at the root.
Min Heap: The value of each node is less than or equal to the values of its children. The smallest value is at the root.
![alt text](image-6.png)
