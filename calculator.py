# Building a simple calculator!


def operation():
    user_input = f"{first_number} {operator} {second_number}"
    print(user_input)


while True:
    first_number = float(input("Enter the first input value: "))
    operator = input("Choose an operator[(+), (-), (*), (/), (%)]: ")
    second_number = float(input("Enter the second input value: "))
    operation()
    if operator == "+":
        result = first_number + second_number
        print(result)

    elif operator == "-":
        result = first_number - second_number
        print(result)

    elif operator == "*":
        result = first_number * second_number
        print(result)

    elif operator == "/":
        result = first_number / second_number
        print(result)

    elif operator == "%":
        result = first_number % second_number
        print(result)

    elif operator == "exit":
        exit()

    else:
        print("Sorry, not a valid input!")
