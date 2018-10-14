import cv2
from geometry import Canvas, Figure


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

    cam_x = 256
    cam_y = 256
    cam_z = 256

    focal_length = 256

    canvas = Canvas()
    # canvas.add_figure(axes)
    canvas.add_figure(tetrahedron)
    canvas.add_figure(cube)

    while True:
        cv2.imshow('image', canvas.get_image(cam_x, cam_y, cam_z, focal_length))

        k = cv2.waitKey(0)
        if k == ord('6'):
            cam_x += 2
        elif k == ord('4'):
            cam_x -= 2
        elif k == ord('8'):
            cam_y += 2
        elif k == ord('2'):
            cam_y -= 2
        elif k == ord('-'):
            cam_z += 2
        elif k == ord('+'):
            cam_z -= 2
        elif k == ord('['):
            focal_length *= 1.1
        elif k == ord(']'):
            focal_length /= 1.1


if __name__ == '__main__':
    main()
