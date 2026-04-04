from src.manager import TaskManager


def test_add_task():
    manager = TaskManager()
    manager.add_task("Estudar")

    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Estudar"


def test_add_empty_task():
    manager = TaskManager()

    try:
        manager.add_task("")
    except ValueError:
        assert True
    else:
        assert False


def test_remove_invalid():
    manager = TaskManager()

    try:
        manager.remove_task(0)
    except IndexError:
        assert True
    else:
        assert False