from src.database import SupabaseClient


class TaskManager:
    def __init__(self, db: SupabaseClient | None = None):
        self._db = db or SupabaseClient()

    def add_task(self, title: str) -> dict:
        if not title:
            raise ValueError("Título não pode ser vazio")
        return self._db.add_task(title)

    def list_tasks(self) -> list[dict]:
        return self._db.get_tasks()

    def remove_task(self, task_id: str) -> None:
        self._db.remove_task(task_id)

    def update_task(self, task_id: str, done: bool) -> dict:
        return self._db.update_task(task_id, done)
