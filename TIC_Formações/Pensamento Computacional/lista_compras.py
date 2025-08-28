def lista_compras():
    produtos = []
    print("---------------Seja muito bem-vindo à sua lista de compras!!---------------")

    while True:
        print("Selecione a ação:\n")
        print("A. Adicionar Produto")
        print("B. Remover Produto")
        print("C. Pesquisar Produtos")
        print("D. Sair")

        guardar_itens = input("Digite a ação desejada (A, B, C ou D): ").upper()
        
        #.upper() para aceitar minusculas e maiusculas

        if guardar_itens == 'D':
            print("Saindo...")
            break
        
        if guardar_itens not in ['A', 'B', 'C', 'D']:
            print("Operação inválida. Tente novamente.")
            continue 

        if guardar_itens == 'A':
            nome_A = input("Digite o nome do produto: ")

            print("Tipos de unidades de Medida")
            print ("1. Quilograma")
            print ("2. Grama")
            print ("3. Litro")
            print ("4. Mililitro")
            print ("5. Unidade")
            print ("6. Metro")
            print ("7. Centímetro")

            unidade_medida = input("Digite a unidade de medida do produto: ")
            if unidade_medida not in ['1', '2', '3', '4', '5', '6', '7']:
                print("Unidade de medida inválida. Tente novamente.")
                continue

            quantidade = int(input("Digite a quantidade do produto: "))
            if quantidade <= 0 or not isinstance(quantidade, int): 
                #Verifica se a quantidade é um número inteiro positivo e retorna true
                print("Quantidade inválida. Tente novamente.")
                continue

            descricao = input("Digite a descrição do produto: ")
            produtos.append({
                "nome": nome_A,
                "unidade": unidade_medida,
                "quantidade": quantidade,
                "descricao": descricao
            })
        
        if guardar_itens == 'B':
            nome_B = input("Digite o nome do produto a ser removido: ")
            for produto in produtos:
                if produto["nome"] == nome_B:
                    produtos.remove(produto)
                    print(f"Produto '{nome_B}' removido com sucesso.")
                    break
            else:
                print(f"Produto '{nome_B}' não encontrado.")

        if guardar_itens == 'C':
            nome_C = input("Digite o nome do produto a ser pesquisado: ")
            for produto in produtos:
                if produto["nome"] == nome_C:
                    print(f"Produto encontrado: {produto}")
                    print(f"Quantidade: {produto['quantidade']} {produto['unidade']}")
                    print(f"Descrição: {produto['descricao']}")
                    break
            else:
                print(f"Produto '{nome_C}' não encontrado.")
                continue
lista_compras()