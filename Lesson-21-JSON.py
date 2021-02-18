import json
filename = "user_settings.txt"
myfile = open(filename, mode='w', encoding='Latin-1')

player1 = {
    'PlayerName': "Donald Duck",
    'Score': 345,
    'awards': ["OR", "NV", "NY"]
}

player2 = {
    'PlayerName': "Guffi",
    'Score': 346,
    'awards': ["WI", "IX", "MI"]
}

myplayers=[]
myplayers.append(player1)
myplayers.append(player2)

# ------- SAVE by JSON ---------

json.dump(myplayers, myfile)
myfile.close()

# ------- LOAD by JSON ----------

myfile = open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile)


for user in json_data:
    print("Player Name is: " + str(user['PlayerName']))
    print("Player Score is " + str(user['Score']))
    print("Player Award #1 " + str(user['awards'][0]))
    print("Player Award #2 " + str(user['awards'][1]))
    print("Player Award #3 " + str(user['awards'][2]))
    print("-------------------------------------\n\n")
