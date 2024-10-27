while True:
    number = input("Please enter a number from 1 to 50: ")
    if number.isdigit() and 1 <= int(number) <= 50:
        break
    else:
        print("Invalid input. Please enter a valid number from 1 to 50.")
