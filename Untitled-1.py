def calculate_bonus_points(points):
    # Үндсэн урамшууллын оноо тооцоолох
    if points <= 100:
        bonus = 5
    elif points <= 1000:
        bonus = points * 0.2
    else:
        bonus = points * 0.1
    
    extra_bonus = 0
    if points % 2 == 0:
        extra_bonus += 1
    if points % 10 == 5:
        extra_bonus += 2
    
    total_bonus = bonus + extra_bonus
    total_points = points + total_bonus
    
    return int(bonus), int(total_bonus), int(total_points)

points = int(input("Оноог оруулна уу: "))
bonus, total_bonus, total_points = calculate_bonus_points(points)

print(f"Урамшууллын оноо: {bonus}")
print(f"Нэмэлт урамшуулал: {total_bonus - bonus}")
print(f"Нийт оноо: {total_points}")
