# Purpose: To run SpaceClaim script from command line, on a headless instance of SpaceClaim
# SpaceClaim script is used to create the fluid domain from a model, it can be run in GUI for easier debugging

import os


def execute():
    # SpaceClaim installation Directory
    # Made a variable in case we want to give the user the choice to change the installation directory later
    filepath = r"E:\ANSYS Inc\ANSYS Student\v232\scdm"


    os.chdir(filepath)
    os.system('cmd /c spaceclaim.exe /RunScript="E:\Summer Placement\Summer Placement Testbed\model42_fluiddomain_topflush.py" /Headless=True /Splash=False /Welcome=False /ExitAfterScript=True"')
    # must use /c instead of /k to close the prompt after execution if running terminal in vscode
    # we may want to keep SCDM open to accept more scripts without having to open a new instance
    # if so, build in a function to close SCDM after all scripts have been run

if __name__=='__main__':
    execute()