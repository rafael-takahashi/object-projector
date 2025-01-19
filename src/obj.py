import trimesh

class Model:
    def __init__(self, object_matrix, faces):
        self.object_matrix = object_matrix 
        self.faces = faces
        self.vertex_quantity = len(object_matrix)
        self.face_quantity = len(faces)
        self.vertices_per_face = len(faces[0])

def get_obj_data(file_path: str) -> Model:
    mesh = trimesh.load_mesh(file_path)

    object_matrix = mesh.vertices
    faces = mesh.faces

    return Model(object_matrix, faces)

def print_obj_data(obj: Model):
    print(f"Object Matrix:\n{obj.object_matrix}\n")
    print(f"Faces:\n{obj.faces}\n")
    print(f"Vertex Quantity: {obj.vertex_quantity}")
    print(f"Face Quantity: {obj.face_quantity}")
    print(f"Vertices per Face: {obj.vertices_per_face}\n")