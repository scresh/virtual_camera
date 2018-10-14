from numpy import full, cos, sin, pi
import cv2


def project(point, observer, x_center, y_center, focal_length):
    p_x, p_y, p_z = point
    o_x, o_y, o_z = observer

    x = p_x - o_x
    y = p_y - o_y
    z = o_z - p_z
 
    if z > 0:
        of = focal_length / z
    else:
        return None

    x = int(x * of)
    y = int(y * of)

    x = x_center + x
    y = y_center - y

    return x, y


class Figure:
    def __init__(self, points, pairs):
        self.points = points
        self.pairs = pairs


class Canvas:
    def __init__(self, width=640, height=640):
        self.points = []
        self.pairs = []
        self.width = width
        self.height = height
        self.image = None

    def add_figure(self, figure):
        for k, v in figure.points.items():
            if v not in self.points:
                self.points.append(v)

        for pair in figure.pairs:
            a_point = figure.points[pair[0]]
            b_point = figure.points[pair[1]]
            self.pairs.append((self.points.index(a_point), self.points.index(b_point)))

    def get_image(self, cam_x, cam_y, cam_z, focal_length):
        self.image = full((self.width, self.height, 1), 255.0)

        x_center = int(self.width / 2)
        y_center = int(self.height / 2)
        o = (cam_x, cam_y, cam_z)

        points_2d = [*map(lambda p: project(p, o, x_center, y_center, focal_length), self.points)]

        for pair in self.pairs:
            a_index = pair[0]
            b_index = pair[1]

            a_point = points_2d[a_index]
            b_point = points_2d[b_index]

            if (a_point is None) or (b_point is None):
                continue

            cv2.line(self.image, a_point, b_point, 0.0, 1)

        return self.image
