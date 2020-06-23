# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 17:06:44 2020

@author: Avinash
"""

import cv2
import numpy as np

#################################
#Creating each images of Gaussian-pyramid manually
img = cv2.imread("Image_pyramid.jpg")
img1 = img.copy()
lr1 = cv2.pyrDown(img1)
lr2 = cv2.pyrDown(lr1)

cv2.imshow("Original Image",img)
cv2.imshow("Pyr Down1", lr1)
cv2.imshow("Pyr Down", lr2)



###############################
#Creating Gaussian-pyramid using loop

layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)
    
#############################
#Creating laplacian-pyramid

layer = gp[5]
cv2.imshow("Upper level of Gaussian Pyramid", layer)

lp = [layer]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.absdiff(gp[i-1], gaussian_extended)
    cv2.imshow(str(i),laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
