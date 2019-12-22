import cv2
import numpy as np
img = cv2.imread("maymun.jpg",cv2.IMREAD_UNCHANGED)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.Canny(img, 0, 50)

kernel = np.ones((5,5),np.uint8)
img = cv2.dilate(img,kernel,iterations = 2)


th, im_th = cv2.threshold(img, 0, 40, cv2.THRESH_OTSU)

im_floodfill = im_th.copy()

h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)

cv2.floodFill(im_floodfill, mask, (0,0), 255)

im_floodfill_inv = cv2.bitwise_not(im_floodfill)

img = im_th | im_floodfill_inv

img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.dilate(img,kernel,iterations = 2)

img = cv2.bitwise_not(img)
img = cv2.Canny(img, 0, 50)




cv2.imshow("Canny", img)
cv2.imwrite(r"C:\Users\alian\Desktop\result.jpg", img)
cv2.waitKey(0)
