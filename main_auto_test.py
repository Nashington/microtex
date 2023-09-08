import microtextures
import os
import numpy as np
import time
import PyAnsys.PyFluent_main as pyfluent_main
import PyAnsys.SC_cmd as sc_cmd
import PyAnsys.boundarylayerthickness as blt

def main(depth, width, gap):
    tick = time.time()
    # change working directory
    os.chdir(r"E:\Summer Placement\Summer Placement Testbed")

    # create model
    model = microtextures.Scallop(depth, width, gap, 90).texture_disc()
    microtextures.CQModel(10,1,4).export_STEP(model, 8)

    tock = time.time()
    print("Model creation time taken: ", tock - tick)

    # run SC script
    tick = time.time()
    sc_cmd.execute()
    tock = time.time()
    print("SC script execution time taken: ", tock - tick)

    # run Fluent meshing and simulations
    tick = time.time()
    pyfluent_main.main()
    tock = time.time()
    print("Fluent meshing and simulation time taken: ", tock - tick)

    # read resultant csv and calculate boundary layer thickness
    tick = time.time()
    y_value = blt.execute()
    tock = time.time()
    print("Boundary layer thickness calculation time taken: ", tock - tick)
    
    return y_value

if __name__=='__main__':
    boundary_layer_thickness = main(0.1, 0.15, 0.2)
    print(boundary_layer_thickness)