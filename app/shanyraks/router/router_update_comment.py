from fastapi import Depends, Response
from app.utils import AppModel

from ..service import Service, get_service
from . import router
from ..adapters.jwt_service import JWTData
from .dependencies import parse_jwt_user_data


class UpdateCommentRequest(AppModel):
    content: str


@router.patch("/{id}/comments/{comment_id}")
def update_comment(
    shanyrak_id: str,
    comment_id: str,
    input: str,
    svc: Service = Depends(get_service),
    jwt_data: JWTData = Depends(parse_jwt_user_data),
) -> None:
    svc.repository.update_comment(shanyrak_id, comment_id, input)
    return Response(status_code=200)
