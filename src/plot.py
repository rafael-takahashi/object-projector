import matplotlib.pyplot as plt

def plot_projection(viewport_points, faces):
    x_coords = [point[0] for point in viewport_points]
    y_coords = [point[1] for point in viewport_points]

    plt.scatter(x_coords, y_coords, color='blue')

    for face in faces:
        face_x = [x_coords[i] for i in face] + [x_coords[face[0]]]
        face_y = [y_coords[i] for i in face] + [y_coords[face[0]]]
        plt.plot(face_x, face_y, color='red', linestyle='-')

    for i, point in enumerate(viewport_points):
        plt.text(point[0], point[1], f'P{i+1}', fontsize=12, ha='right')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Object Projection')

    plt.grid(True)
    plt.axis('equal')
    plt.show()