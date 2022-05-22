from pathlib import Path
import os

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2 as cv
#r = g = b = 250

path2 = r"D:\NUST\Course Data\2nd Semester\Artificial Neural Networks\Dataset Generateion\Generated\Upscaled"
path1 = r"D:\NUST\Course Data\2nd Semester\Artificial Neural Networks\Dataset Generateion\Generated\Boxed"


#locating the Font
#MF = ImageFont.truetype(r"D:\NUST\Course Data\2nd Semester\Artificial Neural Networks\Dataset Generateion\Input\arial.ttf", size=26)

split = int(input("Enter number of training images (range) from 1 - 1040\n"))
test = int(input("Enter the number of test images\n"))
validate = int(input("Enter the number of validation images\n"))

range = test+split+validate

count = 1



for (root, dirs, file) in os.walk(path1):
    for f in file:


        if ('.png' in f):
            #print(f)
            file_path1 = os.path.join(path1, f)
            #loaded1 = cv.imread(file_path1)
            #print(f)

            loaded1 = cv.imread(file_path1)
            #print(loaded1.shape)
            file_name1 = os.path.splitext(f)[0]

            for (root,dirs,file) in os.walk(path2):

                for k in file:
                    #if count>= range:
                        #break
                    if (file_name1 in k) and (count<=range):

                        file_path2 = os.path.join(path2, k)

                        loaded2 = cv.imread(file_path2)
                        #cv.imshow("Loaded2",loaded2)
                        #cv.waitKey()
                        #break
                        print(file_path2)

                        new_name = count
                        new_image = cv.hconcat([loaded1,loaded2])
                        #cv.imshow("combined",new_image)
                        #cv.waitKey()

                        if count <= split:
                            s_path = r"D:\NUST\Course Data\2nd Semester\Artificial Neural Networks\Dataset Generateion\Generated\Capchta\train/" + str(
                                new_name) + ".jpg"
                        if count > split:
                            s_path = r"D:\NUST\Course Data\2nd Semester\Artificial Neural Networks\Dataset Generateion\Generated\Capchta\test/" + str(
                                new_name-split) + ".jpg"
                        if count > split:
                            s_path = r"D:\NUST\Course Data\2nd Semester\Artificial Neural Networks\Dataset Generateion\Generated\Capchta\validate/" + str(
                                new_name-split-validate) + ".jpg"
                        #s_path = r"D:\NUST\Course Data\2nd Semester\Artificial Neural Networks\Dataset Generateion\Generated\Capchta\Train/"+str(new_name)+".jpg"
                        #cv.imshow("captha",new_image)
                        #cv.waitKey()
                        #break
                        #new_image = Image.fromarray(new_image)
                        #new_image.show()
                        #new_image.save(s_path)
                        cv.imwrite(s_path, new_image)
                        print(count, s_path)
                        count+=1
    #print(new_name)
print("Shawshay")