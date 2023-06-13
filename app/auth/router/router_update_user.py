from typing import Any

from fastapi import Depends, Response
from pydantic import Field

from app.utils import AppModel

from ..service import Service, get_service
from . import router
from ..adapters.jwt_service import JWTData
from .dependencies import parse_jwt_user_data


class UpdateUserRequest(AppModel):
    phone: str
    name: str
    city: str


class UpdateMyAccountResponse(AppModel):
    id: Any = Field(alias="_id")
    email: str
    phone: str
    name: str
    city: str


@router.patch("/users/me", response_model=UpdateMyAccountResponse)
def update_my_account(
    input: UpdateUserRequest,
    svc: Service = Depends(get_service),
    jwt_data: JWTData = Depends(parse_jwt_user_data),
) -> None:
    svc.repository.update_user(jwt_data.user_id, input.dict())
    return Response(status_code=200)
