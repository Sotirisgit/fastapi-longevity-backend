# app/routes/wearable_data.py

from fastapi import APIRouter
from app.db import get_db_connection

router = APIRouter(prefix="/wearable", tags=["Wearable Data"])

@router.get("/")
def get_wearable_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM wearable_data;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"wearable_data": rows}
