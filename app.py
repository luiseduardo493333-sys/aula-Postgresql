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