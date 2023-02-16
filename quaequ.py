# start

import numpy


def quaequ():
    print("Input A:")
    a = int(input())
    print("Input B:")
    b = int(input())
    print("Input C:")
    c = int(input())

    # let Numpy = x1 +- x2
    delta = (b ** 2 - 4 * a * c)

    x1 = (-b + numpy.sqrt(delta)) / (2 * a)
    x2 = (-b - numpy.sqrt(delta)) / (2 * a)

    print("X1 is ", x1)
    print("X2 is ", x2)


print("start")
quaequ()
