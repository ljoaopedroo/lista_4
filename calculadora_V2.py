while True:
    print("1: soma")
    print("2: subtração")
    print("3: multiplicação")
    print("4: divisão")
    print("0: sair")
    operaçao = int(input("Escolha uma das opções acima: "))
    if operaçao == 0:
        break
    n1 = float(input("Digite o primeiro número da operação: "))
    n2 = float(input("Digite o segundo número da operação: "))
    if operaçao == 1:
        resultado = n1 + n2
        print(f"O resultado é {resultado}")
    elif operaçao == 2:
        resultado = n1 - n2
        print(f"O resultado é {resultado}")
    elif operaçao == 3:
        resultado = n1 * n2
        print(f"O resultado é {resultado}")
    elif operaçao == 4:
        if n2 == 0:
            print("Operação inválida")
        else:
            resultado = n1 / n2
            print(f"O resultado é {resultado}")
print("Calculadora encerrada")
