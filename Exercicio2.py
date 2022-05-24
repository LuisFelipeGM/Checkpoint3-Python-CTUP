print("Exercicio 02\n")

carros = [0,0,0,0,0]
consumo = [0,0,0,0,0]
litros = [0,0,0,0,0]
gasto = [0,0,0,0,0]
cont = 0

for i in range(5):
    carros[i] = input(f"Digite o {i + 1}° carro: ")
    consumo[i] = float(input(f"Digite quantos km/l o {i + 1}° carro faz:"))
    if consumo[i] >= cont:
        cont = consumo[i]
        car_eco = carros[i]
    litros[i] = 1000 / consumo[i]
    gasto[i] = litros[i] * 6.89

print("\nResultado Final: ")
for i in range(5):
    print(f"Carro {i + 1}: {carros[i]}  - KM/L {consumo[i]}  - {litros[i]:0.2f} litros  - R$ {gasto[i]:0.2f}")
print(f"\nCarro mais economico: {car_eco}")
