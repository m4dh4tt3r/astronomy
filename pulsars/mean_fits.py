#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

def mean_fits(fitsFiles):
  data = fits.open(fitsFiles[0])[0].data
  for i in range(1, len(fitsFiles)):
    tmp = fits.open(fitsFiles[i])[0].data
    data += tmp
  return data/len(fitsFiles)

if __name__ == '__main__':

  data  = mean_fits(['data/image0.fits', 'data/image1.fits', 'data/image3.fits', 'data/image4.fits'])
  print(data[100, 100])

  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()
