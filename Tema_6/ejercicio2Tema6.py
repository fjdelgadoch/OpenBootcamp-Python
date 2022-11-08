class Alumno():
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

    def setCalificacion(self):
        if self.nota < 5:
            return "Suspenso"
        elif self.nota < 6:
            return "Suficiente"
        elif self.nota < 7:
            return "Bien"
        elif self.nota < 9:
            return "Notable"
        elif self.nota <= 10:
            return "Sobresaliente"
        else:
            return "La nota introducida no es correcta"
        
    def getDatos(self):
        return f"{self.nombre}\nNota: {self.nota}\nCalificación: {self.setCalificacion()}\n"

alumno1=Alumno("Francisco", 4.5)
alumno2=Alumno("Alma", 5)
alumno3=Alumno("Rosi", 6.2)
alumno4=Alumno("Jose", 8.9)
alumno5=Alumno("Juan", 9.15)
alumno6=Alumno("Pilar", 11)

print(alumno1.getDatos())
print(alumno2.getDatos())
print(alumno3.getDatos())
print(alumno4.getDatos())
print(alumno5.getDatos())
print(alumno6.getDatos())