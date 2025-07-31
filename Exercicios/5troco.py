# Exercício: Calculadora de Troco

# Este programa calcula o troco a ser devolvido ao cliente após uma compra.

def calcular_troco(preco_unitario, quantidade, dinheiro_pago):
    """Calcula o troco a ser devolvido ao cliente."""
    valor_total = preco_unitario * quantidade

    if dinheiro_pago < valor_total:
        return f"\nSinto muito. Seu dinheiro é insuficiente."
    
    troco = dinheiro_pago - valor_total
    return f"\nSeu troco é de R$ {troco:.2f}"

print("-------------Bem-vindo à Calculadora de Troco!-------------")
print("\nPor favor, forneça os seguintes dados:\n")

# Etapa de Otimização 

# PASSO 1: Obter e validar o preço
try:
    preco_unitario = float(input("Digite o preço unitário do produto: R$ "))
    if preco_unitario <= 0:
        print("Erro: O preço deve ser um número maior que zero.")
        exit() # Encerra o programa se o preço for inválido
except ValueError:
    print("Erro: Preço inválido. Você deve digitar um número.")
    exit() # Encerra o programa se a entrada não for um número

# PASSO 2: Obter e validar a quantidade
try:
    quantidade = int(input("Digite a quantidade comprada: "))
    if quantidade <= 0:
        print("Erro: A quantidade deve ser um número inteiro maior que zero.")
        exit() # Encerra o programa se a quantidade for inválida
except ValueError:
    print("Erro: Quantidade inválida. Você deve digitar um número inteiro.")
    exit() # Encerra o programa se a entrada não for um número inteiro

# PASSO 3: Obter e validar o dinheiro pago
try:
    dinheiro_pago = float(input("Digite o valor pago: R$ "))
    if dinheiro_pago <= 0:
        print("Erro: O valor pago deve ser maior que zero.")
        exit() # Encerra o programa se o valor for inválido
except ValueError:
    print("Erro: Valor pago inválido. Você deve digitar um número.")
    exit() # Encerra o programa se a entrada não for um número

# PASSO 4: Se todas as entradas foram válidas, calcular e mostrar o resultado
resultado_final = calcular_troco(preco_unitario, quantidade, dinheiro_pago)
print(resultado_final)



''''''''''
def dados(precoUnitario, quantidade, dinheiroPago):
    print("--------Calculadora de Troco--------")
    # Entrada de dados
   
    # Solicita o preço unitário do produto e a quantidade comprada
precoUnitario = float(input("Digite o preço unitário do produto: R$ "))
quantidade = int(input("Digite a quantidade comprada: "))
dinheiroPago = float(input("Digite o valor pago: R$ "))
# Função para conferir se a quantidade é válida
def confereQuantidade(quantidade):
     if quantidade <= 0:
        return "Quantidade inválida. Deve ser maior que zero."
     if quantidade != int(quantidade):
        return "Quantidade inválida. Deve ser um número inteiro."
     else:
         return quantidade

funcao_confereQuantidade = int(confereQuantidade(quantidade))

def troco(precoUnitario, funcao_confereQuantidade, dinheiroPago):
    """Calcula o troco a ser devolvido ao cliente."""
    valorTotal = precoUnitario * funcao_confereQuantidade
    if dinheiroPago < valorTotal:
        return "\nSinto muito. Seu dinheiro é insuficiente."
    troco = dinheiroPago - valorTotal
    return f"Seu troco é de R$ {troco:.2f}"
# Deve ser um número inteiro maior que zero

resultado = troco(precoUnitario, funcao_confereQuantidade, dinheiroPago)
print(resultado)
'''