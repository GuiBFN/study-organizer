def update_task(self, task_id: str, done: bool) -> dict:
        response = (
            self._client.table("tasks").update({"done": done}).eq("id", task_id).execute()
        )
        return response.data[0] if response.data else {}
