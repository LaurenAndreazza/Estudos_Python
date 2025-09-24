import time
class Elevador:
    def __init__(self, nome: str):
        self.nome = nome
        self.andar_atual = 1  
        self.total_andares = 4
        print(f"Elevador '{self.nome}' criado e posicionado no andar {self.andar_atual}.")

    def mover(self, destino: int):
        if self.andar_atual == destino:
            print(f"O elevador '{self.nome}' já está no andar {destino}.")
            return

        print(f"Elevador '{self.nome}' movendo-se do andar {self.andar_atual} para o {destino}...")
        time.sleep(1) 
        self.andar_atual = destino
        self.anunciar_chegada()

    def selecionar_andar(self, andar_desejado: int):
        print(f"\n[PAINEL INTERNO - {self.nome}] Botão do andar {andar_desejado} pressionado.")
        if 1 <= andar_desejado <= self.total_andares:
            self.mover(andar_desejado)
        else:
            print(f"Andar inválido. O prédio só tem {self.total_andares} andares.")

    def chamar(self, andar_chamada: int, direcao: str):
        print(f"\n[PAINEL EXTERNO - Andar {andar_chamada}] Elevador '{self.nome}' chamado para {direcao}.")
        if andar_chamada == 1 and direcao == "descer":
            print("AVISO: Não há botão para descer no térreo.")
            return
        if andar_chamada == self.total_andares and direcao == "subir":
            print(f"AVISO: Não há botão para subir no último andar ({self.total_andares}).")
            return            
        self.mover(andar_chamada)

    def anunciar_chegada(self):
        print(f"O elevador '{self.nome}' chegou ao andar {self.andar_atual}.")

class ElevadorSocial(Elevador):
    def __init__(self):
        super().__init__("Social")

    def anunciar_chegada(self):
        print(f"Elevador Social chegou ao andar {self.andar_atual}. Portas abrindo.")

class ElevadorServico(Elevador):
    def __init__(self):
        super().__init__("de Serviço")

    def anunciar_chegada(self):
        print(f"Elevador de Serviço disponível no andar {self.andar_atual}. Cuidado com a carga.")

    def transportar(self, item1: str, item2: str = None):
        if item2 is None:
            print(f"[{self.nome}] Transportando funcionário: {item1}.")
        else:
            print(f"[{self.nome}] Transportando carga: '{item1}' com peso de {item2}.")

if __name__ == "__main__":
    
    elevador_social = ElevadorSocial()
    elevador_servico = ElevadorServico()
    print("\n" + "="*50)

    elevador_social.chamar(2, "subir")
    elevador_social.selecionar_andar(4)
    elevador_social.chamar(4, "subir")
    print("\n" + "="*50)

    elevador_servico.chamar(3, "descer")

    elevador_servico.transportar("Zelador Carlos")
    elevador_servico.transportar("Caixas de Limpeza", "50kg")
