#!/usr/bin/env python3

import numpy as np

def hms2dec(hour, min, sec):
  return 15*(hour + min/60 + sec/(60*60))

def dms2dec(deg, min, sec):
  if deg >= 0:
    return deg + min/60 + sec/(60*60)
  else:
    return -1*(-deg + min/60 + sec/(60*60))

def angular_dist(ra1, dec1, ra2, dec2):
    ra1_rad = np.radians(ra1)
    ra2_rad = np.radians(ra2)
    dec1_rad = np.radians(dec1)
    dec2_rad = np.radians(dec2)
    
    a = np.sin(np.abs(dec1_rad - dec2_rad)/2)**2
    b = np.cos(dec1_rad)*np.cos(dec2_rad)*np.sin(np.abs(ra1_rad - ra2_rad)/2)**2
    d = 2*np.arcsin(np.sqrt(a + b))
    
    return np.degrees(d)

def import_bss(filename):
  cat = np.loadtxt(filename, usecols=range(1, 7))
  catFormat = []
  for i in range(len(cat)):
    tmp = (i+1, hms2dec(cat[i][0], cat[i][1], cat[i][2]), dms2dec(cat[i][3], cat[i][4], cat[i][5]))
    catFormat.append(tmp)
  return catFormat

def import_super(filename):
  cat = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0, 1])
  catFormat = []
  for i in range(len(cat)):
    tmp = (i+1, cat[i][0], cat[i][1])
    catFormat.append(tmp)
  return catFormat

def find_closest(catalog, ra, dec):
  dist = angular_dist(ra, dec, catalog[0][1], catalog[0][2])
  id = catalog[0][0]
  for i in range(1, len(catalog)):
    tmp = angular_dist(ra, dec, catalog[i][1], catalog[i][2])
    if tmp < dist:
      dist = tmp
      id = catalog[i][0]
  
  return (id, dist)

def crossmatch(bss, super, max_dist):
  matches = []
  no_matches = []
  for id1, ra1, dec1 in bss:
    closest_dist = np.Inf
    closest_id2 = None
    for id2, ra2, dec2 in super:
      dist = angular_dist(ra1, dec1, ra2, dec2)
      if dist < closest_dist:
        closest_id2 = id2
        closest_dist = dist
    if closest_dist > max_dist:
      no_matches.append(id1)
    else:
      matches.append((id1, closest_id2, closest_dist))
    
  return matches, no_matches
  
if __name__ == '__main__':
  print(hms2dec(23, 12, 6))
  print(dms2dec(22, 57, 18))
  print(dms2dec(-66, 5, 5.1))
  print(angular_dist(21.07, 0.1, 21.15, 8.2))
  bss_cat = import_bss('data/small_bss.dat')
  super_cat = import_super('data/small_super.csv')
  print(bss_cat)
  print(super_cat)
  cat = import_bss('data/bss.dat')
  print(find_closest(cat, 175.3, -32.5))
  print(find_closest(cat, 32.2, 40.7))
  bss_cat = import_bss(bss.dat)
  super_cat = import_super('data/super.csv')
  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))
  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))