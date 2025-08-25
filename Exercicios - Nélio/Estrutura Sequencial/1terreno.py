largura = float(input(f"Digite a largura do terreno em metros: "))
comprimento = float(input("Digite o comprimento do terreno em metros: "))
area = largura * comprimento

preco = float(input("Digite o preço por metro quadrado: "))
custo_total = ((area) * (preco))

print(f"A área do terreno é: {area:.2f} metros quadrados")
print(f"O custo total do terreno é: R$ {custo_total:.2f}")

