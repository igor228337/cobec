from datetime import datetime, timezone

from sqlmodel import desc, select
from src.repositories.historys import HistoryRepository
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.historys import HistoryRecord
from src.schemas.paginations import PaginationSchema
from src.enviroment import logger


class HistoryService:
    def __init__(
        self,
        session: AsyncSession,
        history_repo: HistoryRepository
        ):
        self.session: AsyncSession = session
        self.history_repo: HistoryRepository = history_repo()
    
    async def create_requests_history(self, address: str) -> HistoryRepository | None:
        data = HistoryRecord(address=address, created_at=datetime.now(timezone.utc)).model_dump()
        logger.info(data)
        history = await self.history_repo.add_one(self.session, data)
        return history
    
    async def get_requests_history(self, pagination: PaginationSchema):
        stmt = (
            select(self.history_repo.model)
            .order_by(desc(self.history_repo.model.created_at))
            .offset(pagination.offset)
            .limit(pagination.limit)
        )
        request = await self.history_repo.find_all_custom(self.session, stmt)
        return request