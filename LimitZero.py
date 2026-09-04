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
def generar_funcion1():
    a = random.randint(-9,9)
    b = random.randint(-9,9)
    c = random.randint(-9,9)
    m = random.randint(1,9)
    n = random.randint(1,9)
    fun1 = f"{a}x^{m} + {b}x^{n} + {c}"
    return fun1

print(generar_funcion1())

def calcular_aciertos(aciertos):
    return aciertos/5
