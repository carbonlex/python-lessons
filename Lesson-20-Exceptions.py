import sys

filename = "my_passwordss.txt"

while True:
    try:
        myfile = open(filename, mode='r', encoding="Latin_1")
    except Exception:
        print("Error Found")
        print(sys.exc_info()[1])
        filename = input("Enter correct path and file name :")
    else:
        print(myfile.read())
        sys.exit()

print("------------EOF----------")

