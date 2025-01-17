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