# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:33:06 2019

@author: saki
"""

import numpy as np


W = np.array([[0.6, 0.1, 0.1, 0.1, 0.1],
              [0.1, 0.6, 0.1, 0.1, 0.1],
              [0.1, 0.1, 0.6, 0.1, 0.1],
              [0.1, 0.1, 0.1, 0.6, 0.1],
              [0.1, 0.1, 0.1, 0.1, 0.6]])

u = np.array([[0.6, 0.5, 0.6, 0.2, 0.1]]).reshape(5,1)

M = np.array([[-0.125, 0, 0.125, 0.125, 0],
              [0, -0.125, 0, 0.125, 0.125],
              [0.125, 0, -0.125, 0, 0.125],
              [0.125, 0.125, 0, -0.125, 0],
              [0, 0.125, 0.125, 0, -0.125]]) * 2


eig_val, eig_vec = np.linalg.eig(M)
v_ss = np.sum(((W @ u).T @ eig_vec / (1 - eig_val)) * eig_vec, axis = 1)
print(v_ss)

