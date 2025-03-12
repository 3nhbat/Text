def format_time(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes}:{remaining_seconds:02d}"

first = int(input("Эхний тамирчны секунд: "))
second = int(input("Хоёр дахь тамирчны секунд: "))
third = int(input("Гурав дахь тамирчны секунд: "))

total_seconds = first + second + third
formatted_time = format_time(total_seconds)

print(f"Нийт хугацаа: {formatted_time}")