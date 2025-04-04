from src.db.db import SQLModel


class WalletInfoResponse(SQLModel):
    address: str
    balance: float
    bandwidth: int
    energy: int