num = input("Please enter a number: ")
number = float(num)
if number.is_integer():
        print(f"The number {int(number)} is an integer.")
elif '.' in num:
        print(f"The number {num} is a decimal.")