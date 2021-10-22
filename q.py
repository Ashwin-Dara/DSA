class Queue:
    def __init__(self):
        self.q_list = []

    def add(self, item):
        self.q_list.append(item)

    def remove(self):
        if len(self.q_list) > 0:
            return self.q_list.pop(0)

    def get_item(self, index):
        if (index >= 0) and (index <= len(self.q_list) - 1):
            return self.q_list[index]
