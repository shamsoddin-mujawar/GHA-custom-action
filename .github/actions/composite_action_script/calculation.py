import os


def addition(num1: int, num2: int) -> int:
    return num1 + num2


def substraction(num1: int, num2: int) -> int:
    return num1 - num2


def multiplication(num1: int, num2: int) -> int:
    return num1 * num2


def divi(num1: int, num2: int) -> float:
    return num1 // num2


def main():

    num1 = int(os.getenv('A', 0))
    num2 = int(os.getenv('B', 0))
    add = addition(num1, num2)
    sub = substraction(num1, num2)
    mul = multiplication(num1, num2)
    div = divi(num1, num2)
    with open(os.getenv("GITHUB_OUTPUT"), 'a') as fp:
        fp.write("addition={}\n".format(add))
        fp.write("subtract={}\n".format(sub))
        fp.write("multiply={}\n".format(mul))
        fp.write("division={}\n".format(div))


if __name__ == '__main__':
    exit(main())
