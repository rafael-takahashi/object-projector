import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

from elements import pov, p1, p2, p3, r0, normal_vector, res_h, res_v, d, perspective_matrix
from obj import Model, get_obj_data
from plot import plot_projection
from transformations import object_to_projection, calculate_window_limits, calculate_scaling, window_to_viewport

print(f"Point of View: {pov}")

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Point 3: {p3}")

print(f"Plane Point: {r0}")

obj = get_obj_data('models/cube.obj')

print(f"Object Matrix: {obj.object_matrix}")
print(f"Faces: {obj.faces}")
print(f"Vertex Quantity: {obj.vertex_quantity}")
print(f"Face Quantity: {obj.face_quantity}")
print(f"Vertices per Face: {obj.vertices_per_face}")

print(f"Normal Vector: {normal_vector}")

print(f"Distance: {d}")

print(f"Perspective Matrix: {perspective_matrix}")

projection_points = object_to_projection(obj.object_matrix, perspective_matrix)

print(f"Projection Points: {projection_points}")

x_min, x_max, y_min, y_max = calculate_window_limits(projection_points)

print(f"Image Limits: {x_min}, {x_max}, {y_min}, {y_max}")

sx, sy = calculate_scaling(x_min, x_max, y_min, y_max)

print(f"Scaling: {sx}, {sy}")

viewport_points = window_to_viewport(projection_points)

plot_projection(viewport_points, obj.faces)