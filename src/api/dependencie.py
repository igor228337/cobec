from fastapi import Depends
from src.db.db import get_session

from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.historys import HistoryRepository
from src.services.historys import HistoryService


async def history_service(session: AsyncSession = Depends(get_session)) -> HistoryService:
    return HistoryService(session, HistoryRepository)
