import numpy as np

pov = np.array([20, 10, 30])

a = pov[0]
b = pov[1]
c = pov[2]

p1 = np.array([1, 0, 0])
p2 = np.array([0, 0, 0])
p3 = np.array([0, 0, 1])

r0 = np.array([0, 0, 0])

x0 = r0[0]
y0 = r0[1]
z0 = r0[2]

normal_vector = np.cross(p1 - p2, p3 - p2)

nx = normal_vector[0]
ny = normal_vector[1]
nz = normal_vector[2]

d0 = x0*nx + y0*ny + z0*nz
d1 = a*nx + b*ny + c*nz
d = d0 - d1

perspective_matrix = np.array([
    [d+a*nx, a*ny, a*nz, -a*d0],
    [b*nx, d+b*ny, b*nz, -b*d0],
    [c*nx, c*ny, d+c*nz, -c*d0],
    [nx, ny, nz, 1]
])

res_h = 32
res_v = 24