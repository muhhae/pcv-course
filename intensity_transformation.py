import cv2
import numpy as np
from matplotlib import pyplot as plt


def T(r: np.uint8, r1: np.uint8, s1: np.uint8, s2: np.uint8, r2: np.uint8) -> np.uint8:
    s = 0
    if (0 < r) & (r < r1):
        s = s1 / r1
    elif (r1 <= r) & (r < r2):
        s = (s2 - s1) / (r2 - r1) * (r - r1) + s1
    elif (r2 <= r) & (r <= 255) & (r < 255):
        s = (255 - s2) / (255 - r2) * (r - r2) + s2
    else:
        s = s2
    s = np.uint8(np.floor(s))
    return s


def main():
    img = cv2.imread("./apel.jpg")

    x = img.shape[0]
    y = img.shape[1]
    z = img.shape[2]

    im = np.zeros((x, y, z), np.uint8)

    r1 = 80
    r2 = 175
    s1 = 20
    s2 = 240

    for i in range(x):
        for j in range(y):
            for k in range(z):
                r = img[i, j, k]
                res = T(r, r1, s1, s2, r2)
                im[i, j, k] = res

    while 1:
        cv2.imshow("win", im)
        cv2.imshow("win_asli", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()
