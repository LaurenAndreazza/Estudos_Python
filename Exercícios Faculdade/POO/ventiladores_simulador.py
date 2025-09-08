class ventilador:
    def __init__(self, cor, marca, voltagem):
        self.cor = cor
        self.marca = marca
        self.voltagem = voltagem
        self.ligado = False
        self.velocidade = 0