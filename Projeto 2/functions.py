import numpy as np
import cv2


def erosao(source, element):
    img = np.pad(source, pad_width=int((element.shape[0]-1)/2), mode='constant', constant_values=0)
    source = np.pad(source, pad_width=int((element.shape[0]-1)/2), mode='constant', constant_values=0)
    for i in range(int(source.shape[0]-(element.shape[0]-1))):
        for j in range(int(source.shape[1]-(element.shape[1]-1))):
            compare = source[i:(element.shape[0]+i), j:(element.shape[1]+j)]
            if(np.array_equal(compare, element)):
                img[int(((element.shape[0]-1)/2)+i), int(((element.shape[1])/2)+j)] = 1
                source[i:(element.shape[0]+i), j:(element.shape[1]+j)] = 0
            else:
                img[int(((element.shape[0]-1)/2)+i), int(((element.shape[1])/2)+j)] = 0
    return img


def printImg(img, windowName, tam):
    newimg = np.zeros((img.shape[0]*tam, img.shape[1]*tam), np.uint8)
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
