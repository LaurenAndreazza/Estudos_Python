class figura:

    def __init__(self, L1,L2, L3, L4):
        self.L1 = float(input("Coloque o primeiro lado: "))
        self.L2 = float(input("Coloque o segundo lado: "))
        self.L3 = float(input("Coloque o terceiro lado: "))
        self.L4 = float(input("Coloque o quarto lado: "))

def confereLado(L1, L2, L3, L4):

    if ( L1 == L2 == L3 == L4 ):
        return("É um Quadrado")
    elif ( L1 == L3 and L2 == L4 ):
        return("Retângulo")
    elif ( L1 != L2 and L1 != L3 and L1 != L):
        return("Trapézio")
    else:
        return("Não é uma figura válida")


class quadrado(figura):

    def __init__(self, L1, L2, L3, L4):
        super().__init__(L1, L2, L3, L4)

    def area(self):
        return self.L1 * self.L2

    def perimetro(self):
        return self.L1 + self.L2 + self.L3 + self.L4

class retangulo(figura):

    def __init__(self, L1, L2, L3, L4):
        super().__init__(L1, L2, L3, L4)

    def area(self):
        return self.L1 * self.L2

    def perimetro(self):
        return self.L1 + self.L2 + self.L3 + self.L4

class trapezio(figura):
    
    def __init__(self, L1, L2, L3, L4):
        super().__init__(L1, L2, L3, L4)

    def area(self):
        return ((self.L1 + self.L2) * self.L3) / 2

    def perimetro(self):
        return self.L1 + self.L2 + self.L3 + self.L4
    


