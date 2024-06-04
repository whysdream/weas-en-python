#Entrada
print("===Don Pepe===")
print("¡Bienvenido al comercio Don Pepe!")

#MENU DE REGISTRO
def menu_registro():
    print("Validación de usuario.")
    print("1. Registrarse")
    print("2. Ingresar cuenta existente")
    resp=int(input("Ingrese su opción (1,2) ->"))
    #Parche
    while resp!=1 or resp!=2:
        print("¡Ingrese opción válida!")
        resp=int(input("Ingrese su opción (1,2) ->"))
    return True
menu_registro()        
fd