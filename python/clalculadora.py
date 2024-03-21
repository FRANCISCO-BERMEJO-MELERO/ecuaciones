import math
import random

def comprobar_max_min(min,max):
    n=int()
    salida=False
    while not salida:
        input(n)
        if n<min or n>max:
            print("\nLo sentimos pero el número que ha elegido está fuera del rango permitido, vuelve a intentarlo.")
        else:
            salida=True
    return n


def multiplicacion(r1,r2,salida):
    while not salida:
        print("\n%d x %d"% (r1,r2) )
        resultado=int(input("\nIntroduce el resultado:"))
        if resultado == r1*r2:
            print("\n***************************")
            print("\n*¡Perfecto!, has acertado.*")
            print("\n***************************")
            salida=True
        else:
            print("\nLo siento pero parece que no has acertado.")


def resta(r1,r2,salida):
    while not salida:
        print("\n%d - %d"% (r1,r2) )
        resultado=int(input("\nIntroduce el resultado:"))
        if resultado == r1-r2:
            print("\n***************************")
            print("\n*¡Perfecto!, has acertado.*")
            print("\n***************************")
            salida=True
        else:
            print("\nLo siento pero parece que no has acertado.")



def suma(r1,r2,salida):
    while not salida:
        print("\n%d + %d"% (r1,r2) )
        resultado=int(input("\nIntroduce el resultado:"))
        if resultado == r1+r2:
            print("\n***************************")
            print("\n*¡Perfecto!, has acertado.*")
            print("\n***************************")
            salida=True
        else:
            print("\nLo siento pero parece que no has acertado.")


def preguntar_max_min(max, min):
    max = int(input("Ingrese el nuevo valor máximo para los números: "))
    min = int(input("Ingrese el nuevo valor mínimo para los números: "))
    return max, min

def menu():
    print("\n======Calculadora======\n")
    print("\t1. Suma\n")
    print("\t2. Resta\n")
    print("\t3. Multiplicación\n")
    print("\t4. Cambiar máximos y mínimos\n")
    print("\t5. Salir")
    print("\nSeleccione una opción: ")


#Comienza la main

salida = False
caracter = input("Introduce (s) si quieres elegir los máximos y los mínimos, sino, introduce (n): ")
max=10
min=1

if caracter.lower() == 's':
    max, min = preguntar_max_min(max, min)
print(max)
print(min)
while not salida:
    r1 = random.randint(min, max)
    r2 = random.randint(min, max)
    menu()
    eleccion = int(input())
    if eleccion == 1:
        suma(r1, r2,salida)
    elif eleccion == 2:
        resta(r1, r2,salida)
    elif eleccion == 3:
        multiplicacion(r1, r2,salida)
    elif eleccion == 4:
        preguntar_max_min(max,min)
    elif eleccion == 5:
        salida = True
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")



