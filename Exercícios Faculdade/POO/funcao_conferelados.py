import math

class Figura:
    def __init__(self, lados):
        self.lados = lados

    def perimetro(self):
        return sum(self.lados)

class Figura3Lados(Figura):
    def __init__(self, lados, tipo):
        super().__init__(lados)
        self.tipo = tipo

    def area(self):
        L1, L2, L3 = self.lados
        if self.tipo == "Triângulo Equilátero":
            # Fórmula da área do triângulo equilátero: (lado² * sqrt(3)) / 4
            return (L1**2 * math.sqrt(3)) / 4
        else:
            # Fórmula de Heron para área de triângulo qualquer (Isósceles e Escaleno)
            s = self.perimetro() / 2
            # Adicionado math.sqrt para calcular a raiz quadrada
            return math.sqrt(s * (s - L1) * (s - L2) * (s - L3))

class Figura4Lados(Figura):
    def __init__(self, lados, tipo):
        super().__init__(lados)
        self.tipo = tipo

    def area(self):
        # Para retângulos e quadrados, os lados opostos são iguais.
        # Ordenar os lados garante que L1 e L2 sejam os lados diferentes de um retângulo.
        lados_ordenados = sorted(self.lados)
        
        if self.tipo == "Quadrado":
            return lados_ordenados[0] * lados_ordenados[0]
        elif self.tipo == "Retângulo":
            return lados_ordenados[0] * lados_ordenados[2] # Multiplica os lados diferentes
        # A área do trapézio precisa de mais informações (altura), então retornamos 0
        else:
            return 0

# --- FUNÇÃO CORRIGIDA ---
def confereLado3(L1, L2, L3):
    # 1. Adicionada a condição de existência de um triângulo
    if not (L1 + L2 > L3 and L1 + L3 > L2 and L2 + L3 > L1):
        return "Figura Inválida"

    # 2. A função agora retorna APENAS o nome (string)
    if L1 == L2 == L3:
        return "Triângulo Equilátero"
    elif L1 == L2 or L1 == L3 or L2 == L3:
        return "Triângulo Isósceles"
    else:
        return "Triângulo Escaleno"


def confereLado4(L1, L2, L3, L4):
    lados = sorted([L1, L2, L3, L4])
    # Verifica se os dois pares de lados opostos são iguais
    if lados[0] == lados[1] and lados[2] == lados[3]:
        # Se todos os quatro são iguais, é um quadrado
        if lados[0] == lados[2]:
            return "Quadrado"
        # Se os pares são diferentes entre si, é um retângulo
        else:
            return "Retângulo"
    else:
        return "figura inválida"

if __name__ == "__main__":
    print("Selecione o número de lados da figura (3 ou 4): ")
    num_lados = input("Número de lados: ")

    if num_lados == "3":
        L1 = float(input("Coloque o primeiro lado: "))
        L2 = float(input("Coloque o segundo lado: "))
        L3 = float(input("Coloque o terceiro lado: "))
        
        tipo = confereLado3(L1, L2, L3)
        
        # Verifica se o tipo é válido antes de criar o objeto
        if tipo != "Figura Inválida":
            figura = Figura3Lados([L1, L2, L3], tipo)
            print(f"Sua figura é um {figura.tipo} com área de {figura.area():.2f} e perímetro de {figura.perimetro():.2f}.")
        else:
            print("Erro: As medidas informadas não formam um triângulo.")

    elif num_lados == "4":
        L1 = float(input("Coloque o primeiro lado: "))
        L2 = float(input("Coloque o segundo lado: "))
        L3 = float(input("Coloque o terceiro lado: "))
        L4 = float(input("Coloque o quarto lado: "))
        
        tipo = confereLado4(L1, L2, L3, L4)

        if tipo != "figura inválida":
            figura = Figura4Lados([L1, L2, L3, L4], tipo)
            area_figura = figura.area()
            if area_figura > 0:
                 print(f"Sua figura é um {figura.tipo} com área de {area_figura:.2f} e perímetro de {figura.perimetro():.2f}.")
            else:
                 print(f"Sua figura é um {figura.tipo} com perímetro de {figura.perimetro():.2f}. Não foi possível calcular a área com os dados fornecidos.")
        else:
            print("Não foi possível identificar um quadrado ou retângulo com essas medidas.")
    else:
        print("Número de lados inválido.")