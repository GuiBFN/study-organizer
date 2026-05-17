# Study Organizer

🚀 **APLICAÇÃO DEPLOYADA:**
[Acesse aqui](https://study-organizer-gzzjzhcwiprsv9hkk7pjsa.streamlit.app)

Projeto desenvolvido para a disciplina de Bootcamp II.

A ideia da aplicação é ajudar estudantes a organizarem suas tarefas de estudo de forma simples, utilizando o terminal ou a interface web.

---

## Funcionalidades Principais

- Adicionar, listar e remover tarefas de estudo
- **Buscar livros relacionados ao tema de estudo** via [Open Library API](https://openlibrary.org) (integração sem chave de API)
- Interface CLI para uso no terminal
- Interface web interativa via Streamlit

---

## Público-alvo

Estudantes que têm dificuldade em manter uma rotina de estudos organizada.

---

## Como executar o projeto

Abra o terminal (Windows + R → CMD) e execute:

### 1. Clonar o repositório

```bash
git clone https://github.com/GuiBFN/study-organizer.git
cd study-organizer
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Executar via CLI

```bash
python -m src.main
```

### 4. Executar via interface web (Streamlit)

```bash
streamlit run app.py
```

---

## Integração com API

A aplicação consome a **Open Library API** para buscar livros relacionados ao tema de estudo informado pelo usuário.

- **Endpoint:** `GET https://openlibrary.org/search.json?q={query}&limit=5`
- **Sem necessidade de chave de API**
- Retorna título, autor e ano de publicação dos livros

### Exemplo de uso (CLI)

```
--- Study Organizer ---
4 - Buscar livros para estudar

Digite o tema para buscar livros: Python

📚 Livros encontrados sobre 'Python':
  1. Learning Python — Mark Lutz (2013)
  2. Python Cookbook — David Beazley, Brian K. Jones (2013)
```

---

## Testes

```bash
python -m pytest tests/ -v
```

Os testes de integração usam mocks para não depender de chamadas reais à API durante o CI/CD.
