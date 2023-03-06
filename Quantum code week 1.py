# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:46:40 2023

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

def psi_well(k,L,x):
    return np.cos(((k*np.pi*x)/L)) + i*np.sin((k*np.pi*x)/L)

def psi(k,x):
    return np.cos(k*x) + i*np.sin(k*x)

def zero(x):
    return range(x)

def zero_complex(x):
    return x*0 + i*x*0 

def PSI(amp,psi,phi):
    return amp*psi*phi

def P(c,d):
    return c*d.conjugate()

k_min = 5
k_max = 15
n_k = 11
n = 11
#k = [5,6,7,8,9,10,11,12,13,14,15]
amp_k = [0,0.2,0.4,0.6,0.8,1,0.8,0.6,0.4,0.2,0]
L = 31
k = np.linspace(k_min, k_max, n_k)
delta_k = 2/(n_k-1)

amp = zero_complex(n_k)
for item in range(n_k):
    if n < (n_k - 1)/2:
       A = 0 + n*delta_k
    elif n == (n_k - 1)/2:
         A = 1
    else:
         A = 1-((n - ((n_k - 1)/2))*delta_k)
    amp += A  

print(A)

t = 0
PSI_total = zero_complex(x)

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
plt.axis([-10,10,-1,25])
plt.xlabel('x values')
plt.ylabel('\u03C8*\u03C8')


plt.show()
