import math
shape = input("square, rectangle, circle, triangle").strip().lower()
if shape == "square":
    side = float(input(""))
    area = round(side ** 2, 3)
    print(area)
elif shape == "rectangle":
    length = float(input(""))
    width = float(input(""))
    area = round(length * width, 3)
    print(area)
elif shape == "circle":
    radius = float(input(""))
    area = round(math.pi * radius ** 2, 3)
    print(area)
elif shape == "triangle":
    base = float(input(""))
    height = float(input(""))
    area = round(0.5 * base * height, 3)
    print(area)
else:
    print("square, rectangle, circle, or triangle.")
