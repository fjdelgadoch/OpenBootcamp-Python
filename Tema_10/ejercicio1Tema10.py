import tkinter

def seleccion():
    variable.config(text=f"{valor.get()}")

def reiniciar():
    valor.set(None)
    variable.config(text="")

ventana = tkinter.Tk()

valor = tkinter.StringVar()
valor.set(None)

tkinter.Radiobutton(ventana, text="Coche", variable=valor, value='Coche', command=seleccion).pack(anchor=tkinter.W)
tkinter.Radiobutton(ventana, text="Tren", variable=valor, value='Tren', command=seleccion).pack(anchor=tkinter.W)
tkinter.Radiobutton(ventana, text="Avión", variable=valor, value='Avión', command=seleccion).pack(anchor=tkinter.W)
tkinter.Radiobutton(ventana, text="Barco", variable=valor, value='Barco', command=seleccion).pack(anchor=tkinter.W)
tkinter.Radiobutton(ventana, text="Autobus", variable=valor, value='Autobus', command=seleccion).pack(anchor=tkinter.W)

variable = tkinter.Label(ventana)
variable.pack()
tkinter.Button(ventana, text="Reiniciar", command=reiniciar).pack()

ventana.mainloop()