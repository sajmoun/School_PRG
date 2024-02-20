class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.prev_node = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node
        self.length += 1

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError
        if abs(index) >= self.length:
            raise IndexError("Index out of range")

        if index < 0:
            node = self.tail
            for i in range(abs(index) - 1):
                node = node.prev_node
        else:
            node = self.head
            for i in range(index):
                node = node.next_node

        return node.data

    def __setitem__(self, index, data):
        if not isinstance(index, int):
            raise TypeError
        if abs(index) >= self.length:
            raise IndexError("Index out of range")

        if index < 0:
            node = self.tail
            for i in range(abs(index) - 1):
                node = node.prev_node
        else:
            node = self.head
            for i in range(index):
                node = node.next_node

        node.data = data

    def __delitem__(self, index):
        if not isinstance(index, int):
            raise TypeError
        if abs(index) >= self.length:
            raise IndexError("Index out of range")

        if index < 0:
            node = self.tail
            for i in range(abs(index) - 1):
                node = node.prev_node
        else:
            node = self.head
            for i in range(index):
                node = node.next_node

        if node.prev_node:
            node.prev_node.next_node = node.next_node
        else:
            self.head = node.next_node

        if node.next_node:
            node.next_node.prev_node = node.prev_node
        else:
            self.tail = node.prev_node

        self.length -= 1

    def __iter__(self):
        node = self.head
        result = []
        while node:
            result.append(node.data)
            node = node.next_node
        return iter(result)

    def insert(self, data, position):
        if not isinstance(position, int):
            raise TypeError
        if position < 0 or position > self.length:
            raise IndexError("Index out of range")

        new_node = Node(data)

        if position == 0:
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next_node = self.head
                self.head.prev_node = new_node
                self.head = new_node
        elif position == self.length:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node
        else:
            current = self.head
            for i in range(position - 1):
                current = current.next_node

            new_node.prev_node = current
            new_node.next_node = current.next_node
            current.next_node.prev_node = new_node
            current.next_node = new_node

        self.length += 1
        
