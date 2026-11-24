import cv2

gray_image = cv2.imread('temp/2.png', 0)
cv2.imwrite('temp/2_gray.png', gray_image)

if gray_image is None:
    print('Error: Image not found.')
else:
    print('Image loaded successfully.')


cv2.imshow("testWindow", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()