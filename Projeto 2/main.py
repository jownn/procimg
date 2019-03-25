import cv2
import numpy as np
import functions as f


def main():
    img = np.array([[1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0]
                    ], dtype=np.uint8
                   )
    # element = np.ones((3, 3), np.uint8)
    f.printImg(img, "Original")
    element = np.array([[1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1],
                        ], dtype=np.uint8
                       )
    f.printImg(element, "Elemento1")
    erosion = cv2.erode(img, element, iterations=1, borderType=cv2.BORDER_CONSTANT, borderValue=0)
    f.printImg(erosion, "Erosão1")

    cv2.waitKey(0)
    cv2.destroyWindow('i')


if __name__ == "__main__":
    main()
