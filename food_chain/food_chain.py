import numpy as np
import matplotlib.pyplot as plt
from colorsys import hls_to_rgb

N = 300
dt = 30/N

n = 10 # number of individuals in population

# initial conditions
y = [np.array([0.1 for _ in range(n+1)])] # [y0]
y = [np.array([0.1*(i+1) for i in range(n+1)])] # [y0]


# global parameters (don't change)
I = 1
eps = [1 for _ in range(n)]
a = [1 for _ in range(n)]
d = 1

def f(t,X):
    """System of n+1 equations for the problem."""
    return np.array(
        [I-a[0]*X[0]*X[1]] + 
    [
        eps[i]*a[i]*X[i]*X[i+1] - a[i+1]*X[i+1]*X[i+2]
        for i in range(n-1)
    ] +
        [eps[-1]*a[-1]*X[-2]*X[-1]-d*X[-1]]
    )


def explicit(f,y):
    t = 0
    for _ in range(N):
        t += dt
        y.append(f(t-dt,y[-1])*dt + y[-1])
    return y

def extract(iter, pos):
    return [iter[i][pos] for i in range(len(iter))]


# set up graphics settings
fig, AX = plt.subplots(n+1)
fig.set_figheight(4)
fig.set_figwidth(9)

# make colour wheel for pretty rainbow species :)
color = [hls_to_rgb(k, 0.5, 0.8) for k in np.linspace(0,1,n+1)]

exV = explicit(f,y)
solt, solX = [dt*i for i in range(N+1)], [extract(exV,k) for k in range(n+1)]

for i, (solx, ax, c) in enumerate(zip(solX, AX, color)): 
    ax.plot(solt, solx, color=c, label="$x_{" + str(i) + "}(t)$")
    ax.set_ylim([0,10])
    ax.legend(loc='center left')

plt.show()
