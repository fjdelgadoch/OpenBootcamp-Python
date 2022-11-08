class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas

    def getDatosVehiculo(self):
        return f"Color: {self.color}\nRuedas: {self.ruedas}\nPuertas: {self.puertas}"
        
class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad,cilindrada):
        Vehiculo.__init__(self, color, ruedas, puertas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def getDatosCoche(self):
        return f"{super().getDatosVehiculo()}\nVelocidad: {self.velocidad} Km/hora\nCilindrada: {self.cilindrada}cc"

coche1= Coche("Rojo", 4, 3,180,1900)

print(coche1.getDatosCoche())