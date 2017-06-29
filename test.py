# -*- coding: utf-8 -*-

"""
Reglas:

Repartir máximo 9 puntos entre todas las materias, con:
- mínimo tres materias con preferencia > 0
- mínimo una materia con preferencia 3
"""

import numpy as np
import random as rnd
import copy
import pylab as pl

materias = [1, 2, 2, 2, 1, 2]
total_cargos = 10
pref = np.loadtxt('pref.dat')

dist = [0, 1, 1, 2, 2, 3, 3, 4, 5, 5] # qué materia le toca a cada uno

def evaluar_dist(dist, pref, materias):
  costo = 0
  for ay, mat in enumerate(dist):
    if pref[ay,mat] == 0: costo += 1000
    else: costo -= pref[ay,mat]
  return costo

def cambiar_dist(dist):
  d_fin = copy.copy(dist)
  ay1 = rnd.randint(0, 9)
  ay2 = rnd.randint(0, 9)
  d_fin[ay1], d_fin[ay2] = dist[ay2], dist[ay1]
  return d_fin

arr_costo = []
for T in np.linspace(3, 0, 100000)[:-1]:
  costo = evaluar_dist(dist, pref, materias)
  dist_fin = cambiar_dist(dist)
  c_fin = evaluar_dist(dist_fin, pref, materias)
  r = rnd.random()
  if r < np.exp((costo - c_fin)/T):
 # if c_fin < costo:
    dist = dist_fin
    costo = c_fin
  arr_costo.append(costo)
  #print r, np.exp((costo - c_fin)/T), T, costo, dist
pl.plot(arr_costo)
pl.show()

print dist
print pref
