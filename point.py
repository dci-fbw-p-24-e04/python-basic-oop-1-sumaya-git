
import math

class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x= x
        self.y= y

    def move(self, x, y):
        self.x= x
        self.y= y

    def reset(self):
        self.x= 0
        self.y= 0

    def calc_distance(self, other):
        self.other= other
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

        
    


if __name__ == "__main__":
    p1 = Point()
    p2 = Point()

    p1.reset()
    p2.reset()

    print(p1.x, p1.y)
    print(p2.x, p2.y)

    p1.move(4, 7)
    p2.move(6, 2)

    print("After moving")
    print(p1.x, p1.y)
    print(p2.x, p2.y)

    print("find difference")
    print(p1.calc_distance(p2))
