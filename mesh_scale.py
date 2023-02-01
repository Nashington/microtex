import trimesh
import polyscope as ps
import os

os.chdir("P:\OneDrive\Cardiff University\OneDrive - Cardiff University\Year 3\EN3100 - Project\Testbed")

#ps.init()
#myobj = trimesh.load_mesh('Real.stl', enable_post_processing=True, solid=True)
#vertices = myobj.vertices
#faces = myobj.faces
# visualize!
#ps_mesh = ps.register_surface_mesh('Real.stl', vertices, faces)
#ps.show()

def show_model(filename):
    ps.init()
    myobj = trimesh.load_mesh(filename, enable_post_processing=True, solid=True) # Import Object fomr stl

    #tf = translation_matrix([1, 2, 3])

    #myobj = trimesh.base.Trimesh.apply_translation(myobj, (1000, 0, 20))
    #myobj.apply_translation((1000, 0, 0))
    myobj.apply_scale((2, 1, 1))

    #myobj = trimesh.transformations()
    vertices = myobj.vertices
    faces = myobj.faces
    # visualize!
    #multimesh = trimesh.Scene(myobj)
    #multimesh.show()
    #multimesh.add_geometry(myobj, geom_name='mesh2')
    #trimesh.viewer.windowed.Sceneviewer(multimesh)
    ps_mesh = ps.register_surface_mesh(filename, vertices, faces)
    ps.show()

show_model('Real.stl')