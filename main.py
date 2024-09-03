import cv2
import copy
import numpy as np

if __name__ == "__main__":
    img = cv2.imread("./apel.jpg")
    print(img)

    # cv2.imshow("win", img)
    # cv2.waitKey(0)

    # print(img.shape)

    b, c, d = img.shape

    # for i in range(b):
    #     for j in range(c):
    #         img[i, j, 0] = 0
    #         img[i, j, 2] = 0
    #
    # cv2.imshow("win", img)

    # img2 = copy.deepcopy(img)
    # # img2[:, :, 2] = 0
    # img2[:, :, 1] = 0

    # cv2.imshow("win", img2)

    imgf64 = img.astype(np.float64)
    img_r = imgf64[:, :, 2]
    img_g = imgf64[:, :, 1]
    img_b = imgf64[:, :, 0]

    img3 = np.floor((img_r + img_g + img_b) / 3)
    print(img3)

    img_gray = np.zeros(img.shape)
    img_gray[:, :, 0] = img3[:, :]
    img_gray[:, :, 1] = img3[:, :]
    img_gray[:, :, 2] = img3[:, :]

    img_gray2 = img_gray.astype(np.uint8)

    print(img_gray)
    print()
    print(img_gray2)

    # cv2.imshow("win", img_gray)

    cv2.waitKey(0)
