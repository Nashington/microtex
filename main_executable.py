import microtextures
import os
import numpy as np
import time

def main():
    tick = time.time()
    # change working directory
    os.chdir(r"E:\Summer Placement\Testbed")

    # https://stackoverflow.com/questions/16552508/python-loops-for-simultaneous-operation-two-or-possibly-more
    # to enable customisable ranges in geometry
    
    for i, angle in zip(range(40,43), np.linspace(0, 90, 3)):
        model = microtextures.Scallop(0.1, 0.15, 0.2, angle).texture_disc()
        microtextures.CQModel().export_STEP(model, i)

    tock = time.time()
    print("Time taken: ", tock - tick)

if __name__=='__main__':
    main()