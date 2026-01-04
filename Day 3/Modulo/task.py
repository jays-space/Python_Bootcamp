
def is_even(num):
    if int(num) % 2 == 0:
        return True
    else:
        return False


number = input("What is the number you want to check?")
print(is_even(number))