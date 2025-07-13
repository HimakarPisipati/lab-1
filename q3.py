import numpy as np
A = np.array([
    [1, 2],
    [3, 4]])
m = 2
res = np.linalg.matrix_power(A, m)
print(f"A^{m} is:{res}")
