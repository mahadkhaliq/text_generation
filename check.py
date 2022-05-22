import os
import PIL.Image
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2 as cv

path1 = r"D:\NUST\Course Data\2nd Semester\Artificial Neural Networks\Dataset Generateion\Generated\Combined"

for (root, dirs, file) in os.walk(path1):
    for f in file:
        file_path1 = os.path.join(path1, f)
        loaded1 = cv.imread(file_path1)

        if (loaded1.shape[0]) != 256:
            print(f)
            break

        if (loaded1.shape[1]) != 512:
            print(f)
            break

print("All files checked successfully")