from fastapi import APIRouter
from fastapi.responses import JSONResponse
from datetime import datetime
import psycopg2
import os
from dotenv import load_dotenv

router = APIRouter()

load_dotenv()

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("SUPABASE_DB_HOST"),
        database=os.getenv("SUPABASE_DB_NAME"),
        user=os.getenv("SUPABASE_DB_USER"),
        password=os.getenv("SUPABASE_DB_PASSWORD"),
        port=os.getenv("SUPABASE_DB_PORT")
    )

@router.get("/wearable/")
def get_wearable_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT user_id, metric_type, value, unit, timestamp 
        FROM wearable_data
        ORDER BY timestamp DESC
        LIMIT 100
    """)
    rows = cursor.fetchall()
    conn.close()

    wearable_data = []
    for row in rows:
        wearable_data.append({
            "user_id": row[0],
            "metric_type": row[1],
            "value": row[2],
            "unit": row[3],
            "timestamp": row[4].isoformat() if isinstance(row[4], datetime) else row[4]
        })

    return JSONResponse(content={"wearable_data": wearable_data})
