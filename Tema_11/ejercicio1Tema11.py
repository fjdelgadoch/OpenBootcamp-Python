import sqlite3

connection_bd = sqlite3.connect('aula.db')

cursor_bd = connection_bd.cursor()

cursor_bd.execute("CREATE TABLE Alumnos(id INT, Nombre TEXT, Apellido TEXT)")

cursor_bd.execute("INSERT INTO Alumnos VALUES(1,'Francisco', 'Delgado')")
cursor_bd.execute("INSERT INTO Alumnos VALUES(2,'Hugo', 'Díaz')")
cursor_bd.execute("INSERT INTO Alumnos VALUES(3,'Pilar', 'Chinchilla')")
cursor_bd.execute("INSERT INTO Alumnos VALUES(4,'Rosa', 'Aquino')")
cursor_bd.execute("INSERT INTO Alumnos VALUES(5,'Carlos', 'Martín')")
cursor_bd.execute("INSERT INTO Alumnos VALUES(6,'José', 'Delgado')")
cursor_bd.execute("INSERT INTO Alumnos VALUES(7,'Carlos', 'Izquierdo')")
cursor_bd.execute("INSERT INTO Alumnos VALUES(7,'Ramón', 'Carrascosa')")

connection_bd.commit()

cursor_bd.execute("SELECT * FROM Alumnos WHERE Nombre = 'Carlos'")

print(cursor_bd.fetchall())

cursor_bd.close()
connection_bd.close()