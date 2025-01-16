import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from definitions import projection_center, p1, p2, p3
from obj import get_obj_data

print(projection_center)

print(p1)
print(p2)
print(p3)

get_obj_data('models/cube.obj')