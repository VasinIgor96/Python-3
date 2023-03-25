
a = int(input("Введіть перше число:"))
b = int(input("Введіть друге число:"))
c = int(input("Введіть третє число:"))
act = int(input("\n Виберіть дію:\n Сума чисел виберіть - 1\n Добуток чисел виберіть - 2\n Введіть 1 або 2: "))
if act == 1:
    print(a+b+c)
elif act == 2:
    print(a*b*c)
else:
    print("Помилка")