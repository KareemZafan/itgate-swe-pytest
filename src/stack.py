
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        popped_item = self.items[-1]
        self.items.pop()
        return popped_item
    
    def get_peek(self):
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def get_stack_size(self):
        return len(self.items)
    
    def get_stack_items(self):
        return self.items
    
    def clear_stack(self):
        for i in range(len(self.items)):
            self.items.pop()

    
