def sum_numbers(a: int, b: int) -> int:
    """
    Суммирование двух чисел.
    :param a: 1 число.
    :param b: 2 число.
    """
    result = a + b
    return result


def multiply_numbers(a: int, b: int) -> int:
    """
    Умножение двух чисел.
    :param a: 1 число.
    :param b: 2 число.
    """
    result = a * b
    return result


def calc_square_area(side_length: int) -> int:
    """
    Вычисление площади квадрата.
    :param side_length: Длина стороны квадрата.
    """
    area = side_length ** 2
    return area


def is_prime(number: int) -> bool:
    """
    Проверка числа на простоту.
    :param number: Число.
    """
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    number1 = 5
    number2 = 10
    sum_result = sum_numbers(number1, number2)
    print("Sum result:", sum_result)

    multiply_result = multiply_numbers(number1, number2)
    print("Multiply result:", multiply_result)

    side_length = 4
    square_area = calc_square_area(side_length)
    print("Square area:", square_area)

    print(is_prime(17))