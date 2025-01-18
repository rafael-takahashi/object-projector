import numpy as np
from elements import res_h, res_v

u_max = res_h
u_min = 0
v_max = res_v
v_min = 0

def to_homogenous(coords):
    return np.append(coords, 1)

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

def calculate_scaling(x_min, x_max, y_min, y_max):
    sx = round(u_max / (x_max - x_min)) 
    sy = round(v_max / (y_max - y_min))
    
    return sx, sy

def calculate_ratio(x_min, x_max, y_min, y_max):
    return (x_max - x_min) / (y_max - y_min)

def window_to_viewport(projection_points):
    x_min, x_max, y_min, y_max = calculate_window_limits(projection_points)
    sx, sy = calculate_scaling(x_min, x_max, y_min, y_max)

    rw = calculate_ratio(x_min, x_max, y_min, y_max)
    rv = calculate_ratio(0, res_h, 0, res_v)

    if rw > rv:
        new_v_max = (u_max - u_min) / rw + v_min

        window_to_viewport_matrix = np.array([
            [sx, 0, u_min - sx*x_min],
            [0, -sy, sy*y_max + v_max/2 - new_v_max/2 + v_min],
            [0, 0, 1]
        ])

    else:
        new_u_max = (v_max - v_min) * rw + u_min

        window_to_viewport_matrix = np.array([
            [sx, 0, -sx*x_min + u_max/2 - new_u_max/2 + u_min],
            [0, -sy, sy*y_max + v_min],
            [0, 0, 1]
        ])

    print(window_to_viewport_matrix)

    viewport_points = []

    for point in projection_points:
        viewport_point = np.dot(window_to_viewport_matrix, to_homogenous(point))
        viewport_points.append(np.array([round(viewport_point[0]), round(viewport_point[1])]))

    return viewport_points