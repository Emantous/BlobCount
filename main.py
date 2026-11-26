import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys



def process_image(image_path):

    # Read the image in greyscale
    greyscale = cv2.imread(image_path, 0)

    # Apply Gaussian blur to the grayscale image
    Gaussian = cv2.GaussianBlur(greyscale, (15, 15), 0)  

    # Apply binary thresholding to the blurred image
    _, thresh_binary = cv2.threshold(Gaussian, 220, 255, cv2.THRESH_BINARY)
    return thresh_binary


def count_objects(image) -> int:
    # Apply Canny edge detection to the binary image
    edges = cv2.Canny(thresh_binary, 100, 700)

    # Find contours in the edge-detected image
    contours, hierarchy = cv2.findContours(edges,
                        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    return len(contours)

if __name__ == "__main__":
    image_path = sys.argv[1]
    thresh_binary = process_image(image_path)
    num_objects = count_objects(thresh_binary)
    print(f"Number of objects detected: {num_objects}")
