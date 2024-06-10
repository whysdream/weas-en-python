#don pepe

def BaseDatos():
        usuarios={
        "maxi": "admin",
        "mati": "admin"
        }
    
        def verificador(user,contraseña):
            if user in usuarios and usuarios[user] == contraseña:   
                print("inicio de sesion exitoso")
                return True
            else:
                return False
    
        def agregar(user,contraseña):
            if user not in usuarios:
                usuarios[user] = contraseña
                print("usuario creado con exito")
                return True
            else:
                print("usuario ya existente")
            return False
        
        return verificador, agregar