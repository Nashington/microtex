# Purpose: To run SpaceClaim script from command line, on a headless instance of SpaceClaim
# SpaceClaim script is used to create the fluid domain from a model, it can be run in GUI for easier debugging

import os

# SpaceClaim installation Directory
# Made a variable in case we want to give the user the choice to change the installation directory later
filepath = r"D:\Program Files\ANSYS Inc\ANSYS Student\v232\scdm"


os.chdir(filepath)
os.system('cmd /c spaceclaim.exe /RunScript="D:\Work\Summer Placement Testbed\model42_fluiddomain_topflush.scscript" /Headless=True /Splash=False /Welcome=False /ExitAfterScript=True"')
# must use /c instead of /k to close the prompt after execution if running terminal in vscode