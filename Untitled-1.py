n = float(input(""))
if n < 0: print("Сөрөг тоо оруулж болохгүй!"); exit()
b = 5 if n <= 100 else n * 0.2 if n <= 1000 else n * 0.1
b += 1 if n % 2 == 0 else 0
b += 2 if str(n).split('.')[0][-1] == '5' else 0
print(b)
print(n + b)
