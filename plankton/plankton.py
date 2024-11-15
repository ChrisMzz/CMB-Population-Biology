import numpy as np
import matplotlib.pyplot as plt
from colorsys import hls_to_rgb

N = int(15e4)
dt = (15e3)/N

n = 6 # number of species
k = 3 # number of resources

D = 1/4 # constant turnover rate

Fig_1c = True

r = [1 for _ in range(n)] # specific growth rate of each species
m = [D for _ in range(n)] # specific mortality rate of each species
S = [6, 10, 14] # supply concentration of each resource
K = np.array([ # weights of each species for each resource
    [1, 0.9, 0.3, 1.04, 0.34, 0.77],
    [0.3, 1, 0.9, 0.71, 1.02, 0.76],
    [0.9, 0.3, 1, 0.46, 0.34, 1.07]
])
C = np.array([ # content of resources in each species
    [0.04, 0.07, 0.04, 0.1, 0.03, 0.02],
    [0.08, 0.08, 0.1, 0.1, 0.05, 0.17],
    [0.14, 0.1, 0.1, 0.16, 0.06, 0.14]
])



# initial conditions
y = [np.array([0.1+i/100 for i in range(1,n+1)]+S)] # for the general case

if Fig_1c:
    y = [np.array([0.11, 0.12, 0.13, 0, 0, 0]+S)] # for Fig 1c


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


def explicit(f,y):
    t = 0
    third_added, fourth_added, fifth_added = False, False, False
    for _ in range(N):
        t += dt

        if Fig_1c: # inserts species 4, 5 and 6 at t=1000, t=2000 and t=5000 respectively.
            if t >= 1000 and not third_added: 
                y[-1][3] = 3/100
                third_added = True
            if t >= 2000 and not fourth_added: 
                y[-1][4] = 4/100
                fourth_added = True
            if t >= 5000 and not fifth_added: 
                y[-1][5] = 5/100
                fifth_added = True
        
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

exV = explicit(f,y)
solt, solN, solR = [dt*i for i in range(N+1)], [extract(exV,i) for i in range(n)], [extract(exV,j) for j in range(n,n+k)]

for i, (soln, c) in enumerate(zip(solN, color)): 
    AX[0].plot(solt, soln, color=c, label="$N_{" + str(i+1) + "}(t)$")
    #ax.set_ylim([0,10])
    AX[0].legend(loc='best')
for j, solr in enumerate(solR): 
    AX[1].plot(solt, solr, label="$R_{" + str(j+1) + "}(t)$")
    #ax.set_ylim([0,10])
    AX[1].legend(loc='best')


plt.show()
