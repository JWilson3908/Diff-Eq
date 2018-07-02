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

#%%

def firstorder(y,t):
    
    k = 2.0
    tau = 5.0
    u = 1.0
    
    dy_dt = ( -y + k*u ) / tau
    
    return dy_dt

#%%

ts = np.linspace(0,10,11)

ys = si.odeint( firstorder, 0, ts )

print( ys )
