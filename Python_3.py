
meters = int(input("Введіть кількість метрів: "))

what = int(input("В що конвертувати метри? \n1. Милі \n2. Дюйми\n3. Ярда \nВиберіть варіант: "))
if what == 1:
   print(f"{meters} метрів = {meters*0.000621} миль")
elif what == 2:
   print(f"{meters} метрів = {meters*39.37} дюймів")
elif what == 3:
    print(f"{meters} метрів = {meters*1.093613} ярдів")