def classify_number(number):
    if number < 0:
        print("The number is negative.")
    elif number == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")

# Example usage:
number = int(input("Enter a number: "))
classify_number(number)
