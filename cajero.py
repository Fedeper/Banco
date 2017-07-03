from cliente import Cliente
from cuenta import Cuenta

class Cajero():
    def __init__(self,cola):
        self.cola=cola
        
    def atender(self):        
        try:
            print('Se atiende al cliente:\n',self.cola[0].nombre,self.cola[0].apellido)
            while True:
                operacion=input('Ingrese la operacion que desea realizar (estado,depositar,extraer,baja,salir):\n')
                if operacion=='extraer':
                    self.cola[0].cuenta.extraerDinero(int(input('Ingrese cantidad de dinero:\n')))  
                elif operacion=='depositar':
                    self.cola[0].cuenta.agregarDinero(int(input('Ingrese cantidad de dinero:\n')))
                elif operacion=='baja':
                    self.cola[0].dar_Baja(input('Ingrese fecha de baja:\n'))
                elif operacion=='estado':
                    self.cola[0].activo()
                elif operacion=='salir':
                    self.cola.remove(self.cola[0])
                    break
                else:
                    print('Vuelva a ingresar la operacion')                        
        except:
            print('No hay mas clientes en la cola')
        
