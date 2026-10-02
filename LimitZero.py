import math
import random


# variable para guardar aciertos
aciertos = 0

# variable de dificultad
dificultad = int(input("¿Qué grado de dificultad quieres practicar? (1-4)"))

if 1 > dificultad > 4:
    print("Grado de dificultad fuera del rango")

# definir el template de las funciones

def select_trig():

    trig_num = random.randint(1, 6)
    """
    (uso de estrucutras de decisión, uso de funciones)
    devuelve: funcion trigonometrica
    """
    if trig_num == 1:
        trig = "sin"
    elif trig_num == 2:
        trig = "cos"
    elif trig_num == 3:
        trig = "tan"
    elif trig_num == 4:
        trig = "cot"
    elif trig_num == 5:
        trig = "sec"
    elif trig_num == 6:
        trig = "csc"
    return trig


def generar_funcion_polinomial():
    a = random.randint(-9, 9)
    b = random.randint(-9, 9)
    c = random.randint(-9, 9)
    m = random.randint(1, 9)
    n = random.randint(1, 9)
    fun1 = f"{a}x^{m} + {b}x^{n} + {c}"
    return fun1


def generar_funcion_producto():
    a = random.randint(-9, 9)
    b = random.randint(-9, 9)
    c = random.randint(-9, 9)
    m = random.randint(1, 9)
    n = random.randint(1, 9)
    fun2 = f"({a}x^{m}) * ({b}x^{n})"
    return fun2


def generar_funcion_cociente():
    a = random.randint(-9, 9)
    b = random.randint(-9, 9)
    c = random.randint(-9, 9)
    m = random.randint(1, 9)
    n = random.randint(1, 9)
    fun3 = f"({a}x^{m}) / ({b}x^{n})"
    return fun3


def generar_funcion_trig1():
    a = random.randint(-9, 9)
    c = random.randint(-9, 9)
    trig = select_trig()
    fun4 = f"{a}{trig}(x) + {c}"
    return fun4


def generar_funcion_trig2():
    a = random.randint(-9, 9)
    b = random.randint(-9, 9)
    c = random.randint(-9, 9)
    m = random.randint(1, 9)
    n = random.randint(1, 9)
    trig = select_trig()
    fun5 = f"{a}{trig}(x^{m} + {b}x^{n}) + {c}"
    return fun5



def calcular_aciertos(num_aciertos):
    return num_aciertos / 5


def seleccionar_pool(nivel_dificultad):
    """
    (uso de estrucutras de decisión, uso de funciones)
    devuelve: funcion trigonometrica
    """
    if nivel_dificultad == 1:
        fun1 = generar_funcion_polinomial()
        fun2 = generar_funcion_polinomial()
    elif nivel_dificultad == 2:
        fun1 = generar_funcion_cociente()
        fun2 = generar_funcion_producto()
    elif nivel_dificultad == 3:
        fun1 = generar_funcion_trig1()
        fun2 = generar_funcion_trig2()
    return fun1, fun2   


fun1, fun2 = seleccionar_pool(dificultad)

print(fun1)
print(fun2)
