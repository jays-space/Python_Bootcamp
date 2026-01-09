def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing? - it is looping from 1 though to 19
# 2. When is the function meant to print "You got it"? - when the loop hits 20
# 3. What are your assumptions about the value of i? - no assumptions. the range method is not inclusive of the argument passed in (20)