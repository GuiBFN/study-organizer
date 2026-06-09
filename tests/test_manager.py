import pytest
from unittest.mock import MagicMock
from src.manager import TaskManager

def make_manager():
    """Cria um TaskManager com banco de dados mockado."""
    mock_db = MagicMock()
    manager = TaskManager(db=mock_db)
    return manager, mock_db

def test_add_task_chama_db():
    manager, mock_db = make_manager()
    mock_db.add_task.return_value = {"id": "abc", "title": "Python", "done": False}
    manager.add_task("Python")
    mock_db.add_task.assert_called_once_with("Python")

def test_add_task_titulo_vazio_levanta_erro():
    manager, mock_db = make_manager()
    with pytest.raises(ValueError):
        manager.add_task("")

def test_list_tasks_retorna_lista():
    manager, mock_db = make_manager()
    mock_db.get_tasks.return_value = [
        {"id": "1", "title": "Task A", "done": False},
        {"id": "2", "title": "Task B", "done": True},
    ]
    tasks = manager.list_tasks()
    assert len(tasks) == 2
    assert tasks[0]["title"] == "Task A"

def test_remove_task_chama_db():
    manager, mock_db = make_manager()
    manager.remove_task("uuid-123")
    mock_db.remove_task.assert_called_once_with("uuid-123")

def test_update_task_chama_db():
    manager, mock_db = make_manager()
    mock_db.update_task.return_value = {"id": "uuid-123", "title": "Task", "done": True}
    manager.update_task("uuid-123", True)
    mock_db.update_task.assert_called_once_with("uuid-123", True)

def test_marcar_tarefa_como_concluida():
    """Ao marcar done=True, o banco deve ser chamado com o id correto."""
    manager, mock_db = make_manager()
    task_id = "uuid-456"
    mock_db.update_task.return_value = {"id": task_id, "title": "Estudar", "done": True}
    resultado = manager.update_task(task_id, True)
    mock_db.update_task.assert_called_once_with(task_id, True)
    assert resultado["done"] is True

def test_desmarcar_tarefa_concluida():
    """Toggle: ao desmarcar (done=False), o banco deve ser chamado corretamente."""
    manager, mock_db = make_manager()
    task_id = "uuid-789"
    mock_db.update_task.return_value = {"id": task_id, "title": "Estudar", "done": False}
    resultado = manager.update_task(task_id, False)
    mock_db.update_task.assert_called_once_with(task_id, False)
    assert resultado["done"] is False

def test_update_task_com_id_invalido_nao_levanta_erro_no_manager():
    """O manager repassa o id ao banco sem validar. A validacao e responsabilidade do BD."""
    manager, mock_db = make_manager()
    mock_db.update_task.return_value = {}
    manager.update_task("id-qualquer", True)
    mock_db.update_task.assert_called_once()