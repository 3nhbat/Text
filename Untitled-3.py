try:
    pens = float(input("Үзэгний багцын тоо: "))
    markers = float(input("Маркерын багцын тоо: "))
    detergent = float(input("Угаалгын нунтаг (литрээр): "))
    
    if pens < 0 or markers < 0 or detergent < 0:
        print("Тоо хэмжээ тэгээс бага байж болохгүй!")
    else:

        pen_price = 5.80  
        marker_price = 7.20  
        detergent_price = 1.20  
        
        total_pens = pens * pen_price
        total_markers = markers * marker_price
        total_detergent = detergent * detergent_price
    
        total_cost = total_pens + total_markers + total_detergent
        
        print(f"\nҮзэгний нийт үнэ: {total_pens:.2f} ам.доллар")
        print(f"Маркерын нийт үнэ: {total_markers:.2f} ам.доллар")
        print(f"Угаалгын нунтагны нийт үнэ: {total_detergent:.2f} ам.доллар")
        print(f"Нийт төлбөр: {total_cost:.2f} ам.доллар")
        
except ValueError:
    print("Дахин оруулна уу!")
