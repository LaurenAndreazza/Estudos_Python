# Função para obter os dados de uma pessoa
def obter_dados_pessoa(numero_da_pessoa):
    """Pede os dados de uma pessoa e retorna um dicionário."""
    print(f"\n--- Forneça os dados da Pessoa {numero_da_pessoa} ---")
    nome = input("Nome: ")
    idade = input("Idade: ")
    cidade = input("Cidade: ")
    # Cria e retorna o dicionário com as informações
    return {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }

# --- Início do Programa Principal ---

# 1. Mostra a instrução inicial
print("--- Bem-vindo ao Sistema de Cadastro ---")

# 2. Chama a função para obter os dados de cada pessoa
pessoa1 = obter_dados_pessoa(1)
pessoa2 = obter_dados_pessoa(2)
# Se quisesse uma terceira pessoa, era só adicionar: pessoa3 = obter_dados_pessoa(3)

# 3. Mostra o resultado final
print("\n--- Resumo dos Dados Cadastrados ---")
print(f"Pessoa 1: {pessoa1}")
print(f"Pessoa 2: {pessoa2}")