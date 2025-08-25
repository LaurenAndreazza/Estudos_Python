import random # carrega métodos para geração de números aleatórios, por exemplo randint

class Lampada: # Classe com os atributos e métodos da lâmpada
    def __init__(self, identificador: str, ciclo: int, status: int): # Construtor da classe para definir os valores iniciais que um objeto terá quando for instanciado
        self.identificador = identificador # self.identificador recebe o valor do parâmetro de entrada identificador
        self.status = status # 0:desligada 1:ligada 2:queimada Inicialmente ela está desligada
        self.ciclo = ciclo # sel.ciclo recebe o valor do parâmetro de entrada ciclo, que é o número de ciclos que a lâmpada possui
    def aleatorio_bool(self, ini: int, fim: int, alvo:int) -> bool: # Método que retorna False ou True de acordo com um sorteio 
        if ini > fim: ini, fim = fim, ini  # Se início do intervalo for maior do que o fim, troca os valores entre ini e fim
        if random.randint(ini,fim) == alvo: return True # Se o número aleatório gerado for igual ao número alvo, informado como entrada do método, retorna True
        else: return False # Se o número gerado não for igual ao número alvo, retorna False
    def pressionar_interruptor(self) -> int: # Método para acionar o interruptor
        if self.status == 0: # se o interruptor está desligado, executa:
            if self.aleatorio_bool(self.ciclo,200,200): # se o a lampada foi sorteada para queimar, execute:
                self.status = 2 # passa o status para queimado
            else: # se a lampada não queimou, executa:
                self.status = 1 # passa para o status ligado
                self.ciclo += 1 # o ciclo é incrementado com uma unidade (x+=1 é o mesmo que x=x+1)
        elif self.status == 1: # se o interruptor está ligado, executa:
            self.status = 0 # passa para o status desligado
        return self.ciclo, self.status # Retorna a quantidade de ciclos e o status
    def __str__(self) -> str: # Executa saída no terminal quando o objeto é chamado
        msg = ["","",""] # inicializa lista local msg
        estado = "" # inicializa variável local estado
        if self.status == 0: estado = "DESLIGADA" # estado recebe "LIGADA" se a lâmpada está ligada
        elif self.status == 1: estado = "LIGADA" # estado recebe "DESLIGADA" se a lâmpada está ligada
        else: estado = "QUEIMADA" # estado recebe "QUEIMADA" se a lâmpada está ligada
        msg[0] = f"[{self.identificador}]" # msg[0] recebe o identificador da lâmpada
        msg[1] = f"[Estado atual: {estado}]" # msg[1] recebe o estado atual da lâmpada
        msg[2] = f"[Ciclo: {self.ciclo}]" # msg[2] recebe o ciclo de vida da lâmpada
        return msg[0]+msg[1]+msg[2] # Retorna as mensagens concatenadas pelos elementos da lista msg
    def exibe_id(self) -> str: # Exibe o identificador da lampada
        return f"{self.identificador}" # retorna o identificador da lâmpada
    def exibe_estado(self) -> str: # Exime
        if self.esta_ligada: estado = "LIGADA" # estado recebe "LIGADA" se a lâmpada está ligada
        else: estado = "DESLIGADA" # estado recebe "DESLIGADA" se a lâmpada está desligada
        return f"[Estado atual: {estado}]" # retorna o estado atual da lâmpada
    def exibe_ciclo(self) -> str:
        return f"[Ciclo: {self.ciclo}]" # retorna o ciclo de vida da lâmpada
    def exibe_status(self) -> str:
        return f"[Status: {self.status}]" # retorna o status da lâmpada
    
    
class TesteLampada: # Classe com as ferramentas para ligar e desligar as lâmpadas
    def consiste_str(self, opt1: str, opt2: str, prompt: str) -> str: # Método para fazer a consistência de um uma opção do tipo string lida
        opt = "" # A aopção é inicializado com vazio
        while opt not in (opt1, opt2): # Enquando a opção não for igual às opções informadas como parâmetros de entrada do método executa:
            opt = input(prompt).upper() # lê opção via teclado e passa para maiúscula
            if opt not in (opt1, opt2): print("ERRO - Opção inválida") # mensagem de erro se a opção não for opt1 e nem opt2
        return opt # Se a opção for igual a opt1 ou opt2, retorna a opção
    def consiste_int(self, ini: int, fim: int, prompt: str) -> int: # Método para fazer a consistência de um valor inteiro no intervalo especificado
        opt = fim + 1 # seta o valor para depois do final do intervalo (depois do fim, que é informado como parâmetro de entrada)
        while not (ini <= opt <= fim): # Se valor estiver fora do intervalo executa:
            try: # Tenta executar sem erros:
                opt = int(input(prompt)) # Lê um número inteiro via teclado (dentro do try)
                if not (ini <= opt <= fim): print("ERRO - Valor fora do intervalo") # Se o valor for inteiro, mas estiver fora do intervalo, exibir mensagem de erro
            except: print("ERRO - Valor não inteiro") # Se o valor lido via teclado não for inteiro, exibe mensagem de erro
        return opt # Retorna o valor lido no intervalo definido pelos parâmetros de entrada informados ini e fim
    def arquivo_leitura(self, nomearq: str) -> list: # Método para fazer a leitura do arquivo identificado por nomearq
        lista = [0,0,0,0,0] # define a lista com 0, que será usado se o arquivo não existir
        try: # Tenta executar sem erros:
            with open(nomearq,"r") as arq_read: lista = arq_read.readlines() # Abre e lê o arquivo armazenando os valores na lista
            lista = list(map(int, lista)) # Converte a linha lida em um inteiro para cada elemento de lista
        except FileNotFoundError: # Se o erro for na abertura do arquivo executar:
            print("ERRO - Arquivo não encontrado") # Mensagem de erro na abertura do arquivo
        return lista # retorna a lista com os valores lidos do arquivo
    def arquivo_escrita(self, lista, nomearq): # Método para sobrescrever os valores no arquivo identificado por nomearq
        try: # Tenta executar sem erros:
            lista = list(map(lambda i: str(i) + "\n", lista)) # Converte cada elemento da lista de inteiro para string usando uma função lambda(1)
            with open(nomearq,"w") as arq_write: arq_write.writelines(lista) # Abre o arquivo e sobrescreve os valores, um em cada linha do arquivo
        except FileNotFoundError: # Se arquivo não pode ser aberto (se ele não existe, é criado, mas pode dar erro na criação) executa:
            print("ERRO - Arquivo não encontrado") # Exibe mensagem de erro de arquivo não encontrado
    def aleatorio_int(self, ini: int, fim: int) -> int: # Método para geração de um número aleatório no intervalo niformado como parâ metro de entrada
        if ini > fim: ini, fim = fim, ini # Se início do intervalo for maior do que o fim, troca os valores entre ini e fim
        return random.randint(ini, fim) # Retorna valor gerado no intervalo
                
if __name__ == "__main__": # Se o nome do trecho de código é "__main__" executa:
    TL_obj = TesteLampada() # Instancia o objeto TL_obj da classe TesteLampada para se ter acesso aos métodos
    lista_ciclos = TL_obj.arquivo_leitura("ciclos.txt") # lista_ciclos recebe os ciclos das lampadas obtidos do arquivo ciclos.txt
    lista_status = TL_obj.arquivo_leitura("status.txt") # lista_status recebe os status das lampadas obtidos do arquivo status.txt
    sala = [ # Instancia 5 objetos a patir da classe Lampada com os parâmetros de identificação e número do cilco para cada lâmpada
        Lampada("Lâmpada 1 (Perto da porta)", lista_ciclos[0], lista_status[0]),
        Lampada("Lâmpada 2 (Centro-Esquerda)", lista_ciclos[1], lista_status[1]),
        Lampada("Lâmpada 3 (Centro-Direita)", lista_ciclos[2], lista_status[2]),
        Lampada("Lâmpada 4 (Fundo-Esquerda)", lista_ciclos[3], lista_status[3]),
        Lampada("Lâmpada 5 (Perto da janela)", lista_ciclos[4], lista_status[4])
    ]
    qtd_testes = TL_obj.consiste_int(1,100,"Número de testes [1- 100]:") # Lê, via teclado, a quantidade de testes
    for ct_teste in range(qtd_testes): # Loop com a quantidade de testes executa:
        print("=" * 40) # Separador das lampadas no teste
        sorteada = TL_obj.aleatorio_int(0,4) # Sorteia um dos 5 objetos lâmpada
        lista_ciclos[sorteada], lista_status[sorteada] = sala[sorteada].pressionar_interruptor() # A lâmpada sorteada tem o seu interruptor pressionado
        print(sala[sorteada]) # Exibe mensagem da lâmpada com sua identificação e status
    TL_obj.arquivo_escrita(lista_ciclos, "ciclos.txt") # Salva os ciclos das lampadas atualizados no arquivo ciclos.txt
    TL_obj.arquivo_escrita(lista_status, "status.txt") # Salva os status das lampadas atualizados no arquivo status.txt
    print("Ciclos das lampadas " + ("=" * 20))
    for lamp in sala: print(lamp.exibe_id(), lamp.exibe_ciclo(), lamp.exibe_status())
    print("=" * 40)