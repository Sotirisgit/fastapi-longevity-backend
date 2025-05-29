{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # app/routes/wearable.py\
from fastapi import APIRouter\
from app.db import get_db_connection\
\
router = APIRouter(prefix="/wearable", tags=["Wearable"])\
\
@router.get("/")\
def get_wearable_data():\
    conn = get_db_connection()\
    cursor = conn.cursor()\
    cursor.execute("""\
        SELECT id, user_id, timestamp, heart_rate, steps, calories\
        FROM wearable_data\
        ORDER BY timestamp DESC\
        LIMIT 100;\
    """)\
    rows = cursor.fetchall()\
    cursor.close()\
    conn.close()\
\
    data = [\
        \{\
            "id": row[0],\
            "user_id": row[1],\
            "timestamp": row[2],\
            "heart_rate": row[3],\
            "steps": row[4],\
            "calories": row[5],\
        \}\
        for row in rows\
    ]\
    return \{"data": data\}\
}