from dataclasses import dataclass
import os

@dataclass
class Config:
    MODEL_BACKEND: str = os.getenv("MODEL_BACKEND", "rule")
    DB_PATH: str = os.getenv("DB_PATH", "data/mood.db")

CFG = Config()
