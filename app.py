#Função para calcular o imc
def calcular_imc(peso, altura):
    resultado = peso / (altura ** 2)
    return resultado

# Função para classificar o imc
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"
    
# Função para sugerir calorias diárias com base na idade
def sugestao_calorias(idade):
    if idade < 18:
        return 2200
    elif idade < 60:
        return 2000
    else:
        return 1800
    
#Função principal    
def main():
    while True:
        print("Calculadora de IMC e Sugestão de Calorias")
        print("=========================================")
        print("Informe seu nome, idade, peso e altura para calcular seu IMC e sugerir calorias diárias.\n")
        nome = input("Insira seu nome: ")
        idade = int(input("Informe sua idade: "))
        peso = float(input("Informe seu peso em quilos: "))
        altura = float(input("Informe sua altura em metros: "). replace(',', '.'))
        print("\nCalculando...\n")
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        print(f"{nome}, seu IMC é: {imc:.2f} e você está classificado como: {classificacao}")
        calorias = sugestao_calorias(idade)
        print(f"Você deve consumir cerca de {calorias} calorias por dia.\n")

if __name__ == "__main__":
    main()