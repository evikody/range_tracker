num_1_10 = 0
num_11_20 = 0
num_21_30 = 0
num_31_40 = 0
num_41_50 = 0

while True:
    number = input("Please enter a number from 1 to 50: ")
    if number.isdigit() and 1 <= int(number) <= 50:
        print("You entered a valid number.")

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


    else:
        print("Invalid input. Please enter a valid number from 1 to 50.")
        break

print(f"1 - 10 = {num_1_10}")
print(f"11 - 20 = {num_11_20}")
print(f"21 - 30 = {num_21_30}")
print(f"31 - 40 = {num_31_40}")
print(f"41 - 50 = {num_41_50}")
