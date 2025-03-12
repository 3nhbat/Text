import math

def calculate_area(shape):
    if shape == "квадрат":
        side = float(input("Квадратын талын урт: "))
        return round(side ** 2, 3)
    elif shape == "тэгш өнцөгт":
        length = float(input("Тэгш өнцөгтийн урт: "))
        width = float(input("Тэгш өнцөгтийн өргөн: "))
        return round(length * width, 3)
    elif shape == "тойрог":
        radius = float(input("Тойргийн радиус: "))
        return round(math.pi * radius ** 2, 3)
    elif shape == "гурвалжин":
        base = float(input("Гурвалжны суурийн урт: "))
        height = float(input("Гурвалжны өндөр: "))
        return round(0.5 * base * height, 3)
    else:
        return "Буруу оролт. Зөвхөн квадрат, тэгш өнцөгт, тойрог, гурвалжин сонгоно уу."

# Хэрэглэгчээс оролт авах хэсэг
shape = input("Геометрийн дүрсийг оруулна уу (квадрат, тэгш өнцөгт, тойрог, гурвалжин): ").strip().lower()
area = calculate_area(shape)
print(f"{shape.capitalize()}-н талбай: {area}")
