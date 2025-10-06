import streamlit as st
from crud import criar_aluno, listar_aluno, atualizar_aluno, deletar_aluno

st.set_page_config(page_title="gerenciamento de alunos", page_icon="👨‍🎓")

st.title("Sistema de aluno com postgreSQL")

menu = st.sidebar.radio("Menu", ["Criar", "listar", "Atualizar", "Deletar"])


if menu =="Criar":
    st.subheader("➕ criar aluno")
    nome = st.text_input("Nome")
    idade = st.number_input("Idade", min_value=14, step=1)
    if st.button("Cadrastar"):
        if nome.strip() != "":
            criar_aluno(nome, idade)
            st.success(f"Aluno {nome} foi cadrastado com sucesso")
        else:
            st.warning("O campo nome não pode estar vazio")
elif menu == "listar":
    st.subheader("Lista de alunos")
    alunos = listar_aluno()
    if alunos:
        st.table(alunos)
    else:
        st.info("Nenhum aluno encontrado")

elif menu == "Atualizar":
    st.subheader("Atualizar idade")
    alunos = listar_aluno()
    if alunos:
        id_aluno = st.selectbox("Escolha aluno", [aluno[0] for aluno in alunos] )
        nova_idade = st.number_input("Nova idade", min_value=10, step=1)
        if st.button("Atualizar"):
            atualizar_aluno(id_aluno, nova_idade)
            st.success(f"idade aluno {id_aluno} atualizada com sucesso")
        else:
            st. info("Nenhum aluno disponivel para atualizar")

elif menu == "Deletar":
    st.subheader("Deletar aluno")
    alunos = listar_aluno()
    if alunos:
        id_aluno = st.selectbox("Esvolha o id para deletar",[linha[0] for linha in alunos])
        if st.button("Deletar"):
            deletar_aluno(id_aluno)
            st.success(f"aluno id  {id_aluno} deletado com sucesso")
        else:
            st.info("Nenhum aluno disponivel para deletar")