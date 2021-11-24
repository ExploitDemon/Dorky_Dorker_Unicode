import subprocess
import os
import platform
try:
    from pypresence import Presence
except Exception as e:
    pass
import time
if platform.system() == "Linux":
    clear = lambda: os.system('clear')
    clear()
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
    clear()
a = "░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░"
b = "██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗"
c = "██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝"
d = "██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗"
e = "╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║"
f = "░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝"
print("")
print("")
print("")
print(a.center(115))
print(b.center(115))
print(c.center(115))
print(d.center(115))
print(e.center(115))
print(f.center(115))
print("")
print("")
message = "Skidded by Branb#4740"
version = "v 0.0.1"
print(message.center(115))
print(version.center(115))
print("")
print("")
print("Please select an option.")
print("1. Dork generator")
print("2. Dork Randomizer")
print("3. File Splitter")
selecting = 1
while selecting == 1:
    try:
        option = int(input("Select what you want to use: "))
    except:
        option = 404

    if option == 1:
        selecting = 0
        if platform.system() == "Linux":
            p = subprocess.call(["python3", "modules/pre-generate.py"])
        if platform.system() == "Windows":
            p = subprocess.call(["python", "modules/pre-generate.py"])
    elif option == 2:
        selecting = 0
        if platform.system() == "Linux":
            p = subprocess.call(["python3", "modules/randomize.py"])
        if platform.system() == "Windows":
            p = subprocess.call(["python", "modules/randomize.py"])
    elif option == 3:
        selecting = 0
        if platform.system() == "Linux":
            p = subprocess.call(["python3", "modules/split.py"])
        if platform.system() == "Windows":
            p = subprocess.call(["python", "modules/split.py"])