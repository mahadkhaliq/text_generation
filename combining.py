from pathlib import Path
import os

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2 as cv
r = g = b = 250

path1 = r"D:\NUST\Course Data\2nd Semester\Artificial Neural Networks\Dataset Generateion\Generated\Upscaled"
path2 = r"D:\NUST\Course Data\2nd Semester\Artificial Neural Networks\Dataset Generateion\Generated\Boxed"


#locating the Font
#MF = ImageFont.truetype(r"D:\NUST\Course Data\2nd Semester\Artificial Neural Networks\Dataset Generateion\Input\arial.ttf", size=26)


for (root, dirs, file) in os.walk(path1):
    for f in file:
        if '.png' in f:
            #print(f)
            file_path1 = os.path.join(path1, f)
            #loaded1 = cv.imread(file_path1)
            #print(f)

            loaded1 = cv.imread(file_path1)
            #print(f," Loaded Successfully")
            #print(loaded1.shape)

            file_name1 = os.path.splitext(f)[0]

            #print("Entering in the loop")

            for (root,dirs,file) in os.walk(path2):
                for k in file:
                    if file_name1 in k:

                        file_path2 = os.path.join(path2, k)

                        loaded2 = cv.imread(file_path2)
                        #cv.imshow("Loaded2",loaded2)
                        #cv.waitKey()
                        #break
                        #print(loaded2.shape)

                        new_name = 1
                        new_image = cv.hconcat([loaded1,loaded2])
                        #cv.imshow("combined",new_image)
                        #cv.waitKey()

                        s_path = r"D:\NUST\Course Data\2nd Semester\Artificial Neural Networks\Dataset Generateion\Generated\Capchta\Train\" + str(new_name)+'.jpg'
                        #cv.imshow("captha",new_image)
                        #cv.waitKey()
                        #new_image = Image.fromarray(new_image)
                        #new_image.show()
                        new_name =  new_name+1
                        cv.imwrite(s_path, new_image)
                        #new_image.save(s_path)
                if new_name >= 100:
                    break

    #print(new_name)
print("Shawshay")