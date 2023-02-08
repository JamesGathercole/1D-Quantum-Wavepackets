# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:46:40 2023

@author: james
"""
import numpy as np
import matplotlib.pyplot as plt
import cmath
from itertools import zip_longest

x = np.linspace(0,2*np.pi,101)
i = complex(0,1)
h_bar = 1.054571817*10**-34
m = 9.11*10**-31

#k = float(input("Enter the value for the wave number k = "))
#t = float(input("Enter the value for the time t = "))
#x = float(input("Enter the value for the x-values x  = ")) 


def phi(k,t):
    E_k = (((h_bar*k)**2)/(2*m))
    return np.e**(-i*(E_k/h_bar)*t)

def psi(k,x):
    return np.cos(k*x) + i*np.sin(k*x)

def zero(x):
    return x*0 + i*x*0 

def PSI(amp,psi,phi):
    return amp*psi*phi

def P(c,d):
    return c*d.conjugate()


k = [8,8.2,8.4,8.6,8.8,9,9.2,9.4,9.6,9.8,10]
amp_k = [0,0.2,0.4,0.6,0.8,1,0.8,0.6,0.4,0.2,0]
#k_0 = 9
#delta_k = 
#n_k = 
t = 0
PSI_total = zero(x)
print(PSI_total)

for a, b in zip_longest(k, amp_k):
    psi_k = psi(a,x)
    phi_k = phi(a,t)
    PSI_k = PSI(b,psi_k,phi_k)
    PSI_total += PSI_k
    print(a)
    print(b)
    print(PSI_total)   


Probability = P(PSI_k,PSI_k)   

plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.plot(x, PSI_k.real)
plt.xlabel('x values')
plt.ylabel('\u03C8 (Re)')

plt.subplot(1,3,2)
plt.plot(x, PSI_k.imag)
plt.xlabel('x values')
plt.ylabel('\u03C8 (Im)')

plt.subplot(1,3,3)
plt.plot(x, Probability)
plt.xlabel('x values')
plt.ylabel('\u03C8*\u03C8')


plt.show()
