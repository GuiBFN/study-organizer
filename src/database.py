import os

import streamlit as st
from dotenv import load_dotenv
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
        response = self._client.table("tasks").select("*").order("created_at").execute()
        return response.data

    def add_task(self, title: str) -> dict:
        response = self._client.table("tasks").insert({"title": title}).execute()
        return response.data[0]

    def remove_task(self, task_id: str) -> None:
        self._client.table("tasks").delete().eq("id", task_id).execute()

    def update_task(self, task_id: str, done: bool) -> dict:
        response = (
            self._client.table("tasks").update({"done": done}).eq("id", task_id).execute()
        )
        return response.data[0]
