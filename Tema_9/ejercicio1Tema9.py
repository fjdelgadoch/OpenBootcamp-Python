paises = input("Introduzca una lista de países separados por comas:\n")

listaPaises = []

for pais in paises.split(","):
    listaPaises.append(pais)
    
ordenados = sorted(set(listaPaises))

print(",".join(ordenados))