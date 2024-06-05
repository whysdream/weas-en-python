#don pepe

class BaseDatos:
    def __init__(self):
        self.usuarios={
            "maxi": "admin",
            "mati": "admin"
        }
    
    def verificador(self,user,contraseña):
        if user in self.usuarios and self.usuarios[user] == contraseña:
                print("inicio de sesion exitoso")
                return True
        else:
            print("usuario y/o contraseña incorrectos")
            return False
    
    def agregar(self,user,contraseña):
        if user not in self.usuarios:
            self.usuarios[user] = contraseña
            print("usuario creado con exito")
            return True
        else:
            print("usuario ya existente")
            return False
