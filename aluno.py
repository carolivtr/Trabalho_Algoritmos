def cadastrar_aluno(alunos):
    matricula = input("Matricula: ")
    nome = input("nome: ")
    curso = input("Curso: ")
    aluno = {
        "matricula": matricula,
        "nome": nome,
        "curso": curso
    }
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")

def listar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print("\n- LISTA DE ALUNOS -")
    for aluno in alunos:
        print("Matricula:", aluno["matricula"], "| Nome:", aluno["nome"], "| Curso:", aluno["curso"])
