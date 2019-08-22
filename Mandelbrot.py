# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:12:50 2019

@author: miles


This function visualizes the mandelbrot set in modular arithmetic 

The process is as follows: 
    -Create a set of points evenly spaced around a circle 
    -The size of this set is equal to the modulus ie if m = 10, then we have 10 points
    -We 'label' the points 0 to m - 1 
    -We choose a value n, and for each value from 0 to m-1 we perform the operation i * n % m 
    -We draw a line between the original point and the resulting value above 
    -Example: let n = 2, and m = 10, thus for all i in {0,9} we do i * 2 % 10 
    - 0 * 2 % 10 = 0, so for the first point we dont draw a line (or a line from 0 to 0)
    - 1 * 2 % 10 = 2, so from the point labled 1 we draw a line to the point labeled 2
    - 6 * 2 % 10 = 2, from the point labled 6 we would draw a line back to  

"""

import seaborn as sb #For stylizing the plots 
import matplotlib.pyplot as plt
import numpy as np



def mandelbrot_lines(r,m,n): # input: r = radius of the circle on which points will be place, m = modulus (also the number of points), n = value for multiplication 
    
    theta = (360/m) * (np.pi/180) # plotting all points in polar cord, this is the value in rads that the theta for each point will be spaced by       
    
    for i in range(m): 
        x, y = -r * np.cos((i * theta)), -r * np.sin((i * theta)) # create a point at (x,y) with polar r,theta   
        
        nextPoint = (i * n % m) # perform the operation on i to find the point that (x,y) will connect to  
        finalX, finalY = -r * np.cos((nextPoint * theta)), -r * np.sin((nextPoint * theta)) #find the location of the connecting point
            
        plt.plot([x,finalX],[y,finalY]) #plot a line by the the two points in cart cord. 
    
    plt.axis('off') # to display an image with out any axis or labeling   
    plt.savefig('mandelbrotGraph5thRun'+str(m)+'.png',dpi = 200) 
    plt.show()
    #To save the final plot uncomment the line below
    

mandelbrot_lines(1,150,2)

#for i in np.arange(0.0,31.0,0.1): # to see how the same changes as we change n at a continous rate 
#    mandelbrot_lines(1,200,i)
