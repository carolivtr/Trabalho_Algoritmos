from aluno import cadastrar_aluno, listar_alunos
from notas import cadastrar_notas, relatorio, inicializar_notas
from busca import buscar_por_nome, buscar_por_matricula
from ordenacao import ordenar_por_nome, ordenar_por_nota
from utils import menu

alunos = []
matriz_notas = [] 

while True:
    opcao = menu()
    if opcao == "1":
        cadastrar_aluno(alunos)
        inicializar_notas(matriz_notas)  # cria linha vazia na matriz
    elif opcao == "2":
        listar_alunos(alunos)
    elif opcao == "3":
        tipo = input("Buscar por (nome/matricula): ").lower()
        if tipo == "nome":
            nome = input("Nome: ")
            resultado = buscar_por_nome(alunos, nome)
            if resultado:
                print("\n- RESULTADO -")
                for aluno in resultado:
                    print("Matricula:", aluno["matricula"], "| Nome:", aluno["nome"], "| Curso:", aluno["curso"])
            else:
                print("Aluno nao encontrado.")
        else:
            matricula = input("Matricula: ")
            resultado = buscar_por_matricula(alunos, matricula)
            if resultado:
                print("Matricula:", resultado["matricula"], "| Nome:", resultado["nome"], "| Curso:", resultado["curso"])
            else:
                print("Aluno nao encontrado.")
    elif opcao == "4":
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            lista = ordenar_por_nome(alunos)
            print("\n- ORDENADOS POR NOME -")
            for aluno in lista:
                print("Matricula:", aluno["matricula"], "| Nome:", aluno["nome"])
    elif opcao == "5":
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            lista = ordenar_por_nota(alunos, matriz_notas)
            print("\n- ORDENADOS POR MEDIA -")
            for aluno, media in lista:
                if media == -1:
                    print(aluno["nome"], "| Media: ---")
                else:
                    print(aluno["nome"], "| Media:", media)
    elif opcao == "6":
        cadastrar_notas(alunos, matriz_notas)
    elif opcao == "7":
        relatorio(alunos, matriz_notas)
    elif opcao == "0":
        print("Encerrando sistema...")
        break
    else:
        print("Opcao invalida.")
