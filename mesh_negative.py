import trimesh
import os
import numpy as np
import stl
from stl import mesh
#import scipy
#import pymesh
import polyscope



os.chdir("P:\OneDrive\Cardiff University\OneDrive - Cardiff University\Year 3\EN3100 - Project\Testbed")

#create a function that takes in a .dat point cloud file and returns an stl object with thickness
def point_cloud_to_stl(filename, thickness):
    #load the point cloud
    point_cloud = np.loadtxt(filename)
    #create a mesh object from the point cloud
    mesh = trimesh.Trimesh(vertices=point_cloud)
    #create a solid object from the mesh object
    solid = mesh.convex_hull
    #save the solid object as an stl file
    solid.export('solid.stl')
    #load the stl file
    solid = stl.mesh.Mesh.from_file('solid.stl')
    #create a new stl object with thickness
    new_solid = stl.mesh.Mesh(np.zeros(solid.vectors.shape[0] * 2, dtype=stl.mesh.Mesh.dtype))
    #create a new array of the same size as the original stl object
    new_solid.vectors[0::2] = solid.vectors
    #create a new array of the same size as the original stl object, but with the z coordinate increased by the thickness
    new_solid.vectors[1::2] = solid.vectors + [0, 0, thickness]
    #save the new stl object
    new_solid.save('pctostl.stl')

#point_cloud_to_stl('Real.dat', 5)

#create a function that takes in an stl file and inverts the bottom and side faces about the z axis to create a negative
def invert_stl(filename):
    #load the stl file
    solid = stl.mesh.Mesh.from_file(filename)
    #create a new stl object with the same number of faces as the original
    new_solid = stl.mesh.Mesh(np.zeros(solid.vectors.shape[0], dtype=stl.mesh.Mesh.dtype))
    #create a new array of the same size as the original stl object
    new_solid.vectors[0::1] = solid.vectors
    #create a new array of the same size as the original stl object, but with the z coordinate inverted
    new_solid.vectors[1::1] = solid.vectors * [1, 1, -1]
    #save the new stl object
    new_solid.save('inverted.stl')

#invert_stl('Real.stl')

#create a function that takes a .dat point cloud file and returns a negative stl object
#def point_cloud_to_negative_stl(filename, thickness):

#create a function using pymesh that makes a mesh object from the point cloud with thickness and saves it as an stl file, don't use trimesh
#def point_cloud_to_stl_pymesh(filename, thickness):

#create a function that translates the bottom face of an stl object by a given distance
def translate_stl(filename, distance):
    #load the stl file
    solid = stl.mesh.Mesh.from_file(filename)
    #create a new stl object with the same number of faces as the original
    new_solid = stl.mesh.Mesh(np.zeros(solid.vectors.shape[0], dtype=stl.mesh.Mesh.dtype))
    #create a new array of the same size as the original stl object
    new_solid.vectors[0::1] = solid.vectors
    #create a new array of the same size as the original stl object, but with the z coordinate increased by the distance
    new_solid.vectors[1::1] = solid.vectors + [0, 0, distance]
    #save the new stl object
    new_solid.save('translated.stl')

#translate_stl('Real.stl', 10)

#create a function that visualises a point cloud with polyscope
def polyscope_point_cloud(filename):
    #load the point cloud
    point_cloud = np.loadtxt(filename)
    #initialise polyscope
    polyscope.init()
    #register the point cloud
    ps_cloud = polyscope.register_point_cloud("my points", point_cloud)
    #show the point cloud
    polyscope.show()

#polyscope_point_cloud('Real.dat')

#import an stl and extract x, y, z coordinates and save them as a .dat file in three columns
def import_stl(filename):
    #load the stl file
    solid = stl.mesh.Mesh.from_file(filename)
    #create an array of the x coordinates
    x = solid.vectors[:, :, 0]
    #create an array of the y coordinates
    y = solid.vectors[:, :, 1]
    #create an array of the z coordinates
    z = solid.vectors[:, :, 2]
    #create an array of the x, y, z coordinates
    #xyz = np.array([x, y, z])
    #save the array as a .dat file
    np.savetxt('exportfromstl.dat', x, fmt='%.18g', delimiter=' ', newline=os.linesep)

#import_stl('Real.stl')

#take a .dat file and find the size of its dimensions
def find_size(filename):
    #load the .dat file
    point_cloud = np.loadtxt(filename)
    #create an array of the x coordinates
    x = point_cloud[:, 0]
    #create an array of the y coordinates
    y = point_cloud[:, 1]
    #create an array of the z coordinates
    z = point_cloud[:, 2]
    #find the maximum and minimum x coordinates
    x_max = np.amax(x)
    x_min = np.amin(x)
    #find the maximum and minimum y coordinates
    y_max = np.amax(y)
    y_min = np.amin(y)
    #find the maximum and minimum z coordinates
    z_max = np.amax(z)
    z_min = np.amin(z)
    #find the size of the x, y, z dimensions
    x_size = x_max - x_min
    y_size = y_max - y_min
    z_size = z_max - z_min
    #print the size of the x, y, z dimensions
    print(x_size, y_size, z_size)
    
#find_size('Real.dat')

#take a .dat file and find the number of elements in each of its dimensions
def find_elements(filename):
    #load the .dat file
    point_cloud = np.loadtxt(filename)
    #create an array of the x coordinates
    x = point_cloud[:, 0]
    #create an array of the y coordinates
    y = point_cloud[:, 1]
    #create an array of the z coordinates
    z = point_cloud[:, 2]
    #find the number of elements in each dimension
    x_elements = len(np.unique(x))
    y_elements = len(np.unique(y))
    z_elements = len(np.unique(z))
    #print the number of elements in each dimension
    print(x_elements, y_elements, z_elements)

#find_elements('Real.dat')

#make an array with the same x and y, but with a z element of -5
def make_array(filename):
    #load the .dat file
    point_cloud = np.loadtxt(filename)
    print(np.size(point_cloud))
    #create an array of the x coordinates
    x = point_cloud[:, 0]
    #create an array of the y coordinates
    y = point_cloud[:, 1]
    z = point_cloud[:, 2]
    z = np.full(((len(np.unique(z))), 1), -5)
    #create an array of the x, y, z coordinates with the z element of -5
    xyz = np.zeros((np.size(point_cloud), 3))
    xyz[:, 0] = np.reshape(x, -1)
    xyz[:, 1] = np.reshape(y, -1)
    xyz[:, 2] = np.reshape(z, -1)
    #concatenate array with the pointcloud
    #xyz_negative = np.concatenate((point_cloud, xyz_negative), axis=0)
    #visualise
    #initialise polyscope
    polyscope.init()
    #register the point cloud
    ps_cloud = polyscope.register_point_cloud("my points", xyz)
    #show the point cloud
    polyscope.show()

#make_array('Real.dat')
    
# generate some neat n times 3 matrix using a variant of sync function
def make_sinc():
    x = np.linspace(-3, 3, 401)
    mesh_x, mesh_y = np.meshgrid(x, x)
    z = np.sinc((np.power(mesh_x, 2) + np.power(mesh_y, 2)))
    z_norm = (z - z.min()) / (z.max() - z.min())
    xyz = np.zeros((np.size(mesh_x), 3))
    xyz[:, 0] = np.reshape(mesh_x, -1)
    xyz[:, 1] = np.reshape(mesh_y, -1)
    xyz[:, 2] = np.reshape(z_norm, -1)
    polyscope.init()
    #register the point cloud
    ps_cloud = polyscope.register_point_cloud("my points", xyz)
    #show the point cloud
    polyscope.show()
    print('xyz')
    print(xyz)

#make_sinc()

#make a function that takes a .dat file cloud of points and inverts it in the z direction
def invert_z(filename):
    #load the .dat file
    point_cloud = np.loadtxt(filename)
    #create an array of the x coordinates
    x = point_cloud[:, 0]
    #create an array of the y coordinates
    y = point_cloud[:, 1]
    #create an array of the z coordinates
    z = point_cloud[:, 2]
    #invert the z coordinates
    z = -z
    #create an array of the x, y, z coordinates
    xyz = np.zeros((np.size(point_cloud), 3))
    xyz[:, 0] = np.reshape(x, -1)
    xyz[:, 1] = np.reshape(y, -1)
    xyz[:, 2] = np.reshape(z, -1)
    #save the array as a .dat file
    np.savetxt('inverted.dat', xyz, fmt='%.18g', delimiter=' ', newline=os.linesep)
    #visualise
    #initialise polyscope
    polyscope.init()
    #register the point cloud
    ps_cloud = polyscope.register_point_cloud("my points", xyz)
    #show the point cloud
    polyscope.show()

#invert_z('Real.dat')

### WORKS!!!!! ###
#make a function that takes a .dat file cloud of points and saves the x coordinates as a .dat file
#modify the function to 
def save_x(filename):
    #load the .dat file
    point_cloud = np.loadtxt(filename)
    #create an array of the x coordinates
    x = point_cloud[:, 0]
    y = point_cloud[:, 1]
    z = point_cloud[:, 2]
    xy = list(zip(x, y, -z))
    #print(x.shape)
    #print(y.shape)
    #print(z.shape)
    #save the array as a .dat file
    np.savetxt('x.dat', xy, fmt='%.3f', delimiter=' ')
    
save_x('Real.dat')
