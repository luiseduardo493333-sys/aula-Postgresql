from db import conectar

def criar_aluno(nome, idade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO alunos (nome,idade)  VALUES (%s, %s)",
                (nome, idade)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir {erro}")
        finally:
            cursor.close()
            conexao.close()

criar_aluno("Luis Eduardo", 17)

def listar_aluno(nome, idade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM alunos ORDER BY id"
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao listar {erro}")
            return[]
        finally:
            cursor.close()
            conexao.close()


def listar_aluno(id_aluno, nova_idade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE alunos SET idade= %s WHERE id = %s",
                (nova_idade, id_aluno)
            )
        except Exception as erro:
            print(f"Erro ao atualizar um aluno:  {erro}")
        finally:
            cursor.close()
            conexao.close()

