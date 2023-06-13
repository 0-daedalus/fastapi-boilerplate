from fastapi import Depends, status
from pydantic import Field
from typing import Any

from app.utils import AppModel

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class CreateShanyrakRequest(AppModel):
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str


class CreateShanyrakResponse(AppModel):
    id: Any = Field(alias="_id")


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=CreateShanyrakResponse
)
def create_shanyrak(
    input: CreateShanyrakRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    shanyrak_id = svc.repository.create_shanyrak(jwt_data.user_id, input.dict())
    print(shanyrak_id)
    return CreateShanyrakResponse(id=shanyrak_id)
