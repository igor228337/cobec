from datetime import datetime

from src.db.db import SQLModel


class HistoryRecord(SQLModel):
    address: str
    created_at: datetime