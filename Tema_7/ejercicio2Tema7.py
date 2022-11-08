from time import strftime

horas = int(strftime("%H"))
minutos = int(strftime("%M"))

print(f"Hora actual: {horas}:{minutos}")

if horas == 19 and minutos == 0:
    print("\nEs la hora de ir a casa.")

elif horas == 19 and minutos > 0:
    print(f"Hace {minutos} minutos que terminó tu jornada.")

elif horas > 19:
    print(f"Hace {horas} horas y {minutos} minutos que terminó tu jornada.")

else:
    print(f"Te quedan {18 - horas} horas y {60 - minutos} para salir del trabajo.")