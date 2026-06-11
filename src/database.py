import os

import streamlit as st
from dotenv import load_dotenv
from postgrest.exceptions import APIError as PostgrestAPIError
from supabase import create_client, Client

load_dotenv()


class SupabaseClient:
    def __init__(self):
        # Tenta st.secrets primeiro (Streamlit Cloud),
        # depois variáveis de ambiente (local com .env)
        try:
            url = st.secrets["SUPABASE_URL"]
            key = st.secrets["SUPABASE_KEY"]
        except Exception:
            url = os.environ.get("SUPABASE_URL", "")
            key = os.environ.get("SUPABASE_KEY", "")

        if not url or not key:
            raise ValueError(
                "SUPABASE_URL e SUPABASE_KEY não encontrados. "
                "Configure as secrets no Streamlit Cloud ou o .env local."
            )
        self._client: Client = create_client(url, key)

    def get_tasks(self) -> list[dict]:
        try:
            response = self._client.table("tasks").select("*").order("created_at").execute()
            return response.data
        except PostgrestAPIError as e:
            raise RuntimeError(f"Erro ao buscar tarefas: {e.message}") from e

    def add_task(self, title: str) -> dict:
        try:
            response = self._client.table("tasks").insert({"title": title}).execute()
            return response.data[0]
        except PostgrestAPIError as e:
            raise RuntimeError(f"Erro ao adicionar tarefa: {e.message}") from e

    def remove_task(self, task_id: str) -> None:
        try:
            self._client.table("tasks").delete().eq("id", task_id).execute()
        except PostgrestAPIError as e:
            raise RuntimeError(f"Erro ao remover tarefa: {e.message}") from e

    def update_task(self, task_id: str, done: bool) -> dict:
        try:
            response = (
                self._client.table("tasks").update({"done": done}).eq("id", task_id).execute()
            )
            return response.data[0]
        except PostgrestAPIError as e:
            raise RuntimeError(f"Erro ao atualizar tarefa: {e.message}") from e
