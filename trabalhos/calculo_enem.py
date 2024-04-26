def calcular_media_enem():
    notas = []
    areas_conhecimento = ["Linguagens", "Humanas", "Natureza", "Matematica", "Redacao"]

    for area in areas_conhecimento:
        nota = float(input(f"Digite a nota de {area}: "))
        if nota < 0 or nota > 1000:
            print(f"Por favor, insira uma nota válida para {area}")
            return
        notas.append(nota)

    if notas[4] == 0:
        print("A nota da redação não pode ser zero. O aluno está reprovado.")
        return

    media = calcular_media(notas)
    status = "Aprovado" if media >= 450 else "Reprovado"
    mensagem = f"Sua média final no ENEM é: {media:.2f}\nStatus: {status}"

    print(mensagem)

def calcular_media(notas):
    total = sum(notas)
    return total / len(notas)

calcular_media_enem()
