def sum_numbers(a, b):
    result = a + b
    return result


def multiply_numbers(a, b):
    result = a * b
    return result


def calc_square_area(side_length):
    area = side_length ** 2
    return area


def isPrime(number):
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

    print(isPrime(17))