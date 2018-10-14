from numpy import full, cos, sin, pi, matmul, array
import cv2


def rotate(p, a_x, a_y, a_z):
    sin_x = sin(a_x * (pi / 180))
    cos_x = cos(a_x * (pi / 180))

    sin_y = sin(a_y * (pi / 180))
    cos_y = cos(a_y * (pi / 180))

    sin_z = sin(a_z * (pi / 180))
    cos_z = cos(a_z * (pi / 180))

    rx = array([
        [1.0, 0.0, 0.0],
        [0.0, cos_x, -sin_x],
        [0.0, sin_x, cos_x],
    ])

    ry = array([
        [cos_y, 0.0, sin_y],
        [0.0, 1.0, 0.0],
        [-sin_y, 0.0, cos_y],
    ])

    rz = array([
        [cos_z, -sin_z, 0.0],
        [sin_z, cos_z, 0.0],
        [0.0, 0.0, 1.0],
    ])

    r = matmul(matmul(matmul(rx, ry), rz), p)

    return r


def project(point, observer, angles, focal_length, center):
    p_x, p_y, p_z = point
    o_x, o_y, o_z = observer
    a_x, a_y, a_z = angles

    x_center, y_center = center

    x = p_x - o_x
    y = p_y - o_y
    z = o_z - p_z

    p = array([x, y, z])
    r = rotate(p, a_x, a_y, a_z)

    x = r[0]
    y = r[1]
    z = r[2]

    # Draw visible points only
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

    def get_image(self, cam_x, cam_y, cam_z, ang_x, ang_y, ang_z, f):
        self.image = full((self.width, self.height, 1), 255.0)

        x_center = int(self.width / 2)
        y_center = int(self.height / 2)

        c = (x_center, y_center)
        o = (cam_x, cam_y, cam_z)
        a = (ang_x, ang_y, ang_z)

        points_2d = [*map(lambda p: project(p, o, a, f, c), self.points)]

        for pair in self.pairs:
            a_index = pair[0]
            b_index = pair[1]

            a_point = points_2d[a_index]
            b_point = points_2d[b_index]

            if (a_point is None) or (b_point is None):
                continue

            cv2.line(self.image, a_point, b_point, 0.0, 1)

        return self.image
