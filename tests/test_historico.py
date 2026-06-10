from unittest.mock import MagicMock
from src.manager import TaskManager


def make_manager_com_tasks():
    mock_db = MagicMock()

    mock_db.get_tasks.return_value = [
        {
            "id": "1",
            "title": "Tarefa A",
            "done": True,
            "created_at": "2025-06-01T10:00:00Z",
        },
        {
            "id": "2",
            "title": "Tarefa B",
            "done": False,
            "created_at": "2025-06-02T12:00:00Z",
        },
        {
            "id": "3",
            "title": "Tarefa C",
            "done": True,
            "created_at": "2025-06-03T14:00:00Z",
        },
    ]

    manager = TaskManager(db=mock_db)
    return manager, mock_db


def test_list_tasks_retorna_todas():
    """list_tasks deve retornar todas as tarefas, concluidas ou nao."""
    manager, _ = make_manager_com_tasks()

    tasks = manager.list_tasks()

    assert len(tasks) == 3


def test_filtrar_concluidas():
    """Filtragem de done=True deve retornar apenas as concluidas."""
    manager, _ = make_manager_com_tasks()

    concluidas = [t for t in manager.list_tasks() if t["done"]]

    assert len(concluidas) == 2
    assert all(t["done"] for t in concluidas)


def test_filtrar_pendentes():
    """Filtragem de done=False deve retornar apenas as pendentes."""
    manager, _ = make_manager_com_tasks()

    pendentes = [t for t in manager.list_tasks() if not t["done"]]

    assert len(pendentes) == 1
    assert pendentes[0]["title"] == "Tarefa B"


def test_limpar_historico_remove_concluidas():
    """Limpar historico deve chamar remove_task para cada tarefa concluida."""
    manager, mock_db = make_manager_com_tasks()

    concluidas = [t for t in manager.list_tasks() if t["done"]]

    for tarefa in concluidas:
        manager.remove_task(tarefa["id"])

    assert mock_db.remove_task.call_count == 2