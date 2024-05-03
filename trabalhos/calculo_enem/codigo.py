import sqlite3 
# Conectar ao banco de dados

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

# Conectar ao banco de dados (se não existir, será criado)
conn = sqlite3.connect('dados_usuarios.db')
cursor = conn.cursor()

# Criar uma tabela se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, notas[] INT, media REAL, status TEXT)''')

# Fechar a conexão com o banco de dados
conn.close()
