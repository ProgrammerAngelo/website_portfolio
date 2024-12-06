class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_beginning(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if not self.head:  # If list becomes empty, update tail
            self.tail = None
        return removed_data

    def remove_at_end(self):
        if not self.head:
            return None
        if self.head == self.tail:  # Only one node
            removed_data = self.head.data
            self.head = None
            self.tail = None
            return removed_data
        current = self.head
        while current.next != self.tail:
            current = current.next
        removed_data = self.tail.data
        current.next = None
        self.tail = current
        return removed_data

    def remove_at(self, data):
        if not self.head:
            return None
        if self.head.data == data:  # Remove from beginning
            return self.remove_beginning()
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if not current.next:  # Data not found
            return None
        removed_data = current.next.data
        current.next = current.next.next
        if current.next is None:  # Update tail if last node was removed
            self.tail = current
        return removed_data

    def printLinkedList(self):
        current_node = self.head
        result = []
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return result
