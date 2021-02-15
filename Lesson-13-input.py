# name = input("Please enter your name: ")
#
# print("Hello " + name)
#
# num1 = input("Enter x: ")
# num2 = input("Enter y: ")
#
# summa = int(num1) + int(num2)
# print(summa)

message = ""
# while True:
#     message = input("Enter Password")
#     if message == 'secret':
#         break
#     print(message +  " Password Incorrect")
# print("Password was:" + message)


mylist = []
msg =""
while msg != 'stop':
    msg = input("Enter new item, and STOP to finish  ")
    mylist.append(msg)

print(mylist)