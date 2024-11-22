import numpy as np

class PlanktonPreset:
    N : int
    dt : float

    n : int # number of species
    k : int # number of resources

    D : float # constant turnover rate

    r : list[float] # specific growth rate of each species
    m : list[float] # specific mortality rate of each species
    S : list[float] # supply concentration of each resource
    K : np.ndarray # weights of each species for each resource
    C : np.ndarray # content of resources in each species
    
    # initial conditions
    y : np.ndarray # for the general case

    insert_time : list[float]

    def set_params(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


# Setup for Figure 1c
Fig_1c = PlanktonPreset()
Fig_1c.set_params(
    N = int(15e4),
    dt = 1e-1,
    n = 6,
    k = 3,
    D = 1/4,
    S = [6, 10, 14]
)
Fig_1c.set_params(    
    r = [1 for _ in range(Fig_1c.n)],
    m = [Fig_1c.D for _ in range(Fig_1c.n)],
    K = np.array([
        [1, 0.9, 0.3, 1.04, 0.34, 0.77],
        [0.3, 1, 0.9, 0.71, 1.02, 0.76],
        [0.9, 0.3, 1, 0.46, 0.34, 1.07]
    ]),
    C = np.array([
        [0.04, 0.07, 0.04, 0.1, 0.03, 0.02],
        [0.08, 0.08, 0.1, 0.1, 0.05, 0.17],
        [0.14, 0.1, 0.1, 0.16, 0.06, 0.14]
    ]),
    y = np.array([0.1+i/100 for i in range(1,Fig_1c.n+1)]+Fig_1c.S),
    insert_time = [0,0,0, 1000, 2000, 5000]
)


# Setup for Figure 1d
Fig_1d = PlanktonPreset()
Fig_1d.set_params(
    N = int(3e4),
    dt = 1e-1,
    n = 9,
    k = 3,
    D = 1/4,
    S = [10, 10, 10]
)
Fig_1d.set_params(    
    r = [1 for _ in range(Fig_1d.n)],
    m = [Fig_1d.D for _ in range(Fig_1d.n)],
    K = np.array([
        [1, 0.75, 0.25, 0.7, 0.2, 0.65, 0.68, 0.38, 0.46],
        [0.25, 1, 0.75, 0.2, 1.01, 0.55, 0.83, 1.1, 0.85],
        [0.75, 0.25, 1, 1.1, 0.7, 0.95, 0.6, 0.5, 0.77]
    ]),
    C = np.array([
        [0.1, 0.2, 0.15, 0.05, 0.01, 0.4, 0.3, 0.2, 0.25],
        [0.15, 0.1, 0.2, 0.15, 0.3, 0.35, 0.25, 0.02, 0.35],
        [0.2, 0.15, 0.1, 0.25, 0.05, 0.2, 0.4, 0.15, 0.1]
    ]),
    y = np.array([0.1+i/100 for i in range(1,Fig_1d.n+1)]+Fig_1d.S),
    insert_time = [0,0,0, 250, 500, 750, 1000, 1250, 1500]
)

# Setup for Figure 4
Fig_4 = PlanktonPreset()
Fig_4.set_params(
    N = int(50e4),
    dt = 2e-2, # needs to be lower to avoid division by 0 because of bad discretization
    n = 12,
    k = 5,
    D = 1/4,
    S = [6, 10, 14, 4, 9]
)
Fig_4.set_params(    
    r = [1 for _ in range(Fig_4.n)],
    m = [Fig_4.D for _ in range(Fig_4.n)],
    K = np.array([
        [0.39, 0.34, 0.30, 0.24, 0.23, 0.41, 0.20, 0.45, 0.14, 0.15, 0.38, 0.28],
        [0.22, 0.39, 0.34, 0.30, 0.27, 0.16, 0.15, 0.05, 0.38, 0.29, 0.37, 0.31],
        [0.27, 0.22, 0.39, 0.34, 0.30, 0.07, 0.11, 0.05, 0.38, 0.41, 0.24, 0.25],
        [0.30, 0.24, 0.22, 0.39, 0.34, 0.28, 0.12, 0.13, 0.27, 0.33, 0.04, 0.41],
        [0.34, 0.30, 0.22, 0.20, 0.39, 0.40, 0.50, 0.26, 0.12, 0.29, 0.09, 0.16]
    ]),
    C = np.array([
        [0.04, 0.04, 0.07, 0.04, 0.04, 0.22, 0.10, 0.08, 0.02, 0.17, 0.25, 0.03],
        [0.08, 0.08, 0.08, 0.10, 0.08, 0.14, 0.22, 0.04, 0.18, 0.06, 0.20, 0.04],
        [0.10, 0.10, 0.10, 0.10, 0.14, 0.22, 0.24, 0.12, 0.03, 0.24, 0.17, 0.01],
        [0.05, 0.03, 0.03, 0.03, 0.03, 0.09, 0.07, 0.06, 0.03, 0.03, 0.11, 0.05],
        [0.07, 0.09, 0.07, 0.07, 0.07, 0.05, 0.24, 0.05, 0.08, 0.10, 0.02, 0.04]
    ]),
    y = np.array([0.1+i/100 for i in range(1,Fig_4.n+1)]+Fig_4.S),
    insert_time = [0]*5+[1000]*3+[3000]*2+[5000]*2
)


