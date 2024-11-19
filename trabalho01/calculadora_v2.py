

saida = ''


def adicao(a, b):
    return a + b

# Função para subtração
def subracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

def calculadora(num1, num2, operacao):
    if operacao == "+" or operacao == "adicao":
        resultado = adicao(num1, num2)
    elif operacao == "-" or operacao == "subtracao":
        resultado = subracao(num1, num2)
    elif operacao == "*" or operacao == "multiplicacao":
        resultado = multiplicacao(num1, num2)
    elif operacao == "/" or operacao == "divisao":
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    
    return resultado

while saida.lower() != 'n':
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (pode ser +, -, *, / ou o nome da operação): ").strip().lower()
        
        resultado = calculadora(num1, num2, operacao)
        
        print(f"Resultado da operação: {resultado}")
        
        saida = input("Deseja continuar? (S/N): ").strip().lower()
        
    except ValueError:
        print("Por favor, insira números válidos.")
