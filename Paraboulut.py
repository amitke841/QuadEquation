# start

import numpy as np
import turtle
import matplotlib.pyplot as plt
import colorama
from colorama import Fore

def quad_equation(a, b, c):
    delta = (b ** 2 - 4 * a * c)
    x1 = (-b + np.sqrt(delta)) / (2 * a)
    x2 = (-b - np.sqrt(delta)) / (2 * a)
    return x1, x2


def pos_neg(a):
    mm = ""
    if a > 0:
        # postive number
        mm = "min"
        print(Fore.YELLOW + "Parabula is Postive")
    elif a == 0:
        # zero
        exit("Error: the input A cannot be 0.")
    else:
        # negative number
        mm = "max"
        print(Fore.YELLOW + "Parabula is Negative")
    return mm


def find_kodkod(a, b, c):
    x_kod = (-b) / (2 * a)
    # print("X KodKod is ", Xkod)
    y_kod = a * x_kod ** 2 + b * x_kod + c
    # print("Y KodKod is ", Ykod)
    return x_kod, y_kod


if __name__ == '__main__':

        # get input from user
    print(Fore.GREEN + "start")
    A = int(input(Fore.WHITE + "Input A:"))
    B = int(input("Input B:"))
    C = int(input("Input C:"))

    min_max = pos_neg(A)
    kodkod = find_kodkod(A, B, C)
    x1, x2 = quad_equation(A, B, C)

    print(min_max + str(kodkod))
    (x_kod, y_kod) = kodkod
    print("Tzir X =", x_kod)
    Points = "(" + str(x1) + ",0), (" + str(x2) + ",0), (0," + str(C) + ")"
    print(Fore.YELLOW + Points)
    print(Fore.RED + "Quadratic Equation Results:")
    print("X1 is ", x1)
    print("X2 is ", x2)

    plt.style.use('_mpl-gallery')
    x = np.linspace(-2 + min(x1, x2), 2 + max(x1, x2), 100)
    y_axis = x * 0
    y = A * (x ** 2) + B * x + C
    x_axis = y * 0
    plt.figure(figsize=(10, 6))
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.plot(x, y_axis, color="k")
    plt.plot(x_axis, y, color="k")
    plt.plot(x_kod*np.ones(100), y, color="gray", linestyle = "--")
    plt.plot(x, y, color="r")
    plt.plot(x1, 0.0, marker="o", markerfacecolor="green", markersize=10, markeredgecolor="red")
    plt.plot(x2, 0.0, marker="o", markerfacecolor="green", markersize=10, markeredgecolor="red")
    plt.plot(0, C, marker="o", markerfacecolor="green", markersize=10, markeredgecolor="red")
    plt.plot(x_kod, y_kod, marker="o", markerfacecolor="blue", markersize=10, markeredgecolor="red")
    plt.show()