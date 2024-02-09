#!/usr/bin/python3
""" """
class Square():
    """ """
    width = 0
    height = 0

    
    def __init__(self, width = 0, height = 0):
        self.height = height
        self.width = width

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())