meuamor = "madu, me diga"

amordeMadu = float(input("Diga o quanto me ama:"))

def calcular_amor(amordeMadu):

    if amordeMadu< 100:
        return "não me ama o suficiente"
    else:
        return "Acho que ta bom"

print(calcular_amor(amordeMadu))