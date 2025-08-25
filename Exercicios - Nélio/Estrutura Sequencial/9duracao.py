
print("Seja bem-vindo ao conversor de segundos para horas, minutos e segundos!")

segundos = int(input("Digite a quantidade de segundos que deseja converter: "))
   
def converter_Segundos (segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60

    exibir_resultado = f"{horas} horas, {minutos} minutos e {segundos_restantes} segundos."
    return exibir_resultado

print(f"A conversão de {segundos} segundos é igual a: {converter_Segundos(segundos)}")

    