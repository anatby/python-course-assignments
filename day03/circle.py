import math    
import sys



if len(sys.argv) != 2:
    print("Usage: python circle.py <radius>")
    sys.exit(1)

try:
    radius = float(sys.argv[1])
    area = math.pi * radius ** 2    
    circumference = 2 * math.pi * radius
    print(f"Area of the circle: {area:.2f}")
    print(f"Circumference of the circle: {circumference:.2f}")
except ValueError:
    print("Please provide a valid number for the radius.")
    sys.exit(1)

