from fastapi import APIRouter
from app.db import get_db_connection

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM users;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"users": rows}
