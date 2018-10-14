import cv2
from geometry import Canvas, Figure, rotate


def main():
    axes = Figure(
        points={'O': (0, 0, 0), 'X': (512, 0, 0), 'Y': (0, 512, 0), 'Z': (0, 0, 512)},
        pairs=(('O', 'X'), ('O', 'Y'), ('O', 'Z')),
    )

    tetrahedron = Figure(
        points={'A1': (0, 0, 222), 'B1': (128, 0, 222), 'C1': (64, 0, 112), 'D1': (64, 104, 184)},
        pairs=(('A1', 'B1'), ('B1', 'C1'), ('C1', 'A1'), ('A1', 'D1'), ('B1', 'D1'), ('C1', 'D1')),
    )

    cube = Figure(
        points={
            'A1': (0, 0, 0), 'B1': (0, 0, 128), 'C1': (128, 0, 128), 'D1': (128, 0, 0),
            'E1': (0, 128, 0), 'F1': (0, 128, 128), 'G1': (128, 128, 128), 'H1': (128, 128, 0),
        },
        pairs=(
            ('A1', 'B1'), ('B1', 'C1'), ('C1', 'D1'), ('D1', 'A1'),
            ('E1', 'F1'), ('F1', 'G1'), ('G1', 'H1'), ('H1', 'E1'),
            ('A1', 'E1'), ('B1', 'F1'), ('C1', 'G1'), ('D1', 'H1'),
        )
    )

    ang_x = 0
    ang_y = 0
    ang_z = 0

    cam_x = 256
    cam_y = 256
    cam_z = 256

    focal_length = 256

    canvas = Canvas()
    canvas.add_figure(axes)
    canvas.add_figure(tetrahedron)
    canvas.add_figure(cube)

    while True:
        cv2.imshow('image', canvas.get_image(cam_x, cam_y, cam_z, ang_x, ang_y, ang_z, focal_length))
        k = cv2.waitKey(0)

        # Shift matrix
        p = [0.0, 0.0, 0.0]

        # Translation
        if k == 83:
            p = [2.0, 0.0, 0.0]
        elif k == 81:
            p = [-2.0, 0.0, 0.0]
        elif k == 82:
            p = [0.0, 2.0, 0.0]
        elif k == 84:
            p = [0.0, -2.0, 0.0]
        elif k == ord('-'):
            p = [0.0, 0.0, 2.0]
        elif k == ord('+'):
            p = [0.0, 0.0, -2.0]

        # Rotation
        elif k == ord('8'):
            ang_x += 2
        elif k == ord('2'):
            ang_x -= 2
        elif k == ord('4'):
            ang_y += 2
        elif k == ord('6'):
            ang_y -= 2
        elif k == ord('7'):
            ang_z += 2
        elif k == ord('9'):
            ang_z -= 2

        # Focal length size
        elif k == ord('['):
            focal_length *= 1.1
        elif k == ord(']'):
            focal_length /= 1.1

        r = rotate(p, ang_x, ang_y, ang_z)
        cam_x = int(round(cam_x + r[0]))
        cam_y = int(round(cam_y + r[1]))
        cam_z = int(round(cam_z + r[2]))


if __name__ == '__main__':
    main()
