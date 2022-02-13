class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False
        self.adjacent = []

    def add_adjacent(self, adjacent):
        self.adjacent.append(adjacent)

    def show_adjacent(self):
        for adjacent in self.adjacent:
            print(adjacent.vertex.label, adjacent.coast)

