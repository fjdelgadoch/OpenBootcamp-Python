import tkinter

ventana = tkinter.Tk()

label = tkinter.Label(text="\nELIGE LA ASIGNATURA\n")
label.pack()

asignaturas= ["Matemáticas", "Literatura", "Naturales", "Física", "Historia", "Filosofia", "Idiomas", "Deporte"]
asignatura = tkinter.StringVar(value=asignaturas)

listbox = tkinter.Listbox(ventana, height=8, listvariable=asignatura)
listbox.pack()

ventana.mainloop()