import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

N = 300
dt = 30/N

y = [1]

Q = 10

term1 = lambda x : R*(1-x/Q)
term2 = lambda x : x/(1+x**2)

def f(t,x):
    """The differential equation."""
    return term1(x) - term2(x)

def explicit(f,y):
    """Euler explicit scheme designed to solve the equation."""
    t = 0
    for _ in range(N):
        t += dt
        y.append(f(t-dt,y[-1])*dt + y[-1])
    return y

equilibria = []

fig, (ax1, ax2, ax3) = plt.subplots(1,3)
fig.set_figheight(4), fig.set_figwidth(9)

x = np.linspace(0,10,100)
Rs = np.linspace(0.2,0.7,100)
solt = [dt*i for i in range(N+1)]

for R in Rs:
    solx = explicit(f,deepcopy(y)) # get solution of equation

    # plot solution on axis 1
    ax1.plot(solt, solx, color=(R,0,1-R))

    # plot term1 and term2 on axis 2 
    ax2.plot(x, term1(x), color=(R,0,0))
    ax2.plot(x, term2(x), color=(0,0,R))

    # get x value of intersection points of term1 and term2 for the current R value
    for xi in x:
        r1, r2 = term1(xi), term2(xi) 
        if abs(r1-r2)<5e-3: equilibria.append([R,xi])

# plot x value of intersection points of term1 and term2 for each R
ax3.plot(*(np.array(equilibria).T), ".")
plt.show()

# The type of birfucation diagram we obtain shows that we hve hysteresis

# see berryman turchin 2001 paper for details on second order dynamics

