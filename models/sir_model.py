import numpy as np
from scipy.integrate import solve_ivp

def solve_sir(N, I0, R0, b, k, t_max):
    S0 = N - I0 - R0
    def deriv(t, y):
        S, I, R = y
        dSdt = -b * S * I
        dIdt = b * S * I - k * I
        dRdt = k * I
        return [dSdt, dIdt, dRdt]
    
    sol = solve_ivp(deriv, [0, t_max], [S0, I0, R0], t_eval=np.linspace(0, t_max, 300))
    return sol.y[0], sol.y[1], sol.y[2], sol.t