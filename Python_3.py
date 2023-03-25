
a = int(input("Введіть перше число:"))
b = int(input("Введіть друге число:"))
c = int(input("Введіть третє число:"))
act = int(input("\n Виберіть дію:\n 1. Максимум із трьох\n 2. Мінімум із трьох\n 3. Середнє арефметичне\n Введіть один з варіантів: "))

if act == 1:
    if a>b and a>c:
        print(int(a))
    elif b>a and b>c:
        print(int(b))
    elif c>a and c>b:
        print(int(c))
    else:
        print("Помилка")
elif act == 2:
    if a<b and a<c:
        print(int(a))
    elif b<a and b<c:
        print(int(b))
    elif c<a and c<b:
        print(int(c))
    else:
        print("Помилка")
elif act == 3:
    print(float((a+b+c)/3))
else:
    print("Помилка")