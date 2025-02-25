class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
        
    def size(self):
        return len(self.items)
    
    def view_queue(self):
        return self.items
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Current queue:",queue.view_queue())

print("Queue size:", queue.size())
print("Front element:", queue.peek())

print("Dequed element:", queue.dequeue())
print("Dequed element:", queue.dequeue())

print("Is queue empty?", queue.is_empty())

print("Dequed element:", queue.dequeue())
print("Is queue empty?", queue.is_empty())

print("Dequed Element:", queue.dequeue())
