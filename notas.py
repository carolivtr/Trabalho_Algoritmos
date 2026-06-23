NUM_NOTAS = 3

def inicializar_notas(matriz_notas):
    linha = []
    for i in range(NUM_NOTAS):
        linha.append(-1)
    matriz_notas.append(linha)
def cadastrar_notas(alunos, matriz_notas):
    matricula = input("Matricula do aluno: ")
    indice = -1
    for i in range(len(alunos)):
        if alunos[i]["matricula"] == matricula:
            indice = i
            break
    if indice == -1:
        print("Aluno nao encontrado.")
        return
    print("Aluno:", alunos[indice]["nome"])
    for i in range(NUM_NOTAS):
        while True:
            try:
                nota = float(input("Nota " + str(i + 1) + ": "))
                if 0 <= nota <= 10:
                    matriz_notas[indice][i] = nota
                    break
                else:
                    print("A nota deve ser entre 0 e 10.")
            except ValueError:
                print("Digite um numero valido.")
    print("Notas cadastradas com sucesso!")

def calcular_media(linha_notas):
    soma = 0
    quantidade = 0
    for nota in linha_notas:
        if nota != -1:
            soma = soma + nota
            quantidade = quantidade + 1
    if quantidade == 0:
        return -1
    return round(soma / quantidade, 2)
def situacao(media):
    if media == -1:
        return "Sem notas"
    elif media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"
def relatorio(alunos, matriz_notas):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print("\n- RELATORIO -")
    for i in range(len(alunos)):
        media = calcular_media(matriz_notas[i])
        sit = situacao(media)
        notas_str = ""
        for j in range(NUM_NOTAS):
            if matriz_notas[i][j] == -1:
                notas_str = notas_str + "N" + str(j + 1) + ": ---  "
            else:
                notas_str = notas_str + "N" + str(j + 1) + ": " + str(matriz_notas[i][j]) + "  "
        if media == -1:
            media_str = "---"
        else:
            media_str = str(media)
        print(alunos[i]["nome"], "| Matricula:", alunos[i]["matricula"])
        print("  Notas:", notas_str)
        print("  Media:", media_str, "| Situacao:", sit)
        print()
