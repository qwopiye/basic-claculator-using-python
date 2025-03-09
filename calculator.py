# Function Definitions for Arithmetic Operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def modulus(x, y):
    return x % y

def floor_division(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x // y

def power(x, y):
    return x ** y

# Main Calculator Function
def calculator():
    while True:
        print("\n========== Python Calculator ==========")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Floor Division (//)")
        print("7. Power (**)")
        print("8. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

        if choice == '8':
            print("Exiting the calculator. Thank you!")
            break

        if choice in ('1', '2', '3', '4', '5', '6', '7'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
                elif choice == '5':
                    print(f"Result: {num1} % {num2} = {modulus(num1, num2)}")
                elif choice == '6':
                    print(f"Result: {num1} // {num2} = {floor_division(num1, num2)}")
                elif choice == '7':
                    print(f"Result: {num1} ** {num2} = {power(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select a valid option.")

calculator()
