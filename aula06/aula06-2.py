import cv2
from matplotlib import pyplot as plt

img = cv2.imread("../data/lena.jpg", cv2.IMREAD_GRAYSCALE)

	

#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
hist = cv2.calcHist([img],[0],None,[256],[0,256])

plt.hist(img.ravel(),256,[0,256])
plt.show()




cv2.waitKey()

cv2.destroyAllWindows()