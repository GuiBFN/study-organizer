from unittest.mock import MagicMock
from src.manager import TaskManager


def make_task(task_id="abc-123", title="Estudar", done=False):
    return {"id": task_id, "title": title, "done": done, "created_at": "2024-01-01T00:00:00"}


def make_manager():
    db = MagicMock()
    return TaskManager(db=db), db


def test_add_task():
    manager, db = make_manager()
    db.add_task.return_value = make_task(title="Estudar")

    result = manager.add_task("Estudar")

    db.add_task.assert_called_once_with("Estudar")
    assert result["title"] == "Estudar"


def test_add_empty_task():
    manager, db = make_manager()

    try:
        manager.add_task("")
    except ValueError:
        assert True
    else:
        assert False

    db.add_task.assert_not_called()


def test_list_tasks():
    manager, db = make_manager()
    db.get_tasks.return_value = [make_task(), make_task(task_id="xyz", title="Revisar")]

    tasks = manager.list_tasks()

    db.get_tasks.assert_called_once()
    assert len(tasks) == 2
    assert tasks[0]["title"] == "Estudar"


def test_remove_task():
    manager, db = make_manager()

    manager.remove_task("abc-123")

    db.remove_task.assert_called_once_with("abc-123")


def test_update_task():
    manager, db = make_manager()
    db.update_task.return_value = make_task(done=True)

    result = manager.update_task("abc-123", True)

    db.update_task.assert_called_once_with("abc-123", True)
    assert result["done"] is True
