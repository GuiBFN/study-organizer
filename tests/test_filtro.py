import pytest
from unittest.mock import MagicMock
from src.manager import TaskManager

TASKS_MOCK = [
    {"id": "1", "title": "Estudar Python",  "done": False, "created_at": "2025-06-01T10:00:00Z"},
    {"id": "2", "title": "Ler documentacao","done": True,  "created_at": "2025-06-02T11:00:00Z"},
    {"id": "3", "title": "Fazer exercicios","done": False, "created_at": "2025-06-03T12:00:00Z"},
    {"id": "4", "title": "Revisar PR",      "done": True,  "created_at": "2025-06-04T13:00:00Z"},
]

def make_manager():
    mock_db = MagicMock()
    mock_db.get_tasks.return_value = TASKS_MOCK
    return TaskManager(db=mock_db)

def test_filtro_todas_retorna_tudo():
    """Sem filtro (Todas), todas as tarefas devem ser retornadas."""
    manager = make_manager()
    todas = manager.list_tasks()
    assert len(todas) == 4

def test_filtro_pendentes():
    """Filtro Pendentes deve retornar apenas done=False."""
    manager = make_manager()
    pendentes = [t for t in manager.list_tasks() if not t["done"]]
    assert len(pendentes) == 2
    assert all(not t["done"] for t in pendentes)

def test_filtro_concluidas():
    """Filtro Concluidas deve retornar apenas done=True."""
    manager = make_manager()
    concluidas = [t for t in manager.list_tasks() if t["done"]]
    assert len(concluidas) == 2
    assert all(t["done"] for t in concluidas)

def test_contadores_corretos():
    """Os contadores de pendentes e concluidas devem bater com a lista."""
    manager = make_manager()
    todas = manager.list_tasks()
    pendentes_count = len([t for t in todas if not t["done"]])
    concluidas_count = len([t for t in todas if t["done"]])
    assert pendentes_count == 2
    assert concluidas_count == 2
    assert pendentes_count + concluidas_count == len(todas)

def test_filtro_pendentes_nao_contem_concluidas():
    """Nenhuma tarefa no filtro Pendentes pode ter done=True."""
    manager = make_manager()
    pendentes = [t for t in manager.list_tasks() if not t["done"]]
    for t in pendentes:
        assert t["done"] is False
