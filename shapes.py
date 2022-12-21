# whenever string literals are present after the definition
# of a function, module, class, or method, they are associated
# with the object as their __doc__ attribute -> shapes.__doc__

# single-line docstring convention: triple quote, should not be
# descriptive but rather say """do this, return that"""

class Shapes:
    """shapes class"""
    def __init__(self, sides):
        """
        initializes sides and name attribute
        :param sides: (int) number of sides of shape
        """
        self.sides = 0
        self.name = ""

    def add_name(self, name):
        """
        takes in name, assigns name attribute
        :param name: (str)
        """
        self.name = name

    def get_name(self):
        """returns name"""
        return self.name


triangle = Shapes(3)
triangle.add_name("Triangle")
print(triangle.get_name())
print(Shapes.__doc__)
