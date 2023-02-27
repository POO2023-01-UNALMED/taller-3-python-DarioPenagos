
class Marca:
    def __init__(self, nom):
        self.nombre = nom
    def getNombre(self):
        return self.nombre
    def setNombre(self, nom):
        self.nombre = nom

class TV:
    numTV = 0
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.volumen = 1
        self.precio = 500
        self.control = control()
        numTV += 1
    def getMarca(self):
        return self.marca
    def getControl(self):
        return self.control
    def getPrecio(self):
        return self.precio
    def getVolumen(self):
        return self.volumen
    def getCanal(self):
        return self.canal
    def getNumTV(self):
        return self.numTV

    def setMarca(self, marca):
        self.marca = marca
    def setControl(self, control):
        self.control = control
    def setPrecio(self, precio):
        self.precio = precio
    def setVolumen(self, volumen):
        if 8 > volumen > 0 and self.estado:
            self.volumen = volumen
    def setCanal(self, canal):
        self.canal = canal
    
    def turnOn(self):
        self.estado = True
    def turnOff(self):
        self.estado = False
    def getEstado(self):
        return self.estado

    def canalUp(self):
        if 120 > self.canal and self.estado:
            self.canal += 1
    def canalDown(self):
        if self.canal > 1 and self.estado:
            self.canal -= 1
    def volumenUp(self):
        if 7 > self.volumen and self.estado:
            self.volumen += 1
    def volumenDown(self):
        if self.volumen > 0 and self.estado:
            self.volumen -= 1

class control:
    def __init__(self, tv):
        self.tv = TV()
    def turnOn(self):
        self.tv.turnOn()
    def turnOff(self):
        self.tv.turnOff
    def canalUp(self):
        self.tv.canalUp()
    def canalDown(self):
        self.tv.canalDown()
    def volumenUp(self):
        self.tv.volumenUp
    def volumenDown(self):
        self.tv.volumenDown()
    def setCanal(self, canal):
        self.tv.canal = canal
    
    def enlazar(self, tv):
        self.tv = tv
        tv.control = self
    
    def getTV(self):
        return self.tv
    def setTv(self, tv):
        self.tv = tv



