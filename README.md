<!--
 * @Author: your name
 * @Date: 2021-06-18 10:04:20
 * @LastEditTime: 2021-07-08 17:19:29
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /genetic-drawing/README.md
-->
# Genetic Drawing
This is a toy project I did around 2017 for imitating a drawing process given a target image (inspired by many examples of genetic drawing on the internet, and this was my take on it, mostly as an exercise). 

Due to a popular request, it is now opensource 🙂

Examples of generated images:

![](imgs/img1.gif) <img src="imgs/img2.gif" width="380">

It also supports user-created sampling masks, in case you'd like to specify regions where more brushstrokes are needed (for ex, to allocate more finer details)


<img src="imgs/img3.gif">


## Python
you would need the following python 3 libraries:

* opencv 3.4.1
* numpy 1.16.2
* matplotlib 3.0.3
* and Jupyter Notebook

To start, open the GeneticDrawing.ipynb and run the example code


## 添加功能

添加彩色绘图的功能
<img src="02.gif">

## 待添加

现在只有4种笔画素材，再加入些笔画的素材；笔画除了正常的旋转，还需要加入一些形变模拟运笔差异；根据初始边缘轮廓随机生成一些直线椭圆，模拟草图构图；相应笔画附近随机加入模糊处理，模拟手蹭的地方；
