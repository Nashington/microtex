import cadquery as cq
from cadquery import exporters
from stl import mesh
import trimesh
import numpy as np
import polyscope as ps
import os
from cqmore import Workplane

########### Class Definitions ###########
# Define a class per texture shape to make future texture creations easier
# Draw a diagram to define variables (plot with cadquery as well?)
# Python classes are capitalised

diameter = 10
height = 1
angle = 0
area_w = 5

class CQModel:
    def __init__(self) -> None:
        self.diameter = diameter
        self.height = height
        self.angle = angle
        self.area_w = area_w

    # Creates an untextured plain disc, then moves workplane to prepare for texture cut
    def create_plain_disc(self):
        disc = cq.Workplane("front").circle(self.diameter / 2).extrude(self.height)
        disc = disc.workplane().transformed(offset=cq.Vector(0, 0, self.height / 2), rotate=cq.Vector(90, 0, 0))
        return disc

    # Rotates model around center axis
    def rotate_model(self):
        model = model.rotateAboutCenter((0,0,1), self.angle)
        return model

    # Creates an untextured plain square


    # visualize!
    def show_model(self, filename):
        ps.init()
        myobj = trimesh.load_mesh(filename, enable_post_processing=True, solid=True) # Import Object fomr stl
        vertices = myobj.vertices
        faces = myobj.faces
        # visualize!
        ps_mesh = ps.register_surface_mesh(filename, vertices, faces)
        ps.show()

    # Saves as STL
    # https://stackoverflow.com/questions/12560600/creating-a-new-file-filename-contains-loop-variable-python
    def export_STL(self, model, i, toggle_show):
        exporters.export(model, "model" + str(i) + ".stl")  # Save stl file
        # insert conditional statement, or modify .show_model, so we don't have to display every model
        CQModel().show_model("model" + str(i) + ".stl")

class Scallop(CQModel):
    def __init__(self, depth, width, gap) -> None:
        super().__init__()
        self.depth = depth
        self.width = width
        self.gap = gap

    # Cuts scallop texture into plain model
    def texture_disc(self):
        disc = CQModel.create_plain_disc(self)
        disc = disc.center(-self.diameter / 2 + self.width +self.gap, 0).ellipse(self.width, self.depth).cutThruAll()
        total = 2 * self.width + self.gap
        while total < self.diameter:
            total += 2 * self.width + self.gap
            disc = disc.center(2 * self.width + self.gap, 0).ellipse(self.width, self.depth).cutThruAll()
        return disc

########### Main Program Start ############
def main ():
    # change working directory
    os.chdir("P:\OneDrive\Cardiff University\OneDrive - Cardiff University\Year 3\EN3100 - Project\Testbed")

    # https://stackoverflow.com/questions/16552508/python-loops-for-simultaneous-operation-two-or-possibly-more
    # to enable customisable ranges in geometry
    for i, gap in zip(range(30,35), np.linspace(0.1, 0.5, 5)):
        model = Scallop(0.1, 0.15, gap).texture_disc()
        CQModel().export_STL(model, i)

if __name__=='__main__':
    main()


########### Functions Definitions ############
# Add function to Rotate working plane with Angle to get different orientation of textures - Done: function rotate_model
# Add function to transform an STL into a cadquery model - so we can manipulate real scans - Identified a library that allows this: cqmore
def create_plain_disc(Diameter, Height, EllipseW, EllipseH, gap):
    Disc = cq.Workplane("front").circle(Diameter / 2).extrude(Height)
    return Disc

def create_disc(Diameter, Height, EllipseW, EllipseH, gap):
    Disc = cq.Workplane("front").circle(Diameter / 2).extrude(Height)
    # Change Extrusion Working Plane
    Disc = Disc.workplane().transformed(offset=cq.Vector(0, 0, Height / 2), rotate=cq.Vector(90, 0, 0))
    # Create Scallops
    Disc = Disc.center(-Diameter / 2 + EllipseW + gap, 0).ellipse(EllipseW, EllipseH).cutThruAll()
    total = 2 * EllipseW + gap
    while total < Diameter:
        total += 2 * EllipseW + gap
        Disc = Disc.center(2 * EllipseW + gap, 0).ellipse(EllipseW, EllipseH).cutThruAll()
    return Disc

def reduce_area(model,Diameter,Height,AreaW) :
    if AreaW < Diameter and AreaW != 0:
        model = model.workplane(centerOption="CenterOfMass").center(Diameter / 4 + AreaW / 2, 0).rect(Diameter / 2, Height + 1).cutThruAll()
        model = model.center(-Diameter / 2 - AreaW, 0).rect(Diameter / 2, Height + 1).cutThruAll()
    return model

def create_square(Diameter, Height, EllipseW, EllipseH, gap):
    # Square version
    Square = cq.Workplane("XY").box(Diameter, Diameter, Height).faces(">Y").workplane()

    Square = Square.center(-Diameter / 2 + EllipseW + gap, 0.5).ellipse(EllipseW, EllipseH).cutThruAll()
    total = 2 * EllipseW + gap
    while total < Diameter:
        total += 2 * EllipseW + gap
        Square = Square.center(2 * EllipseW + gap, 0).ellipse(EllipseW, EllipseH).cutThruAll()
    return Square

def cutout_disc(model,Diameter) :
    model = model.cut(cq.Workplane("XY").rect(Diameter * 3, Diameter * 3).circle(Diameter / 2).extrude(2))
    model = model.cut(cq.Workplane("XY").rect(Diameter * 3, Diameter * 3).circle(Diameter / 2).extrude(-2))
    return model

# plot in polyscope
def show_model(filename):
    ps.init()
    myobj = trimesh.load_mesh(filename, enable_post_processing=True, solid=True) # Import Object fomr stl
    vertices = myobj.vertices
    faces = myobj.faces
    # visualize!
    ps_mesh = ps.register_surface_mesh(filename, vertices, faces)
    ps.show()

# function to rotate model around center axis
def rotate_model(model, Angle):
    # rotate the working plane to get a different orientation
    model = model.rotateAboutCenter((0,0,1), Angle)
    return model

# function to import STL to cadquery 
# numpy-stl 2.16 or later is required
# uses cqmore
def import_stl(filename):
    vectors = mesh.Mesh.from_file(filename).vectors
    points = tuple(map(tuple, vectors.reshape((vectors.shape[0] * vectors.shape[1], 3))))
    faces = [(i, i + 1, i + 2) for i in range(0, len(points), 3)]
    model_import = Workplane().polyhedron(points, faces)
    exporters.export(model_import, 'model_import.stl')
    show_model('model_import.stl')

# import step to cadquery
def import_step(filename):
    import_model = cq.importers.importStep('filename')
    #how_model(import_model)

def demo(Diameter,Height,EllipseW,EllipseH,gap,Angle): 
    model1 = create_disc(Diameter,Height,EllipseW,EllipseH,gap) # Create Disc
    #model1 = rotate_model(model1, 30)
    exporters.export(model1, 'Disc1.stl')  # Save stl file
    show_model('Disc1.stl')

    AreaW = 5  # Area to be simulated to reduce computation
    model2 = reduce_area(model1,Diameter,Height,AreaW) # Reduce Area by removing solid each side
    exporters.export(model2, 'Disc2.stl') # Save stl file
    show_model('Disc2.stl')

    # This Square1.stl is mimicking what we would get from a surface constructed with real scan
    model3 = create_square(Diameter,Height,EllipseW,EllipseH,gap) # Create Square
    exporters.export(model3, 'Square1.stl') # Save stl file
    show_model('Square1.stl')

    # 1 add a function to import stl with real texture in a mesh object (smallest possible texture) - Refer to previous STL import functions

    # 2 ad a scaling function to scale up the real texture to test various width and heights

    # 3 transfer mesh object into a cadquery object

    # We now cut out the disc out (this is useful to cutout different scale)
    model4 = cutout_disc (model3,Diameter)
    exporters.export(model4, 'Square2.stl') # Save stl file
    show_model('Square2.stl')

    AreaW = 3  # Area to be simulated to reduce computation
    model4 = reduce_area(model4,Diameter,Height,AreaW) # Reduce Area by removing solid each side
    exporters.export(model4, 'Square3.stl') # Save stl file
    show_model('Square3.stl')
########### Main Program Start ############
#def main():
    # change working directory
    #os.chdir("P:\OneDrive\Cardiff University\OneDrive - Cardiff University\Year 3\EN3100 - Project\Testbed")
    
    #demo(Diameter,Height,EllipseW,EllipseH,gap,Angle)
    #show_model('scallop  - Filled-in non-measured points(1).stl')
    #import_step('scallopSTEP.step')
    #import_stl('Real.stl')
    #show_model('Real.stl')
    # result = cq.importers.importStep('scallop STEP.step')

#if __name__=='__main__':
    #main()