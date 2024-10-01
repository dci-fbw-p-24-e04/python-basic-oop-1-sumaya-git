"""
Queue may be implemented with Lists just as Stacks. But deque are preferred
because they allowed optimized accessing/deleting from both ends.

Deleting from the front of a list is O(n) as all other elements need to be shifted

Also, with deque, we can implement double-ended Queues.
"""

from collections import deque


class Queue:
    def __init__(self):
        self._data = deque()

    def is_empty(self):
        # TODO: Replace 'pass' with your code
        pass

    @property
    def size(self):
        # TODO: Replace 'pass' with your code
        pass

    def enqueue(self, item):
        # TODO: Replace 'pass' with your code
        pass

    def peek(self):
        # TODO: Replace 'pass' with your code
        pass

    def dequeue(self):
        # TODO: Replace 'pass' with your code
        pass

    def __str__(self) -> str:
        return str(self._data)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(0)
    q.enqueue(1)
    print(q)
    print("Size of Queue: ", q.size)
    print("Peek the Queue: ", q.peek())
    print("Pop from Queue: ", q.dequeue())
    print("Peek the Queue: ", q.peek())
    print("Size of Queue: ", q.size)
    print("Pop from Queue: ", q.dequeue())
    print("Size of Queue: ", q.size)
    print("Peek the Queue: ", q.peek())
