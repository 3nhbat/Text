def calculate_total_cost(pen_packs, marker_packs, detergent_liters, discount):
    pen_price = 5.80
    marker_price = 7.20
    detergent_price = 1.20
    
    total_cost = (pen_packs * pen_price) + (marker_packs * marker_price) + (detergent_liters * detergent_price)
    discounted_cost = total_cost - (total_cost * discount / 100)
    
    return round(discounted_cost, 2)

pen_packs = int(input("Үзэгний багцын тоо: "))
marker_packs = int(input("Маркерын багцын тоо: "))
detergent_liters = float(input("Угаалгын нунтаг (литр): "))
discount = float(input("Хөнгөлөлтийн хувь: "))

total_amount = calculate_total_cost(pen_packs, marker_packs, detergent_liters, discount)
print(f"Софи нийт {total_amount} ам.доллар цуглуулах хэрэгтэй.")
