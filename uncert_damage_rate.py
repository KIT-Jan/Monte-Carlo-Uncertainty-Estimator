import numpy as np
from matplotlib import pyplot as plt

sigma_ni_weight = 0.025
sigma_activity = 0.1
sigma_fluence = np.sqrt(0.025**2+0.1**2) # = 0.103

T_range = 1 # stable measurement range +- 1

def estimate_error(T, fluence):
    k = 8.617333262e-5 #eV/K
    T += 273.15
    T_dist = np.random.uniform(T-T_range, T+T_range, 100_000_000)
    plt.hist(T_dist)
    plt.show()
    fluence_dist = np.random.normal(fluence, sigma_fluence*fluence, 100_000_000)
    plt.hist(fluence_dist)
    plt.show()
    scaling_dist = T_dist**2 * np.exp(-1.21/(2*k*T_dist)) * fluence_dist
    plt.hist(scaling_dist)
    plt.show()
    mean = np.mean(scaling_dist)
    std = np.std(scaling_dist)
    return std/mean

print(estimate_error(20, 1e14))
#outcome: 11.52%