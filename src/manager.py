from src.task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        if not title:
            raise ValueError("Título não pode ser vazio")
        task = Task(title)
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def remove_task(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Tarefa não encontrada")
        self.tasks.pop(index)