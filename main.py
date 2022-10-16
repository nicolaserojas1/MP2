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
        self.rueda = []
        self.aceleracion = 0
        self.velocidad = 0
        self.__kilometros = kilometraje

    def avanzar(self, tiempo):
        tiempo = int(input("tiempo en seg"))
        self.kilometraje += velocidad*tiempo
        

    def aceleracion(self):
        tiempo_aceleracion = int(input("tiempo aceleracion en segundos"))
        avanzar()

    def frenar(self):
        pass

    def  obtener_kilometraje():
        pass

    def  reemplazar_rueda():
        pass
    

class Moto: 

    # Completar
    pass

    def __str__(self):
        return f"Moto del año {self.ano}."


class Camion:
    # Completar
    pass

    def __str__(self):
        return f"Camión del año {self.ano}."


# Parte 2: Completar acciones

def accion(vehiculo, opcion):
    # Completar
    if opcion == 2:  # Acelerar
        pass
    elif opcion == 3:  # Frenar
        pass
    elif opcion == 4:  # Avanzar
        pass
    elif opcion == 5:  # Cambiar rueda
        pass
    elif opcion == 6:  # Mostrar Estado
        pass


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