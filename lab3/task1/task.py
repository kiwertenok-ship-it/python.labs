import abc


class Figure(abc.ABC):
    def __init__(self):
        self.coord = []

    def point_in_figure(self, xp, yp, coord):
        pass

    def move(self, x, y):
        coord_changes = (x, y)
        for j in range(2):
            for i in range(len(self.coord)):
                self.coord[i][j] += coord_changes[j]

    def is_intersect(self, other):
        if any(self.point_in_figure(x, y, self.coord) for x, y in other.coord) \
                and any(not (self.point_in_figure(x, y, self.coord)) for x, y in other.coord):
            return True
        if any(other.point_in_figure(x, y, other.coord) for x, y in self.coord) \
                and (any(not (other.point_in_figure(x, y, other.coord)) for x, y in self.coord)):
            return True
        return False


class Quad(Figure):

    def __init__(self, h1, h2, h3, h4):
        super().__init__()
        self.coord = [h1, h2, h3, h4]

    @staticmethod
    def point_in_figure(xp, yp, coord):
        if (coord[0][0]) <= xp <= (coord[1][0]) and (coord[0][1] <= yp <= coord[2][1]):
            return True
        return False


class Pentagon(Figure):

    def __init__(self, h1, h2, h3, h4, h5):
        super().__init__()
        self.coord = [h1, h2, h3, h4, h5]

    @staticmethod
    def point_in_figure(xp, yp, coord):
        ans = False
        for i in range(len(coord)):
            if (((coord[i][1] <= yp <= coord[i - 1][1]) or (coord[i - 1][1] <= yp <= coord[i][1])) and
                    (xp >= (coord[i - 1][0] - coord[i][0]) * (yp - coord[i][1]) / (coord[i - 1][1] - coord[i][1]) + coord[i][1])):
                ans = not ans
        return ans

f1 = Quad([0, 0], [1, 0], [1, 1], [0, 1])
print("Квадрат - ", *f1.coord)
f1.move(3, 0)
f2 = Pentagon([-4, 1], [-2, 4], [2, 5], [5, 2], [0, -3])
print(f1.is_intersect(f2))
print("Квадрат - ", *f1.coord)
print("Пятиугольник - ", *f2.coord)