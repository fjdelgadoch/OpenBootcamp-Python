print("Muestra los números del 1 al 100 en orden inverso:\n")

for i in reversed (range (1,101)):
    print(i)

print("\nLista con los números del 1 al 100 en orden inverso:\n")

lista=[]

for j in range(1,101):
    lista.append(j)

print(sorted(lista, reverse=True))