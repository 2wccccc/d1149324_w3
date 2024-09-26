import math
a = int(input("輸入係數 a: "))
b = int(input("輸入係數 b: "))
c = int(input("輸入係數 c: "))
D = b**2 - 4*a*c
x1 = (-b + math.sqrt(D)) / (2*a)
x2 = (-b - math.sqrt(D)) / (2*a)

print(f"方程式的根為:x1 = {x1}, x2 = {x2}")