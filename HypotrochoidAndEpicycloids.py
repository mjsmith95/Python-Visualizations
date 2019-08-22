
import numpy as np
import turtle as tr
import matplotlib.pyplot as plt


    
def hypotrochoid(R,r,d,theta):
    Rr = R - r
    theta_val = (((R - r) / r) * theta)*180/np.pi
    x = Rr*np.cos(theta)+d*np.cos(theta_val)
    y = Rr*np.sin(theta)+d*np.sin(theta_val)
    return(x,y)
x_vals = [] 
y_vals = []   
x_vals2 = [] 
y_vals2 = []


def create_spiro(a, b, d):
    dt = 0.001
    t = 0
    pts = []
    while t < 2*np.pi*b/np.gcd(a, b):
        t += dt
        x = (a - b) * np.cos(t) + d * np.cos((a - b)/b * t)
        y = (a - b) * np.sin(t) - d * np.sin((a - b)/b * t)
        pts.append((x, y))
    return pts

    
    


vals=create_spiro(5,6,1) #8 7 1 are good vals  
x = list(zip(*vals))[0]
y = list(zip(*vals))[1]
plt.axis('off')
plt.plot(x,y) #plot a line by the the two points in cart cord. 
plt.savefig('Hypotrochoid1.png')
plt.show()