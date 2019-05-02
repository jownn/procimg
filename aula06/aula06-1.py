import cv2

img = cv2.imread("../data/lena.jpg", cv2.IMREAD_GRAYSCALE)

	

#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
hist = cv2.calcHist([img],[0],None,[256],[0,256])

for i, val in  zip(range(0,256), hist):
    print ("hist[",i,"]=", val)
    





cv2.waitKey()

cv2.destroyAllWindows()