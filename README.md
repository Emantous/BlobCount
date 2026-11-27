# BlobCount

Counts blobs in an image using OpenCV.

## How it works
Grayscale → Gaussian blur → threshold → find contours → print the count.

## Requirements
- Python 3
- opencv-python
- sys

## Usage
    python src/main.py path/to/image.jpg