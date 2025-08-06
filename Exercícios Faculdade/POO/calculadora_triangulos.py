print("Seja bem-vindo a Classificação de triângulos")


L1 = int(input("Coloque o primeiro lado: "))
L2 = int(input("Coloque o segundo lado: "))
L3 = int(input("Coloque o terceiro lado: "))



## Tipos de triângulos
def triangulo(L1, L2, L3):
    if (L1 + L2 > L3) and (L1 + L3 > L2) and (L2 + L3 > L1):
        return confereLado(L1, L2, L3)
    else:
        return "Não é um triângulo"
    
def confereLado(L1, L2, L3):

    if ( L1 == L2 == L3 ):
        return("Triângulo Equilátero")
    elif ( L1 == L2 or L1 == L3 or L2 == L3 ):
        return("Triângulo Isósceles")
    elif ( L1 != L2 and L1 != L3 and L2 != L3 ):
        return("Triângulo Escaleno")

      

def confereAngulo(L1, L2, L3):
    if (L1**2 == L2**2 + L3**2) or (L2**2 == L1**2 + L3**2) or (L3**2 == L1**2 + L2**2):
        return("Retângulo")
    elif (L1**2 > L2**2 + L3**2) or (L2**2 > L1**2 + L3**2) or (L3**2 > L1**2 + L2**2):
        return("Obtusângulo")
    elif (L1**2 < L2**2 + L3**2) or (L2**2 < L1**2 + L3**2) or (L3**2 < L1**2 + L2**2):
        return("Acutângulo")

print (f"{triangulo(L1, L2, L3)} e foi classificado como {confereAngulo(L1, L2, L3)}")

#Ideia de upgrade: Colocar a opção de calcular o perímetro e a área do triângulo.
#Fazer um loop para que o usuário possa fazer várias classificações sem precisar reiniciar o programa.
#Adicionar tratamento de erros para entradas inválidas (ex: letras, números negativos, etc).
#Adicionar uma interface gráfica para tornar o programa mais amigável.