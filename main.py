import cv2
import numpy as np
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage.feature import peak_local_max
from skimage.morphology import watershed
from matplotlib import pyplot as plt

kernel = np.ones((5, 5), np.uint8)
img = cv2.imread(r"D:\maymun.jpg", 0)
img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.Canny(img, 0, 50)

cv2.imwrite('keni.jpg',img)
img = cv2.dilate(img, kernel, iterations=1)

img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

img_open = cv2.dilate(cv2.erode(img, kernel, iterations=1), kernel, iterations=1)

img_close = cv2.erode(cv2.dilate(img, kernel, iterations=2), kernel, iterations=2)

# Threshold
th, im_th = cv2.threshold(img, 0, 90, cv2.THRESH_BINARY)

# Copy the thresholded image
im_floodfill = im_th.copy()

# Mask used to flood filling.
# NOTE: the size needs to be 2 pixels bigger on each side than the input image
h, w = im_th.shape[:2]
mask = np.zeros((h + 2, w + 2), np.uint8)

# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (150, 150), 255)

# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)

# Combine the two images to get the foreground
im_out = im_th | im_floodfill_inv

cv2.imwrite('bilmem.jpg',im_out)
cv2.imshow("Result", im_out)

# img = cv2.imread(r"D:\maymun.jpg")
# b, g, r = cv2.split(img)
# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])
# plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()

# ADIMLAR ONEMLI
# İlk aşama canny 0,50
# İkinci aşama Açma Kapama
# Üçüncü aşama alttaki fill
# bulanıklaştır erozyon *5

# https://stackoverflow.com/questions/37409811/smoothing-edges-of-a-binary-image
# http://learnopencv.com/filling-holes-in-an-image-using-opencv-python-c/
# https://docs.opencv.org/trunk/d9/d61/tutorial_py_morphological_ops.html


#
#
# im_in = cv2.imread("deneme.jpg", cv2.IMREAD_GRAYSCALE)
#
# # Threshold
# th, im_th = cv2.threshold(im_in, 0, 90, cv2.THRESH_BINARY)
#
# # Copy the thresholded image
# im_floodfill = im_th.copy()
#
# # Mask used to flood filling.
# # NOTE: the size needs to be 2 pixels bigger on each side than the input image
# h, w = im_th.shape[:2]
# mask = np.zeros((h+2, w+2), np.uint8)
#
# # Floodfill from point (0, 0)
# cv2.floodFill(im_floodfill, mask, (0,0), 255)
#
# # Invert floodfilled image
# im_floodfill_inv = cv2.bitwise_not(im_floodfill)
#
# # Combine the two images to get the foreground
# im_out = im_th | im_floodfill_inv
#
# # Display images.
# cv2.imwrite("circles_filled.png", im_out)
