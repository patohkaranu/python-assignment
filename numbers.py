def divide_numbers():
    try:
        num1_str = input("Enter the first number: ")
        num2_str = input("Enter the second number: ")

        num1 = int(num1_str)
        num2 = int(num2_str)

        result = num1 / num2

    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print("Result:", result)
    finally:
        print("Operation complete.")

# Call the function to execute it
divide_numbers()
