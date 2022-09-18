import itertools


class SlidingWindow:
    def __init__(self, n):
        self.n = n
        self.queue = []
        combinations = list(itertools.product(range(3), repeat=self.n))
        self.history = {c: 0 for c in combinations}

    def update(self, item):
        is_full = True if len(self.queue) == self.n else False
        if is_full:
            record = tuple(self.queue)
            self.history[record] += 1
            self.dequeue()
        self.enqueue(item)

    def dequeue(self):
        for i in range(self.n - 1):
            self.queue[i] = self.queue[i + 1]
        del self.queue[-1]

    def enqueue(self, item):
        self.queue.append(item)

    def is_same_item(self):
        return True if len(set(self.queue)) == 1 else False
