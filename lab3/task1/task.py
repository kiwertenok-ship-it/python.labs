import abc


class Figure(abc.ABC):
    def __init__(self):
        self.coord = []

    @abc.abstractmethod
    def point_in_figure(self, xp, yp, coord):
        pass

    def move(self, x, y):
        coord_changes = (x, y)
        for j in range(2):
            for i in range(len(self.coord)):
                self.coord[i][j] += coord_changes[j]

    def is_intersect(self, other):
        other_points_inside = [self.point_in_figure(x, y, self.coord) for x, y in other.coord]
        if any(other_points_inside) and not all(other_points_inside):
            return True

        self_points_inside = [other.point_in_figure(x, y, other.coord) for x, y in self.coord]
        if any(self_points_inside) and not all(self_points_inside):
            return True

        return False


class Quad(Figure):

    def __init__(self, h1, h2, h3, h4):
        super().__init__()
        self.coord = [h1, h2, h3, h4]

    def point_in_figure(self, xp, yp, coord):
        min_x = min(coord[0][0], coord[1][0], coord[2][0], coord[3][0])
        max_x = max(coord[0][0], coord[1][0], coord[2][0], coord[3][0])
        min_y = min(coord[0][1], coord[1][1], coord[2][1], coord[3][1])
        max_y = max(coord[0][1], coord[1][1], coord[2][1], coord[3][1])

        return min_x <= xp <= max_x and min_y <= yp <= max_y


class Pentagon(Figure):

    def __init__(self, h1, h2, h3, h4, h5):
        super().__init__()
        self.coord = [h1, h2, h3, h4, h5]

    def point_in_figure(self, xp, yp, coord):
        ans = False
        n = len(coord)
        for i in range(n):
            x1, y1 = coord[i]
            x2, y2 = coord[(i + 1) % n]

            if ((y1 > yp) != (y2 > yp)) and (xp < (x2 - x1) * (yp - y1) / (y2 - y1) + x1):
                ans = not ans
        return ans


f1 = Quad([0, 0], [1, 0], [1, 1], [0, 1])
print("Квадрат - ", *f1.coord)
f1.move(3, 0)
f2 = Pentagon([-4, 1], [-2, 4], [2, 5], [5, 2], [0, -3])
print(f1.is_intersect(f2))
print("Квадрат - ", *f1.coord)
print("Пятиугольник - ", *f2.coord)