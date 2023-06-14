from fastapi import Depends, status
from pydantic import Field
from typing import Any

from app.utils import AppModel

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class CreateCommentRequest(AppModel):
    content: str


class CreateCommentResponse(AppModel):
    id: Any = Field(alias="_id")


@router.post(
    "/{id}/comments",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateCommentResponse,
)
def add_comment(
    input: CreateCommentRequest,
    shanyrak_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    shanyrak_id = svc.repository.create_comment(
        shanyrak_id, jwt_data.user_id, input.content
    )
    return CreateCommentResponse(id=shanyrak_id)
