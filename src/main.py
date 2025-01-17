import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from definitions import pov, p1, p2, p3, r0
from obj import get_obj_data

print(pov)

print(p1)
print(p2)
print(p3)
print(r0)

get_obj_data('models/pyramid.obj')