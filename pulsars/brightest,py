#!/usr/bin/env python3

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

def load_fits(fitsFile):
  hdulist = fits.open(fitsFile)
  data = hdulist[0].data
  coordArr = np.where(data == np.amax(data))
  return tuple(zip(coordArr[0], coordArr[1]))[0]

if __name__ == '__main__':
  bright = load_fits('image2.fits')
  print(bright)

  from astropy.io import fits
  import matplotlib.pyplot as plt

  hdulist = fits.open('image2.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()
