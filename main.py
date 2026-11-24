import cv2
from matplotlib import pyplot as plt


# Read the image in grayscale
gray_image = cv2.imread('temp/2.png', 0)
cv2.imwrite('temp/2_gray.png', gray_image)
if gray_image is None:
    print('Error: Image not found.')
else:
    print('Image loaded successfully.')


# Apply Gaussian blur to the grayscale image
Gaussian = cv2.GaussianBlur(gray_image, (15, 15), 0)  
Gaussian_rgb = cv2.cvtColor(Gaussian, cv2.COLOR_BGR2RGB)  




cv2.imshow("testWindow", Gaussian_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
