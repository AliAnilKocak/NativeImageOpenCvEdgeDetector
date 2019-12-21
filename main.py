import cv2
import numpy as np
from matplotlib import pyplot as plt
kernel = np.ones((5,5),np.uint8)

img = cv2.imread(r"D:\maymun.jpg")
img = cv2.GaussianBlur(img, (11, 11), 0)

img = cv2.Canny(img, 0, 50)

# img = cv2.addWeighted(img, 48, cv2.blur(img, (60, 30)), -4, 40)

img = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel)
img = cv2.bitwise_not(img)
cv2.imwrite('keni.jpg',img)
cv2.imshow("Canny", img)




cv2.waitKey(0)
cv2.destroyAllWindows()


#ADIMLAR ONEMLI
# İlk aşama canny 0,50
# İkinci aşama Açma Kapama
# Üçüncü aşama alttaki fill
# bulanıklaştır erozyon *5

# https://stackoverflow.com/questions/37409811/smoothing-edges-of-a-binary-image
# http://learnopencv.com/filling-holes-in-an-image-using-opencv-python-c/
# https://docs.opencv.org/trunk/d9/d61/tutorial_py_morphological_ops.html


# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# from scipy import ndimage
# from skimage.feature import peak_local_max
# from skimage.morphology import watershed
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