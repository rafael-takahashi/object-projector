import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from geometry import perspective_matrix
from obj import get_obj_data
from plot import plot_projection
from projection import object_to_projection
from window_viewport import window_to_viewport

obj_name = input("Type your object name (e.g. cube.obj): ")
file_path = os.path.join("models", obj_name)

if not os.path.isfile(file_path):
    print(f"{obj_name} does not exist in the models folder.")
    exit()

obj = get_obj_data(file_path)

print(f"Object Matrix:\n{obj.object_matrix}")
print(f"Faces:\n{obj.faces}")
print(f"Vertex Quantity: {obj.vertex_quantity}")
print(f"Face Quantity: {obj.face_quantity}")
print(f"Vertices per Face: {obj.vertices_per_face}")

print(f"Perspective Matrix:\n{perspective_matrix}")

projection_points = object_to_projection(obj.object_matrix, perspective_matrix)
print(f"Projection Points:")
for point in projection_points:
    print(f"({point[0]}, {point[1]})", end=" ")

viewport_points = window_to_viewport(projection_points)
print(f"\nViewport Points:")
for point in viewport_points:
    print(f"({point[0]}, {point[1]})", end=" ")

plot_projection(viewport_points, obj.faces)