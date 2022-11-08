from io import open

archivo = open("./Tema_8/archivo.txt", "w")#Con permiso "w" creamos y escribimos en el archivo.
archivo.write("Archivo creado desde codigo Python.\n")
archivo.close()

archivo = open("./Tema_8/archivo.txt", "r+")#Con permiso "r+" podemos leer y escribir en el archivo.
print(archivo.readline())#Visualizamos la primera linea.
archivo.write("Escribimos más lineas en el archivo.\n")

archivo.seek(0)#Nos colocamos al inicio del archivo.

print(archivo.readlines())#Visualizamos todas la líneas en una lista.

archivo.seek(0)

print(archivo.read())#Mostramos el contenido completo del archivo.
archivo.close()