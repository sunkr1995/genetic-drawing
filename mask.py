'''
Author: your name
Date: 2021-07-08 10:50:22
LastEditTime: 2021-07-08 14:10:04
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /genetic-drawing/mask.py
'''
import cv2
import numpy as np


def main():

    # 1.导入图片
    img_src = cv2.imread("03.jpg")

    # 2.灰度化,二值化
    img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
    img_canny=cv2.Canny(img_gray,40,140)
    ret, img_bin = cv2.threshold(img_canny, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((50,50),np.uint8)
    img_binmax = cv2.dilate(img_bin,kernel)
    ## 3.连通域分析
    contours, hierarchy = cv2.findContours(img_binmax,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #print (len(contours))   
    color = [255, 255, 255]
    
    
    img_result0 = img_binmax.copy()
    img_result0 = cv2.fillPoly(img_result0, [np.array(contours[0])] ,color)
    cv2.imwrite("masks-03/mask-0.jpg",img_result0)

    
    kernels = [30,10,5,3]
    for i in range(4):
        k = kernels[i]
        kernel = np.ones((k,k),np.uint8)
        img_bin_i = cv2.dilate(img_bin,kernel)
        cv2.imwrite("masks-03/mask-{}.jpg".format(i+1),img_bin_i)


if __name__ == '__main__':
    main()