#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 11:35:48 2021

@author: alirezakheirandish
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

path = 'books.jpg'
img = mpimg.imread(path, format=np.uint8)
plt.imshow(img)

pts_src = np.array([[807,968],[611,1096],[420,783],[615,661]],dtype = np.float64)

W = np.linalg.norm(pts_src[0]-pts_src[1])
H = np.linalg.norm(pts_src[1]-pts_src[2])
pts_dst = np.array([[0,0],[W,0],[W,H],[0,H]],dtype = np.float64)
Tform, status = cv2.findHomography(pts_dst,(pts_src),cv2.RANSAC)
height, width = img.shape[:2]
D = np.zeros((np.int(H),np.int(W),3))
for i in range (D.shape[0]-2):
    for j in range(D.shape[1]-2):
            I,J,c = np.dot(Tform,np.array([j,i,1]))
            I,J = I/c,J/c
            x = np.floor(J)
            y = np.floor(I)
#             if x<0 or y < 0 or x>=img.shape[0] or y >= img.shape[1]:
#                 continue
            x = np.int(x)
            y = np.int(y)
            a = J-x
            b = I-y
            D[i,j] = (img[x,y]*(1-a)*(1-b)+img[np.int(x+1),y]*a*(1-b)+img[x,np.int(y+1)]*(1-a)*b+img[np.int(x+1),np.int(y+1)]*a*b)#.astype(int)
            

plt.imshow(np.uint8(D))
plt.imsave('res18.jpg',np.uint8(D))

pts_src = np.array([[108,382],[292,319],[396,600],[210,666]],dtype = np.float64)

W = np.linalg.norm(pts_src[0]-pts_src[1])
H = np.linalg.norm(pts_src[1]-pts_src[2])
pts_dst = np.array([[0,0],[W,0],[W,H],[0,H]],dtype = np.float64)
Tform, status = cv2.findHomography(pts_dst,np.flip(pts_src),cv2.RANSAC)
height, width = img.shape[:2]
D = np.zeros((np.int(H),np.int(W),3))
for i in range (D.shape[0]-2):
    for j in range(D.shape[1]-2):
            I,J,c = np.dot(Tform,np.array([j,i,1]))
            I,J = I/c,J/c
            x = np.floor(J)
            y = np.floor(I)
#             if x<0 or y < 0 or x>=img.shape[0] or y >= img.shape[1]:
#                 continue
            x = np.int(x)
            y = np.int(y)
            a = J-x
            b = I-y
            D[i,j] = (img[x,y]*(1-a)*(1-b)+img[np.int(x+1),y]*a*(1-b)+img[x,np.int(y+1)]*(1-a)*b+img[np.int(x+1),np.int(y+1)]*a*b)#.astype(int)
            

plt.imshow(np.uint8(D))
plt.imsave('res16.jpg',np.uint8(D))

pts_src = np.array([[361,744],[153,707],[206,427],[407,465]],dtype = np.float64)

W = np.linalg.norm(pts_src[0]-pts_src[1])
H = np.linalg.norm(pts_src[1]-pts_src[2])
pts_dst = np.array([[0,0],[W,0],[W,H],[0,H]],dtype = np.float64)
Tform, status = cv2.findHomography(pts_dst,(pts_src),cv2.RANSAC)
height, width = img.shape[:2]
D = np.zeros((np.int(H),np.int(W),3))
for i in range (D.shape[0]-2):
    for j in range(D.shape[1]-2):
            I,J,c = np.dot(Tform,np.array([j,i,1]))
            I,J = I/c,J/c
            x = np.floor(J)
            y = np.floor(I)
#             if x<0 or y < 0 or x>=img.shape[0] or y >= img.shape[1]:
#                 continue
            x = np.int(x)
            y = np.int(y)
            a = J-x
            b = I-y
            D[i,j] = (img[x,y]*(1-a)*(1-b)+img[np.int(x+1),y]*a*(1-b)+img[x,np.int(y+1)]*(1-a)*b+img[np.int(x+1),np.int(y+1)]*a*b)#.astype(int)
            

plt.imshow(np.uint8(D))
plt.imsave('res17.jpg',np.uint8(D))