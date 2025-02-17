class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, items):
        self.items.append(items)
    
    def pop(self):  
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)
    
    def view_stack(self):
        return self.items
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Current Stack:", stack.view_stack())

print("Stack size:", stack.size())
print("Pop element:", stack.peek())

print("Popped element:", stack.pop())
print("Popped element:", stack.pop())

print("Is stack empty?", stack.is_empty())

print("Popped element:", stack.pop())
print("Is stack empty?", stack.is_empty())

print("Popped element:", stack.pop())


