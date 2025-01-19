import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from geometry import perspective_matrix
from obj import get_obj_data, print_obj_data
from plot import plot_projection
from projection import object_to_projection
from window_viewport import window_to_viewport
from get_parameteres import get_parameters

file_path = get_parameters()

obj = get_obj_data(file_path)

print_obj_data(obj)

print(f"Perspective Matrix:\n{perspective_matrix}")
print("")

projection_points = object_to_projection(obj.object_matrix, perspective_matrix)
print(f"Projection Points:")
for point in projection_points:
    print(f"({point[0]}, {point[1]})", end=" ")
print("")

viewport_points = window_to_viewport(projection_points)
print(f"\nViewport Points:")
for point in viewport_points:
    print(f"({point[0]}, {point[1]})", end=" ")
print("")

plot_projection(viewport_points, obj.faces)