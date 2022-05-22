from pathlib import Path
import os

#for generating numbers
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2 as cv
r = g = b = 250

#for generating strings
import random
import string


path = r"D:\NUST\Course Data\2nd Semester\Artificial Neural Networks\Dataset Generateion\Input\samples"



#locating the Arial Font
MF = ImageFont.truetype(r"D:\NUST\Course Data\2nd Semester\Artificial Neural Networks\Dataset Generateion\Input\arial.ttf", size=80)


for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.png' in f:

            #print(f)
            file_path = os.path.join(path, f)
            #print(file_path)

            loaded = cv.imread(file_path)
            loaded_shape = loaded.shape

            file_name = os.path.splitext(f)[0]
            #print(file_name)

            ##LOAD White Image

            #print("White Image Part")

            h = loaded_shape[0]
            w = loaded_shape[1]

            #print("Step 2")

            h_n = 256
            w_n = 256
            white = np.zeros([h_n, w_n, 3], dtype=np.uint8)
            white[:, :] = [255, 255, 255]
            white = Image.fromarray(white)

            #print("Step 3")
            d1 = ImageDraw.Draw(white)
            d1.text((w_n/11, 90), file_name, fill=(0, 0, 0), font=MF)

            #white.show()
            #break

            save_path = r"D:\NUST\Course Data\2nd Semester\Artificial Neural Networks\Dataset Generateion\Generated\Boxed"
            s_path=os.path.join(save_path,f)
            white.save(s_path)
            print(file_name)

            #print("h=",h)

print("Shawshay")