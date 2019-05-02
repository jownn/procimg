import cv2
from matplotlib import pyplot as plt

img = cv2.imread("../data/lena.jpg", cv2.IMREAD_COLOR)

	

#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
hist = cv2.calcHist([img],[0],None,[256],[0,256])


color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

plt.show()






cv2.waitKey()

cv2.destroyAllWindows()