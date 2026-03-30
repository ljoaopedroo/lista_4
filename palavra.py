palavra = input("Digite uma palavra: ")
numero = len(palavra)

while numero < 3 or numero > 10:
    print("Palavra invalida")
    palavra = input("Digite outra palavra: ")
    numero = len(palavra)
print(f"A palavra é {palavra} e tem {numero} letras")