# Entrada
from Login import *

verificar, agregar = BaseDatos()
import csv
import time
import random
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
        print("Por favor seleccione el número de la opción que desee llevar.")
        resp3=int(input(""))
        if resp3>1  or resp3<8:
            print("¡Ingrese un número valido!")
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
                    print("Usted a puesto en el carro esta cantidad del producto:",leche)
                    resp3=0
            #Cantidad leche   
        
            
            


# OPCION 2 REALIZAR COMPRA
    while resp2== 2:
        print("~~REALIZAR COMPRA~~")
        print("1. Pagar carro de compras.")
        print("2. Salir")
        resp5=int(input("Ingrese opción (1,2) ->"))
        while resp5<1 or resp5>2:
            print("¡Ingrese opción válida!")
            resp5=int(input("Ingrese opción (1,2) ->"))
        if resp5 == 2:
            resp2=0
        
        
# OPCION 3 CAJERO
    while resp2 == 3:
       print("~~CAJA VECINA~~")
       print("1. Depositar")
       print("2. Girar dinero")
       print("3. Salir")
       cajvc=int(input("Ingrese la opción (1,2,3) ->"))
       while cajvc<1 or cajvc>3:
           print("¡Ingrese opción válida!")
           #PARCHE
           cajvc=int(input("Ingrese la opción (1,2,3) ->"))
#OPCION1CAJERO
       if cajvc ==1:
           print("~DEPOSITAR~")
           print("Ingrese la tarjeta al lector de la máquina.")
           time.sleep(1)
           print("Espere un momento . . .")
           time.sleep(1)
           print("Ingrese la clave de 4 digitos")
           clave=(input("->"))
           while len(clave) != 4 or not clave.isdigit():
             print("La clave debe tener exactamente 4 caracteres. Inténtelo de nuevo.")
             clave=input("->")
           time.sleep(1)
           print("Aprobado, se continuará con la operación.")
           print("Ingrese el rut de la persona la cual le desea depositar (Sin puntos ni guión) (*DEBE TENER 8 CARACTERES*)")
           rut=(input("->"))
           while len(rut) != 8 or not rut.isdigit():
             print("El RUT debe tener exactamente 8 caracteres. Inténtelo de nuevo.")
             rut = input("-> ")
           print("MONTO")
           print("1. $5000")
           print("2. $10000")
           print("3. $20000")
           print("4. $50000")
           print("5. $100000")
           print("6. Monto personalizado")
           respmont=int(input("Ingrese su opción (1,2,3,4,5,6) ->"))
           #PARCHE 
           while respmont<1 or respmont>6:
               print("Ingrese opción válida.")
               respmont=int(input("Ingrese su opción (1,2,3,4,5,6) ->"))
           if respmont == 1:
               print("Depositando $5000 al rut ",rut)
               print("Favor, espere un momento . . .")
               time.sleep(2)
               print("¡Deposito completado!")
               print("Número de operación ",random.randint(10000,20000))
           if respmont == 2:
               print("Depositando $10000 al rut ",rut)
               print("Favor, espere un momento . . .")
               time.sleep(2)
               print("¡Deposito completado!")
               print("Número de operación ",random.randint(10000,20000))
           if respmont == 3:
               print("Depositando $20000 al rut ",rut)
               print("Favor, espere un momento . . .")
               time.sleep(2)
               print("¡Deposito completado!")
               print("Número de operación ",random.randint(10000,20000))
           if respmont == 4:
               print("Depositando $50000 al rut ",rut)
               print("Favor, espere un momento . . .")
               time.sleep(2)
               print("¡Deposito completado!")
               print("Número de operación ",random.randint(10000,20000))
           if respmont == 5:
               print("Depositando $100000 al rut ",rut)
               print("Favor, espere un momento . . .")
               time.sleep(2)
               print("¡Deposito completado!")
               print("Número de operación ",random.randint(10000,20000))
           if respmont == 6:
               montoper=int(input("Favor ingrese el monto a depositar ->"))
               while montoper<3000 or montoper>200000:
                   print("No se aceptan depositos de menos de $3000 o más de $200000, favor intentelo denuevo con un monto válido")
                   montoper=int(input("Favor ingrese el monto a depositar ->"))
               print("¿Está seguro de que este es el monto que desea operar? :",montoper)
               ree=input("(S/N) ->").lower()
               while ree!="s" and ree!="n":
                   ree=input("Ingrese opción válida (S/N) ->").lower
               while ree == "n":
                 montoper=int(input("Favor ingrese el monto a depositar ->"))
                 print("Depositando $",montoper, "al rut:",rut)
                 print("Favor, espere un momento . . .")
                 time.sleep(2)
                 print("¡Deposito completado!")
                 print("Número de operación ",random.randint(10000,20000))
                 break;
               if ree == "s":
                   print("Depositando $", montoper ,"al rut :",rut)
                   print("Favor, espere un momento . . .")
                   time.sleep(2)
                   print("¡Deposito completado!")
                   print("Número de operación ",random.randint(10000,20000))
#OPCION2CAJERO
       if cajvc == 2:
           print("~~GIRAR DINERO~~")
           print("Ingrese la tarjeta al lector de la maquina.")
           time.sleep(1)
           print("Espere un momento . . .")
           time.sleep(1)
           print("Ingrese la clave de 4 digitos")
           clave=(input("->"))
           while len(clave) !=4:
             print("La clave debe tener exactamente 4 caracteres. Inténtelo de nuevo.")
             clave=(input("->"))
           time.sleep(1)
           print("Aprobado, se continuará con la operación.")
           print("~MONTOS~")
           print("1. $5000")
           print("2. $10000")
           print("3. $20000")
           print("4. $50000")
           print("5. $100000")
           print("6. Monto personalizado")
           girar=int(input("Ingrese su opción (1,2,3,4,5,6) ->"))
           #PARCHE
           while girar<1 or girar>6:
             print("Ingrese opción válida.")
             girar=int(input("Ingrese su opción (1,2,3,4,5,6) ->"))
           if girar == 1:
               print("Girando $5000, Favor espere un momento...")
               time.sleep(2)
               print("Retire los billetes por favor.")
               print("Monto realizado, ¿Desea realizar otro giro?")
               rd=input("(S/N) ->").lower()
               if rd == "n":
                   resp2==2
               elif rd == "s":
                   cajvc==2
               while rd!="s" and rd!="n":
                   rd=input("Ingrese opción válida (S/N) ->").lower()
           if girar == 2:
               print("Girando $10000, Favor espere un momento...")
               time.sleep(2)
               print("Retire los billetes por favor.")
               print("Monto realizado, ¿Desea realizar otro giro?")
               rd=input("(S/N) ->").lower()
               if rd == "n":
                   resp2==2
               elif rd == "s":
                   cajvc==2
               while rd!="s" and rd!="n":
                   rd=input("Ingrese opción válida (S/N) ->").lower()
           if girar == 3:
               print("Girando $20000, Favor espere un momento...")
               time.sleep(2)
               print("Retire los billetes por favor.")
               print("Monto realizado, ¿Desea realizar otro giro?")
               rd=input("(S/N) ->").lower()
               if rd == "n":
                   resp2==2
               elif rd == "s":
                   cajvc==2
               while rd!="s" and rd!="n":
                   rd=input("Ingrese opción válida (S/N) ->").lower()
           if girar == 4:
               print("Girando $50000, Favor espere un momento...")
               time.sleep(2)
               print("Retire los billetes por favor.")
               print("Monto realizado, ¿Desea realizar otro giro?")
               rd=input("(S/N) ->").lower()
               if rd == "n":
                   resp2==2
               elif rd == "s":
                   cajvc==2
               while rd!="s" and rd!="n":
                   rd=input("Ingrese opción válida (S/N) ->").lower()
           if girar == 5:
               print("Girando $100000, Favor espere un momento...")
               time.sleep(2)
               print("Retire los billetes por favor.")
               print("Monto realizado, ¿Desea realizar otro giro?")
               rd=input("(S/N) ->").lower()
               if rd == "n":
                   resp2==2
               elif rd == "s":
                   cajvc==2
               while rd!="s" and rd!="n":
                   rd=input("Ingrese opción válida (S/N) ->").lower()
           if girar == 6:
               montto=int(input("Favor ingrese el monto a girar ->"))
               while montto<5000 or montto>200000:
                   print("No se aceptan giros de menos de $5000 o más de $200000, favor intentelo denuevo con un monto válido")
                   montto=int(input("Favor ingrese el monto a girar ->"))
               print("¿Está seguro de que este es el monto que desea operar? :",montto)
               rd=input("(S/N) ->").lower()
               while rd!="s" and rd!="n":
                   rd=input("Ingrese opción válida (S/N) ->").lower()
               while rd == "n":
                 montto=int(input("Favor ingrese el monto a girar ->"))
                 print("Girando $", montto)
                 print("Favor, espere un momento . . .")
                 time.sleep(2)
                 print("¡Giro completado!")
                 break
               if rd == "s":
                   print("Girando $", montto)
                   print("Favor, espere un momento . . .")
                   time.sleep(2)
                   print("¡Giro completado!")
#OPCION3SALIR
       if cajvc==3:
           resp2=0

                   

                   
                   


        

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


