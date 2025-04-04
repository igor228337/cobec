from tronpy import Tron

from src.exceptions import HTTPNotFoundTronAddress


def is_valid_tron_address(address: str) -> bool:
    """Проверяет валидность формата адреса Tron."""
    try:
        return Tron.is_address(address)
    except ValueError:
        raise HTTPNotFoundTronAddress()