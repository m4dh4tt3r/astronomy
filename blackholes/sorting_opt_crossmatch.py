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
  order = np.argsort(cat2[:, 1])
  cat2_ordered = cat2[order]
  
  for id1, (ra1, dec1) in enumerate(cat1):
    min_dist = np.Inf
    min_id2 = None
    max_dec = dec1 + max_rad
    for id2, (ra2, dec2) in enumerate(cat2_ordered):
      if dec2 > max_dec:
        break
        
      dist = angular_dist(ra1, dec1, ra2, dec2)
      if dist < min_dist:
        min_id2 = order[id2]
        min_dist = dist
        
    if min_dist > max_rad:
      no_matches.append(id1)
    else:
      matches.append((id1, min_id2, np.degrees(min_dist)))
      
  time_taken = time.perf_counter() - start
  return matches, no_matches, time_taken
  
# Test crossmatch function with sorting optimization
if __name__ == '__main__':
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
