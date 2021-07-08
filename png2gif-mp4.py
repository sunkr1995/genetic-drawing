'''
Author: your name
Date: 2021-07-02 18:13:07
LastEditTime: 2021-07-08 13:49:31
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /genetic-drawing/3.py
'''
import imageio
import os
import cv2
'''
# 只支持png格式，需要先命名排序好(默认按照字母序排列)
# source(字符串)：素材图片路径，生成的gif也保存在该路径
# gifname(字符串)：生成的gif的文件名，命名时带后缀如：'1.gif'
# time(数字)：生成的gif每一帧的时间间隔，单位（s）
'''
def png2gif(source, gifname, time):
    #os.chdir(source) # os.chdir()：改变当前工作目录到指定的路径
    file_list = os.listdir(source) # os.listdir()：文件夹中的文件/文件夹的名字列表
    frames = [] #读入缓冲区
    file_list = sorted(file_list)
    for png in file_list:
        frames.append(imageio.imread(os.path.join(source,png)))
    imageio.mimsave(gifname, frames, 'GIF', duration=time)

def png2mp4(source, name):
    fps = 30    #FPS
    size=(360, 640)    #图片、视频尺寸
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    videoWriter = cv2.VideoWriter(name,fourcc,fps,size, True)
    file_list = os.listdir(source) # os.listdir()：文件夹中的文件/文件夹的名字列表
    frames = [] #读入缓冲区
    file_list = sorted(file_list)
    for png in file_list:
        frame = cv2.imread(os.path.join(source,png))
        videoWriter.write(frame)
    videoWriter.release()

 
address = "out"
#png2gif(address, '02.gif', 0.1)
png2mp4(address, '01.mp4')
