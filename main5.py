def maclaurin_sin(x, iterations=10):
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

def maclaurin_ln1_minus_x(x, iterations=10):
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

def maclaurin_power_series(x, m, iterations=10):
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
