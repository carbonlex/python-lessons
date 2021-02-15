cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

for car in cars:
    print(car.upper())


for car in range(1,6):
    print(car)


mynumber_list = list(range(0, 10))
print(mynumber_list)
print("--------------------------")

for x in mynumber_list:
    x = x * 2
    print(x)

mynumber_list.sort(reverse=True)
print(mynumber_list)

print(max(mynumber_list))
print(min(mynumber_list))
print(sum(mynumber_list))
print("----------------------------------")

cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
mycars = cars[1:4]
print(mycars)
mycars = cars[:4]
print(mycars)
mycars = cars[-3:-1]
print(mycars)
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
mycars = cars[:]
