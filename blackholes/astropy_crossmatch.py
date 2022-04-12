#!/usr/bin/env python3

import numpy as np
from astropy.coordinates import SkyCoord
from astropy import units as u
import time

def crossmatch(cat1, cat2, max_rad):
  start_time = time.perf_counter()
  
  matches = []
  no_matches = []
  
  cat1_sc = SkyCoord(cat1*u.degree, frame='icrs')
  cat2_sc = SkyCoord(cat2*u.degree, frame='icrs')
  
  closest_ids, closest_dists, _ = cat1_sc.match_to_catalog_sky(cat2_sc)
  
  for id1, (closest_id2, dist) in enumerate(zip(closest_ids, closest_dists)):
    closest_dist = dist.value
    if closest_dist > max_rad:
      no_matches.append(id1)
    else:
      matches.append([id1, closest_id2, closest_dist])
      
  time_taken = time.perf_counter() - start_time
  return matches, no_matches, time_taken

# Test crossmatch function using k-d tree optimization
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