# Calculator app

try:
    num1 = num2 = 1
    num1 = int(input('Enter the first integer :'))
    num2 = int(input("Enter teh second integer"))
except ValueError as err:
    print(err)

else:

    while True:
        operator = input("Enter the operator")
        if not (operator in "+-*/"):
            print("Please Enter a valid Operator +,-,*,/")
        else:
            break;


finally:
    operator="+"
    if operator == "+":
        result = num2 + num1
    elif operator == "-":
        result = num1 - num2;
    elif operator == "*":
        result = num1 * num2;
    elif operator == "/":
        result = num1 / num2;
    try:
        print("Result of the operation is " + str(result))
    except TypeError as err:
        print(err)
