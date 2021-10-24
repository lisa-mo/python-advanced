# def is_int(str):
#     try:
#         int(str)
#         return True
#     except ValueError:
#         return False
# a = '-123'
# print(is_int(a))
# print(a)
import math


def enter_coefficients():
    while True:
        try:
            a1, a2, b1, b2, c1, c2 = input("Please enter coefficients for the equation 'ax^2 + bx + c = 0'. "
                                           "They have to be integers and be split by commas.").split(',')
            return int(a1), int(a2), int(b1), int(b2), int(c1), int(c2)
        except ValueError as e:
            pass


def discriminant_calculation(a, b, c):
    return b ** 2 - 4 * a * c


def root_check(a1, a2, b1, b2, c1, c2):
    for a in range(a1, a2+1):
        for b in range(b1, b2+1):
            for c in range(c1, c2+1):
                temp_discriminant = discriminant_calculation(a, b, c)
                if a == 0:
                    continue
                elif temp_discriminant > 0:
                    x1 = round((-b + math.sqrt(temp_discriminant)) / (2 * a), 2)
                    x2 = round((-b - math.sqrt(temp_discriminant)) / (2 * a), 2)
                    print(f'a = {a} b = {b} c = {c} D = {temp_discriminant} x1 = {x1} x2 = {x2}')
                elif temp_discriminant == 0:
                    x = -b / (2 * a), 2
                    print(f'a = {a} b = {b} c = {c} D = {temp_discriminant} x = {x}')
                else:
                    continue
    else:
        print("There is no valid example with the roots")


root_check(*enter_coefficients())
