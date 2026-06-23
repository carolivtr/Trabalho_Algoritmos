from notas import calcular_media

def ordenar_por_nome(alunos):
    lista = []
    for aluno in alunos:
        lista.append(aluno)
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j]["nome"].lower() > lista[j + 1]["nome"].lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def ordenar_por_nota(alunos, matriz_notas):
    lista = []
    for i in range(len(alunos)):
        media = calcular_media(matriz_notas[i])
        lista.append([alunos[i], media])
    # Bubble Sort pela media, maior primeiro
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j][1] < lista[j + 1][1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
