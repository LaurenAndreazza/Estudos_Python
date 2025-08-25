print("----------Calculadora de Medidas--------------")

todas_medidas = (
float(input("Digite a primeira medida A: ")),
float(input("Digite a segunda medida B: ")),
float(input("Digite a terceira medida C: "))
)

def calcular_e_exibir_medidas(todas_medidas):

    area_Quadrado = (todas_medidas[0] ** 2)
    area_Triangulo = (todas_medidas[0] * todas_medidas[1]) / 2
    area_trapezio = (todas_medidas[0] + todas_medidas[1]) * todas_medidas[2] / 2

    exibir_resultados =f" ÁREA DO QUADRADO: {area_Quadrado:.4f}\nÁREA DO TRIÂNGULO: {area_Triangulo:.4f}\nÁREA DO TRAPÉZIO: {area_trapezio:.4f}"

    print("\n---------- Resultados ----------")
    print(exibir_resultados)

calcular_e_exibir_medidas(todas_medidas)