from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pymysql
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_CONFIG = {
    "host": os.environ.get("HOST"),
    "user": os.environ.get("USER"),
    "password": os.environ.get("PASSWORD"),
    "database": os.environ.get("DATABASE")
}

@app.get("/data")
def get_data():
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CARMDI")
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
        return result
    except Exception as e:
        return {"error": str(e)}