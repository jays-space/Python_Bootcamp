min_height = 120

toddler_age = 12
adult_age = 18

toddler_price = 5
teen_price = 7
adult_price = 12

def get_ride_cost():
    age = int(input("How old are you? "))

    if age > adult_age:
        print(f"The ride will cost ${adult_price}.")
    elif age < toddler_age:
        print(f"The ride will cost ${toddler_price}")
    else:
        print(f"The ride will cost ${teen_price}.")

def check_height():
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))

    if height >= min_height:
        print("You can ride the rollercoaster")
        get_ride_cost()
    else:
        print("Sorry you have to grow taller before you can ride.")


check_height()