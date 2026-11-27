import cv2
import sys



def process_image(image_path):

    # Read the image in greyscale
    greyscale = cv2.imread(image_path, 0)

    # Apply Gaussian blur to the grayscale image
    Gaussian = cv2.GaussianBlur(greyscale, (15, 15), 0)  

    # Apply binary thresholding to the blurred image
    _, thresh_binary = cv2.threshold(Gaussian, 220, 255, cv2.THRESH_BINARY)
    return thresh_binary


def count_objects(thresh_binary) -> int:
    # Apply Canny edge detection to the binary image
    edges = cv2.Canny(thresh_binary, 100, 700)

    # Find contours in the edge-detected image
    contours, hierarchy = cv2.findContours(edges,
                        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    min_area = 37
    big = [c for c in contours if cv2.contourArea(c) >= min_area]

    return len(big)


def main(image_path):
    thresh_binary = process_image(image_path)
    num_objects = count_objects(thresh_binary)
    print("The number of objects on the image is:", num_objects)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
