
# coding: utf-8

# Chapter 5: Elliptic  Curves


#Libs 
import seaborn as sb 
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.cm as cm  


# Elliptic cruve over a finite field,
# This func generates the set of points for a given ec equation, over a finite field 
# where A, and B are the constants in the elliptic curve equation, and M is the modulus

def E_C_F(A,B,M):  
    # Create an empty list where
    # we can store all points that work in the elliptic curve equation
    points = [] 
    
    for Y in range(0,M):
        for X in range(0,M): 
            if(((X**3+A*X+B)%M)==(Y**2%M)): 
                points.append((X,Y))
                
    points = np.array(points) # cast to numpy array so that we can plot the set on a scatter plot 
    return(points) 

 
# Check if our points are valid
# Used when adding two points together on a curve over a finite field  
def check_Valid(P,a,b,p):  
    # Check if it is the point at infinity
    if(P[1] == 0 and P[0]==0):  
        return(True)
    # If Y^2 - (X^3+AX+B) = 0 mod p, then we have a valid point 
    if(((P[1]**2-(P[0]**3 + a*P[0] + b))%p == 0) and 0 <= P[0] < p and 0 <= P[1] < p):  
        return(True)
    else: 
        return(str(P)+' is not a point on the curve, with A = '+str(a)+' and B = '+str(b)) # return the invalid points points
           


# Adding points together algorithm mod p, where p is a prime
# p1 is point 1, p2 is point 2, p is the modulus, where p1,p2 should vectors, a,b are from the equation 
# get all the x,y values for the points p1,p2
def add_Points(p1,p2,a,b,p):  
    
    x1,y1 = p1[0],p1[1]
    x2,y2 = p2[0],p2[1]
       
    # If the points are indeed valid, we add them together
    if(check_Valid(p2,a,b,p) == True and check_Valid(p1,a,b,p) == True):
        # p1 = -p2 return an empty point, since we can't actualy make a point at infinity
        if ((y1 == -1*y2%p)) and ((x1==x2)): 
            q = [0,0]
            return(q)
       
        # The points are not equal
        if (p1 != p2 ): 
            slope = ((y2-y1))*((x2-x1)**(p-2))%p 
            print(slope)

        # The points are equal
        if (p1 == p2):    
            slope = ((3*x1**2+a)%p*((2*y1)**(p-2)))%p 
            print(slope)
            
        # Generate the new point (x,y) 
        x3 = (slope**2-x1-x2)%p
        y3 = (slope*(x1-x3)-y1)%p
        q = [x3,y3]
        
        return(q)
    
    else:
        return('One of the points is not on the curve.')



######################################################################################################################################################
#                                                                             EXAMPLES: PLOTS AND FUNCS                                              #
######################################################################################################################################################

# Elliptic Curve: Y^2 = X^3 - 3X + 3 
# First figure with a walkthrough of how to make it.



plt.figure() # Create a new figure window

xlist = np.linspace(-3,7 , 100) # Create 1-D arrays for x,y dimensions
ylist = np.linspace(-7,7, 100)

X,Y = np.meshgrid(xlist, ylist) # Create 2-D grid xlist,ylist values

Z = X**3 -3*X+3- Y**2 # we express Z as a parametric equation of X and Y, this is how we are able to plot an Elliptic Curve



CS=plt.contour(X, Y, Z,[0.0],cmap = 'plasma') # cmap changes the color map of the contor plot 
                                              # and [0.0] restricts the map to a single contour 

plt.title(r'$E:Y^2 = X^3 -3X + 3$') # r'$...$' lets you write in latex math mode in the title of the plot ! 
plt.savefig('fig5.4.svg', format='svg', dpi=1200) # Savig a figure, dpi changes the resolution, and format changes the file type
                                                  # 'svg' file type stands for Scalable Vector Graphics, so you look good at every Size ! 
plt.show() # Show the plot ! 


# # Elliptic Curve: Y^2 = X^3 - 6X + 5 
# 
# For the next Elliptic curve, we can just use the same code as above. All need to do, is change the equation to 
# $$Y^2=X^3-6X+5$$
# 



plt.figure() 
xlist = np.linspace(-3,7, 100) 
ylist = np.linspace(-10,10,100)
X,Y = np.meshgrid(xlist, ylist) 
Z = X**3 -6*X+5- Y**2




CS=plt.contour(X, Y, Z,[0.0],cmap = 'plasma') 

plt.title(r'$E:Y^2 = X^3 -6X + 5$')
plt.savefig('fig5.6.svg', format='svg', dpi=1200)

plt.show()


# # E: Y^2 = X^3 - 3X + 2



plt.figure() 

xlist = np.linspace(-3,7, 100) 
ylist = np.linspace(-9,7, 100)

X,Y = np.meshgrid(xlist, ylist) 

Z = X**3 -3*X+2- Y**2




CS=plt.contour(X, Y, Z,[0.00000],cmap = 'plasma') 

#plt.clabel(CS, inline=1, fontsize=10) # adds a label within the plot if you want it 

plt.title(r'$E:Y^2 = X^3 -3X + 2$') 
plt.savefig('fig5.7.svg', format='svg', dpi=1200)

plt.show()


# # Example 5.1.1 
# With the elliptic curve $E: Y^2 = X^3-15X+18$



def f(x): #create a function for the slope/line 
    return (7/3)*x-(1/3)

t1 = np.arange(-5.0, 20.0, 0.1) # a plotting range 

xVals=[7,1] # the x cooridantes for points P and Q
yVals=[16,2] # the y cooridantes for points P and Q  
rX = [-23/9,-23/9] # x cooridantes for R and R'
rY = [170/27,-170/27] # y cooridantes for R and R'




plt.figure() 

xlist = np.linspace(-5,20 , 100) 
ylist = np.linspace(-50,50, 100)

X,Y = np.meshgrid(xlist, ylist) 

Z = X**3 -15*X+18- Y**2




CS=plt.contour(X, Y, Z,[0.0],cmap = 'plasma') # plot the elliptic equation 

plt.scatter(xVals,yVals,color='red') # plot points P and Q, 'ro' makes the points red
plt.plot(rX,rY,'ro',linestyle=':') #plot points R and R', the linestyle arugment adds the dotted line between the two points
plt.plot(t1, f(t1),color='purple') # plot the line between P and Q 

#plt.clabel(CS, inline=1, fontsize=10) #adds an in plot label for the elliptic function 
plt.title(r'$E:Y^2 = X^3 -15X + 18$') 
plt.savefig('example5.1.1.svg', format='svg', dpi=1200)

plt.show()




e1=E_C_F(3,8,13) # get the set of points for E: Y^2=X^3+3*X+8 over F13 
print(e1)




plt.scatter(e1[:,0],e1[:,1],color='teal',marker='x')# create a scatter plot, with all the points the work for E: Y^2=X^3+3X+8
plt.title(r'$E:Y^2=X^3+3X+8  \quad  over \quad \mathbb{F}_{13}$') 
plt.savefig('fig_5.9.svg', format='svg', dpi=1200) 

plt.show() 



e2=E_C_F(3,8,1009) # get the set of points for E: Y^2=X^3+3*X+8 over F1009 
print(e2)




plt.scatter(e2[:,0],e2[:,1],color='teal',marker='.')

plt.title(r'$E:Y^2=X^3+3X+8  \quad  over \quad \mathbb{F}_{1009}$') 
plt.savefig('fig_5.10.svg', format='svg', dpi=1200) 
                                                    
plt.show() 
# Notice there is actually really cool symtery in this plot !



