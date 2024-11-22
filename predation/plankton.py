import numpy as np
import matplotlib.pyplot as plt
from colorsys import hls_to_rgb
from plankton_presets import *



preset = Fig_4

N = preset.N
dt = preset.dt

n = preset.n # number of species
k = preset.k # number of resources

D = preset.D # constant turnover rate

r = preset.r # specific growth rate of each species
m = preset.m # specific mortality rate of each species
S = preset.S # supply concentration of each resource
K = preset.K
C = preset.C

# initial conditions
y = preset.y

insert_time = preset.insert_time

def mu(i, R):
    return r[i]*np.min(R/(K[:,i]+R))


def f(t,X):
    """
    System of n+k equations for the problem, where the n first ones are for the species, and k next ones for the resources.
    """
    N, R = X[:n], X[n:]
    return np.array(
        [N[i]*(mu(i,R)-m[i]) for i in range(n)] +
        [D*(S[j]-R[j]) - np.sum([C[j,i]*mu(i,R)*N[i] for i in range(n)]) for j in range(k)]        
    )


def explicit(f,y0, insert_time=False):
    t = 0
    y = [np.zeros_like(y0)]
    added = [False for _ in range(n)]
    if not insert_time: insert_time = [0 for _ in range(n)]
    for _ in range(N):
        t += dt
        if not np.all(added):
            for k, T in enumerate(insert_time):
                # inserts species 4, 5 and 6 at t=1000, t=2000 and t=5000 respectively.
                if t >= T and not added[k]: 
                    y[-1][k] = 0.1 # specified in the paper, species added at a later time start at 0.1
                    added[k] = True
        y.append(f(t-dt,y[-1])*dt + y[-1])
    return y

def extract(iter, pos):
    return [iter[i][pos] for i in range(len(iter))]


# set up graphics settings
fig, AX = plt.subplots(1,2)
fig.set_figheight(4)
fig.set_figwidth(9)

# make colour wheel for pretty rainbow species :)
color = [hls_to_rgb(k, 0.5, 0.8) for k in np.linspace(0,1,n+1)]

exV = explicit(f,y, insert_time)
solt, solN, solR = [dt*i for i in range(N+1)], [extract(exV,i) for i in range(n)], [extract(exV,j) for j in range(n,n+k)]

for i, (soln, c) in enumerate(zip(solN, color)): 
    AX[0].plot(solt, soln, color=c, label="$N_{" + str(i+1) + "}(t)$")
    #ax.set_ylim([0,10])
    AX[0].legend(loc='best')
for j, solr in enumerate(solR): 
    AX[1].plot(solt, solr, label="$R_{" + str(j+1) + "}(t)$")
    #ax.set_ylim([0,10])
    AX[1].legend(loc='best')

# todo : show legend outside
# https://stackoverflow.com/a/4701285

plt.show()
