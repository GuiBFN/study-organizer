done_label = "↩️" if tarefa["done"] else "✅"
        if col2.button(done_label, key=f"done_{tarefa['id']}"):
            manager.update_task(tarefa["id"], not tarefa["done"])
            st.rerun()
        if col3.button("🗑️", key=f"remove_{tarefa['id']}"):
            manager.remove_task(tarefa["id"])
            st.rerun()
