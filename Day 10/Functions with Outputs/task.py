# PAUSE 1
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide any name."

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    # PAUSE 2
    return f"{formatted_f_name + ' ' + formatted_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))