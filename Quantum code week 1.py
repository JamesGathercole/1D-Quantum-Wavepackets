# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:46:40 2023

@author: james
"""
import numpy as np
import matplotlib.pyplot as plt
import cmath
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

def psi(k,x):
    return np.cos(k*x) + i*np.sin(k*x)

def psi_step(k,x):
    return 0

def zero(x):
    return x*0 + i*x*0 

def PSI(amp,psi,phi):
    return amp*psi*phi

def P(c,d):
    return c*d.conjugate()


k = [5,6,7,8,9,10,11,12,13,14,15]
amp_k = [0,0.2,0.4,0.6,0.8,1,0.8,0.6,0.4,0.2,0]
#k_0 = 9
#delta_k = 
#n_k = 
t = 100
PSI_total = zero(x)

for a, b in zip_longest(k, amp_k):
    psi_k = psi(a,x)
    phi_k = phi(a,t)
    PSI_k = PSI(b,psi_k,phi_k)
    PSI_total += PSI_k
       

Probability = P(PSI_total,PSI_total)   

plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.plot(x, PSI_total.real, label = 'Time = 100')
plt.legend(loc = 'lower right')
plt.xlabel('x values')
plt.ylabel('\u03C8 (Re)')

plt.subplot(1,3,2)
plt.plot(x, PSI_total.imag, label = 'Time = 100')
plt.legend(loc = 'lower right')
plt.xlabel('x values')
plt.ylabel('\u03C8 (Im)')

plt.subplot(1,3,3)
plt.plot(x, Probability, label = 'Time =100')
plt.legend(loc = 'lower right')
plt.axis([-2,4,-1,25])
plt.xlabel('x values')
plt.ylabel('\u03C8*\u03C8')


plt.show()
