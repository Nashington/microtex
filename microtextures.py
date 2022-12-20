import cadquery as cq
from cadquery import exporters
from stl import mesh
import trimesh
import numpy as np
import polyscope as ps

########### Functions Definitions ############
# Add function to Rotate working plane with Angle to get different orientation of textures
# Add function to transform an STL into a cadquery model - so we can manipulate real scans
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
        model = model.workplane(centerOption="CenterOfMass").center(Diameter / 4 + AreaW / 2, 0).rect(Diameter / 2,                                                                                               Height + 1).cutThruAll()
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

def cutout_disc (model,Diameter) :
    model = model.cut(cq.Workplane("XY").rect(Diameter * 3, Diameter * 3).circle(Diameter / 2).extrude(2))
    model = model.cut(cq.Workplane("XY").rect(Diameter * 3, Diameter * 3).circle(Diameter / 2).extrude(-2))
    return model

def show_model(filename):
    ps.init()

    myobj = trimesh.load_mesh(filename, enable_post_processing=True, solid=True) # Import Object fomr stl
    vertices = myobj.vertices
    faces = myobj.faces
    # visualize!
    ps_mesh = ps.register_surface_mesh(filename, vertices, faces)
    ps.show()

def demo(Diameter,Height,EllipseW,EllipseH,gap): 
    model1 = create_disc(Diameter,Height,EllipseW,EllipseH,gap) # Create Disc
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

    # 1 add a function to import stl with real texture in a mesh object (smallest possible texture)

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
# Part Parameters
Diameter = 10
Height = 1
# Scallop Texture Parameters
EllipseH = 0.1
EllipseW = 0.15
gap = 0.1
Angle = 0

demo(Diameter,Height,EllipseW,EllipseH,gap)
