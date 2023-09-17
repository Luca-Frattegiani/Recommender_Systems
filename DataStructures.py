class MaxHeap:
    
    #Constructor:
    def __init__(self):
        self.keys = [(0, None)]
        self.size = 0
        
    #Obtain parents and children of each item stored in the MaxHeap:
    def parent(self, position):
        return position//2
    
    def left(self, position):
        return position*2
    
    def right(self, position):
        return (position*2) + 1
    
    def maxchild(self, position):
        if self.left(position) >= self.size:
            return self.left(position)
        else:
            if self.keys[self.left(position)][0] > self.keys[self.right(position)][0]:
                return self.left(position)
            else:
                return self.right(position)
    
    #Methods to travers and re-order the MaxHeap:
    def unheap(self, position):
        while self.parent(position) > 0:
            if self.keys[position][0] > self.keys[self.parent(position)][0]:
                self.keys[position], self.keys[self.parent(position)] = self.keys[self.parent(position)], self.keys[position]
            position = self.parent(position)
    
    def downheap(self, position):
        while self.left(position) <= self.size:
            upper = self.maxchild(position)
            if self.keys[upper][0] > self.keys[position][0]:
                self.keys[position], self.keys[upper] = self.keys[upper], self.keys[position]
            position = upper
            
    #Insert/Remove elements:
    
    def insert(self, key, item = None):
        self.keys.append((key, item))
        self.size += 1
        self.unheap(self.size)
    
    def delete(self):
        if len(self.keys) == 1:
            print("Empty MaxHeap")
            return None
        else:
            root = self.keys[1]
            
            self.keys[1] = self.keys[self.size]
            self.keys.pop()
            self.size -= 1
            
            self.downheap(1)
            return root
        
    #Other Utilities:
    def to_string(self, i, depth = 0):
        ret = ""

        if self.right(i) <= self.size:
            ret += self.to_string(self.right(i), depth + 1)

        ret += "\n" + ("    "*depth) + str(self.keys[i])

        if self.left(i) <= self.size:
            ret += self.to_string(self.left(i), depth + 1)

        return ret
    
    def __str__(self):
        if self.size > 0:
            return self.to_string(1)
        return "[]"
    
    def copy(self):
        new = MaxHeap()
        new.keys = self.keys.copy()
        new.size = self.size
        return new
    
    def show(self):
        new = self.copy()
        while new.size > 0:
            print(new.delete())
            
class Queue_c:
    
    #Constructor:
    def __init__(self, size):
        self.queue = [(None, None) for element in range(0, size)]
        self.back = size - 1 #Index for insertions
        self.front = 0 #Index for deletions
        self.size = size
        self.n = 0
    
    #Adding objects:
    def enqueue(self, key, item = None):
        if self.is_full():
            return "Full Queue"
        else:
            self.back = (self.back + 1) % (self.size)
            self.queue[self.back] =  (key, item)
            self.n += 1
        
    #Removing objects:
    def dequeue(self):
        if self.is_empty():
            return "Empty Queue"
        else:
            removed = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % (self.size)
            self.n -= 1
            return removed
    
    #Other utilities
    def is_empty(self):
        return self.n == 0
    
    def is_full(self):
        return self.n == self.size
    
    def size_(self):
        return self.size
    
    def first_in(self):
        return self.queue[self.front]
    
    def __str__(self):
        print(self.queue)