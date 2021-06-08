import os
# Clase Padre
class Vehiculo:
  tanque = False
  parqueo = False
  aceleracion = 0
# Constructor1

  def __init__(self,modelo,motor, asientos, marca, puertas, combustible, placa):
    self.modelo=modelo
    self.motor=motor
    self.asientos=asientos
    self.marca=marca
    self.puertas=puertas
    self.combustible=combustible
    self.placa=placa
# Metodos
  def acelerar(self):
    aceleracion = float(input("           Introduce la velocidad :"))
    self.aceleracion = self.aceleracion + aceleracion
    print("\n              Acelerando a",self.aceleracion,"Km/h")
  def parquear(self):
    if self.parqueo==False:
      print("\n ***Parqueando Vehiculo***")
      self.parqueo=True
    else:
      print("\n        **El vehículo ya esta parqueado**")
  def gasolina(self):
    if self.tanque==False:
      print("\n          **LLenando Tanque**")
      self.tanque=True
    else:
      print("              *El tanque ya esta lleno*")
  def info(self):
     print("\n Modelo:",self.modelo,"\n Motor:",self.motor,"\n Asientos:",self.asientos,"\n Marca:",self.marca,"\n Puertas:",self.puertas,"\n Capacidad Tanque:",self.combustible,"\n Placa:",self.placa)

# Creacación de la clase Hijo para el Transporte Público

class bus(Vehiculo):
  pasajeros=0
  def subirpasajeros(self):
    pasajeros = int(input("\nCuantos pasajeros quiere ingresar :"))
    self.pasajeros = self.pasajeros + pasajeros
    print("              ***Subiendo***\n")
    print("El bus lleva ",self.pasajeros,"asientos ocupados\n")

# Creacación de la clase Hijo para el Carro Policial
class CarroPolicia(Vehiculo):
  sirena=False
  def sonarsirena(self):
    if self.sirena==False:
      print("\n          **Encendiendo Sirena**")
      self.sirena=True
    else:
      print("         *La Sirena ya esta encendida*")

#Creación dela clase Hijo para el Camión de Bomberos
class CamionBomberos(Vehiculo):
  escalera=False
  def sacarescalera(self):

    n1= int(input("""\nQue acción desea realizar?
          1-Bajar Escalera
          2-Subir Escalera\n"""))
    if n1==1 and self.escalera==False:
      print("\n           **Bajando Escalera**")
      self.escalera=True
    elif n1==1 and self.escalera==True:
      print("          *La escalera ya esta Abajo*")
    elif n1==2 and self.escalera==True:
      print("\n          ***Subiendo Escalera***")
      self.escalera=False
    elif n1==2 and self.escalera==False:
      print("          *La Escalera ya esta arriba*")
    else:
        print("Opción incorrecta")
        print("")
# Creación de los objetos
Carro = Vehiculo("Rio","V3",5,"Kia",4,"43 litros","979787A")
TransPublico=bus("All American","V16",56,"Blue Bird",5,"300 Litros","H6Q977J")
Bomberos=CamionBomberos(" FREIGHTLINER","460908U1037830",4,"FREIGHTLINER",5,"350 Litros","7667JA55")
Policia=CarroPolicia("HILUX","V6",5,"TOYOTA",4,"80 Litros","182791IJ")

print("""             *****Bienvenido*****\n     
      Tenemos Cuatro Vehículos Registrados
 """)
opcion = 0
# Condición para volver a presentar el menú
while True:
  # Menú Principal
    print("""

    ¿Que Vehículo deseas elegir?

    1) Carro 
    2) Transporte Publico 
    3) Vehículo Policial
    4) Camión de Bomberos 
    5)Salir
    """)
    
    opcion = int(input("Elige una opción: ") ) 
      
# Opciones del Menú del Carro
    if opcion == 1:
      os.system ("cls")  
      opcionc = 0
# Condición para volver a presentar el menú
      while True:
        # Menú
          print("""
                    ________Carro_______      
          
          ¿Que operación deseas realizar con el Carro?

          1) Acelerar 
          2) Parquear 
          3) Echar Gasolina
          4) Conocer Información del Vehiculo
          5)Cambiar Vehiculo
          """)
          
          opcionc = int(input("Elige una opción: ") )
              
      # Opciones del Menú
          if opcionc == 1:
              print("\n                  -Acelerar-")
              Carro.acelerar()
              input1 = input()
              os.system ("cls") 
          elif opcionc == 2:
              print("\n                           -Parquear-")     
              Carro.parquear()
              input1 = input()
              os.system ("cls") 
          elif opcionc == 3:
            print("\n                   -LLenar tanque-")
            Carro.gasolina()
            input1 = input()
            os.system ("cls") 
          elif opcionc == 4:
              print("\n               -Información-")
              Carro.info()
              input1 = input()
              os.system ("cls") 
          # Opcion para cerrar el menú
          elif opcionc == 5:
              os.system ("cls") 
              False 
              break
    # Condición para no permitir opciones incorrectas
          else:
            print("Opción incorrecta")
            print("")
# Opción Para Elegir el transporte publico
    elif opcion == 2:
        os.system ("cls") 
        opcionp = 0
# Condición para volver a presentar el menú
        while True:
          # Menú
            print("""
                       ________Bus_______  

            ¿Que operación deseas realizar con el Bus ?

            1) Acelerar 
            2) Parquear 
            3) Echar Gasolina
            4) Conocer Información del Vehiculo
            5)Subir Pasajeros
            6)Cambiar de Vehiculo
            """)
            
            opcionp = int(input("Elige una opción: ") )     
        # Opciones del Menú
            if opcionp == 1:
                print("\n                       -Acelerar-")
                TransPublico.acelerar()
                input1 = input()
                os.system ("cls") 
            elif opcionp == 2:
                print("\n                       -Parquear-")                
                TransPublico.parquear()
                input1 = input()
                os.system ("cls") 
            elif opcionp == 3:
              print("\n      -LLenar tanque-")
              TransPublico.gasolina()
              input1 = input()
              os.system ("cls") 
            elif opcionp == 4:
                print("\n                     -Información-")
                TransPublico.info()
                input1 = input()
                os.system ("cls") 
            elif opcionp == 5:
              print("\n                 -Subir Pasajeros-")
              TransPublico.subirpasajeros()
              input1 = input()
              os.system ("cls") 
            # Opcion para cerrar el menú
            elif opcionp == 6:
                os.system ("cls") 
                False 
                break
      # Condición para no permitir opciones incorrectas
            else:
              print("Opción incorrecta")
              print("")
# Opcion para Elegir el Vehículo Policial
    elif opcion == 3:
      os.system ("cls") 
      opcionp = 0
# Condición para volver a presentar el menú
      while True:
        # Menú
          print("""
                     ________Vehículo  Policial_______

          ¿Que operación deseas realizar con el Vehiculo Policial?

          1) Acelerar 
          2) Parquear 
          3) Echar Gasolina
          4) Conocer Información del Vehiculo
          5)Encender Sirena
          6)Cambiar Vehiculo
          """)
          
          opcionp = int(input("Elige una opción: ") )     
      # Opciones del Menú
          if opcionp == 1:
              print("\n             -Acelerar-")
              Policia.acelerar()
              input1 = input()
              os.system ("cls") 
          elif opcionp == 2: 
              print("\n                          -Parquear-")                
              Policia.parquear()
              input1 = input()
              os.system ("cls") 
          elif opcionp == 3:
            print("\n      -LLenar tanque-")
            Policia.gasolina()
            input1 = input()
            os.system ("cls") 
          elif opcionp == 4:
              print("\n      -Información-")
              Policia.info()
              input1 = input()
              os.system ("cls") 
          elif opcionp == 5:
              print("\n                 -Sirena-")
              Policia.sonarsirena()
              input1 = input()
              os.system ("cls") 
          # Opcion para cerrar el menú
          elif opcionp == 6:
              os.system ("cls") 
              False 
              break
    # Condición para no permitir opciones incorrectas
          else:
            print("Opción incorrecta")
            print("")
# Opcion para elegir 
    elif opcion == 4:
        os.system ("cls") 
        opcionc = 0
# Condición para volver a presentar el menú
        while True:
          # Menú
            print("""

                       ________Camion de Bomberos_______ 
                       
            ¿Que operación deseas realizar con el Camion de Bomberos?

            1) Acelerar 
            2) Parquear 
            3) Echar Gasolina
            4) Conocer Información del Vehiculo
            5)Mover Escalera
            6)Cambiar Vehiculo
            """)
            
            opcionc = int(input("Elige una opción: ") )     
        # Opciones del Menú
            if opcionc == 1:
                print("\n                        -Acelerar-")
                Bomberos.acelerar()
                input1 = input()
                os.system ("cls") 
            elif opcionc == 2:
                print("\n                        -Parquear-")                
                Bomberos.parquear()
                input1 = input()
                os.system ("cls") 
            elif opcionc == 3:
              print("\n                         -LLenar tanque-")
              Bomberos.gasolina()
              input1 = input()
              os.system ("cls") 
            elif opcionc == 4:
                print("\n                        -Información-")
                Bomberos.info()
                input1 = input()
                os.system ("cls") 
            elif opcionc == 5:
                print("\n                      -Mover Escalera-")
                Bomberos.sacarescalera()
                input1 = input()
                os.system ("cls") 
            # Opcion para cerrar el menú
            elif opcionc == 6:
                os.system ("cls") 
                False 
                break
      # Condición para no permitir opciones incorrectas
            else:
              print("Opción incorrecta")
              print("")
# Opcion para cerrar el menú principal
    elif opcion == 5:
      print("          Felíz día :)         ")
      input1 = input()
      False 
      break
      # Condición para no permitir opciones incorrectas
    else:
       print("Opción incorrecta")
       print("")







