print("Verifique se sua nota da escola é válida")
nota = int(input("Digite sua nota: "))

while nota < 0 or nota > 10:
    print("Nota inválida")
    nota = int(input("Digite outra nota: "))
print(f"Sua nota é válida e foi {nota}")