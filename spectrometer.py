#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import tifffile as tiff

a = tiff.imread('still3.tif')
pixels = []

for x in range(0,1300):
    s = 0.0
    c = 0
    
    for y in range(0,123):
        s += (int(a[y][x][0]) + int(a[y][x][1]) + int(a[y][x][2]))/3.0
        c += 1.0

    pixels.append(s/c)

plt.plot(range(len(pixels)),pixels)
plt.show()
