import sys
import os

x = len(sys.argv)
if x >1:
    if sys.argv[1] == "help":
        print("Help Requested")
        print("Usage of this program is: python.exe")
    print("Arguments entered " + str(sys.argv[1:]))
else:
    print("Arguments mot provided")

os.system("ls > list_of_folder.txt")
sys.exit()