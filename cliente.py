from persona import Persona
from cuenta import Cuenta

class Cliente(Persona):
    def __init__(self,nombre,apellido,domicilio,telefono,f_Nac,dni,genero,f_Alta,sucursal,nro_Cuenta):
        Persona.__init__(self,nombre,apellido,domicilio,telefono,f_Nac,dni,genero)
        self.cuenta=Cuenta(nro_Cuenta)
        self.lista_Cuentas=[].append(self.cuenta)
        self.f_Alta=f_Alta
        self.f_Baja=None
        self.sucursal=sucursal

    def activo(self):
        if self.f_Baja == None:
            print ("Activo")
        else:
            print("No activo")

    def dar_Baja(self,f_Baja):
        self.f_Baja=f_Baja
        print('Baja dia:\n',self.f_Baja)

