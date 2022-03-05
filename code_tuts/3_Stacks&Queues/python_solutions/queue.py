
'''
 FIFO - First in First Out Algorithm
'''
class Queue:
    def __init__(self) -> None:
        self.items = []
    
    # Check if the list is empty
    def isEmpty(self):
        return self.items == []
    
    # Insert at the rear (O(N)); elems have to be shifted to the right
    # If the list is empty, insertion will be of O(1)
    def enqueue(self, item):
        self.items.insert(0, item)
    
    # Remove element from the front of the list (pop); O(1)
    def dequeue(self):
        # pop() without index value, removes the element at the last index i.e (-1)
        return self.items.pop()
    
    def size(self):
        return f'The size of the queue is: {len(self.items)}'
    
    def printQueue(self):
        print(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue("First Item")
    q.enqueue("Item 1")
    q.enqueue("Item 2")
    q.enqueue("Item 3")
    q.enqueue("Last Item")
    q.printQueue()

    q.dequeue()
    q.printQueue()