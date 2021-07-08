'''
Author: your name
Date: 2021-07-07 17:01:54
LastEditTime: 2021-07-08 14:11:29
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /genetic-drawing/test.py
'''
import cv2 as cv
import math
import numpy as np
 
#读取原始图像
img = cv.imread('masks/mask-1.jpg')
#print (img.shape)
#img = np.zeros((400,640,3)) 
#获取图像行和列
rows, cols = img.shape[:2]
 
#设置中心点和光照半径
centerX = 285#rows / 2 - 20
centerY = 329#cols / 2 + 20
radius = 200#min(centerX, centerY)
 
#设置光照强度
strength = 500
 
#新建目标图像
dst = np.zeros((rows, cols, 3), dtype="uint8")
img0 = img.copy()
#图像光照特效
for i in range(rows):
  for j in range(cols):
    #计算当前点到光照中心距离(平面坐标系中两点之间的距离)
    distance = math.pow((centerY-j), 2) + math.pow((centerX-i), 2)
    #获取原始图像
    B = img0[i,j][0]
    G = img0[i,j][1]
    R = img0[i,j][2]
    if (distance < radius * radius):
      #按照距离大小计算增强的光照值
      result = (int)(strength*( 1.0 - math.sqrt(distance) / radius ))
      B = img0[i,j][0] + result
      G = img0[i,j][1] + result
      R = img0[i,j][2] + result
      #判断边界 防止越界
      B = min(255, max(0, B))
      G = min(255, max(0, G))
      R = min(255, max(0, R))
      dst[i,j] = np.uint8((B, G, R))
    else:
      dst[i,j] = np.uint8((B, G, R))

#cv.imwrite("masks/mask-3.jpg",dst)

img1 = dst.copy()
dst = np.zeros((rows, cols, 3), dtype="uint8")
centerX = 290#rows / 2 - 20
centerY = 180#cols / 2 + 20
radius = 300#min(centerX, centerY)
#图像光照特效
for i in range(rows):
  for j in range(cols):
    #计算当前点到光照中心距离(平面坐标系中两点之间的距离)
    distance = math.pow((centerY-j), 2) + math.pow((centerX-i), 2)
    #获取原始图像
    B = img1[i,j][0]
    G = img1[i,j][1]
    R = img1[i,j][2]
    if (distance < radius * radius):
      #按照距离大小计算增强的光照值
      result = (int)(strength*( 1.0 - math.sqrt(distance) / radius ))
      B = img1[i,j][0] + result
      G = img1[i,j][1] + result
      R = img1[i,j][2] + result
      #判断边界 防止越界
      B = min(255, max(0, B))
      G = min(255, max(0, G))
      R = min(255, max(0, R))
      dst[i,j] = np.uint8((B, G, R))
    else:
      dst[i,j] = np.uint8((B, G, R))

cv.imwrite("masks/mask-0.jpg",dst)

#显示图像
cv.imshow('result',np.hstack((img,dst)))
cv.waitKey()
cv.destroyAllWindows()
