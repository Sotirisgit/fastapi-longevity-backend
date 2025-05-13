import os
from dotenv import load_dotenv

load_dotenv()

print("DB_URL =", os.getenv("DB_URL"))
