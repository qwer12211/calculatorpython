import math
while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("11. Выход")
    choice = input("Введите номер операции: ")
    if choice == '11':
        print("Остановка программы.")
        break
    if choice in ('1', '2', '3', '4', '5'):
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        if choice == '1':
            result = a + b
        elif choice == '2':
            result = a - b
        elif choice == '3':
            result = a * b
        elif choice == '4':
            if b == 0:
                print("Деление на 0 невозможно.")
                continue
            result = a / b
        elif choice == '5':
            result = a ** b
    elif choice in ('6', '7', '8', '9', '10'):
        c = float(input("Введите число: "))
        if choice == '6':
            if c < 0:
                print("Квадратный корень отрицательного числа не может быть.")
                continue
            result = math.sqrt(c)
        elif choice == '7':
            if c < 0:
                print("Факториал отрицательного числа не можнт быть.")
                continue
            result = math.factorial(int(c))
        elif choice == '8':
            result = math.sin(c)
        elif choice == '9':
            result = math.cos(c)
        elif choice == '10':
            result = math.tan(c)
    else:
        print("Неверный выбор операции.")
        continue
    print(f"Результат: {result}")
