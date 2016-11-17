class Point(object):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return '{0}, {1}'.format(self.x, self.y)

    def __add__(self, other):
        return self.x + other.x, self.y + other.y


p1 = Point(5, 10)
p2 = Point(5, 10)

print p1 + p2
