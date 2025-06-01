# app/routes/wearable_data.py
from fastapi import APIRouter
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv()

router = APIRouter()
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_SERVICE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

@router.get("/wearable/")
def get_wearable_data():
    response = supabase.table("wearable_data").select("*").execute()
    records = response.data

    # Group values by metric type
    grouped = defaultdict(list)
    for record in records:
        metric = record["metric_type"]
        value = record["value"]
        timestamp = record["timestamp"]
        grouped[metric].append({"value": value, "timestamp": timestamp})

    return grouped
