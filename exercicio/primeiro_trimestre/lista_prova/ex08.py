lado1 = float(input("Digite a medida do primeiro lado: "))
lado2 = float(input("Digite a medida do segundo lado: "))
lado3 = float(input("Digite a medida do terceiro lado: "))

if lado1==0 or lado2==0 or lado3==0:
    print("Suas medidas não correspondem com um triângulo.")
else:
    if lado1==lado2 and lado1==lado3:
        print("Seu triângulo é do tipo equilátero.")
    elif lado1!=lado2 and lado1==lado3 or lado1==lado2 and lado1!=lado3 or lado2==lado1 and lado2!=lado3 or lado2!=lado1 and lado2==lado3:
        print("Seu triângulo é do tipo isósceles.")
    else:
        print("Seu triângulo é do tipo escaleno.")
