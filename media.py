numero = int(input("Digite um número: "))
lista_numeros = [numero]
divisao = 1
while True:
    numero = int(input("Digite outro número: "))
    if numero == -1:
        break
    lista_numeros.append(numero)
    divisao += 1
media = sum(lista_numeros) / divisao
print(f"A média dos valores é: {media:.2f}")