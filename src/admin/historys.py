from sqladmin import ModelView
from src.models.historys import RequestHistory


class RequestHistoryAdmin(ModelView, model=RequestHistory):
    name = "Запрос"
    name_plural = "Запрос"
    icon = "fa-solid fa-store"

    column_list = [
        RequestHistory.id,
        RequestHistory.address,
        RequestHistory.created_at
    ]

    column_details_list = [
        RequestHistory.id,
        RequestHistory.address,
        RequestHistory.created_at
    ]

    column_sortable_list = [
        RequestHistory.id,
        RequestHistory.address,
        RequestHistory.created_at
    
    ]
    page_size = 30
    page_size_options = [10, 30, 50, 100]