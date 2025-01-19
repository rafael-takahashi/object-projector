import numpy as np

from geometry import to_homogenous

def object_to_projection(object_matrix, perspective_matrix):
    projection_points = []
    
    for point in object_matrix:
        projected_point = np.dot(perspective_matrix, to_homogenous(point))
        x = projected_point[0] / projected_point[3]
        y = -(projected_point[1] / projected_point[3])
        projection_points.append(np.array([x, y]))
    
    return projection_points