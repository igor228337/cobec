from sqlmodel import Field
from src.db.db import SQLModel


class AddressRequest(SQLModel):
    address: str = Field(min_length=5, description="Адрес кошелька")