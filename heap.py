class MinHeap:
    def __init__(self):
        self.arr = []

    def insert(self, value):
        if len(self.arr) == 0:
            self.arr.append(value)
        else:
            self.arr.append(value)
            parent_index = (len(self.arr) - 2)//2
            curr_index = len(self.arr) - 1
            while self.arr[parent_index] > self.arr[curr_index]:
                self.arr[parent_index], self.arr[curr_index] = self.arr[curr_index], self.arr[parent_index]
                parent_index, curr_index = curr_index, parent_index

    def extract(self):
        if len(self.arr) != 0:
            self.arr[0] = self.arr[len(self.arr) - 1]
            self.arr.pop(len(self.arr) - 1))

            curr_index = 0
            r_child = curr_index * 2 + 2
            l_child = curr_index * 2 + 1
            while (self.arr[curr_index] > self.arr[l_child]) or (self.arr[curr_index] > self.arr[r_child]):
                self.arr[curr_index], 
