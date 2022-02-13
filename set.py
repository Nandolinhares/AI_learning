class Set:

    def __init__(self, array):
        self.array = array

    def insert(self, number_to_insert):
        position_to_insert = 0
        self.array.append(0)

        for i in range(len(self.array)):
            position_to_insert = i
            if self.array[i] >= number_to_insert:
                break
        last_position = len(self.array) - 1
        while last_position >= position_to_insert:
            self.array[last_position] = self.array[last_position - 1]
            if last_position == position_to_insert:
                self.array[last_position] = number_to_insert
            last_position -= 1

    def print(self):
        print(self.array)
