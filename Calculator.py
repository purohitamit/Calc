def calculator():
    if calc == "+":
        answer = num1 + num2
    elif calc == "-":
        answer = num1 - num2
    elif calc == "*":
        answer = num1 * num2
    elif calc == "/":
        answer = float(num1 / num2)
    elif calc == "%":
        answer = num1 % num2
    else:
        print("Please enter a valid choice")

    return answer


num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
calc = input("Please enter your choice: + , - , *, / or % ")
num = calculator()
print(f"You have decided {calc} and the {num1} {calc} {num2} is {num}")
