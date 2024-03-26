x = int(input("Digite um número de dois dígitos (menor que 100): "))
if x>=100:
    print("O número é maior que 100.")
else:
    dezena= x//10
    unidade= x%10
    soma = dezena + unidade
    print(soma)

