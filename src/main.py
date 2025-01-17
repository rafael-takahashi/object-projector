import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from elements import pov, p1, p2, p3, r0, normal_vector, res_h, res_v
from obj import Model, get_obj_data

print(f"Point of View: {pov}")

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Point 3: {p3}")

print(f"Plane Point: {r0}")

obj = get_obj_data('models/pyramid.obj')

print(f"Object Matrix: {obj.object_matrix}")
print(f"Faces: {obj.faces}")
print(f"Vertex Quantity: {obj.vertex_quantity}")
print(f"Face Quantity: {obj.face_quantity}")
print(f"Vertices per Face: {obj.vertices_per_face}")

print(f"Normal Vector: {normal_vector}")