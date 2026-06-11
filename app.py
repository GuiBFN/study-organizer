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
todas_tarefas = manager.list_tasks()
pendentes = [t for t in todas_tarefas if not t["done"]]
concluidas_count = len([t for t in todas_tarefas if t["done"]])
pendentes_count = len(pendentes)

col_info1, col_info2, col_info3 = st.columns(3)
col_info1.metric("Total", len(todas_tarefas))
col_info2.metric("Pendentes", pendentes_count)
col_info3.metric("Concluidas", concluidas_count)

status_filtro = st.selectbox(
    "Filtrar por status:",
    options=["Todas", "Pendentes", "Concluidas"],
    key="filtro_status"
)

if status_filtro == "Pendentes":
    tarefas = [t for t in todas_tarefas if not t["done"]]
elif status_filtro == "Concluidas":
    tarefas = [t for t in todas_tarefas if t["done"]]
else:
    tarefas = todas_tarefas

if not tarefas:
    st.info(f"Nenhuma tarefa encontrada para o filtro '{status_filtro}'.")
else:
    for tarefa in tarefas:
        col1, col2, col3 = st.columns([4, 1, 1])
        label = f"~~{tarefa['title']}~~" if tarefa["done"] else tarefa["title"]
        col1.write(label)
        done_label = "&#x21A9;" if tarefa["done"] else "&#x2705;"
        if col2.button(done_label, key=f"done_{tarefa['id']}"):
            manager.update_task(tarefa["id"], not tarefa["done"])
            st.rerun()
        if col3.button("&#x1F5D1;", key=f"remove_{tarefa['id']}"):
            manager.remove_task(tarefa["id"])
            st.rerun()

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
