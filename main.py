import parametros as p
import random

# NO MODIFICAR
class Rueda:
    def __init__(self):
        self.resistencia_actual = random.randint(*p.RESISTENCIA)
        self.resistencia_total = self.resistencia_actual
        self.estado = "Perfecto"

    def gastar(self, accion):
        if accion == "acelerar":
            self.resistencia_actual -= 5
        elif accion == "frenar":
            self.resistencia_actual -= 10
        self.actualizar_estado()

    def actualizar_estado(self):
        if self.resistencia_actual < 0:
            self.estado = "Rota"
        elif self.resistencia_actual < self.resistencia_total / 2:
            self.estado = "Gastada"
        elif self.resistencia_actual < self.resistencia_total:
            self.estado = "Usada"


# NO MODIFICAR
def seleccionar(vehiculos):
    for indice in range(len(vehiculos)):
        print(f"[{indice}] {str(vehiculos[indice])}")

    elegido = int(input())
    while elegido < 0 or elegido >= len(vehiculos):
        print("intentelo de nuevo.")
        elegido = int(input())

    vehiculo = vehiculos[elegido]
    print("Se seleccionó el vehículo", str(vehiculo))
    return vehiculo


# Parte 1: Definición de clases

class Automovil:
    def __init__(self, a, kilometraje,velocidad):
        self.ano = a
        self.rueda = list()
        self.aceleracion = 0
        self.velocidad = 0
        self.__kilometraje = kilometraje

    def avanzar(self, tiempo:int):
        self.tiempo = int(input("tiempo en seg"))
        self.__kilometraje = self.velocidad*self.tiempo
        
    def acelerar(self, tiempo):
        #Recibe como argumento un int que corresponde al tiempo 
        #expresado en segundos. Primero agrega tiempo*0.5 al 
        #atributo aceleración. 
        self.aceleracion = self.tiempo*0.5 
        self.velocidad += self.aceleracion * self.tiempo * 3,6
        self.avanzar(tiempo)
        self.aceleracion = 0

    def frenar(self, tiempo:int):
        self.aceleracion -= self.tiempo * 0,5
        self.velocidad -= self.aceleracion * self.tiempo * 3,6
        if self.velocidad < 0:
            self.velocidad = 0
        else:
            pass
        self.avanzar(tiempo)
        aceleracin = 0


    def  obtener_kilometraje(self):
        return self.__kilometraje
        

    def  reemplazar_rueda(self):
        minimo = float("inf")
            

class Moto(Rueda, Automovil): 
    def __init__(self,a, kilometraje, velocidad, cilindrada):
        super().__init__(a, kilometraje,velocidad)
        self.cilindrada = cilindrada
        
    def acelerar(self):
        self.tiempo = int(input("Tiempo en Seg"))
        self.aceleracion()
        self.gastar()
    
    def frenar(self):
        self.tiempo = int(input("Tiempo en segundos\n:"))
        self.frenar()
        for frenado in self.rueda:
            frenado = self.gastar("frenar")

    def __str__(self):
        self.cilindrada = cilindrada
        return f"Moto del año {self.ano}."


class Camion(Rueda, Automovil):
    def __init__(self, a, kilometraje, velocidad, carga):
        super().__init__(a, kilometraje,velocidad)
        self.carga = carga

    def acelerar(self, tiempo):
        super().acelerar(tiempo)
        super().gastar("acelerar")

    def frenar(self, tiempo):
        super().frenar(tiempo)
        super().gastar("frenar")



    def __str__(self):
        return f"Camión del año {self.ano}."


# Parte 2: Completar acciones

def accion(vehiculo, opcion):
    # Completar
    if opcion == 2:  # Acelerar
        tiempo = int(input("ingresa el tiempo de aceleracion"))
        Automovil.acelerar(tiempo)
        print(f"se a acelerado por {tiempo} seg llegando a una velocidad de {Automovil.velocidad}")

    elif opcion == 3:  # Frenar
        tiempo = int(input("Escoja el tiempo de frenado\n:"))
        Automovil.acelerar(tiempo)
        print(f"Se ha frenado por {tiempo} segundos, llegando a una velocidad de {Automovil.velocidad} km/h")
    elif opcion == 4:  # Avanzar
        tiempo = int(input("Escoja el tiempo a avanzar\n:"))
        Automovil.avanzar(tiempo)
        print(f"Se ha avanzado por {tiempo} segundos a una velocidad de {Automovil.velocidad}km/h")

    elif opcion == 5:  # Cambiar rueda
        Automovil.reemplazar_rueda()
        print("Se ha reemplazado una rueda con éxito")
    elif opcion == 6:  # Mostrar Estado
        print({self.ano},{self.velocidad},{self.__kilometraje} )


def main():
    vehiculos = []

    # Parte 3: Completar código principal
    # Completar


    # NO MODIFICAR
    vehiculo = vehiculos[0]

    dict_opciones = {
        1: ("Seleccionar Vehiculo", seleccionar),
        2: ("Acelerar", accion),
        3: ("Frenar", accion),
        4: ("Avanzar", accion),
        5: ("Reemplazar Rueda", accion),
        6: ("Mostrar Estado", accion),
        0: ("Salir", None)
                    }

    opcion = -1
    while opcion != 0:

        for llave, valor in dict_opciones.items():
            print(f"{llave}: {valor[0]}")

        try:
            opcion = int(input("Opción: "))

        except ValueError:
            print("Ingrese opción válida.")
            opcion = -1

        if opcion != 0 and opcion in dict_opciones.keys():
            if opcion == 1:
                vehiculo = dict_opciones[opcion][1](vehiculos)
            else:
                dict_opciones[opcion][1](vehiculo, opcion)
        elif opcion == 0:
            pass
        else:
            print("Ingrese opción válida.")
            opcion = -1


if __name__ == "__main__":
    main()