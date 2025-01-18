import numpy as np
from elements import res_h, res_v

def to_homogenous(coords):
    return np.array([coords[0], coords[1], coords[2], 1])

def object_to_projection(object_matrix, perspective_matrix):
    projection_points = []
    
    for point in object_matrix:
        projected_point = np.dot(perspective_matrix, to_homogenous(point))
        x = projected_point[0] / projected_point[3]
        y = projected_point[1] / projected_point[3]
        projection_points.append(np.array([x, y]))
    
    return projection_points

def calculate_image_limits(projection_points):
    x_min = min([point[0] for point in projection_points])
    x_max = max([point[0] for point in projection_points])
    y_min = min([point[1] for point in projection_points])
    y_max = max([point[1] for point in projection_points])
    
    return x_min, x_max, y_min, y_max

def calculate_window_limits(projection_points):
    img_x_min, img_x_max, img_y_min, img_y_max = calculate_image_limits(projection_points)

    x_min = round(img_x_min - 0.2 * abs(img_x_max - img_x_min))
    x_max = round(img_x_max + 0.2 * abs(img_x_max - img_x_min))
    y_min = round(img_y_min - 0.2 * abs(img_y_max - img_y_min))
    y_max = round(img_y_max + 0.2 * abs(img_y_max - img_y_min))
    
    return x_min, x_max, y_min, y_max