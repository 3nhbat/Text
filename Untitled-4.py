import math
shape = input("Дүрсийн төрлийг оруулна уу (квадрат, тэгш өнцөгт, тойрог, гурвалжин): ").lower()
try:
    if shape == "квадрат":
        side = float(input("Талын урт: "))
        if side < 0:
            print("Талын урт тэгээс бага байж болохгүй!")
        else:
            area = side * side
            print(f"Квадратын талбай: {area:.3f}")
    elif shape == "тэгш өнцөгт":
        length = float(input("Урт: "))
        width = float(input("Өргөн: "))
        if length < 0 or width < 0:
            print("Урт болон өргөн тэгээс бага байж болохгүй!")
        else:
            area = length * width
            print(f"Тэгш өнцөгтийн талбай: {area:.3f}")
    elif shape == "тойрог":
        radius = float(input("Радиус: "))
        if radius < 0:
            print("Радиус тэгээс бага байж болохгүй!")
        else:
            area = math.pi * radius * radius
            print(f"Тойргийн талбай: {area:.3f}")
    elif shape == "гурвалжин":
        base = float(input("Хажуугийн урт: "))
        height = float(input("Өндөр: "))
        if base < 0 or height < 0:
            print("Хажуугийн урт болон өндөр тэгээс бага байж болохгүй!")
        else:
            area = (base * height) / 2
            print(f"Гурвалжны талбай: {area:.3f}")
    else:
        print("Зөв дүрсийн төрлийг оруулна уу: квадрат, тэгш өнцөгт, тойрог, гурвалжин")
except ValueError:
    print("Зөвхөн тоо оруулна уу!")
