class formas_geometricas:

    def __init__(self, tipo):
        self.tipo = tipo
        self.altura = 0
        self.largura = 0
        self.areaPi = 0
        self.base = 0

    def calcular_tamanho(self):
        if self.tipo == "Quadrado":
            self.area = self.largura * self.altura
        elif self.tipo == "Círculo":
            self.area = 3.14 * (self.areaPi * self.areaPi)
        elif self.tipo == "Triangulo":
            self.area = self.altura * self.base / 2
        return self.area


objeto_quadrado = formas_geometricas("Quadrado")
objeto_quadrado.altura = 10
objeto_quadrado.largura = 10
area2 = objeto_quadrado.calcular_tamanho()
print(area2)
objeto_triangular = formas_geometricas("Triangulo")
objeto_triangular.altura = 10
objeto_triangular.base = 4
area2 = objeto_triangular.calcular_tamanho()
print(area2)
