from datetime import datetime, timezone
from sqlmodel import DateTime, Field
from src.schemas.historys import HistoryRecord


class RequestHistory(HistoryRecord, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(
        sa_type=DateTime(timezone=True),
        default_factory=lambda: datetime.now(timezone.utc)
    )
