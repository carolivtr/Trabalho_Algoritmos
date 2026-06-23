def buscar_por_nome(alunos, nome):
    resultado = []
    for aluno in alunos:
        if nome.lower() in aluno["nome"].lower():
            resultado.append(aluno)
    return resultado

def buscar_por_matricula(alunos, matricula):
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None
