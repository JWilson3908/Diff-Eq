# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 13:43:58 2018

@author: John Wilson

T dy/dt = -y + k u
Example function from a youtube video
http://apmonitor.com/pdc/index.php/Main/SolveDifferentialEquations
"""

#%%

import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as plt

#%% define the integral

def firstorder(y,t,k,u):
    
    tau = 5.0
    
    dy_dt = ( -y + k*u ) / tau
    
    return dy_dt

#%% define constants

ts = np.linspace(0,10,11)

k = 2.0

u = np.zeros( len( ts ) )

u[3:] = 1.0

y0 = 0

#%% Loop through and solve one time interval at a time
# This could possibly be helpful in a PID controller
# Allows for an input to be changed based on an output measurement

ystorage = np.zeros( len( ts ) )
ystorage[0] = y0

for i in range(len(ts)-1) :
       
    step=[ ts[i], ts[i+1] ]
    
    ys = si.odeint( firstorder, y0, step, args=( k, u[i] ) )
    
    y0 = ys[1]
    
    ystorage[i+1] = y0
    
    print( ys[1] )

#%%

plt.plot(ts,ystorage)

plt.show