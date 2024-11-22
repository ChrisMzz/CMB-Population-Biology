import numpy as np
import matplotlib.pyplot as plt

N = 300
dt = 10/N

# feel free to play around with this
y = [np.array([1,1])] # [y0]

# all parameters for the model
r = 1.4
K = 3
a = 0.8
h = 0.6
c = 1.4
d = 0.9

def f(t,y):
    """Differential equation system where y=(N,P)."""
    N, P = y
    return np.array([
    r*N*(1-N/K)-a*N/(1+a*h*N)*P,
    c*a*N/(1+a*h*N)*P-d*P
])

def explicit(f,y):
    t = 0
    for _ in range(N):
        t += dt
        y.append(f(t-dt,y[-1])*dt + y[-1])
    return y

def extract(iter, pos):
    return [iter[i][pos] for i in range(len(iter))]


# set up graphics settings
fig, ax = plt.subplots()
fig.set_figheight(4)
fig.set_figwidth(9)

exV = explicit(f,y)
solt, solx, soly = [dt*i for i in range(N+1)], extract(exV,0), extract(exV,1)

# draw phase diagram for the model
ax.plot(solx, soly, color=(0.1,0.1,0.1))

plt.show()
