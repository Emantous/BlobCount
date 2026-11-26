import cv2
import numpy as np
from matplotlib import pyplot as plt


greyscale = cv2.imread('temp/4.png', 0)
print(greyscale.shape)
print(greyscale[25,20])

# Apply Gaussian blur to the grayscale image
Gaussian = cv2.GaussianBlur(greyscale, (9, 9), 0)  

# Apply binary thresholding to the blurred image
_, thresh_binary = cv2.threshold(Gaussian, 230, 255, cv2.THRESH_BINARY)

# Apply Canny edge detection to the binary image
edges = cv2.Canny(thresh_binary, 100, 700)

# Find contours in the edge-detected image
contours, hierarchy = cv2.findContours(edges,
                      cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print("Number of Contours Found = " + str(len(contours)))

cv2.imshow("testWindow", edges)
cv2.imshow("testWindow2", greyscale)
cv2.waitKey(0)
cv2.destroyAllWindows()
