#Entrada
from steps import*

db = BaseDatos()

#Funcion DEL MENU PRINCIPAL

def menu_principal():
    print("~~Menu~~")
    print("1. Ver stock a disponibilidad")
    print("2. Realizar la compra")
    print("3. Caja vecina (Depositar o girar dinero.)")
    print("4. Salir")

    resp2 = int(input("Ingrese su opción (1,2,3,4) ->"))

    #Parche2
    while resp2!=1 and resp2!=2 and resp2!=3 and resp2!=4:
        print("¡Ingrese opción válida!")
        resp2=int(input("Ingrese su opción (1,2,3,4) ->"))
    return resp2

#IFS
    if resp2==1:
        print("===STOCK===")
        print("""1. Leche
    Codigo = QWERT1
    Cantidad disponible = 5
    Precio unitario = $1.100""")
        print("""2. Pan
    Codigo = ASDFG2
    Cantidad disponible = 10
    Precio unitario = $800""")
        print("""3. Paquete de fideos
    Codigo = ZXCVB3
    Cantidad disponible = 6
    Precio unitario = $2.500""")
        print("""4. Enérgetica
    Codigo = LKJHG8
    Cantidad disponible = 12
    Precio unitario = $1.800""")
        print("""5. Agua
    Codigo = XEDCR3
    Cantidad disponible = 7
    Precio unitario = $1.000""")
        print("""6. Cigarros(Pallwo de 20 Unidades)
    Codigo = LOPIU1
    Cantidad disponible = 12
    Precio unitario = $3.700""")
        print("""7. Aceite maravilla 900mL
    Codigo = QAZWS2
    Cantidad disponible = 5
    Precio unitario = $2.250""")
        print("""8. Bebida cola coca 1500mL
    Codigo = LKMSW 9
    Cantidad disponible = 5
    Precio unitario = $1.850""")

#INICIO DE MENU
abrir=1

while abrir==1:
    print("===Don Pepe===")
    print("¡Bienvenido al comercio Don Pepe!")

    #MENU DE REGISTRO
    print("Validación de usuario.")
    print("1. Registrarse")
    print("2. Ingresar cuenta existente")
    resp = int(input("Ingrese su opción (1,2) ->"))

    #Parche
    while resp!=1 and resp!=2:
        print("¡Ingrese opción válida!")
        resp=int(input("Ingrese su opción (1,2) ->"))

    #primera opcion
    while resp==1:
        print("----------------")
        print("ingrese su nombre")
        user = input("")
        print("ingrese contraseña")
        contraseña= input("")
        if db.agregar(user,contraseña):
            resp=0
            print("----------------")
    #SEGUNDA OPICION
    while resp==2:
        print("----------------")
        user = input("user:")
        contraseña = input("contraseña:")
        if db.verificador(user,contraseña):
            print("----------------")
            menu_principal()