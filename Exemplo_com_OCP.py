from abc import ABC, abstractmethod

class formas_geometricas(ABC):
    @abstractmethod
    def calcular(self):
        pass

class quadrado(formas_geometricas):
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
        
    def calcular(self):
        area = self.altura * self.largura
        return area
    

class triangulo(formas_geometricas):
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
        
    def calcular(self):
        area = self.altura * self.base / 2
        return area
    

class circulo(formas_geometricas):
    def __init__(self, raio):
        self.raio = raio
        
    def calcular(self):
        area = 3.14 * (self.raio * self.raio)
        return area


quadra = quadrado(2,3)
area = quadra.calcular()
print(area)
