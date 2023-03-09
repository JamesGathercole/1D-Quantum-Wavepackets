# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:33:59 2023

@author: james
"""

import numpy as np
import matplotlib.pyplot as plt
from itertools import zip_longest

x = np.linspace(-5,5,101)
i = complex(0,1)
h_bar = 1
m = 1

#k = float(input("Enter the value for the wave number k = "))
#t = float(input("Enter the value for the time t = "))
#x = float(input("Enter the value for the x-values x  = ")) 


def phi(k,t):
    E_k = (((h_bar*k)**2)/(2*m))
    return np.e**(-i*(E_k/h_bar)*t)

def psi_well(n_min,n_max,L,x):
    n = np.linspace(n_min, n_max, (n_max-n_min+1))
    k = (n*np.pi)/(2*L)
    for value in n:
        if (value % 2) == 0:
           return np.sin(k*x)
        else:
           return np.cos(k*x)

n_min = 41
n_max = 51
L = 100
n = np.linspace(n_min, n_max, (n_max-n_min+1))
k = (n*np.pi)/(2*L)
print(n)
print(k)

psi_well(41,51,100,x)
#print(psi_well)








