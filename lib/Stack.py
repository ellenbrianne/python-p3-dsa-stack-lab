class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return True if not self.items else False

    def push(self, item):
        self.items.append(item) if len(self.items) < self.limit else None

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return True if self.limit == len(self.items) else False

    def search(self, target):
        search = -1
        if target in self.items:
            search = (len(self.items) - 1) - self.items.index(target)
            return search
        else:
            return search
