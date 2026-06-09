import streamlit as st
from src.manager import TaskManager
from src.api_client import search_books

st.set_page_config(page_title="Study Organizer", page_icon="📚", layout="centered")

if "manager" not in st.session_state:
    st.session_state.manager = TaskManager()

manager: TaskManager = st.session_state.manager

st.title("📚 Study Organizer")
st.caption("Organize suas tarefas de estudo e descubra livros relacionados.")

st.divider()

# --- Adicionar tarefa ---
st.subheader("Adicionar Tarefa")
with st.form("add_task_form", clear_on_submit=True):
    nova_tarefa = st.text_input("Nome da tarefa", placeholder="Ex: Estudar Python")
    submitted = st.form_submit_button("Adicionar")
    if submitted:
        try:
            manager.add_task(nova_tarefa)
            st.success(f"Tarefa '{nova_tarefa}' adicionada!")
        except ValueError as e:
            st.error(str(e))

st.divider()

# --- Listar e remover tarefas ---
st.subheader("Minhas Tarefas")
tarefas = manager.list_tasks()
if not tarefas:
    st.info("Nenhuma tarefa cadastrada. Adicione uma acima!")
else:
    for tarefa in tarefas:
        col1, col2, col3 = st.columns([4, 1, 1])
        label = f"~~{tarefa['title']}~~" if tarefa["done"] else tarefa["title"]
        col1.write(label)
        done_label = "↩️" if tarefa["done"] else "✅"
        if col2.button(done_label, key=f"done_{tarefa['id']}"):
            manager.update_task(tarefa["id"], not tarefa["done"])
            st.rerun()
        if col3.button("🗑️", key=f"remove_{tarefa['id']}"):
            manager.remove_task(tarefa["id"])
            st.rerun()

st.divider()

# --- Buscar livros ---
st.subheader("Buscar Livros para Estudar")
st.caption("Integração com a [Open Library API](https://openlibrary.org) — gratuita e sem chave de API.")

with st.form("search_books_form"):
    query = st.text_input("Tema de estudo", placeholder="Ex: machine learning")
    buscar = st.form_submit_button("Buscar Livros")
    if buscar and query:
        with st.spinner("Buscando livros..."):
            try:
                livros = search_books(query)
                if not livros:
                    st.warning("Nenhum livro encontrado para este tema.")
                else:
                    st.success(f"{len(livros)} livro(s) encontrado(s) sobre '{query}':")
                    for livro in livros:
                        autores = ", ".join(livro["authors"][:2])
                        ano = f" ({livro['year']})" if livro["year"] else ""
                        st.markdown(f"- **{livro['title']}** — {autores}{ano}")
            except ConnectionError as e:
                st.error(f"Erro de conexão: {e}")
