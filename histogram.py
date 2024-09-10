import cv2
import numpy as np
from matplotlib import pyplot as plt


# write it yourself
def method_1(img: cv2.UMat) -> cv2.UMat:
    histogram = np.zeros((256, 1), np.int32)
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            n = img[i, j]
            histogram[n] += 1
    return histogram


# using library
def method_2(img: cv2.UMat) -> cv2.UMat:
    histogram = cv2.calcHist([img], [0], None, [256], [0, 256])
    return histogram


def main():
    img = cv2.imread("./apel.jpg")

    histogram = method_2(img)
    plt.bar(np.arange(0, 256, 1), histogram[:, 0])
    plt.show()

    # cv2.imshow("win", img)
    # cv2.waitKey(0)


if __name__ == "__main__":
    main()
