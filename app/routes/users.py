from fastapi import APIRouter
from app.db import get_db_connection

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, first_name, last_name, date_birth, height, weight, gender, created_at FROM users;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    users = [
        {
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "date_birth": row[3],
            "height": row[4],
            "weight": row[5],
            "gender": row[6],
            "created_at": row[7],
        }
        for row in rows
    ]
    return {"users": users}
