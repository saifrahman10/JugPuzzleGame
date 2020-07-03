class Jug:
    def __init__(self, cap=3):
        self.capacity = cap
        self.amount = 0

    def fill(self):
        self.amount = self.capacity

    def is_empty(self):
        return self.capacity == 0

    def empty(self):
        self.amount = 0