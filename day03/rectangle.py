import sys

def calculate_area_and_perimeter(width, length):
    area = width * length
    perimeter = 2 * (width + length)
    return area, perimeter

if len(sys.argv) != 3:
    print("Usage: py script.py <width> <length>")
    sys.exit(1)

try:
    width = float(sys.argv[1])
    length = float(sys.argv[2])
    area, perimeter = calculate_area_and_perimeter(width, length)
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
except ValueError:
    print("Please provide valid numbers for width and length.")