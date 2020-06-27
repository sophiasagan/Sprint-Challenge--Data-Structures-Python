class RingBuffer:
    def __init__(self, capacity): # initialize capacity
        self.capacity = capacity
        self.data = []
        self.cur_index = 0

    def append(self, item):
        if len(self.data) >= self.capacity: # if data is longer than capacity
            self.data[self.cur_index] = item #replace current node 
            self.cur_index = (self.cur_index + 1) % self.capacity #increment index

        else:
            self.data.append(item) # append item at the end

    def get(self):
        return self.data # return items from oldest to newest