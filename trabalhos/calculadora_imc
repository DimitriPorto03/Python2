x = float(input("Digite o seu peso em quilos: "))
y = float(input("DIgite a sua altura em metros: "))

imc = x/(y**2)
print(f"{imc:.2f}")

if x<= 0 or y <= 0:
    print("Digite um valor válido para peso e altura.")
else:
    if imc<18.5:
        print("Você está abaixo do peso.")
    elif imc>=18.5 and imc<25.0:
        print("Seu peso está normal.")
    elif imc>=25.0 and imc<30.0:
        print("Você está com sobrepeso.")
    elif imc>=30.0 and imc<35.0:
        perda=x*0.2
        print("Seu peso está com obesidade em grau 1, precisa perder cerca de ", perda, "quilos.")
    elif imc>=35.0 and imc<40.0:
        perda=x*0.3
        print("Seu peso está com obesidade em grau 2, precisa perder cerca de ", perda, "quilos.")
    else:
        perda=x*0.4
        print("Seu peso está com obesidade em grau 3, precisa perder cerca de ", perda, "quilos.")
