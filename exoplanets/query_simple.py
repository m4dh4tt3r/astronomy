#!/usr/bin/env python3

import numpy as np

# SELECT kepler_id, radius
# FROM Star
# WHERE radius > 1.0;

def query(file):
  data = np.loadtxt(file, delimiter=',', usecols=(0,2))
  return data[data[:, 1] > 1, :]
  
if __name__ == '__main__':
  result = query('data/stars2.csv')