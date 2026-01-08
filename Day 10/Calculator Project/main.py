import art

# TODO: Write out the other 3 functions - subtract, multiply and divide.
def add(n1, n2):
    """
    Adds two numbers together
    :param n1:
    :param n2:
    :return: float
    """
    return n1 + n2

def subtract(n1, n2):
    """
    Subtracts two numbers together
    :param n1:
    :param n2:
    :return: float
    """
    return n1 - n2

def multiply(n1, n2):
    """
    Multiplies two numbers together
    :param n1:
    :param n2:
    :return: float
    """
    return n1 * n2

def divide(n1, n2):
    """
    Divides two numbers together
    :param n1:
    :param n2:
    :return: float
    """
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
# print(operations['*'](4, 8))

def check_float(operand_1, operand_2):
    """Checks if the operands are both float"""
    is_operand_1_float = type(operand_1) == float
    is_operand_2_float = type(operand_2) == float

    return is_operand_1_float and is_operand_2_float

def prompt(re_calc = False):
    if re_calc:
        num_1 = None
    else:
        num_1 = input("What's the first number? ")

    print(f"+ \n - \n * \n /")
    operation = input("Pick an operation: ")
    num_2 = input("What's the second number? ")
    return {"operation": operation, "num_1": num_1, "num_2": num_2}

def compute(operand_1, operand_2, computation, current_result=None):
    if not check_float(operand_1, operand_2):
        return None

    if computation in operations:
        if current_result is None:
            return float(operations[computation](float(operand_1), float(operand_2)))
        else:
            return float(operations[computation](float(current_result), float(operand_2)))
    return 0.0

# TODO: Improve by implementing a recursion pattern
# def run(res, re_calc = False):
#     inputs = prompt(re_calc)
#     previous_result = res
#     resultant = compute(operand_1 = inputs["num_1"], operand_2 = inputs["num_2"], computation = inputs["operation"], current_result = previous_result)
#     if resultant is None:
#         print("Invalid input")
#     else:
#         print(f"{previous_result} {inputs["operation"]} {inputs["num_2"]} = {resultant}")
#         user_decision = input(f"Type 'y' to continue calculating with {resultant}, or 'n' to start a new calculation. Otherwise type 'e' to exit: ").lower()
#
#     return {"user_decision": user_decision}

def print_header():
    print(f"\n" * 20)
    print(art.logo)

print(art.logo)
result = 0.0
running = True
decision = 'n'
while running:
    if decision == 'y':
        user_inputs = prompt(True)
        # use result and new num_2 to re-calc result
        prev_result = result
        result = compute(operand_1 = user_inputs["num_1"], operand_2 = user_inputs["num_2"], computation = user_inputs["operation"], current_result = prev_result)
        if result is None:
            print_header()
            print("Invalid input")
        else:
            print(f"{prev_result} {user_inputs["operation"]} {user_inputs["num_2"]} = {result}")
            decision = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation. Otherwise type 'e' to exit: ").lower()
            continue
    elif decision == 'e':
        running = False
        break
    elif decision == 'n':
        user_inputs = prompt()
        result = compute(operand_1 = user_inputs["num_1"], operand_2 = user_inputs["num_2"], computation = user_inputs["operation"], current_result = None)
        if result is None:
            print_header()
            print("Invalid input")
        else:
            print(f"{user_inputs["num_1"]} {user_inputs["operation"]} {user_inputs["num_2"]} = {result}")
            decision = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation. Otherwise type 'e' to exit: ").lower()
    else:
        print_header()
        print("Invalid operation")