#!/usr/bin/env python3

import numpy as np

def mean_datasets(fileList):
  data = np.loadtxt(fileList[0], delimiter=',')
  for n in range(1, len(fileList)):
    tmp = np.loadtxt(fileList[n], delimiter=',')
    data += tmp
  return np.round(data/len(fileList), 1)

if __name__ == '__main__':
  print(mean_datasets(['data/data1.csv', 'data/data2.csv', 'data/data3.csv']))
  print(mean_datasets(['data/data4.csv', 'data/data5.csv', 'data/data6.csv']))
