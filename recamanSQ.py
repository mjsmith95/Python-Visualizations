# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:30:13 2019

@author: miles

A rundown of how the Sequence works: 
- The basic idea is subract if you can and its a new value (go back), otherwise add (go forward) 
- Mathematicaly the seq is defined as 
       
        (n-1)-n if (n-1)-n > 0 and is new, ie not already in the seq 
a(n) = 
        n-1 + n otherwise,
       
- The first ten terms in the recaman seq are:
    1 3 6 2 7 13 20 12 21 11 22  ￼

Visualizing the recaman seq: 
- To visualize we draw a semi circle between the current value n, in the seq, and the next value, n+1 
- The radius of a given semi circle is the distance between n+1 and n divided by 2 
- If the distance between the two values in the seq are postive (we are going foward) the semi circle will be located in the postive plane 
- Else the distance is negative and we are going back, then the semi circle is located in the negative xy plane 
- We shift each semi circle by current distance traveled, or the current value in the seq        
    """
import matplotlib.pyplot as plt
import numpy as np
#import imageio # for creating a gif of the visualization, not currently being used 




def recaman(bound): # Choose an upper bound inclusive to ternimate the seq 

  seq = [] # create a list of all order values in the seq 

  for i in range(bound): 

    if(i == 0):  # edge case, when n = 0 , set the current val to zero 
        x = 0

    else:  # otherwise proced as normal, going back 
        x = seq[i-1]-i 

    if(x>=0 and x not in seq):  # check if we cant go back and if the current value is not it the seq 
        seq+=[x] # We just add x to the list 

    else:  # If the above is not true, then we move forward, meeting the other case 
        seq+=[seq[i-1]+i] # add the new value to the lise 

  return seq


def recaman_viz(bound,stepSize): #Have to now include a step size, to plot the semi circles  
    
    seq = recaman(bound) # First we generate a list of values in the recaman seq 
    t = np.arange(-100,100,stepSize)  
    
    for i in range(len(seq)):  
              
        if i == len(seq)-1: #Stop if we reached the final value, as we have not more semi circles to plot  
            break
        
        else:  # otherwise draw a semi circle 
            
            radius = (seq[i+1] - seq[i])/2 # radius = the difference between two points in the sequence divided by 2      
            xShift = (seq[i+1] - seq[i])/2 + seq[i] # move the center of the semicircle to half way between the current value and the next value 
            x,y = (radius * np.sqrt(2) * np.sin(t/2)) + xShift,(radius * np.sqrt(np.cos(t))) #generated points, using the parametric equations for a semi circle 
            # plot the current semi circle 
            plt.plot(x,y,linewidth=0.1)
    plt.axis('off')
    plt.savefig('recaman'+str(bound)+'.png')
    plt.show() 
 
    
    
recaman_viz(50,0.01)    
# For creating a animation,not currently working will be updated / fixed     
    
#def animated_recaman(points,stepSize): 
#    a,b=points[0],points[1]
#    t = np.arange(-100,100,stepSize) 
#    
#    fig, ax = plt.subplots(figsize=(10,5))
#    ax.axis('off')
#    
#
#    radius = (b - a)/2 # radius = the difference between two points in the sequence     
#    xShift = (b - a)/2 + a # move the center of the semicircle to the middle of the current to points
#            
#    x,y = (radius * np.sqrt(2) * np.sin(t/2)) + xShift,(radius * np.sqrt(np.cos(t)))
#            
#    ax.plot(x, y,color = 'teal')  
#           
#
#    # Used to return the plot as an image rray
#    fig.canvas.draw()       # draw the canvas, cache the renderer
#    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
#    image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
#    
#    return image
#seq = recaman(20)
#kwargs_write = {'fps':1.0, 'quantizer':'nq'}
#imageio.mimsave('./recaman1.gif', [animated_recaman([seq[i],seq[i+1]], 0.1) for i in range(20)], fps=1)