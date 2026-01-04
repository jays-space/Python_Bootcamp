sml_pizza = 15
md_pizza = 20
lg_pizza = 25
with_pepperoni = 2
with_extra_cheese = 1

def get_pizza_base(pizza_size):
    bill = 0

    if pizza_size == "S":
        bill = sml_pizza
    elif pizza_size == "M":
        bill = md_pizza
    else :
        bill = lg_pizza

    return int(bill)

def add_pepperoni(answer):
    bill = 0

    if answer == "Y":
        bill = with_pepperoni

    return int(bill)

def add_extra_cheese(answer):
    bill = 0
    if answer == "Y":
        bill = with_extra_cheese

    return int(bill)

def order_pizza():
    total_bill = 0

    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M or L: ")
    total_bill += get_pizza_base(size)

    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    total_bill += add_pepperoni(pepperoni)

    extra_cheese = input("Do you want extra cheese? Y or N: ")
    total_bill += add_extra_cheese(extra_cheese)

    print(f"Your total bill is ${total_bill}")

order_pizza()