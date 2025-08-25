import math

Base_Retangulo = float(input("Digite a base do retângulo em metros: "))

Altura_Retangulo = float(input("Digite a altura do retângulo em metros: "))
                               
Area = Base_Retangulo * Altura_Retangulo
Perimetro = 2 * (Base_Retangulo + Altura_Retangulo)

# Usando a operação de potência
Diagonal = (Base_Retangulo**2 + Altura_Retangulo**2)**0.5

print(f"A área do retângulo é: {Area:.4f}")
print(f"O perímetro do retângulo é: {Perimetro:.4f}")
print(f"A diagonal do retângulo é: {Diagonal:.4f}")

