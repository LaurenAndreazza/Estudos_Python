print("Seja bem-vindo ao sistema de cálculo de média")

notas = {
    float(input("Digite a primeira Nota: ")),
    float(input("Digite a segunda Nota: :"))}
somadasnotas = sum(notas)
  
def calcular_media (somadasnotas):

    if somadasnotas < 60:
        return "Reprovado"
    else:
        return "Aprovado"

print(f'NOTA FINAL:{somadasnotas}')
print(calcular_media(somadasnotas))
