import trimesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Function to read an OBJ file and plot it
def plot_3d_obj(file_path):
    # Load the .obj file using trimesh
    mesh = trimesh.load_mesh(file_path)

    # Get vertices and faces
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
    ax.set_title('3D OBJ Plot')

    plt.show()

# Replace with your .obj file path
plot_3d_obj('models/cube.obj')  # Adjust the file path as needed
