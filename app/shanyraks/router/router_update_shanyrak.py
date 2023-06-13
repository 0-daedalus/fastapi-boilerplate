from fastapi import Depends, Response

from app.utils import AppModel

from ..service import Service, get_service
from . import router
from ..adapters.jwt_service import JWTData
from .dependencies import parse_jwt_user_data


class UpdateShanyrakRequest(AppModel):
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str


class UpdateShanyrakResponse(AppModel):
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str


@router.patch("{/:shanyrak_id}", response_model=UpdateShanyrakResponse)
def update_my_account(
    shanyrak_id: str,
    input: UpdateShanyrakRequest,
    svc: Service = Depends(get_service),
    jwt_data: JWTData = Depends(parse_jwt_user_data),
) -> None:
    svc.repository.update_shanyrak(shanyrak_id, input.dict())
    return Response(status_code=200)
