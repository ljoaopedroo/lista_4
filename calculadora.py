print("1: soma")
print("2: subtração")
print("3: multiplicação")
print("4: divisão")
print("0: sair")
operaçao = int(input("Escolha uma das opções acima: "))

while operaçao != 0:
    
    if operaçao == 1:
        n1 = int(input("Digite o primeiro número da operação: "))
        n2 = int(input("Digite o segundo número da operação: "))
        resultado = n1 + n2
        print(f"O resultado é {resultado}")
        print("1: soma")
        print("2: subtração")
        print("3: multiplicação")
        print("4: divisão")
        print("0: sair")
        operaçao = int(input("Escolha uma das opções acima: "))
        
    elif operaçao ==  2:
        n1 = int(input("Digite o primeiro número da operação: "))
        n2 = int(input("Digite o segundo número da operação: "))
        resultado = n1 - n2
        print(f"O resultado é {resultado}")
        print("1: soma")
        print("2: subtração")
        print("3: multiplicação")
        print("4: divisão")
        print("0: sair")
        operaçao = int(input("Escolha uma das opções acima: "))
    
    elif operaçao == 3:
        n1 = int(input("Digite o primeiro número da operação: "))
        n2 = int(input("Digite o segundo número da operação: "))
        resultado = n1 * n2
        print(f"O resultado é {resultado}")
        print("1: soma")
        print("2: subtração")
        print("3: multiplicação")
        print("4: divisão")
        print("0: sair")
        operaçao = int(input("Escolha uma das opções acima: "))
    
    elif operaçao == 4:
        n1 = int(input("Digite o dividendo: "))
        n2 = int(input("Digite o divisor: "))
        if n2 == 0:
            print("Operação inválida")
        else:
            resultado = n1 / n2
            print(f"O resultado é {resultado:.2f}")
            print("1: soma")
            print("2: subtração")
            print("3: multiplicação")
            print("4: divisão")
            print("0: sair")
            operaçao = int(input("Escolha uma das opções acima: "))
print("Calculadora encerrada")