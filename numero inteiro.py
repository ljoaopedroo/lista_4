limite = int(input("Digite um número inteiro: "))
soma = 0
contador = 1 

while contador <= limite:
    soma += contador
    contador += 1
print(f"A soma de 1 ate {limite} é {soma}")