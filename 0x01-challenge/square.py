#!/usr/bin/python3
"""x """


class Square():
    """x """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """x """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ x"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ x"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ x"""

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
