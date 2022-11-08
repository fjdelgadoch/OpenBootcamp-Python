from pickle import *

class Vehiculo:

    def __init__(self, color, puertas, ruedas):
        self.color = color
        self.puertas = puertas
        self.ruedas = ruedas

    def __str__(self):
        return f"Color: {self.color}\nPuertas: {self.puertas}\nRuedas: {self.ruedas}"

coche = Vehiculo("Rojo", 4, 3)

archivo = open("./Tema_8/objetoVehiculo", 'w+b')
dump(coche, archivo)
archivo.seek(0)
newCoche = load(archivo)

print(newCoche)
archivo.close()