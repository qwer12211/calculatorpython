import math
while True:
    print("�������� ��������:")
    print("1. ��������")
    print("2. ���������")
    print("3. ���������")
    print("4. �������")
    print("5. ���������� � �������")
    print("6. ���������� ������")
    print("7. ���������")
    print("8. �����")
    print("9. �������")
    print("10. �������")
    print("11. Exit")
    choice = input("������� ����� ��������: ")
    if choice == '11':
        print("�����.")
        break
    if choice in ('1', '2', '3', '4', '5'):
        a = float(input("������� ������ �����: "))
        b = float(input("������� ������ �����: "))
        if choice == '1':
            result = a + b
        elif choice == '2':
            result = a - b
        elif choice == '3':
            result = a * b
        elif choice == '4':
            if b == 0:
                print("������� �� 0 ����������.")
                continue
            result = a / b
        elif choice == '5':
            result = a ** b
    elif choice in ('6', '7', '8', '9', '10'):
        c = float(input("������� �����: "))
        if choice == '6':
            if c < 0:
                print("���������� ������ �������������� ����� �� ����� ����.")
                continue
            result = math.sqrt(c)
        elif choice == '7':
            if c < 0:
                print("��������� �������������� ����� �� ����� ����.")
                continue
            result = math.factorial(int(c))
        elif choice == '8':
            result = math.sin(c)
        elif choice == '9':
            result = math.cos(c)
        elif choice == '10':
            result = math.tan(c)
    else:
        print("�������� ����� ��������.")
        continue
    print(f"���������: {result}")
