import numpy as np
import cv2


def erosao(source, element):
    for i in range(source.shape[0]):
        for j in range(source.shape[1]):
            compare = source[i:element.shape[0], j::element.shape[1]]
            print(compare)


def printImg(img, windowName):
    newimg = np.zeros((img.shape[0]*50, img.shape[1]*50), np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            tam = newimg.shape[0]/img.shape[0]
            radius = int(tam/2)
            x = int((i*tam)+(tam/2))
            y = int((j*tam)+(tam/2))
            if img[i, j] == 1:
                color = 255
            else:
                color = 0
            cv2.circle(newimg, (y, x), radius, (color, color, color), -1)
    ret,thresh1 = cv2.threshold(newimg, 0, 255, cv2.THRESH_BINARY_INV)
    img = np.array(thresh1)
    cv2.imshow(str(windowName), thresh1)
