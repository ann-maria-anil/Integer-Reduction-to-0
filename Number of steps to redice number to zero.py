def reduce_to_zero(num):
    count = 0  

    while num > 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        count += 1

    return count

# Take an integer input from the user
num = int(input("Enter a positive integer: "))

if num <= 0:
    print("Please enter a positive integer.")
else:
    # Calculate the number of steps needed to reduce the number to 0
    steps = reduce_to_zero(num)
    print(f"{steps} steps are needed to reduce {num} to 0.")
