class Shelves:

    def __init__(self, amount):
        self.items=[0]*amount

    def add(self, x):
        self.items.append(x)
    
    def delete(self): 
        try:
            return self.items.pop(0)
        except:
            raise ValueError("Empty")

    def size(self):
        return len(self.items)

    def replace(self,position, objeto):
        self.items[position] = objeto
