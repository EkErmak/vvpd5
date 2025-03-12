from math import factorial, comb

def maclaurin_sin(x, iterations=10): #4 функция
    """
    Вычисляет значение синуса с использованием ряда Маклорена.

    :param x: Угол в радианах.
    :param iterations: Количество итераций для вычисления.
    :return: Значение синуса.
    :raises ValueError: Если количество итераций меньше 1.
    :example: maclaurin_sin(1.0, 10)
    """
    if iterations < 1:
        raise ValueError("Количество итераций должно быть больше 0.")
    
    result = 0
    for n in range(iterations):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
        result += term
    return result

def maclaurin_ln1_minus_x(x, iterations=10): #7 функция
    """
    Вычисляет значение ln(1-x) с использованием ряда Маклорена.

    :param x: Значение x.
    :param iterations: Количество итераций для вычисления.
    :return: Значение ln(1-x).
    :raises ValueError: Если x не в диапазоне (-1, 1].
    :example: maclaurin_ln1_minus_x(0.5, 10)
    """
    if not (-1 < x <= 1):
        raise ValueError("x должно быть в диапазоне (-1, 1].")
    
    result = 0
    for n in range(1, iterations + 1):
        term = (-1) ** (n + 1) * (x ** n) / n
        result += term
    return result

def maclaurin_power_series(x, m, iterations=10): #10 функция
    """
    Вычисляет значение (1-x)^m с использованием ряда Маклорена.

    :param x: Значение x.
    :param m: Параметр степени.
    :param iterations: Количество итераций для вычисления.
    :return: Значение (1-x)^m.
    :raises ValueError: Если x не в диапазоне (-1, 1).
    :example: maclaurin_power_series(0.5, 2, 10)
    """
    if not (-1 < x < 1):
        raise ValueError("x должно быть в диапазоне (-1, 1).")
    
    result = 0
    for n in range(iterations):
        term = ((-1) ** n) * (comb(m, n) * (x ** n)) / factorial(n)
        result += term
    return result

def maclaurin_cos(x, iterations=10): #5 функция
    """
    Вычисляет значение косинуса с использованием ряда Маклорена.

    :param x: Угол в радианах.
    :param iterations: Количество итераций для вычисления.
    :return: Значение косинуса.
    :raises ValueError: Если количество итераций меньше 1.
    :example: maclaurin_cos(1.0, 10)
    """
    if iterations < 1:
        raise ValueError("Количество итераций должно быть больше 0.")
    
    result = 0
    for n in range(iterations):
        term = ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
        result += term
    return result

def maclaurin_ln1_plus_x(x, iterations=10): #6 функция
    """
    Вычисляет значение ln(1+x) с использованием ряда Маклорена.

    :param x: Значение x.
    :param iterations: Количество итераций для вычисления.
    :return: Значение ln(1+x).
    :raises ValueError: Если x не в диапазоне (-1, 1].
    :example: maclaurin_ln1_plus_x(0.5, 10)
    """
    if not (-1 < x <= 1):
        raise ValueError("x должно быть в диапазоне (-1, 1].")
    
    result = 0
    for n in range(1, iterations + 1):
        term = (-1) ** (n + 1) * (x ** n) / n
        result += term
    return result

def maclaurin_power_series_plus(x, m, iterations=10): #9 функция
    """
    Вычисляет значение (1+x)^m с использованием ряда Маклорена.

    :param x: Значение x.
    :param m: Параметр степени.
    :param iterations: Количество итераций для вычисления.
    :return: Значение (1+x)^m.
    :raises ValueError: Если x не в диапазоне (-1, 1).
    :example: maclaurin_power_series_plus(0.5, 2, 10)
    """
    if not (-1 < x < 1):
        raise ValueError("x должно быть в диапазоне (-1, 1).")
    
    result = 0
    for n in range(iterations):
        term = (comb(m, n) * (x ** n))
        result += term
    return result

def main_menu(): #Меню
    while True:
        print("\nВыберите функцию:")
        print("1. sin(x) с использованием ряда Маклорена")
        print("2. ln(1-x) с использованием ряда Маклорена")
        print("3. (1-x)^m с использованием ряда Маклорена")
        print("4. cos(x) с использованием ряда Маклорена")
        print("5. ln(1+x) с использованием ряда Маклорена")
        print("6. (1+x)^m с использованием ряда Маклорена")
        print("7. Выход")

        choice = input("Введите номер функции: ")

        if choice == '7':
            break

        try:
            if choice in ['1', '4']:
                x = float(input("Введите x (в радианах): "))
                iterations = 10  #Константа для итераций
                if choice == '1':
                    result = maclaurin_sin(x, iterations)
                else:
                    result = maclaurin_cos(x, iterations)
                print(f"Результат: {result}")

            elif choice in ['2', '5']:
                x = float(input("Введите x: "))
                iterations = 10
                if choice == '2':
                    result = maclaurin_ln1_minus_x(x, iterations)
                else:
                    result = maclaurin_ln1_plus_x(x, iterations)
                print(f"Результат: {result}")

            elif choice in ['3', '6']:
                x = float(input("Введите x: "))
                m = float(input("Введите m: "))
                iterations = 10
                if choice == '3':
                    result = maclaurin_power_series(x, m, iterations)
                else:
                    result = maclaurin_power_series_plus(x, m, iterations)
                print(f"Результат: {result}")

            else:
                print("Некорректный выбор. Пожалуйста, попробуйте снова.")

        except ValueError as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main_menu()
