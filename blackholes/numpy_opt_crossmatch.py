#!/usr/bin/env python3

import numpy as np
import time

def angular_dist(ra1, dec1, ra2, dec2):
    a = np.sin(np.abs(dec1 - dec2)/2)**2
    b = np.cos(dec1)*np.cos(dec2)*np.sin(np.abs(ra1 - ra2)/2)**2
    return 2*np.arcsin(np.sqrt(a + b))

def crossmatch(cat1, cat2, max_rad):
  start = time.perf_counter()
  max_rad = np.radians(max_rad)
  
  matches = []
  no_matches = []
  
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)
  ra2s = cat2[:, 0]
  dec2s = cat2[:, 1]
  
  for id1, (ra1, dec1) in enumerate(cat1):
    dists = angular_dist(ra1, dec1, ra2s, dec2s)
    min_id = np.argmin(dists)
    min_dist = dists[min_id]
    if min_dist > max_rad:
      no_matches.append(id1)
    else:
      matches.append((id1, min_id, np.degrees(min_dist)))
      
  time_taken = time.perf_counter() - start
  return matches, no_matches, time_taken  

# Test crossmatch optimizations
if __name__ == '__main__':
  ra1, dec1 = np.radians([180, 30])
  cat2 = [[180, 32], [55, 10], [302, -44]]
  cat2 = np.radians(cat2)
  ra2s, dec2s = cat2[:,0], cat2[:,1]
  dists = angular_dist(ra1, dec1, ra2s, dec2s)
  print(np.degrees(dists))

  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)
