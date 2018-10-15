import cv2
from geometry import Canvas, Figure, rotate


def main():
    figure_1 = Figure(
        points={
            'A': (0, 0, 0), 'B': (0, 0, 128), 'C': (128, 0, 128), 'D': (128, 0, 0),
            'E': (0, 384, 0), 'F': (0, 384, 128), 'G': (128, 384, 128), 'H': (128, 384, 0),

        },
        pairs=(
            ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'),
            ('E', 'F'), ('F', 'G'), ('G', 'H'), ('H', 'E'),
            ('A', 'E'), ('B', 'F'), ('C', 'G'), ('D', 'H'),
        )
    )

    figure_2 = Figure(
        points={
            'A': (0, 0, 256), 'B': (0, 0, 384), 'C': (128, 0, 384), 'D': (128, 0, 256),
            'E': (0, 128, 256), 'F': (0, 128, 384), 'G': (128, 128, 384), 'H': (128, 128, 256),

        },
        pairs=(
            ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'),
            ('E', 'F'), ('F', 'G'), ('G', 'H'), ('H', 'E'),
            ('A', 'E'), ('B', 'F'), ('C', 'G'), ('D', 'H'),
        )
    )

    figure_3 = Figure(
        points={'A1': (256, 0, 0), 'B1': (256, 0, 128), 'C1': (367, 0, 64), 'D1': (293, 104, 64)},
        pairs=(('A1', 'B1'), ('B1', 'C1'), ('C1', 'A1'), ('A1', 'D1'), ('B1', 'D1'), ('C1', 'D1')),
    )

    figure_4 = Figure(
        points={
            'A': (256, 0, 256), 'B': (256, 0, 512), 'C': (512, 0, 512), 'D': (512, 0, 256),
            'E': (256, 256, 256), 'F': (256, 256, 512), 'G': (512, 256, 512), 'H': (512, 256, 256),

        },
        pairs=(
            ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'),
            ('E', 'F'), ('F', 'G'), ('G', 'H'), ('H', 'E'),
            ('A', 'E'), ('B', 'F'), ('C', 'G'), ('D', 'H'),
        )
    )

    ang_x = 0
    ang_y = 0
    ang_z = 0

    cam_x = 192
    cam_y = 256
    cam_z = 1024

    focal_length = 128

    canvas = Canvas()
    canvas.add_figure(figure_1)
    canvas.add_figure(figure_2)
    canvas.add_figure(figure_3)
    canvas.add_figure(figure_4)


    while True:
        cv2.imshow('image', canvas.get_image(cam_x, cam_y, cam_z, ang_x, ang_y, ang_z, focal_length))
        k = cv2.waitKey(0)

        # Shift matrix
        p = [0.0, 0.0, 0.0]

        # Translation
        if k == 83:
            p = [8.0, 0.0, 0.0]
        elif k == 81:
            p = [-8.0, 0.0, 0.0]
        elif k == 82:
            p = [0.0, 8.0, 0.0]
        elif k == 84:
            p = [0.0, -8.0, 0.0]
        elif k == ord('-'):
            p = [0.0, 0.0, 8.0]
        elif k == ord('+'):
            p = [0.0, 0.0, -8.0]

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
