class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue_App:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return "Queue is empty!"
        dequeued_value = self.front.data
        self.front = self.front.next
        if self.front is None:  # If the queue becomes empty
            self.rear = None
        return dequeued_value

    def view_queue(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements  # type: ignore
