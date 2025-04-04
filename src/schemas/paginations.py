from fastapi import Query
from sqlmodel import SQLModel


class PaginationSchema(SQLModel):
    """SQLModel for pagination."""

    offset: int = Query(default=0, ge=0, description="Смещение")
    limit: int = Query(default=10, gt=0, le=100, description="Лимит")
