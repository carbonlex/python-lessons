enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name' : 'Mudilo',
    'image': ['image1.jpg', 'image2.jpg', 'image3.jpg']
}

all_enemies = []

for x in range(0,10):
    all_enemies.append(enemy.copy())


for ene in all_enemies:
    print(ene)

all_enemies[5]['health'] = 30
all_enemies[8]['name'] = "Mudak"
all_enemies[2]['loc_x'] +=10
print("---------------")
for ene in all_enemies:
    print(ene)