class Cuenta():
    def __init__(self,nro_Cuenta):
        self.nro_Cuenta=nro_Cuenta
        self.saldo=0
        
        
    def __limite(funcion):
        
        def decorador(*args,**kwargs):
            saldo = funcion(*args,**kwargs)
            if args[1] > saldo:
                print('El saldo no es suficiente\nSu saldo actual es:',saldo)               
            else:
                saldo-=args[1]
                print('Operacion realizada\nSu saldo actual es:',saldo)        
                args[0].saldo=saldo

        return decorador

    def agregarDinero(self,importe):
        self.saldo+=importe
        print('Operacion realizada\nSu saldo actual es:',self.saldo)

    @__limite
    def extraerDinero(self,importe):
        return self.saldo
