# Librería Math
import math

# Funciones de operaciones Basicas
def suma(Num1,Num2):
  return Num1+Num2

def resta(Num1,Num2):
  return Num1-Num2

def multiplicacion(Num1,Num2):
  return round(Num1*Num2,2)

def division(Num1,Num2):
  return round(Num1/Num2,2)

def modulo(Num1,Num2):
  return Num1%Num2
# Operaciones con funciones de la librería Math
def potencia(Num1,Num2):
  return round(math.pow(Num1,Num2),2)

def raiz(Num1):
  return round(math.sqrt(Num1),2)
# Función recursiva para el opreación de un número factorial
def factorial(Num1):
    if Num1 == 0:
        r = 1
    else:
        r = Num1 * factorial(Num1 - 1)
    return r
