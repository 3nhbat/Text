a = int(input()) 
b = int(input()) 
c = int(input()) 
niit = a + b + c
minut = niit // 60
second = niit % 60
print(f"{minut:02}:{second:02}")
