print("Exercicio 01\n")

continuar = "sim"
saltos = [0, 0, 0, 0, 0]
soma = 0

while continuar == "sim" or "s":
    nome = input("Digite o Nome do Atleta: ")
    for i in range(5):
        saltos[i] = float(input(f"Digite o {1 + i}° salto: "))
    print(f"\nResultado Final: \nAtleta: {nome}")
    for i in range(5):
        print(f"{i + 1}° Salto: {saltos[i]}")
        soma += saltos[i]
    print(f"Média de Saltos : {soma / 5} m")
    continuar = input("Deseja continuar o programa? ")
