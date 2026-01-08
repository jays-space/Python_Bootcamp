import random
import my_module

# my_random_number = random.randint(my_module.min_random_number, my_module.max_random_number)
#
# print(my_random_number)


print("Heads or Tails?")
value = input('Type H for "Heads" or T for "Tails": ').lower()
random_number = random.randint(my_module.min_random_number, my_module.max_random_number)

isHeads = True if random_number == 1 else False
isTails = True if value == 't' or value == 'tails' and random_number == 0 else False

isWinner = None

if isHeads and value == 'heads' or value == 'h':
    isWinner = True
elif isTails and value == 'tails' or value == 't':
    isWinner = True
else :
    isWinner = False

print(f"winning value {value} is {isWinner}")
print(f"{'You WIN!!' if isWinner  else 'GAVE OVER!!!!!!'}")