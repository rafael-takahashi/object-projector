import trimesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def get_obj_data(file_path):
    # Load the .obj file using trimesh
    mesh = trimesh.load_mesh(file_path)

    # Get object data
    vertices = mesh.vertices
    vertice_quantity = len(vertices)
    faces = mesh.faces
    face_quantity = len(faces)
    vertices_per_faces = [len(face) for face in faces]
    face_vertices = [vertice for vertice in faces]

    print(f"NV: {vertice_quantity}")
    print("========================================")
    print(f"X[i], Y[i], Z[i]: \n {vertices}")
    print("========================================")
    #print(f" {faces}")
    #print("========================================")
    print(f"NS: {face_quantity}")
    print("========================================")
    print(f"NVPS[i]: {vertices_per_faces}")
    print("========================================")
    for i in range(face_quantity):
        print(f"VS[{i}]: {face_vertices[i]}")

get_obj_data('models/cube.obj')

projection_center = [1, -1, 1]

p1 = [1, 0, 0]
p2 = [0, 1, 0]
p3 = [0, 0, 1]

def plot_3d_obj(file_path):
    # Load the .obj file using trimesh
    mesh = trimesh.load_mesh(file_path)

    # Get object data
    vertices = mesh.vertices
    faces = mesh.faces

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create the 3D mesh using the faces and vertices
    mesh_faces = []
    for face in faces:
        mesh_faces.append([vertices[vertex] for vertex in face])

    # Plot the object
    ax.add_collection3d(Poly3DCollection(mesh_faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
    
    # Set plot limits
    ax.set_xlim([vertices[:, 0].min(), vertices[:, 0].max()])
    ax.set_ylim([vertices[:, 1].min(), vertices[:, 1].max()])
    ax.set_zlim([vertices[:, 2].min(), vertices[:, 2].max()])

    # Labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('.obj Plot')

    #plt.show()