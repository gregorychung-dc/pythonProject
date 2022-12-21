class Shapes:
    def __init__(self, sides):
        self.sides = 0
        self.name = ""

    def add_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


triangle = Shapes(3)

triangle.add_name("Triangle")

print(triangle.get_name())

# slicing operation
shapeName = "decagon"

print(shapeName[-2:-5:-1])
