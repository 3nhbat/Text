try:
    time1 = int(input("Эхний тамирчны цаг (1-50 секунд): "))
    time2 = int(input("Хоёр дахь тамирчны цаг (1-50 секунд): "))
    time3 = int(input("Гурав дахь тамирчны цаг (1-50 секунд): "))
    if not (1 <= time1 <= 50 and 1 <= time2 <= 50 and 1 <= time3 <= 50):
        print("Цагууд 1-ээс 50 секундын хооронд байх ёстой!")
    else:
        total_seconds = time1 + time2 + time3
        minutes = total_seconds // 60
        seconds = total_seconds % 60х
        seconds_str = f"{seconds:02d}"
        print(f"{minutes}:{seconds_str}")
except ValueError:
    print("Зөвхөн бүхэл тоо оруулна уу!")
