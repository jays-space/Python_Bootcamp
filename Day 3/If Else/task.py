print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
min_height = 120

if height < min_height:
    print("Sorry, your height is too small.")
else:
    print(f"Your height is {height}cm. You can ride the rollercoaster!")