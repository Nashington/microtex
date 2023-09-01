# Python Script, API Version = V23

# Open File
DocumentOpen.Execute(r"D:\Work\Summer Placement Testbed\model40.step")
# EndBlock



# Set Sketch Plane
sectionPlane = Plane.PlaneXY
result = ViewHelper.SetSketchPlane(sectionPlane, None)
# EndBlock

# Sketch Rectangle
point1 = Point2D.Create(MM(-1.00084070880403),MM(-6))
point2 = Point2D.Create(MM(1),MM(-6))
point3 = Point2D.Create(MM(1),MM(6))
result = SketchRectangle.Create(point1, point2, point3)
# EndBlock


# Change Object Visibility
selection = BodySelection.Create(GetRootPart().Bodies[0])
visibility = VisibilityType.Hide
inSelectedView = False
faceLevel = False
ViewHelper.SetObjectVisibility(selection, visibility, inSelectedView, faceLevel)
# EndBlock

# Solidify Sketch
mode = InteractionMode.Solid
result = ViewHelper.SetViewMode(mode, None)
# EndBlock

# Extrude 1 Face
selection = FaceSelection.Create(GetRootPart().Bodies[1].Faces[0])
options = ExtrudeFaceOptions()
options.ExtrudeType = ExtrudeType.Add
result = ExtrudeFaces.Execute(selection, MM(2.5), options)
# EndBlock

# Change Object Visibility
selection = BodySelection.Create(GetRootPart().Bodies[0])
visibility = VisibilityType.Show
inSelectedView = False
faceLevel = False
ViewHelper.SetObjectVisibility(selection, visibility, inSelectedView, faceLevel)
# EndBlock

# Intersect Bodies
targets = BodySelection.Create(GetRootPart().Bodies[1])
tools = BodySelection.Create(GetRootPart().Bodies[0])
options = MakeSolidsOptions()
result = Combine.Intersect(targets, tools, options)
# EndBlock

# Delete Objects
selection = BodySelection.Create(GetRootPart().Bodies[2])
result = Combine.RemoveRegions(selection)
# EndBlock

# Delete Objects
selection = BodySelection.Create(GetRootPart().Bodies[0])
result = Delete.Execute(selection)
# EndBlock

# Create Named Selection Group
primarySelection = FaceSelection.Create(GetRootPart().Bodies[0].Faces[1])
secondarySelection = Selection.Empty()
result = NamedSelection.Create(primarySelection, secondarySelection)
# EndBlock

# Rename Named Selection
result = NamedSelection.Rename("Group1", "Input")
# EndBlock

# Create Named Selection Group
primarySelection = FaceSelection.Create(GetRootPart().Bodies[0].Faces[0])
secondarySelection = Selection.Empty()
result = NamedSelection.Create(primarySelection, secondarySelection)
# EndBlock

# Rename Named Selection
result = NamedSelection.Rename("Group1", "Output")
# EndBlock

# Create Named Selection Group
primarySelection = FaceSelection.Create([GetRootPart().Bodies[0].Faces[59],
    GetRootPart().Bodies[0].Faces[2],
    GetRootPart().Bodies[0].Faces[58]])
secondarySelection = Selection.Empty()
result = NamedSelection.Create(primarySelection, secondarySelection)
# EndBlock

# Rename Named Selection
result = NamedSelection.Rename("Group1", "Free flow")
# EndBlock

# Create Named Selection Group
primarySelection = FaceSelection.Create([GetRootPart().Bodies[0].Faces[3],
    GetRootPart().Bodies[0].Faces[4],
    GetRootPart().Bodies[0].Faces[5],
    GetRootPart().Bodies[0].Faces[6],
    GetRootPart().Bodies[0].Faces[7],
    GetRootPart().Bodies[0].Faces[8],
    GetRootPart().Bodies[0].Faces[9],
    GetRootPart().Bodies[0].Faces[10],
    GetRootPart().Bodies[0].Faces[11],
    GetRootPart().Bodies[0].Faces[12],
    GetRootPart().Bodies[0].Faces[13],
    GetRootPart().Bodies[0].Faces[14],
    GetRootPart().Bodies[0].Faces[15],
    GetRootPart().Bodies[0].Faces[16],
    GetRootPart().Bodies[0].Faces[17],
    GetRootPart().Bodies[0].Faces[18],
    GetRootPart().Bodies[0].Faces[19],
    GetRootPart().Bodies[0].Faces[20],
    GetRootPart().Bodies[0].Faces[21],
    GetRootPart().Bodies[0].Faces[22],
    GetRootPart().Bodies[0].Faces[23],
    GetRootPart().Bodies[0].Faces[24],
    GetRootPart().Bodies[0].Faces[25],
    GetRootPart().Bodies[0].Faces[26],
    GetRootPart().Bodies[0].Faces[27],
    GetRootPart().Bodies[0].Faces[28],
    GetRootPart().Bodies[0].Faces[29],
    GetRootPart().Bodies[0].Faces[30],
    GetRootPart().Bodies[0].Faces[31],
    GetRootPart().Bodies[0].Faces[32],
    GetRootPart().Bodies[0].Faces[33],
    GetRootPart().Bodies[0].Faces[34],
    GetRootPart().Bodies[0].Faces[35],
    GetRootPart().Bodies[0].Faces[36],
    GetRootPart().Bodies[0].Faces[37],
    GetRootPart().Bodies[0].Faces[38],
    GetRootPart().Bodies[0].Faces[39],
    GetRootPart().Bodies[0].Faces[40],
    GetRootPart().Bodies[0].Faces[41],
    GetRootPart().Bodies[0].Faces[42],
    GetRootPart().Bodies[0].Faces[43],
    GetRootPart().Bodies[0].Faces[44],
    GetRootPart().Bodies[0].Faces[45],
    GetRootPart().Bodies[0].Faces[46],
    GetRootPart().Bodies[0].Faces[47],
    GetRootPart().Bodies[0].Faces[48],
    GetRootPart().Bodies[0].Faces[49],
    GetRootPart().Bodies[0].Faces[50],
    GetRootPart().Bodies[0].Faces[51],
    GetRootPart().Bodies[0].Faces[52],
    GetRootPart().Bodies[0].Faces[53],
    GetRootPart().Bodies[0].Faces[54],
    GetRootPart().Bodies[0].Faces[55],
    GetRootPart().Bodies[0].Faces[56],
    GetRootPart().Bodies[0].Faces[57]])
secondarySelection = Selection.Empty()
result = NamedSelection.Create(primarySelection, secondarySelection)
# EndBlock

# Rename Named Selection
result = NamedSelection.Rename("Group1", "Walls")
# EndBlock