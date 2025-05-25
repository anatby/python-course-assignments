numbers = [1203, 1256, 312456, 98]

# Initialize a list to count digits 0-9
digit_counts = [0] * 10

# Count digits in all numbers
for number in numbers:
    for digit in str(number):
        digit_counts[int(digit)] += 1

# Print the results
for digit in range(10):
    print(f"{digit}  {digit_counts[digit]}")
