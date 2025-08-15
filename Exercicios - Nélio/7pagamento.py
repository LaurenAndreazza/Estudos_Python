def obter_dados_funcionario():
    nome = str(input("Digite o nome do funcionário: "))
    salarioHora = float(input("Digite o Salário por hora do funcionário: "))
    horasTrabalhadas = int(input("Digite o número de horas trabalhadas no mês: "))
    return nome, salarioHora, horasTrabalhadas


def calcular_salario(nome, salarioHora, horasTrabalhadas):

    if salarioHora < 0 or horasTrabalhadas < 0:
        print("Salário por hora e horas trabalhadas devem ser valores não negativos.")
        return salarioHora,horasTrabalhadas
    elif salarioHora == 0 or horasTrabalhadas == 0:
        print("Salário por hora e horas trabalhadas não podem ser zero.")
        return salarioHora,horasTrabalhadas

    salarioMensal = salarioHora * horasTrabalhadas
    print(f"O salário mensal de {nome} é: {salarioMensal:.2f}")


calcular_salario(*obter_dados_funcionario())
