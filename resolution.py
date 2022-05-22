import os
import PIL.Image
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2 as cv

path1 = r"D:\NUST\Course Data\2nd Semester\Artificial Neural Networks\Dataset Generateion\Input\samples"

for (root, dirs, file) in os.walk(path1):
    for f in file:
        if '.png' in f:
            file_path1 = os.path.join(path1, f)
            #print(f)

            h_n = 256
            w_n = 256
            bg = np.zeros([h_n, w_n, 3], dtype=np.uint8)
            bg[:, :] = [255, 255, 255]
            bg = Image.fromarray(bg)

            #bg.show()

            im2 = Image.open(file_path1)


            #############################
            width = 200
            height = 50

            new_width = 256
            new_height = 256
            img = im2.resize((new_width, new_height), Image.ANTIALIAS)

            #img.show()


            img2 = img.copy()
            bg.paste(img2, (0, 0))
            #bg.show()
            save_path = r"D:\NUST\Course Data\2nd Semester\Artificial Neural Networks\Dataset Generateion\Generated\Upscaled"
            save_loc = os.path.join(save_path, f)
            #print(save_loc)
            bg.save(save_loc)
            #bg.show()
            #break
            #loaded1 = cv.imread(save_loc)
            #print(loaded1.shape)


print("SHAWSHAY")










