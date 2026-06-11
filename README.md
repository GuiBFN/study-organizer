# Study Organizer

Aplicação web para organização de tarefas de estudo, com interface Streamlit, integração ao Supabase (PostgreSQL) na nuvem e busca de livros via Open Library API.

**Aplicação publicada:** [https://study-organizer-gzzjzhcwiprsv9hkk7pjsa.streamlit.app](https://study-organizer-gzzjzhcwiprsv9hkk7pjsa.streamlit.app)

**Repositório:** [https://github.com/GuiBFN/study-organizer](https://github.com/GuiBFN/study-organizer)

Projeto desenvolvido para a disciplina de Bootcamp II.

---

## Equipe

| Nome | Matrícula |
|---|---|
| Guilherme Borges | 22502047 |
| Filipe Portela | 22501026 |
| Caio de Almeida | 22451984 |
| Danilo Vilela | 22508899 |

---

## Funcionalidades Principais

- Adicionar, listar e remover tarefas de estudo
- Marcar tarefas como concluídas (texto tachado na interface)
- **Buscar livros relacionados ao tema de estudo** via [Open Library API](https://openlibrary.org) (integração sem chave de API)
- Interface web interativa via Streamlit
- Persistência de dados no Supabase (PostgreSQL na nuvem)

---

## Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| Python 3.11+ | Linguagem principal |
| Streamlit | Interface web |
| Supabase — PostgreSQL na nuvem | Banco de dados |
| supabase-py + python-dotenv | Cliente Supabase e variáveis de ambiente |
| pytest | Testes automatizados |
| ruff | Linter |
| GitHub Actions | CI/CD |
| Open Library API | Busca de livros (sem chave de API) |

---

## Como Executar Localmente

Abra o terminal e execute:

### 1. Clonar o repositório

```bash
git clone https://github.com/GuiBFN/study-organizer.git
cd study-organizer
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```
SUPABASE_URL="https://aajzupwplxptbvxjbuqf.supabase.co"
SUPABASE_KEY="sua-anon-key-aqui"
```

A anon key pode ser obtida em: **Supabase Dashboard → Project Settings → API → anon public**.

### 4. Executar a interface web

```bash
streamlit run app.py
```

---

## Testes

```bash
python -m pytest tests/ -v
```

Os testes usam mocks para não depender de chamadas reais ao banco ou à API durante o CI/CD.

---

## Integração com API Externa

A aplicação consome a **Open Library API** para buscar livros relacionados ao tema de estudo informado pelo usuário.

- **Endpoint:** `GET https://openlibrary.org/search.json?q={query}&limit=5`
- **Sem necessidade de chave de API**
- Retorna título, autor e ano de publicação dos livros

### Exemplo de uso

```
Tema de estudo: Python

📚 5 livro(s) encontrado(s) sobre 'Python':
- Learning Python — Mark Lutz (2013)
- Python Cookbook — David Beazley, Brian K. Jones (2013)
```
