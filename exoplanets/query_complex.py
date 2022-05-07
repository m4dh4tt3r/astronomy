#!/usr/bin/env python3

import numpy as np

# SELECT p.radius/s.radius AS radius_ratio
# FROM Planet AS p
# INNER JOIN star AS s USING (kepler_id)
# WHERE s.radius > 1.0
# ORDER BY p.radius/s.radius ASC;

def query(file1, file2):
  stars = np.loadtxt(file1, delimiter=',', usecols=(0,2))
  planets = np.loadtxt(file2, delimiter=',', usecols=(0,5))
  
  filtered_stars = stars[stars[:, 1] > 1, :]
  sorted_stars = filtered_stars[np.argsort(filtered_stars[:, 1]), :]
  
  results = np.zeros((1,1))
  for i in range(sorted_stars.shape[0]):
    kepler_id = sorted_stars[i, 0]
    star_radius = sorted_stars[i, 1]
    
    planet_match = planets[np.where(planets[:, 0] == kepler_id), 1].T
    results = np.concatenate((results, planet_match/star_radius))
  
  return np.sort(results[1:], axis=0)
  
if __name__ == '__main__':
  result = query('data/stars2.csv', 'data/planets2.csv')