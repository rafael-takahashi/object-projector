import numpy as np

from geometry import to_homogenous

u_max = 32
u_min = 0
v_max = 24
v_min = 0

def calculate_image_limits(projection_points):
    img_x_min = min([point[0] for point in projection_points])
    img_x_max = max([point[0] for point in projection_points])
    img_y_min = min([point[1] for point in projection_points])
    img_y_max = max([point[1] for point in projection_points])
    
    return img_x_min, img_x_max, img_y_min, img_y_max

def calculate_window_limits(projection_points):
    img_x_min, img_x_max, img_y_min, img_y_max = calculate_image_limits(projection_points)

    window_x_min = round(img_x_min - 0.2 * abs(img_x_max - img_x_min))
    window_x_max = round(img_x_max + 0.2 * abs(img_x_max - img_x_min))
    window_y_min = round(img_y_min - 0.2 * abs(img_y_max - img_y_min))
    window_y_max = round(img_y_max + 0.2 * abs(img_y_max - img_y_min))
    
    return window_x_min, window_x_max, window_y_min, window_y_max

def calculate_scaling(x_min, x_max, y_min, y_max):
    if x_max - x_min == 0:
        sx = float('inf')
    else:
        sx = round((u_max - u_min) / (x_max - x_min)) 
    if y_max - y_min == 0:
        sy = float('inf')
    else:
        sy = round((v_max - v_min) / (y_max - y_min))
    
    return sx, sy

def calculate_ratio(x_min, x_max, y_min, y_max):
    return (x_max - x_min) / (y_max - y_min)

def window_to_viewport(projection_points):
    x_min, x_max, y_min, y_max = calculate_window_limits(projection_points)
    sx, sy = calculate_scaling(x_min, x_max, y_min, y_max)
    rw = calculate_ratio(x_min, x_max, y_min, y_max)
    rv = calculate_ratio(0, u_max, 0, v_max)

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

    viewport_points = []

    for point in projection_points:
        viewport_point = np.dot(window_to_viewport_matrix, to_homogenous(point))
        viewport_points.append(np.array([viewport_point[0], viewport_point[1]]))

    return viewport_points