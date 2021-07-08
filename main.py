'''
Author: your name
Date: 2021-06-18 10:13:00
LastEditTime: 2021-07-08 14:13:07
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /genetic-drawing/main.py
'''
import cv2
import os
import time
from IPython.display import clear_output
from genetic_drawing import *

gen = GeneticDrawing('03.jpg', seed=time.time())
out = gen.generate(400, 50)
brushesRange = np.array([[0.1, 0.3], [0.3, 0.7]])
for i in range(len(gen.imgBuffer)):
        cv2.imwrite(os.path.join("out", f"{i:06d}.png"), gen.imgBuffer[i])
try:
    for i in range(5):
        brushesRange_tmp = brushesRange/(2**(i+1))
        gen.brushesRange = brushesRange_tmp.tolist()
        maskname = "masks-03/mask-{}.jpg".format(i)
        gen.sampling_mask = cv2.cvtColor(cv2.imread(maskname), cv2.COLOR_BGR2GRAY)
        
        #keep drawing on top of our previous result
        out = gen.generate(100, 30)
        for i in range(len(gen.imgBuffer)):
            cv2.imwrite(os.path.join("out", f"{i:06d}.png"), gen.imgBuffer[i])

except:
    if not os.path.exists('out'):
        os.mkdir("out")
    for i in range(len(gen.imgBuffer)):
        cv2.imwrite(os.path.join("out", f"{i:06d}.png"), gen.imgBuffer[i])
#brushesRange_tmp = brushesRange/100
#gen.brushesRange = brushesRange_tmp.tolist()
##gen.brushesRange = [[0.005, 0.015],[0.015, 0.035]]
#gen.sampling_mask = cv2.cvtColor(cv2.imread("masks/mask-end.jpg"), cv2.COLOR_BGR2GRAY)
#
##keep drawing on top of our previous result
#out = gen.generate(50, 30)


#save all the images from the image buffer
if not os.path.exists('out'):
    os.mkdir("out")
for i in range(len(gen.imgBuffer)):
    cv2.imwrite(os.path.join("out", f"{i:06d}.png"), gen.imgBuffer[i])