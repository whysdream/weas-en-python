# Entrada
from Login import *

verificar, agregar = BaseDatos()
import csv
import time
stock = "stockk.csv"


# Funcion PARA CARGAR LOS DATOS
def cargar_archivo():
    productos = []
    with open(stock, "r", newline="") as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            nombre = fila[0]
            precio = fila[1]
            cantidad = fila[2]
            productos.append(
                (nombre, precio, cantidad)
            )  # es una tupla por eso el doble parentesis
    return productos


# FUNCION PARA GUARDAR LOS DATOS EN EL ARCHIVO DE TEXTO
def guardar_archivo(productos):
    with open(stock, "w", newline="") as archivo:
        escritor_csv = csv.writer(archivo)
        for producto in productos:
            escritor_csv.writerow(producto)


# funcion para mostrar el stock
def mostrar_stock(productos):
    print("=============================|Stock|=================================")
    for i, producto in enumerate(productos, start=1):
        nombre, precio, cantidad = producto
        print(f"{i}. [{nombre}]---Precio:[${precio}]---Cantidad:[{cantidad}]")


# Funcion DEL MENU PRINCIPAL
def menu_principal(productos):
    print("~~Menu~~")
    print("1. Ver stock a disponibilidad")
    print("2. Realizar la compra")
    print("3. Caja vecina (Depositar o girar dinero.)")
    print("4. Salir")

    resp2 = int(input("Ingrese su opción (1,2,3,4) ->"))

    # Parche2
    while resp2 < 1 or resp2 > 4:
        print("¡Ingrese opción válida!")
        resp2 = int(input("Ingrese su opción (1,2,3,4) ->"))

    while resp2 == 1:
        mostrar_stock(productos)
        resp3=int(input(""))
        if resp3>1 and resp3<8:
            print("¡ingrese un numero valido!")
        else:
            resp2=0
            #cantidad de leche
            if resp3==1:
                print("¿Cuanto desea de leche?")
                leche=int(input())
                if leche>24:
                    print("¡No hay tanto stock!")
                    resp2=1
                else:
                    print("usted a puesto en el carro esta cantidad del producto:",leche)
                    resp3=0
            #Cantidad leche   
        
            
            


# OPCION 2 REALIZAR COMPRA

# ----------------------------INICIO PRIMER MENU-------------------->TERMINADO
abrir = 1
acces = 0
productos = cargar_archivo()
intentos = 3
while abrir == 1:
    print("===Don Pepe===")
    print("¡Bienvenido al comercio Don Pepe!")

    # MENU DE REGISTRO
    print("1. Ingresar cuenta existente")
    print("2. Salir")
    resp = int(input("Ingrese su opción (1,2) ->"))

    # Parche
    while resp != 1 and resp != 2:
        print("¡Ingrese opción válida!")
        resp = int(input("Ingrese su opción (1,2) ->"))

    # PRIMERA OPCION PRIMER MENU
    while resp == 1:
        if acces == 1:
            menu_principal(productos)
        else:
            print("----------------")
            user = input("user:")
            contraseña = input("contraseña:")

            if verificar(user, contraseña) == True:
                acces = 1
                print("----------------")
                menu_principal(productos)
            elif verificar(user, contraseña) == False:
                intentos = intentos - 1
                print("----|Usuario y/o Contraseña incorrectas|----")
                if intentos == 0:
                    print("-----------|Cuenta Bloqueada|--------------")
                    time.sleep(10)
                    abrir = 0
                    break
    # SEGUNDA OPCION PRIMER MENU
    if resp == 2:
        print("Hasta luego...")
        abrir = 0
# ----------------------------FIN PRIMER MENU---------------------------
