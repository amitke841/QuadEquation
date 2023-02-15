#start

import numpy as np
import turtle
import matplotlib.pyplot as plt
import colorama
from colorama import Fore

def quaequ():
    global x1,x2
    delta = (b**2-4*a*c)

    x1 = (-b+np.sqrt(delta))/(2*a)
    x2 = (-b-np.sqrt(delta))/(2*a)
    
    print(Fore.RED + "Quadratic Equation Results:")
    print("X1 is ",x1)
    print("X2 is ",x2)

def Posneg():
    global mm
    if a > 0:
        #postive Number
        mm = "min"
        print(Fore.YELLOW + "Parabula is Postive")
    elif a == 0:
        #zero
        mm = "0"
    else:
        #negative number
        mm = "max"
        print(Fore.YELLOW + "Parabula is Negative")

def Findkod():
    global Xkod
    global Ykod
    Xkod = (-b)/(2*a)
    #print("X KodKod is ", Xkod)
    Ykod = a* Xkod**2 + b*Xkod + c
    #print("Y KodKod is ", Ykod)

def Tzir():
    global Xkod
    print("Tzir X =", Xkod)

def Nekudot():
    global Ypoint
    Ypoint = c
    quaequ()
    Points = "(" + str(x1) + ",0), (" + str(x2) + ",0), (0," + str(Ypoint) + ")"
    print(Fore.YELLOW + Points)

def Graph():
    plt.style.use('_mpl-gallery')
    x  = np.linspace(-50,50,100)
    y = a*(x**2)+b*x+c
    plt.plot(x,y)
    plt.show()
    #plt.axis('equal')


print(Fore.GREEN + "start")


a = int(input(Fore.WHITE + "Input A:"))
b = int(input("Input B:"))
c = int(input("Input C:"))

Posneg()
Findkod()
KodKod = Xkod, Ykod
print(mm + str(KodKod))
Tzir()
Nekudot()
Graph()
#s = turtle.getscreen()