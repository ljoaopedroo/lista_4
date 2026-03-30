count = 1
lista_par= []
qnt_par = 0
lista_impar = []
qnt_impar = 0

while count <= 10:
    numero = int(input("Digite um número: "))
    count += 1
    if numero % 2 == 0:
        lista_par.append (1)
        qnt_par = sum(lista_par)
    else:
        lista_impar.append(1)
        qnt_impar = sum(lista_impar)
print(f"Essa é quantidade de números pares: {qnt_par}")
print(f"Essa é quantidade de números ímpares: {qnt_impar}")