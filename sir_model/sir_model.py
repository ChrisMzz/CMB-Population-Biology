from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt
from colorsys import hls_to_rgb


class SIRConfig:
    """SIR model config metadata. Includes final computation time `T`, number of data points `N`.
    Time delta `dt` is computed from these."""
    def __init__(self, T:int, N:int):
        self.T = T
        self.N = N
        self.dt = T/(N+1)

class SIR:
    """SIR model implementation. Initialise with `beta`, `gamma`, `y0` and `config`, where `y0` is an array `(s0,i0,r0)`."""
    def __init__(self, beta:float, gamma:float, y0:np.ndarray, config:SIRConfig):
        self.beta = beta
        self.gamma = gamma
        self.config = config if config is not None else SIRConfig(T=10, N=300)
        self.dt = self.config.dt
        self.y0 = y0
        assert np.all(y0 >= 0)
        assert (beta >= 0) and (gamma >= 0)
        assert (self.dt > 0)

    def f(self, X):
        """System of equations."""
        S, I, R = X
        return np.array([
            -self.beta*S*I,
            self.beta*S*I - self.gamma*I,
            self.gamma*I
        ])

    def solve(self):
        """Solve using Euler explicit method. Equations are assumed to be time-independent."""
        y = [self.y0]
        for t in np.linspace(self.dt,self.config.T, self.config.N): y.append(self.f(y[-1])*self.dt + y[-1])
        return y

    @classmethod
    def extract(self, iter, pos):
        return [iter[i][pos] for i in range(len(iter))]

    def display(self, ax, *, showRinfty=False):
        if ax is None: fig, ax = plt.subplots()
        color = [hls_to_rgb(k, 0.5, 0.8) for k in np.linspace(0.25,0.7,3)]
        names = ["$S(t)$","$I(t)$","$R(t)$"]
        exV = self.solve()
        solt, sol = [self.dt*i for i in range(self.config.N+1)], [self.extract(exV,i) for i in range(3)]
        for i, (soln, c, name) in enumerate(zip(sol, color, names)): 
            ax.plot(solt, soln, color=c, label=name)
        if showRinfty:
            R0 = self.beta/self.gamma
            ri = np.linspace(0,1,100)
            Rinfty = ri[np.argmin(np.abs(ri - 1 + self.y0[0]*np.exp(-R0*ri)))]
            ax.plot(solt, Rinfty*np.ones_like(solt), color=color[-1], linestyle="--", label=r"$R_{\infty}$ estimate")
        ax.legend(loc='best')
        ax.set_ylim([0,1])
        ax.set_title("SIR model computation")

    def show_SvI(self, ax):
        if ax is None: fig, ax = plt.subplots()
        exV = self.solve()
        S = np.array(self.extract(exV,0))
        R0 = self.beta/self.gamma

        ax.plot(S, -S+np.log(S)/R0 + self.y0[0] + self.y0[1], label="$I(S)$")
        ax.plot(1/R0, -1/R0+np.log(1/R0)/R0 + self.y0[0] + self.y0[1], 'o', color=(1,0.4,0), label=r"$I(R_0^{-1})$")
        ax.plot(np.ones_like(S)/R0, -S+np.log(S)/R0 + self.y0[0] + self.y0[1], '--', color=(1,0.4,0))
        ax.set_title("Plot of $I(S)$")
        ax.set_xlim([0,1])
        ax.set_xlabel("$S$"), ax.set_ylabel("$I$")
        ax.legend()

