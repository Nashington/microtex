import microtextures
import os
import numpy as np

def main ():
    # change working directory
    os.chdir(r"C:\Users\nashi\OneDrive - Cardiff University\Year 3\EN3100 - Project\Testbed")

    # https://stackoverflow.com/questions/16552508/python-loops-for-simultaneous-operation-two-or-possibly-more
    # to enable customisable ranges in geometry
    for i, gap in zip(range(30,35), np.linspace(0.1, 0.2, 2)):
        model = microtextures.Scallop(0.1, 0.15, gap).texture_disc()
        microtextures.CQModel().export_STL(model, i)

if __name__=='__main__':
    main()