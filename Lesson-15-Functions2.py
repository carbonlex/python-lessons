def create_record(name, telephone, address):
    """"Create Record"""
    record = {
        'name' : name,
        'phone' : telephone,
        'address' : address
    }
    return record

user1 = create_record("Alexey", "+380746574", "Ukraine")
user2 =create_record("Vika", "+3805789574", "Germany")

print(user1)
print(user2)

def give_award(medal, *persons):
    """Give Medals to persons"""
    for person in persons:
        print("Tovarish " + person.title() + " nagrajdaetsa medaliyu " + medal)

give_award("Za Berlin", "Vasya", "Petya")
give_award("Za Horoshee Povedeniye", "Alexey", "Vasya")