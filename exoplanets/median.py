#!/usr/bin/env

import psycopg2 as pg
import numpy as np

def column_stats(table, column):
  conn = pg.connect(dbname='db', user='grok')
  cursor = conn.cursor()
  
  query = 'SELECT ' + column + ' FROM ' + table + ';'
  
  cursor.execute(query)
  col = np.array(cursor.fetchall())
  
  return np.mean(col), np.median(col)