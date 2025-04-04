from src.models.historys import RequestHistory
from src.utils.repository import SQLAlchemyRepository


class HistoryRepository(SQLAlchemyRepository):
    model = RequestHistory
