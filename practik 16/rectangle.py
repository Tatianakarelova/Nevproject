class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    @property
    def getArea(self):
        return self.width * self.height
