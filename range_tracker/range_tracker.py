while True:
    number = input("Please enter a number from 1 to 50: ")
    if number.isdigit() and 1 <= int(number) <= 50:
        print("You entered a valid number.")

        while True:
            retry = input("Do you want to enter another number? ").lower()
            if retry == "yes":
                break
            elif retry == "no":
                print("Thank You!")
                exit()
            else:
                print("Invalid. Please type yes or no.")

    else:
        print("Invalid input. Please enter a valid number from 1 to 50.")
