from cliente import Cliente
from cuenta import Cuenta
from cajero import Cajero

cola=[]
def encolar_Cliente(cola,cliente):
    cola.append(cliente)

encolar_Cliente(cola,Cliente('Monica','Galindo','lalla 123',152369854,'12051980',25987645,'M','05062010','Cordoba23',1))
encolar_Cliente(cola,Cliente('Laura','Garcia','lalla 123',152369854,'12051980',25987645,'M','05062010','Cordoba23',2))
encolar_Cliente(cola,Cliente('Esteban','Ayala','lalla 123',152369854,'12051980',25987645,'M','05062010','Cordoba23',3))
encolar_Cliente(cola,Cliente('Zacarias','Flores de la Plaza','lalla 123',152369854,'12051980',25987645,'M','05062010','Cordoba23',4))
encolar_Cliente(cola,Cliente('Pedro','Picapiedra','lalla 123',152369854,'12051980',25987645,'M','05062010','Cordoba23',5))

cajero=Cajero(cola)

while len(cola)>=1:
    cajero.atender()
else:
    print('No hay mas clientes en la cola')
