from tkinter import*
raiz= Tk() #Cambiar el tamaño

#Definimos una variable




miFrame=Frame(raiz)
miFrame.pack()
miFrame.config(bg="#DBFA98")
miFrame.config(width="650",height="350")
raiz.config(bg="#C0BDC8")
miFrame.pack(fill="both", expand=True)


minombre=StringVar()
cuadroTexto=Entry(miFrame,textvariable=minombre)
#cuadroTexto.place(x=100,y=100)
cuadroTexto.grid(row=0,column=1,padx=10,pady=10)
cuadroTexto.config(fg="green",)

apellidos=Entry(miFrame)
apellidos.grid(row=1,column=1,padx=10,pady=10)
apellidos.config(fg="green")

direccion=Entry(miFrame)
direccion.grid(row=2,column=1,padx=10,pady=10)
direccion.config(fg="green")

contraseña=Entry(miFrame)
contraseña.grid(row=3,column=1,padx=10,pady=10)
contraseña.config(show="#",fg="red")


nombreLabel=Label(miFrame, text="Nombre:")
#nombreLabel.place(x=100,y=70)
nombreLabel.grid(row=0,column=0,sticky=W,padx=10,pady=10,)
nombreLabel.config(bg="#DBFA98")

label_apellidos=Label(miFrame, text="Apellidos:")
label_apellidos.grid(row=1,column=0,sticky=W,padx=10,pady=10)
label_apellidos.config(bg="#DBFA98")


label_direccion=Label(miFrame, text="Direccion:")
label_direccion.grid(row=2,column=0,sticky=W,padx=10,pady=10)
label_direccion.config(bg="#DBFA98")


contraseña=Label(miFrame, text="Contraseña:")
contraseña.grid(row=3,column=0,sticky=W,padx=10,pady=10)
contraseña.config(bg="#DBFA98")


#Video 2

comentarios=Label(miFrame, text="Comentarios:")
comentarios.grid(row=4,column=0,sticky=W,padx=10,pady=10)
comentarios.config(bg="#DBFA98")


texto_comentario=Text(miFrame,width=16, height=5)
texto_comentario.grid(row=4,column=1)



scrollvert=Scrollbar(miFrame, command=texto_comentario.yview)
scrollvert.grid(row=4,column=2,sticky="nsew")



texto_comentario.config(yscrollcommand=scrollvert.set)

def codigoBoton():
    minombre.set("Juan")


botonEnvio=Button(raiz,text="Enviar", command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()