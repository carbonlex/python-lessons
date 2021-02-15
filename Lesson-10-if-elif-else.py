x = 456

if x == 45:
    print("Yes you are right")
else:
    print("No you are wrong")


age = 99


if age <=4:
    print("You are baby")
elif age >4 and age <12:
    print("You are kid")
elif age>=12 and age <19:
    print("You are teenager")
else:
    print("You are old!")


all_cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
german_cars = ['bmw', 'vw', 'audi']

if 'lada' in all_cars:
    print("Lada in the list")
else:
    print("not in the list")


for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx + " is German car")
    else:
        print(xxxx + " is not German car")