# First, read an image.
# Dependencies

import numpy as np
import cv2 as cv # Import openCV
# Read the image's content and put it into an array.

# img = cv.imread('images.jpg', 0)
# # cv.imshow('window', img)

# cv.imshow('Grayscale', img)

img_weighted = cv.imread('images2.jpg')
img_blurred = cv.GaussianBlur(img_weighted, (5, 5), 0)

def process_image(image, name):
    rows, cols = image.shape[:2]

    # cv.imshow('Grayscale Image (Weighted)', img_weighted)
    gray_scale_data = np.dot(image[...,:3], [0.1140, 0.5870, 0.2989])
    # Scale values
    scale_indices = (gray_scale_data / 255.0) * 69
    # Transform to int values
    index_array = scale_indices.astype(int)

    # Convert your string into a list of characters, then into a NumPy array
    chars_str = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    chars_reversed = chars_str[::-1]
    chars_array = np.array(list(chars_reversed))

    ascii_array = chars_array[index_array]
    final_output = "\n".join(["".join(row) for row in ascii_array])
    
    file_name = f"{name}.txt"
    with open(file_name, "w") as f:
        f.write(final_output)

process_image(img_weighted, "img_weighted")
process_image(img_blurred, "img_blurred")
