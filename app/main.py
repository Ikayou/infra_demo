import os
import psycopg
from fastapi import FastAPI
from psycopg.rows import dict_row

app = FastAPI()

def get_db_conn():
    host = os.getenv("DB_HOST", "localhost")
    port = int(os.getenv("DB_PORT", "5432"))
    name = os.getenv("DB_NAME", "appdb")
    user = os.getenv("DB_USER", "appuser")
    password = os.getenv("DB_PASSWORD", "apppass")

    return psycopg.connect(
        host=host,
        port=port,
        dbname=name,
        user=user,
        password=password,
        row_factory=dict_row,
    )

@app.get("/")
def root():
    return {"status": "ok", "message": "FastAPI is running"}

@app.get("/db")
def db_check():
    # DB疎通確認：SELECT 1 と version()
    with get_db_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1 as one;")
            one = cur.fetchone()
            cur.execute("SELECT version() as version;")
            ver = cur.fetchone()
    return {"db": "ok", "select_1": one["one"], "version": ver["version"]}

@app.get("/healthz")
def healthz():
    # K8sのreadiness/liveness用に軽く
    return {"ok": True}
