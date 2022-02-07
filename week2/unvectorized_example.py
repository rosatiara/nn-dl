import numpy as np
import math as math

n = 100
u = np.zeros((n, 1))
v = np.zeros((n, 1))
for i in range(n):
    u[i] = math.exp(v[i])
