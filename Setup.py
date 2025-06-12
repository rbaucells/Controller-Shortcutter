import os
import subprocess
import time
def Main():
    result = os.system("dotnet --version >nul 2>&1")
    if result == 0:
        print(".NET SDK is installed.")
    else:
        print(".NET SDK is not installed.")

    packages = ["pyglet", "logging", "pystray", "pillow"]

    for package in packages:
        subprocess.check_call([os.sys.executable, "-m", "pip", "install", package])
    
    print("Setup Complete")
    time.sleep(5)
    
Main()