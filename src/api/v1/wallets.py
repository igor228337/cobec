from typing import Annotated

from fastapi import APIRouter, Depends, Form
from tronpy import Tron
from tronpy.exceptions import AddressNotFound
from src.api.dependencie import history_service
from src.exceptions import HTTPNotFoundTronAddress, HTTPServerBad, HTTPNotCorrectTronAddress
from src.schemas.addresses import AddressRequest
from src.schemas.wallets import WalletInfoResponse
from src.services.historys import HistoryService, HistoryRecord, PaginationSchema
from src.utils.chech_address import is_valid_tron_address


router = APIRouter(prefix="/wallet", tags=["Кошелёк"])


@router.post('/wallet-info', response_model=WalletInfoResponse, description="Получить информацию о кошельке")
async def get_wallet_info(
    response_service: Annotated[HistoryService, Depends(history_service)], 
    address_request: Annotated[AddressRequest, Form()]
):
    if not is_valid_tron_address(address_request.address):
        raise HTTPNotCorrectTronAddress()
    
    try:
        client = Tron(network="nile")
        account = client.get_account(address_request.address)
        balance = account['balance'] / 1_000_000
        resources = client.get_account_resource(address_request.address)
        bandwidth = resources.get('freeNetLimit', 0)
        energy = resources.get('energyLimit', 0)
    except AddressNotFound:
        raise HTTPNotFoundTronAddress()
    except Exception as e:
        raise HTTPServerBad()

    await response_service.create_requests_history(address_request.address)
    return WalletInfoResponse(address=address_request.address, balance=balance, bandwidth=bandwidth, energy=energy)


@router.get("/request-history", response_model=list[HistoryRecord])
async def read_request_history(response_service: Annotated[HistoryService, Depends(history_service)], pag: Annotated[PaginationSchema, Depends()]):
    return await response_service.get_requests_history(pag)
