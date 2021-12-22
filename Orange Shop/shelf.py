class Shelf:
    def __init__(self):
        self.items=[]

    def add(self, x):
        self.items.append(x)
    
    def delete(self): 
        try:
            return self.items.pop(0)
        except:
            raise ValueError("Empty")

    def size(self):
        return len(self.items)