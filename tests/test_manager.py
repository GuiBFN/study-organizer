from src.manager import TaskManager
from src.task import Task


def test_add_task():
    manager = TaskManager()
    task = Task("Estudar Python")

    manager.add_task(task)

    assert len(manager.tasks) == 1
    assert manager.tasks[0].name == "Estudar Python"


def test_remove_task():
    manager = TaskManager()
    task = Task("Estudar Python")

    manager.add_task(task)
    manager.remove_task(0)

    assert len(manager.tasks) == 0


def test_list_tasks():
    manager = TaskManager()
    task1 = Task("Estudar Python")
    task2 = Task("Revisar CI")

    manager.add_task(task1)
    manager.add_task(task2)

    tasks = manager.list_tasks()

    assert len(tasks) == 2