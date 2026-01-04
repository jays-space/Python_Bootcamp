print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
child_ticket_price = 5
youth_ticket_price = 7
adult_ticket_price = 12
photo_price = 3
total_bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print(f"Child tickets are ${child_ticket_price}.")
        total_bill += child_ticket_price
    elif age <= 18:
        print(f"Youth tickets are ${youth_ticket_price}.")
        total_bill += youth_ticket_price
    else:
        print(f"Adult tickets are ${adult_ticket_price}.")
        total_bill += adult_ticket_price

    with_photo = input("DO you want a photo taken? Type y for Yes and n for No.")
    if with_photo == "y":
        total_bill += photo_price
        print(f"Your total bill is ${total_bill}")
    else:
        print(f"Your total bill is ${total_bill}")
else:
    print("Sorry you have to grow taller before you can ride.")