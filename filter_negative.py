import cv2
import numpy as np
from matplotlib import pyplot as plt


def main():
    img = cv2.imread("./apel.jpg", cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread("./apel.jpg")

    img_negative = 255 - img
    # img_float = img.astype(np.float32) / 255

    plt.bar(np.arange(0, 256, 1), cv2.calcHist([img], [0], None, [256], [0, 256])[:, 0])
    plt.bar(
        np.arange(0, 256, 1),
        cv2.calcHist([img_negative], [0], None, [256], [0, 256])[:, 0],
    )
    plt.show()


if __name__ == "__main__":
    main()
