qth = 0
qtm = 0

for i in range(10):
    nome = input("Digite Nome:")
    sexo = input("digite F para Feminino ou M para masculino : ")
if sexo == "M":
    qth += 1
elif sexo == "F":
    qtm += 1
else:
    print("digite F para Feminino ou M para masculino : ")

    print(f"Quantidade de Homens : {qth} - Quantidade de Mulheres : {qtm}")


