# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:24:15 2018

@author: John Wilson
"""

import numpy as np

# dy/dx + y = x

def dintt(argF,y0,x0,x1,N) :
    
    # This is a definite integral function
    
    xs = np.linspace( x0, x1, num=N, endpoint=True )
    
    ys = argF( xs ) + y0
    
    h = ( x1 + x0 ) / N
    
    area = 0
    
    for i in range( len( xs ) - 1 ):
        
        temp = h*( ys[i] + ys[i + 1] ) / 2
        
        area = area + temp
    
    return(area)
    
    
def f(x) :
    
    return( np.float64( x ) )

dintt(f,1,0,1,5000)

