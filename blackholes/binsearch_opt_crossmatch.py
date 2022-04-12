#!/usr/bin/env python3

import numpy as np
import time

def angular_dist_rad(ra1, dec1, ra2, dec2):
  deltar = np.abs(ra1 - ra2)
  deltad = np.abs(dec1 - dec2)
  angle = 2*np.arcsin(np.sqrt(np.sin(deltad/2)**2 
                      + np.cos(dec1)*np.cos(dec2)*np.sin(deltar/2)**2))
  return angle

def crossmatch(cat1, cat2, max_rad):
  start_time = time.perf_counter()
  deg2rad = np.pi/180
  rad2deg = 180/np.pi
  max_rad = max_rad*deg2rad
  
  matches = []
  no_matches = []
  
  cat1 = cat1*deg2rad
  cat2 = cat2*deg2rad
  
  asc_dec = np.argsort(cat2[:, 1])
  cat2_sorted = cat2[asc_dec]
  dec2_sorted = cat2_sorted[:, 1]

  for id1, (ra1, dec1) in enumerate(cat1):
    closest_dist = np.Inf
    closest_id2 = None
    
    min_dec = dec1 - max_rad
    max_dec = dec1 + max_rad
    
    start = dec2_sorted.searchsorted(min_dec, side='left')
    end = dec2_sorted.searchsorted(max_dec, side='right')
    
    for s_id2, (ra2, dec2) in enumerate(cat2_sorted[start:end+1], start):
      dist = angular_dist_rad(ra1, dec1, ra2, dec2)
      if dist < closest_dist:
        closest_sorted_id2 = s_id2
        closest_dist = dist
        
    if closest_dist > max_rad:
      no_matches.append(id1)
    else:
      closest_id2 = asc_dec[closest_sorted_id2]
      matches.append([id1, closest_id2, closest_dist*rad2deg])
      
  time_taken = time.perf_counter() - start_time
  return matches, no_matches, time_taken

# Test crossmatch function using binary search
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
