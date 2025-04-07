# rectangle.py

# Ask the user for height and width
height = float(input("Enter the height of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area and perimeter
area = height * width
perimeter = 2 * (height + width)

# Display the results
print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")