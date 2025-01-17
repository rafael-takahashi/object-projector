import trimesh

def get_obj_data(file_path):
    # Load the .obj file using trimesh
    mesh = trimesh.load_mesh(file_path)

    mesh.show()

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