try:

    initial_score = int(input("Эхлэлийн оноог оруулна уу: "))
    
    if initial_score < 0:
        print("Оноо тэгээс бага байж болохгүй!")
    else:
        if initial_score <= 100:
            bonus = 5
        elif initial_score <= 1000:
            bonus = initial_score * 0.20 
        else:
            bonus = initial_score * 0.10  
        extra_bonus = 0

        if initial_score % 2 == 0:
            extra_bonus += 1

        if str(initial_score)[-1] == '5':
            extra_bonus += 2

        total_bonus = bonus + extra_bonus
        total_score = initial_score + total_bonus

        print(f"\nЭхлэлийн оноо: {initial_score}")
        print(f"Үндсэн урамшууллын оноо: {bonus}")
        print(f"Нэмэлт урамшууллын оноо: {extra_bonus}")
        print(f"Нийт урамшууллын оноо: {total_bonus}")
        print(f"Нийт оноо: {total_score}")

except ValueError:
    print("Зөвхөн бүхэл тоо оруулна уу!")
