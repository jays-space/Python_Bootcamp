import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

def who_pays(list_of_people):
    index = random.randint(0, len(list_of_people) - 1)
    return list_of_people[index]

print(f"{who_pays(friends)} is paying today")
print(f"{random.choice(friends)} is also paying today")