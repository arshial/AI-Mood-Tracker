import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, List, Dict, Any

DB_PATH = Path("data/mood.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

def _ts_utc_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_conn() as c:
        c.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts TEXT NOT NULL,
            text TEXT NOT NULL,
            lang TEXT,
            sentiment TEXT,
            score REAL,
            meta TEXT
        );
        ''')
        c.commit()

def insert_entry(text: str, lang: Optional[str], sentiment: str, score: float, meta: str = "") -> int:
    ts = _ts_utc_str()
    with get_conn() as c:
        cur = c.execute(
            "INSERT INTO entries (ts, text, lang, sentiment, score, meta) VALUES (?,?,?,?,?,?)",
            (ts, text, lang, sentiment, score, meta),
        )
        c.commit()
        return cur.lastrowid

def fetch_entries(limit: int = 50) -> List[Dict[str, Any]]:
    with get_conn() as c:
        rows = c.execute("SELECT * FROM entries ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
        return [dict(r) for r in rows]

def fetch_daily_mean() -> List[Dict[str, Any]]:
    with get_conn() as c:
        rows = c.execute('''
            SELECT substr(ts, 1, 10) AS day, AVG(score) AS mean_score, COUNT(*) AS n
            FROM entries
            GROUP BY day
            ORDER BY day ASC
        ''').fetchall()
        return [dict(r) for r in rows]