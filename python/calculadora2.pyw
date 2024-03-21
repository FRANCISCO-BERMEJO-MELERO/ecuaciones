from tkinter import *

raiz = Tk()

miFrame = Frame(raiz)
miFrame.pack()
miFrame.config(bg="#222222")

numero1 = ""
operacion = ""
resultado = 0

# -------------------------------------------Pantalla------------------------------

numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="#4A4A4A", fg="#DCDCDC", justify=RIGHT)

# ----------------------------Pulsaciones teclado-----------------
def numeroPulsado(num):
    global operacion
    global numero1
    if operacion != "":
        numeroPantalla.set(num)
        numero1 = int(num)
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

# ---------------------------Funcion suma
def suma():
    global operacion
    global resultado
    global numero1
    resultado += numero1
    operacion = "suma"
    numeroPantalla.set(resultado)

# ---------------------------Funcion Resta
def resta():
    global operacion
    global resultado
    global numero1
    resultado -= numero1
    operacion = "resta"
    numeroPantalla.set(resultado)

# ---------------------------Funcion Multiplicacion
def mul():
    global operacion
    global resultado
    global numero1
    resultado *= numero1
    operacion = "mul"
    numeroPantalla.set(resultado)

# ---------------------------Funcion division
def div():
    global operacion
    global resultado
    global numero1
    if numero1 != 0:
        resultado /= numero1
        operacion = "div"
        numeroPantalla.set(resultado)
    else:
        numeroPantalla.set("Error")

# ---------------------------------EL Resultado
def el_resultado():
    global resultado
    global operacion
    global numero1
    if operacion == "suma":
        numeroPantalla.set(resultado + int(numeroPantalla.get()))
    elif operacion == "resta":
        numeroPantalla.set(resultado - int(numeroPantalla.get()))
    elif operacion == "mul":
        numeroPantalla.set(resultado * int(numeroPantalla.get()))
    elif operacion == "div":
        if int(numeroPantalla.get()) != 0:
            numeroPantalla.set(resultado / int(numeroPantalla.get()))
        else:
            numeroPantalla.set("Error")
    resultado = 0

# -------------------------Fila 1---------------------------------------------------
Boton7 = Button(miFrame, text="7", width=3, command=lambda: numeroPulsado("7"))
Boton7.grid(row=2, column=1)
Boton8 = Button(miFrame, text="8", width=3, command=lambda: numeroPulsado("8"))
Boton8.grid(row=2, column=2)
Boton9 = Button(miFrame, text="9", width=3, command=lambda: numeroPulsado("9"))
Boton9.grid(row=2, column=3)
Div = Button(miFrame, text="/", width=3, command=lambda: div())
Div.grid(row=2, column=4)

# ---------------------------Fila 2-----------------------------------------------
Boton4 = Button(miFrame, text="4", width=3, command=lambda: numeroPulsado("4"))
Boton4.grid(row=3, column=1)
Boton5 = Button(miFrame, text="5", width=3, command=lambda: numeroPulsado("5"))
Boton5.grid(row=3, column=2)
Boton6 = Button(miFrame, text="6", width=3, command=lambda: numeroPulsado("6"))
Boton6.grid(row=3, column=3)
Mul = Button(miFrame, text="X", width=3, command=lambda: mul())
Mul.grid(row=3, column=4)

# ---------------------------Fila 3-----------------------------------------------
Boton1 = Button(miFrame, text="1", width=3, command=lambda: numeroPulsado("1"))
Boton1.grid(row=4, column=1)
Boton2 = Button(miFrame, text="2", width=3, command=lambda: numeroPulsado("2"))
Boton2.grid(row=4, column=2)
Boton3 = Button(miFrame, text="3", width=3, command=lambda: numeroPulsado("3"))
Boton3.grid(row=4, column=3)
Rest = Button(miFrame, text="-", width=3, command=lambda: resta())
Rest.grid(row=4, column=4)

# ---------------------------Fila 3-----------------------------------------------
Coma = Button(miFrame, text=",", width=3, command=lambda: numeroPulsado(","))
Coma.grid(row=5, column=1)
Boton0 = Button(miFrame, text="0", width=3, command=lambda: numeroPulsado("0"))
Boton0.grid(row=5, column=2)
Sum = Button(miFrame, text="+", width=3, command=lambda: suma())
Sum.grid(row=5, column=3)
igual = Button(miFrame, text="=", width=3, command=lambda: el_resultado())
igual.grid(row=5, column=4)

raiz.mainloop()
