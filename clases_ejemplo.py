# esto es un ejemplo de clase


class MiPunto:
    def __init__(self,x ,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Objeto Punto x={self.x} y={self.y}'
    def distancia(self, otro_punto=None):
        import math
        if otro_punto is None:
            return math.sqrt(self.x**2 + self.y**2)
        if isinstance(otro_punto,MiPunto):
            return math.sqrt((self.x-otro_punto.x) ** 2 +
                             (self.y-otro_punto.y) ** 2)
#p1 = MiPunto(2,4)
#p2 = MiPunto(2,-2)
#distancia = p1.distancia(p2)

class MiLinea(MiPunto):
    def __init__(self, par1, par2):
        self.p1 = MiPunto(*par1)
        self.p2 = MiPunto(*par2)

    def medida(self):
        return self.p1.distancia(self.p2)

l1 = MiLinea( par1 = (2,3), par2 = (1,2))
resultado = l1.medida()
pass