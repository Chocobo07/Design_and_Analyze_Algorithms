import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            return None
        
    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None
        
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0
    
min_heap = MinHeap()
min_heap.push(5)
min_heap.push(1)
min_heap.push(9)
min_heap.push(2)

print("Heap size:", min_heap.size())
print("Smallest element:", min_heap.peek())

print("Is heap empty?", min_heap.is_empty())

print("Popped element:", min_heap.pop())
print("Popped element:", min_heap.pop())
print("Is heap empty?", min_heap.is_empty())
print("Popped element:", min_heap.pop())
