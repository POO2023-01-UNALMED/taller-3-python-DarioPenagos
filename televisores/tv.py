from televisores.control import Control


class TV:
    numTV = 0
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.volumen = 1
        self.precio = 500
        self.control = Control()
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
    def setNumTV(num):
        numTV = num
    
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
