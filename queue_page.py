class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None  # For the double-ended queue (Deque)

class Deque_App:
    def __init__(self):
        self.front = None
        self.rear = None

    # Simple Queue Methods
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None  # Empty Queue
        dequeued_value = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None  # Queue becomes empty
        return dequeued_value

    def view_deque(self):
        current = self.front
        queue = []
        while current:
            queue.append(current.data)
            current = current.next
        return queue

    # Double-Ended Queue (Deque) Methods
    def push(self, data):
        new_node = Node(data)
        if self.front is None:  # If the deque is empty
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def pop(self):
        if self.front is None:  # If deque is empty
            return None
        popped_value = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None  # Deque becomes empty
        return popped_value

    def inject(self, data):
        new_node = Node(data)
        if self.rear is None:  # If deque is empty
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def eject(self):
        if self.rear is None:  # If deque is empty
            return None
        ejected_value = self.rear.data
        self.rear = self.rear.prev
        if self.rear:
            self.rear.next = None
        else:
            self.front = None  # Deque becomes empty
        return ejected_value
