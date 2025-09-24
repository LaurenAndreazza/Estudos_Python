import random

# classe do ventilador
class Ventilador:
    # inicializador dos atributos
    # argumentos: id_local, diametro, num_pas, velocidade, sentido
    # atributos: self.id_local, self.diametro, self.num_pas, self.velocidade, self.sentido
    def __init__(self, id_local: str, diametro: int, num_pas: int, velocidade: int, sentido: int):
        self.id_local = id_local
        self.diametro = diametro
        self.num_pas = num_pas
        self.velocidade = velocidade
        self.sentido = sentido
    # seleciona a velocidade
    # argumento: velocidade
    # consistência: se está no intervalo [0,2] self.velocidade recebe velocidade, senão recebe -1
    def selecionar_velocidade(self, velocidade: int):
        if 0 <= velocidade <= 2: self.velocidade = velocidade
        else: self.velocidade = -1
    # seleciona sentido
    # argumento: sentido
    # consistência: se está no intervalo [0,1] self.sentido recebe sentido, senão recebe -1
    def selecionar_sentido(self, sentido: int):
        if 0 <= sentido <= 1: self.sentido = sentido
        else: self.sentido = -1
    # informação retornada quando o objeto é chamado
    # retorna: atributos do objeto formatados
    def __str__(self) -> str:
        velocidade = "ERRO: Velocidade incorreta"
        sentido = "ERRO: Sentido incorreto"
        if self.velocidade == 0: velocidade = "Desligado"
        elif self.velocidade == 1: velocidade = "Lento    "
        elif self.velocidade == 2: velocidade = "Rápido   "
        if self.sentido == 0: sentido = "Vento para cima "
        elif self.sentido == 1: sentido = "Vento para baixo"
        loc = f"[Loc: {self.id_local}" + " " * (30 - len(self.id_local)) + "]"
        dia = f"[Tam: {self.diametro}cm.]"
        pas = f"[Num: {self.num_pas}]"
        vel = f"[Vel: {velocidade}]"
        sen = f"[Sen: {sentido}]"
        return loc +dia + pas + vel + sen

# classe das operações feitas no ventilador
class OperaVent:
    # inicializador dos atributos
    # atributo: self.lista_vent
    def __init__(self):
        self.lista_vent = []
    # trazer para dentro da classe a lista de objetos ventiladores
    # argumento: lista_vent
    def put_lista_vent(self, lista_vent):
        self.lista_vent = lista_vent
    # enviar para que chamou o método a lista de objetos ventiladores
    # retorna: self.lista_vent
    def get_lista_vent(self):
        return self.lista_vent
    # exibe a lista de objetos ventiladores
    def exibe_vent(self):
        for vent in self.lista_vent: print(vent)
        print("=" * 40)
    # consiste valor inteiro entre ini e fim
    # argumentos: ini, fim, prompt
    # retorna: opt que tem o número inteiro entre ini e fim
    def consiste_int(self, ini: int, fim: int, prompt: str) -> int:
        opt = fim + 1
        while not (ini <= opt <= fim):
            try:
                opt = int(input(prompt))
                if not (ini <= opt <= fim): print("ERRO - Valor fora do intervalo")
            except: print("ERRO - Valor não inteiro")
        return opt
    # sorteia o ventilador para mudar a velocidade e o sentido do vento
    # retorna: o objeto ventilador sorteado
    def sorteio(self):
        num_vent = random.randint(0,4)
        velocidade = random.randint(0,2)
        sentido = random.randint(0,1)
        self.lista_vent[num_vent].selecionar_velocidade(velocidade)
        self.lista_vent[num_vent].selecionar_sentido(sentido)
        return num_vent

# função que executa os seguintes procedimentos:
# - instacia os objetos
# - opera os ventiladores
# - exibe o status dos vetiladores
def principal():
    # instancia os objetos (cria os ventiladores)
    lista_vent = []
    lista_vent.append(Ventilador("Canto inferior esquerdo", 30, 4, 0, 0))
    lista_vent.append(Ventilador("Canto inferior direito", 30, 4, 0, 0))
    lista_vent.append(Ventilador("Canto superior esquerdo", 30, 4, 0, 0))
    lista_vent.append(Ventilador("Canto superior direito", 30, 4, 0, 0))
    lista_vent.append(Ventilador("Centro superior", 50, 5, 0, 0))
    # instancia o objeto da classe com as operações com os ventiladores
    OV_obj = OperaVent()
    print("\nVentiladores fabricados!")
    # envia para o objeto OV_obj a lista dos ventiladores
    OV_obj.put_lista_vent(lista_vent)
    # exibe os ventiladores
    OV_obj.exibe_vent()
    print("\nOperação dos ventiladores")
    # lê o número de operações com os ventiladores
    opt = OV_obj.consiste_int(1,100,"Número de operações entre 1 e 100:")
    # realiza as operações com os ventiladores
    for ct_ite in range(opt):
        # envia para o objeto OV_obj a lista dos ventiladores
        OV_obj.put_lista_vent(lista_vent)
        # sorteio do ventilador e o tipo de operação na velocidade e sentido do vento
        num_vent = OV_obj.sorteio()
        # pega do objeto OV_obj a lista de ventiladores atualizada
        lista_vent = OV_obj.get_lista_vent()
        # exibe os atributos do ventilador
        print(lista_vent[num_vent])
    # exibe os ventiladores
    print("\nStatus dos ventiladores")
    OV_obj.exibe_vent()

    



# chama a função principal
principal()