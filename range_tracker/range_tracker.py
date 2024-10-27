# Counters for each range of numbers
num_1_10 = 0 # Counter for numbers from 1 to 10
num_11_20 = 0 # Counter for numbers from 11 to 20
num_21_30 = 0 # Counter for numbers from 21 to 30
num_31_40 = 0 # Counter for numbers from 31 to 40
num_41_50 = 0 # Counter for numbers from 41 to 50

# A loop that will continue asking for a number
while True:
    number = input("Please enter a number from 1 to 50: ")
    # Check if the input is a digit within the range from 1 to 50
    if number.isdigit() and 1 <= int(number) <= 50:
        print("You entered a valid number.")

        # Add the right range counter
        if 1 <= int(number) <= 10:
            num_1_10 += 1
        elif 11 <= int(number) <= 20:
            num_11_20 += 1
        elif 21 <= int(number) <= 30:
            num_21_30 += 1
        elif 31 <= int(number) <= 40:
            num_31_40 += 1
        elif 41 <= int(number) <= 50:
            num_41_50 += 1

    # Print an error message and break out from the loop when the input is invalid
    else:
        print("Invalid input. Please enter a valid number from 1 to 50.")
        break

# Display the results
print(f"1 - 10 = {num_1_10}")
print(f"11 - 20 = {num_11_20}")
print(f"21 - 30 = {num_21_30}")
print(f"31 - 40 = {num_31_40}")
print(f"41 - 50 = {num_41_50}")