
import Funciones
import os
# Titulo
print("***     Bienvenido a la Calculadora    ***")
opcion = 0
# Condición para volver a presentar el menú
while True:
  # Menú
    print("""
    ¿Que operación deseas realizar?

    1) Suma de dos números
    2) Resta de dos números
    3) Multiplicación de dos números
    4) División
    5)Modulo
    6)Potencia de un número
    7)Raíz Cuadrada
    8)Factorial de un número
    9)Apagar calculadora
    """)
    opcion = int(input("Elige una opción: ") )     
# Opciones de la Calculadora
    if opcion == 1:
        print("\n             -Suma-")
        n1 = float(input("Introduce el primer número a sumar: ") )
        n2 = float(input("Introduce el segundo número a sumar: ") )
        print("\nEl resultado de la suma es: ", Funciones.suma(n1,n2))
        input1 = input()
        os.system ("cls")
    elif opcion == 2:
        print("\n           -Resta-")
        n1 = float(input("Introduce el primer número :") )
        n2 = float(input("Introduce el número a restar: ") )
        print("\nEl resultado de la resta es: ", Funciones.resta(n1,n2))
        input1 = input()
        os.system ("cls")
    elif opcion == 3:
        print("\n             -Multiplicación-")
        n1 = float(input("Introduce el primer número a multiplicar:") )
        n2 = float(input("Introduce el segundo número a multiplicar:") )
        print("\nEl resultado de la multiplicación es : ", Funciones.multiplicacion(n1,n2))
        input1 = input()
        os.system ("cls")
    elif opcion == 4:
        print("\n      -División-")
        n1 = float(input("Introduce el dividendo: ") )
        n2 = float(input("Introduce el divisor: ") )
        while n2==0:
          n2 = float(input("Introduce un número diferente de 0: ") )
        print("\nEl resultado de la división es: ", Funciones.division(n1,n2))
        input1 = input()
        os.system ("cls")
    elif opcion == 5:
        print("\n       -Módulo-")
        n1 = float(input("Introduce el dividendo: ") )
        n2 = float(input("Introduce el divisor: ") )
        while n2==0:
          n2 = float(input("Introduce un número diferente de 0: ") )
        print("\nEl resultado del módulo es: ", Funciones.modulo(n1,n2))
        input1 = input()
        os.system ("cls")
    elif opcion == 6:
        print("\n       -Potencia-")
        n1 = float(input("Introduce el número base: ") )
        n2 = float(input("Introduce el número de la potencia: ") )
        print("\nEl resultado de la potencia es: ", Funciones.potencia(n1,n2))
        input1 = input()
        os.system ("cls")
    elif opcion == 7:
        print("\n   -Raíz Cuadrada-")
        n1 = float(input("Introduce el número : ") )
        print("\nEl resultado de la raíz es: ", Funciones.raiz(n1))
        input1 = input()
        os.system ("cls")
    elif opcion == 8:
      print("\n      -Factorial-")
      n1 = float(input("Introduce tu número: ") )
      print("\nEl resultado del factorial es: ", Funciones.factorial(n1))
      input1 = input()
      os.system ("cls")
    # Opcion para cerrar la calculadora
    elif opcion == 9:
        print("\n Gracias por usar la calculadora")
        print("          Felíz día :)         ")
        input1 = input()
        os.system ("cls")
        False
        break
    # Condición para no permitir opciones incorrectas
    else:
        print("Opción incorrecta")
        print("")


 