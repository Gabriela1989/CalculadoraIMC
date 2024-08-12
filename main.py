def calcular_imc(peso, altura):
    # Calcula o IMC usando a fórmula Peso / Altura²
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    # Classifica o IMC de acordo com os intervalos definidos
    if imc < 18.5:
        return "Magreza"
    elif 18.5 <= imc < 24.9:
        return "Normal"
    elif 24.9 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    # Solicita ao usuário o peso e a altura
    try:
        peso = float(input("Digite o seu peso (em kg): "))
        altura = float(input("Digite a sua altura (em metros): "))
        
        # Calcular IMC
        imc = calcular_imc(peso, altura)
        
        # Classificar IMC
        classificacao = classificar_imc(imc)
        
        # Exibir o resultado
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos para peso e altura.")

# Executar o programa
if __name__ == "_main_":
    main()
