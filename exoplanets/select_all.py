#!/usr/bin/env python3

import psycopg2 as pg

def select_all(tb_name):
  conn = pg.connect(dbname='db', user='grok')
  cursor = conn.cursor()

  cursor.execute('SELECT * FROM ' + tb_name + ';')
  records = cursor.fetchall()

  return records