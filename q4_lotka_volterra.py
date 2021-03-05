#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BE523 Biosystems Analysis & Design
HW15 - Question 4. Lotka-Volterra model for owls and voles

Created on Fri Mar  5 00:15:20 2021
@author: eduardo
"""
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
steps = 500

# delta = 1
# alpha = 1
# gamma = 1
# epsilon = 1
# V0, O0 = 0.5, 2  # initial population of voles and owls

delta = 0.02
alpha = 0.06
gamma = 1e-3
epsilon = 2e-4
V0, O0 = 45, 45  # initial population of voles and owls

t = np.linspace(0, steps, int(steps/dt)+1)
V = np.zeros(len(t))
O = np.zeros(len(t))
V[0], O[0] = V0, O0

for i in range(1, len(t)):
    V[i] = V[i-1] + V[i-1] * (alpha - gamma * O[i-1]) * dt
    O[i] = O[i-1] + O[i-1] * (epsilon * V[i-1] - delta) * dt

plt.figure(0)
plt.plot(t, V, 'b-', label='V')
plt.plot(t, O, 'r-', label='O')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend(loc='best')
plt.savefig('q4_lotka_volterra_%dsteps.png' % steps, dpi=300, bbox_inches='tight')
plt.plot()

plt.figure(1)
plt.plot(V, O)
plt.xlabel('V')
plt.ylabel('O')
plt.savefig('q4_lotka_volterra_phase_%dsteps.png' % steps, dpi=300, bbox_inches='tight')
plt.plot()