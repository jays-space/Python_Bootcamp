print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")

# def main():
#     # Direction choice
#     direction = input("You are at a cross road. Where do you want to go? \nType 'left' or 'right': ").lower()
#     if direction != "left":
#         print("You fell into a hole. Game Over!")
#         return
#
#     # Transport choice
#     transport = input("You've come to a lake. There is an island in the middle of the lake. \nType 'wait' to wait for a boat. Type 'swim' to swim across the lake: ").lower()
#     if transport != "wait":
#         print("Attacked by trout. Game Over!")
#         return
#
#     # Door choice
#     door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ").lower()
#
#     if door == "yellow":
#         print("You found the treasure! You Win!")
#     elif door == "red":
#         print("Burned by fire. Game Over!")
#     elif door == "blue":
#         print("Eaten by beasts. Game Over!")
#     else:
#         print("Game Over!")
#
# main()

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Game configuration - easy to modify rules
VALID_CHOICES = {
    'direction': {'correct': 'left', 'failure': 'You fell into a hole. Game Over!'},
    'transport': {'correct': 'wait', 'failure': 'Attacked by trout. Game Over!'},
    'door': {
        'yellow': 'You found the treasure! You Win!',
        'red': 'Burned by fire. Game Over!',
        'blue': 'Eaten by beasts. Game Over!',
        'default': 'Game Over!'
    }
}

def get_user_input(prompt):
    """Get and normalize user input"""
    return input(prompt).lower().strip()

def validate_binary_choice(user_choice, choice_type):
    """Validate choices with a single correct answer"""
    config = VALID_CHOICES[choice_type]
    if user_choice != config['correct']:
        print(config['failure'])
        return False
    return True

def handle_door_choice(door_color):
    """Handle the final door selection with multiple outcomes"""
    door_config = VALID_CHOICES['door']
    message = door_config.get(door_color, door_config['default'])
    print(message)
    return door_color == 'yellow'

def main():
    # Direction decision
    direction = get_user_input(
        "You are at a cross road. Where do you want to go? \nType 'left' or 'right': "
    )
    if not validate_binary_choice(direction, 'direction'):
        return

    # Transport decision
    transport = get_user_input(
        "You've come to a lake. There is an island in the middle of the lake. \n"
        "Type 'wait' to wait for a boat. Type 'swim' to swim across the lake: "
    )
    if not validate_binary_choice(transport, 'transport'):
        return

    # Door decision
    door = get_user_input(
        "You arrive at the island unharmed. There is a house with 3 doors. "
        "One red, one yellow and one blue. Which color do you choose? "
    )
    handle_door_choice(door)

main()