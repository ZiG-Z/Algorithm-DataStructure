class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        if self.is_empty():
            return "This is no item in the stack"
        else:
            return len(self.items)
        