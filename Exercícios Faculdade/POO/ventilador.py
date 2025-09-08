class ventilador:
    def __init__(self, status: int, direcao_vento: bool, diametro: bool, helice: bool, local: int):
        self.status = status
        self.direcao_vento = direcao_vento
        self.diametro = diametro
        self.helice = helice
        self.local = local

    def exibirStatus(self) -> str:
        match self.status:
            case 0:
                return (f"Desligado")
            case 1:
                return (f"Lento")
            case 2:
                return (f"Rápido")

    def exibirLocal(self) -> str:
        match self.local:
            case 1:
                return (f"Canto inferior esquerdo")
            case 2:
                return (f"Canto inferior direito")
            case 3:
                return (f"Centro da sala")
            case 4:
                return (f"Canto superior esquerdo")
            case 5:
                return (f"Canto superior direito")

    def exibirDirecao(self) -> str:
        if self.direcao_vento:
            return (f"Para cima")
        else:
            return (f"Para baixo")

    def exibirDiametro(self) -> str:
        if self.diametro:
            return (f"30cm")
        else:
            return (f"50cm")
        
    def exibirHelice(self) -> str:
        if self.helice:
            return (f"4 pás")
        else:
            return (f"5 pás")        


if __name__ == "__main__":

    print("\n"+"="*20+" Ventilador 01 "+"="*20+"\n")

    ventilador1 = ventilador(1, True, False, True, 3)
    print(ventilador1.exibirStatus())
    print(ventilador1.exibirDirecao())
    print(ventilador1.exibirDiametro())
    print(ventilador1.exibirHelice())
    print(ventilador1.exibirLocal())

    print("\n"+"="*20+" Ventilador 02 "+"="*20+"\n")

    ventilador2 = ventilador(2, False, True, False, 5)
    print(ventilador2.exibirStatus())  
    print(ventilador2.exibirDirecao())
    print(ventilador2.exibirDiametro())
    print(ventilador2.exibirHelice())
    print(ventilador2.exibirLocal())

    print("\n"+"="*20+" Ventilador 03 "+"="*20+"\n")

    ventilador3 = ventilador(0, True, True, True, 1)
    print(ventilador3.exibirStatus())  
    print(ventilador3.exibirDirecao())
    print(ventilador3.exibirDiametro())
    print(ventilador3.exibirHelice())
    print(ventilador3.exibirLocal())

    print("\n"+"="*20+" Ventilador 04 "+"="*20+"\n")

    ventilador4 = ventilador(2, False, False, False, 5)
    print(ventilador4.exibirStatus())  
    print(ventilador4.exibirDirecao())
    print(ventilador4.exibirDiametro())
    print(ventilador4.exibirHelice())
    print(ventilador4.exibirLocal())

    
    print("\n"+"="*20+" Ventilador 05 "+"="*20+"\n")

    ventilador5 = ventilador(1, True, False, True, 4)
    print(ventilador5.exibirStatus())  
    print(ventilador5.exibirDirecao())
    print(ventilador5.exibirDiametro())
    print(ventilador5.exibirHelice())
    print(ventilador5.exibirLocal())
