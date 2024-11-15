import numpy as np
import matplotlib.pyplot as plt

N = 300
dt = 10/N

y = [np.array([0.75,0.17,9.9])] # [y0] (that's the initial state that the professor had in his R code)

a1, a2 = 5, 0.1
b1, b2 = None, 2 # we will modify b1 later
d1, d2 = 0.4, 0.01


def f(t,u):
    x,y,z = u
    return np.array([
    x*(1-x) - (a1*x*y)/(1+b1*x),
    (a1*x*y)/(1+b1*x) - (a2*y*z)/(1+b2*y) - d1*y,
    (a2*y*z)/(1+b2*y) - d2*z
])

def explicit(f,y):
    t = 0
    for _ in range(N):
        t += dt
        y.append(f(t-dt,y[-1])*dt + y[-1])
    return y

def extract(iter, pos):
    return [iter[i][pos] for i in range(len(iter))]

# figure settings
fig = plt.figure()
fig.set_figheight(4)
fig.set_figwidth(9)
# project in 3D because we have 3 variables in our system
ax = fig.add_subplot(projection='3d')

B = np.arange(2, 6.2,0.1) # list of b1
for b1, color in zip(B, np.linspace(0,1,B.size)):
    exV = explicit(f,y)
    solt, solx, soly, solz = [dt*i for i in range(N+1)], extract(exV,0), extract(exV,1), extract(exV,2)
    # solutions stack off of each other so I gave 10% opacity
    ax.plot(solx, soly, solz, color=(color, 0.1, 0.1, 0.1)) 
    
plt.show()
