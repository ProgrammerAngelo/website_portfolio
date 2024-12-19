class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue_App:
    def __init__(self):
        self.front = None
        self.rear = None

    # Method to enqueue a value
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            # If the queue is empty, both front and rear will point to the new node
            self.front = self.rear = new_node
        else:
            # Attach the new node to the rear and move the rear pointer
            self.rear.next = new_node
            self.rear = new_node

    # Method to dequeue a value
    def dequeue(self):
        if self.front is None:
            return None  # Return None if the queue is empty
        dequeued_value = self.front.data
        self.front = self.front.next
        if self.front is None:  # If the queue becomes empty, set rear to None as well
            self.rear = None
        return dequeued_value

    # Method to view the current state of the queue
    def view_queue(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements
