import numpy as np
import os
from PIL import Image

target = ['happy','sad','surprise','angry','disgust','fear']

file = open("jaffe.txt","r")
file.readline()                     #skip first line

while True:
    line = file.readline()
    if not line:
        break
    imageData = line.split(' ')
    expVal = []
    for x in range(1,7):
        expVal.append(float(imageData[x]))

    result = np.where(expVal == np.amax(expVal))
    expIndex = result[0][0]         #first index is for axis(row)   
                                    #result[0] is an array of indices of max element

    imagePath = imageData[7]
    imagePrefix = imagePath[0:2] + '.' + imagePath[3:6]

    for imgfile in os.listdir('./jaffedbase'):
        if(imgfile.startswith(imagePrefix)):
            infile = Image.open(os.path.join('./jaffedbase',imgfile))
            outfile = infile.convert("L")
            outfile.save(os.path.join('./datasets/training-set/',target[expIndex],imgfile[0:-5]+'.jpeg'),"JPEG")
            print("Progress : Image " + imageData[0] + " " + imagePrefix + " converted...")