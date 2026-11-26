import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('temp/4.png', 0)
greyscale = cv2.imread('temp/4.png', 0)
print(greyscale.shape)
print(greyscale[25,20])

# Apply Gaussian blur to the grayscale image
Gaussian = cv2.GaussianBlur(greyscale, (15, 15), 0)  

# Apply binary thresholding to the blurred image
_, thresh_binary = cv2.threshold(Gaussian, 245, 255, cv2.THRESH_BINARY)

# Apply Canny edge detection to the binary image
edges = cv2.Canny(thresh_binary, 100, 700)

# Find contours in the edge-detected image
contours, hierarchy = cv2.findContours(edges,
                      cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print("Number of Contours Found = " + str(len(contours)))

cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
cv2.imshow('Thresh', thresh_binary)
cv2.imshow('Contours', image)
cv2.imshow('Grey', greyscale)
cv2.waitKey(0)
cv2.destroyAllWindows()
