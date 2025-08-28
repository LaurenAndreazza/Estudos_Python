def calculadora():
    while True: #Continua a opração após on inicio
        print("Selecione a operação:")
        print()
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("s. Sair")
        operacao = input("Digite a operação desejada ou 's' para sair: ")

        if operacao == 's' or operacao == 'S':
            print("Encerrando a calculadora. Até mais!")
            break #Sai do loop e encerra a calculadora

        if operacao not in ['1', '2', '3', '4']:
            print("Operação inválida. Tente novamente.")
            continue 

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if operacao == '1':
            resultado = num1 + num2
            print(f"Resultado: {resultado}")
        elif operacao == '2':
            resultado = num1 - num2
            print(f"Resultado: {resultado}")
        elif operacao == '3':
            resultado = num1 * num2
            print(f"Resultado: {resultado}")
        else: #Cuidar para que o ultimo sempre seja else
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")

calculadora()