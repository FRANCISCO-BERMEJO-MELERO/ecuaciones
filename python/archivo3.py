from tkinter import *

root = Tk()
root.config(bg="#D3D3D3", relief="groove")


otros = Entry(root)
otros.grid(row=3, column=1)
otros.grid_remove()

boton=Button(root, text="Enviar")
boton.grid(row=4, column=1)
boton.grid_remove()

def imprimir():
    if varOpcion.get() == 1:
        etiqueta.config(text= "Has seleccionado Masculino")
        otros.grid_remove()
    elif varOpcion.get() == 2:
        etiqueta.config(text= "Has seleccionado Femenino")
        otros.grid_remove()
    elif varOpcion.get() == 3:
        etiqueta.config(text= "Has seleccionado Otros")
        otros.grid()
    boton.grid()

varOpcion=IntVar()

Label(root, text="Sexo",background="#D3D3D3").grid(row=0, column=0)
Radiobutton(root, text="Masculino",variable=varOpcion, value=1, command=imprimir, background="#D3D3D3").grid(row=1,column=0)
Radiobutton(root, text="Femenino", variable=varOpcion, value=2,command=imprimir,background="#D3D3D3").grid(row=2,column=0)
Radiobutton(root, text="Otros", variable=varOpcion, value=3,command=imprimir,background="#D3D3D3").grid(row=3,column=0)

etiqueta=Label(root)
etiqueta.config(bg="#D3D3D3")
etiqueta.grid(row=4, column=0)

root.mainloop()
