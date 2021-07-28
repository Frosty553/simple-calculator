from time import sleep
print("Before we start: This calculator only works with integers, so numbers like 1 2 3")
sleep(3)
print("Numbers like 0.15 30.30 12.3 will not work")
sleep(3)
print("Okay that's all let's start!")
sleep(3)
while True:
    try:
        first_number = int(input("What's the first number? : "))
    except ValueError:
        print("Please only input numbers, you can't calculate words")
        sleep(2)
        print("The program will now be closed, please start it again and input correct numbers")
        sleep(1)
        print(".")
        sleep(1)
        print("..")
        sleep(1)
        print("...")
        sleep(1)
        print("....")
        sleep(1)
        print(".....")
        sleep(1)
        break
    try:
        second_number = int(input("What's the second number? : "))
    except ValueError:
        print("Please only input numbers, you can't calculate words")
        sleep(2)
        print("The program will now be closed, please start it again and input correct numbers")
        sleep(1)
        print(".")
        sleep(1)
        print("..")
        sleep(1)
        print("...")
        sleep(1)
        print("....")
        sleep(1)
        print(".....")
        sleep(1)
        break
    calculation_method = input("How should the numbers be calculated? Please type as:\nm-multiplication\nd-division\na-addition\ns-subtraction : ")
    if calculation_method == "m":
        result = first_number * second_number
        print(f"Here is the output: {result}")
    elif calculation_method == "d":
        result = first_number / second_number
        print(f"Here is the output: {result}")
    elif calculation_method == "a":
        result = first_number + second_number
        print(f"Here is the output: {result}")
    elif calculation_method == "s":
        result = first_number - second_number
        print(f"Here is the output: {result}")
    else:
        print("Sorry either this type of calculation method isn't supported or it doesn't exist, please try again")
        sleep(3)
