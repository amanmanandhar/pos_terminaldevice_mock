import uuid
from app.db.memory_store import terminals

def register_terminal():
    terminal_id = str(uuid.uuid4())

    terminals[terminal_id] = {
        "name": data.name,
        "username": data.username,
        "password": data.password,
        "status": offline,
        "last_transaction": None
    }
    return{
        "terminal_id": terminal_id,
        "message": "Terminal Registered Successfully",
    }