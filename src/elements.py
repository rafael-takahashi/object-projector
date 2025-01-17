import numpy as np

pov = np.array([20, 10, 30])

p1 = np.array([1, 0, 0])
p2 = np.array([0, 0, 0])
p3 = np.array([0, 0, 1])

r0 = np.array([0, 0, 0])

normal_vector = np.cross(p1 - p2, p3 - p2)

res_h = 32
res_v = 24