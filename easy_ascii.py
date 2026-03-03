from __future__ import annotations
from pathlib import Path
import numpy as np
import cv2 as cv


class EasyAscii:
    def __init__(self, image_path: str | Path) -> None:
        img = cv.imread(str(image_path))
        if img is None:
            raise FileNotFoundError
        self.img_weighted: Image = img
        self.img_gblurred: Image = cv.GaussianBlur(img, (5, 5), 0)

    def genGaussianBlur(self, file_name, reversed: bool = False) -> None:
        self.process_image(self.img_gblurred, file_name, reversed)

    def gen_weighted(self, file_name, reversed: bool = False) -> None:
        self.process_image(self.img_weighted, file_name, reversed)

    def process_image(self, image, file_name: string, reversed: bool = False) -> None:

        rows, cols = image.shape[:2]

        gray_scale_data = np.dot(image[..., :3], [0.1140, 0.5870, 0.2989])
        # Scale values
        scale_indices = (gray_scale_data / 255.0) * 69
        # Transform to int values
        index_array = scale_indices.astype(int)

        # Convert your string into a list of characters, then into a NumPy array
        chars_str = (
            r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
        )
        chars = chars_str[::-1] if reversed else chars_str

        chars_array = np.array(list(chars))

        ascii_array = chars_array[index_array]
        final_output = "\n".join(["".join(row) for row in ascii_array])

        name = f"{file_name}.txt"
        with open(name, "w") as f:
            f.write(final_output)
