a = int(input("Перше число: "))

b = int(input("Друге число: "))

c = input("\n1. Сума чисел\n2. Різниця чисел\n3. Середнє арифметичне\n4. Добуток чисел\nВибери дію від 1 до 4: ")

if c == "1":

   print(a + b)

elif c == "2":

   print(a - b)

elif c == "3":

   print((a + b) / 2)

elif c == "4":

   print(a * b)

else:

   print("Помилка")