from tkinter import *
raiz=Tk()

raiz.title("Primera ventana") #Indicamos el nombre de la ventana
raiz.resizable(1,1) #Se utiliza para indicar si se puede o no redimensionar ancho y alto
# deberia de cambiar el icono raiz.iconbitmap("icono.ico")
# raiz.geometry("650x350") #Cambiar el tamaño

raiz.config(background="#BDF5E7")

miFrame=Frame(raiz)
miFrame.pack()


#Configuracion del Frame
miFrame.config(bg="#CABDF5")
miFrame.config(width="650",height="350")
miFrame.pack( anchor="center")
# miFrame.pack(fill="both", expand=True)
miFrame.config(relief="groove")
miFrame.config(bd=35)
miFrame.config(cursor="pirate")


#Label(miFrame, text="Hola mundo", fg="red", font=(18)).place(x=100,y=200)

# miImage=PhotoImage(file="imagenes/gato.png")

# Label(miFrame,image=miImage).place(x=100,y=200)


raiz.mainloop()


