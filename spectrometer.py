#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import tifffile as tiff

class Spectrometer:
    def __init__(self, images):
        self.images = images
        self.spectra = {}

    def process(self):
        for img in self.images:
            a = tiff.imread(img)
            width = a.shape[1]
            height = a.shape[0]
            pixels = []
            for x in range(width):
                s = 0.0
                c = 0
                for y in range(height):
                    s += (int(a[y][x][0]) + int(a[y][x][1]) + int(a[y][x][2]))/3.0
                    c += 1.0
                pixels.append(s/c)
            self.spectra[img] = pixels

    def show(self):
        for k in self.spectra:
            pixels = self.spectra[k]
            plt.plot(range(len(pixels)),pixels)
            plt.show()

spectrometer = Spectrometer(["img/still3.tif"])
spectrometer.process()
spectrometer.show()
