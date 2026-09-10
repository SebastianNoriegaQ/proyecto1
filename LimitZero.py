import math
import random

# definir las variables para las funciones
# coeficientes

a = 1 
b = 1 
c = 1
d = 1
# exponentes
m = 1 
n = 1 
p = 1 
q = 1

# funciones
fun1 = ""
fun2 = ""
fun3 = ""
fun4 = ""
fun5 = ""

#variable para guardar aciertos
aciertos = 0

# definir el template de las funciones

def select_trig():
    trig_num = random.randint(1,6)
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

def generar_funcion1():
    a = random.randint(-9,9)
    b = random.randint(-9,9)
    c = random.randint(-9,9)
    m = random.randint(1,9)
    n = random.randint(1,9)
    fun1 = f"{a}x^{m} + {b}x^{n} + {c}"
    return fun1

def generar_funcion2():
    a = random.randint(-9,9)
    b = random.randint(-9,9)
    c = random.randint(-9,9)
    m = random.randint(1,9)
    n = random.randint(1,9)
    fun2 = f"({a}x^{m}) * ({b}x^{n})"
    return fun2

def generar_funcion3():
    a = random.randint(-9,9)
    b = random.randint(-9,9)
    c = random.randint(-9,9)
    m = random.randint(1,9)
    n = random.randint(1,9)
    fun3 = f"({a}x^{m}) / ({b}x^{n})"
    return fun3 


def generar_funcion4():
    a = random.randint(-9,9)
    trig = select_trig()
    fun4 = f"{a}{trig}(x) + {c}"
    return fun4

def generar_funcion5():
    a = random.randint(-9,9)
    b = random.randint(-9,9)
    c = random.randint(-9,9)
    m = random.randint(1,9)
    n = random.randint(1,9)
    trig = select_trig()
    fun5 = f"{a}{trig}(x^{m} + {b}x^{n}) + {c}"
    return fun5



def calcular_aciertos(aciertos):
    return aciertos/5

def imprimir_funciones():
    print(generar_funcion1())
    print(generar_funcion2())
    print(generar_funcion3())
    print(generar_funcion4())
    print(generar_funcion5())

imprimir_funciones()
