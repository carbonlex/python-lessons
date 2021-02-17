inputfile = "/Users/oshcherbakov/Downloads/rockyou.txt"
outputfile = "my_passwords.txt"

password_to_look_for = "kolya"

myfile1 = open(inputfile, mode='r', encoding='latin_1')
myfile2 = open(outputfile, mode='a', encoding='latin_1')

# print(myfile.read())

# for num, line in enumerate(myfile1, 1):
#     if "petya" in line:
#       print(str(num) + " " + line.strip())


for num, line in enumerate(myfile1, 1):
    if password_to_look_for in line:
      print(str(num) + " " + line.strip())
      myfile2.write("Found password: " + line)

myfile1.close()
myfile2.close()