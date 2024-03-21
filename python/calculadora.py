from  tkinter import*

raiz =Tk()
#raiz.geometry("650x350")

miFrame=Frame(raiz)
miFrame.pack()
miFrame.config(bg="#222222")


operacion=""
resultado=0


#-------------------------------------------Pantalla------------------------------


numeroPantalla=StringVar()



pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1,column=1, padx=10, pady=10,columnspan=4)
pantalla.config(bg="#4A4A4A",fg="#DCDCDC", justify=RIGHT)


#----------------------------Pulsaciones teclado-----------------
def numeroPulsado(num):
    global operacion
    if numeroPantalla.get() == "ERROR":
        numeroPantalla.set("")
    if operacion!="":
        numeroPantalla.set(num)
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

#--------------------------------Suma----------------------
def suma():
    global operacion
    global resultado
    if numeroPantalla.get() == "":
        numeroPantalla.set("ERROR")
    else:
        resultado = int(numeroPantalla.get())
        operacion="suma"
        numeroPantalla.set("")


#--------------------------------Resta----------------------
def resta():
    global operacion
    global resultado
    if numeroPantalla.get() == "":
        numeroPantalla.set("ERROR")
    else:
        resultado = int(numeroPantalla.get())
        operacion="resta"
        numeroPantalla.set("")

#--------------------------------Multiplicación----------------------
def mul():

    global operacion
    global resultado
    if numeroPantalla.get() == "":
        numeroPantalla.set("ERROR")
    else:
        resultado = int(numeroPantalla.get())
        operacion="mul"
        numeroPantalla.set("")


#--------------------------------Division----------------------
def div():
    global operacion
    global resultado
    if numeroPantalla.get() == "":
        numeroPantalla.set("ERROR")
    else:
        resultado = int(numeroPantalla.get())
        operacion="div"
        numeroPantalla.set("")

#---------------------------------Limpiar-----------------------------
def limpiar():
    numeroPantalla.set("")
    resultado=0




#---------------------------------Igual---------------------------------
def el_resultado():
    global resultado
    global operacion
    if operacion == "suma":
        numeroPantalla.set(resultado + int(numeroPantalla.get()))
    elif operacion == "resta":
        numeroPantalla.set(resultado - int(numeroPantalla.get()))
    elif operacion == "mul":
        numeroPantalla.set(resultado * int(numeroPantalla.get()))
    elif operacion == "div":
        numeroPantalla.set(resultado / int(numeroPantalla.get()))
    resultado = 0
    operacion = ""


#-------------------------Fila 1---------------------------------------------------
Boton7=Button(miFrame, text="7",width=3, command=lambda:numeroPulsado("7"))
Boton7.grid(row=2,column=1)
Boton8=Button(miFrame, text="8",width=3, command=lambda:numeroPulsado("8"))
Boton8.grid(row=2,column=2)
Boton9=Button(miFrame, text="9",width=3, command=lambda:numeroPulsado("9"))
Boton9.grid(row=2,column=3)
Div=Button(miFrame, text="/",width=3,command=lambda:div())
Div.grid(row=2,column=4)



#---------------------------Fila 2-----------------------------------------------
Boton4=Button(miFrame, text="4",width=3, command=lambda:numeroPulsado("4"))
Boton4.grid(row=3,column=1)
Boton5=Button(miFrame, text="5",width=3, command=lambda:numeroPulsado("5"))
Boton5.grid(row=3,column=2)
Boton6=Button(miFrame, text="6",width=3, command=lambda:numeroPulsado("6"))
Boton6.grid(row=3,column=3)
Mul=Button(miFrame, text="X",width=3,command=lambda:mul())
Mul.grid(row=3,column=4)

#---------------------------Fila 3-----------------------------------------------
Boton1=Button(miFrame, text="1",width=3, command=lambda:numeroPulsado("1"))
Boton1.grid(row=4,column=1)
Boton2=Button(miFrame, text="2",width=3, command=lambda:numeroPulsado("2"))
Boton2.grid(row=4,column=2)
Boton3=Button(miFrame, text="3",width=3, command=lambda:numeroPulsado("3"))
Boton3.grid(row=4,column=3)
Rest=Button(miFrame, text="-",width=3,command=lambda:resta())
Rest.grid(row=4,column=4)


#---------------------------Fila 3-----------------------------------------------
Coma=Button(miFrame, text="C",width=3,command=lambda:limpiar())
Coma.grid(row=5,column=1)
Boton0=Button(miFrame, text="0",width=3, command=lambda:numeroPulsado("0"))
Boton0.grid(row=5,column=2)
Sum=Button(miFrame, text="+",width=3, command=lambda:suma())
Sum.grid(row=5,column=3)
igual=Button(miFrame, text="=",width=3, command=lambda:el_resultado())
igual.grid(row=5,column=4)


raiz.mainloop()