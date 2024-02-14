class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyLinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.length = 0

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.prev_node = None


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.prev_node = None

#######################
class DoublyLinkedList:
    def __init__(self):
        super().__init__()
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
            new_node.prev_node = new_node
            self.tail = new_node
        self.length += 1

    def __len__(self):
        return self.length

    def __getitem__(self, index:int):
        if not isinstance(index, int):
            raise TypeError
        node = self.head
        if index < 0:
            node = self.tail
            for i in range(abs(index)-1):
                node = node.prev_node
            return node.data
        else:
            for i in range(index):
                node = node.next_node
            return node.data
