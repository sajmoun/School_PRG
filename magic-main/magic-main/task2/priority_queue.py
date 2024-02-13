class PriorityQueue:
    def __init__(self):
        self.tasks = []

    def push(self, task, priority):
        self.tasks.append((priority, task))
        self.tasks.sort(reverse=True)

    def pop(self):
        if not self.tasks:
            raise IndexError("pop from an empty priority queue")
        return self.tasks.pop()[1]

    def __len__(self):
        return len(self.tasks)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.tasks:
            raise StopIteration
        return self.pop()

# Test
priority_queue = PriorityQueue()
priority_queue.push("Task 1", 3)
priority_queue.push("Task 2", 1)
priority_queue.push("Task 3", 2)

print("Priority Queue Length:", len(priority_queue))

print("Processing tasks in Priority Order:")
for task in priority_queue:
    print("Processing:", task)

# Additional Tests
def test_empty_pop():
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.pop()

def test_iteration():
    pq = PriorityQueue()
    pq.push("Task 1", 3)
    pq.push("Task 2", 1)
    pq.push("Task 3", 2)

    tasks = list(pq)
    assert tasks == ["Task 2", "Task 3", "Task 1"]
