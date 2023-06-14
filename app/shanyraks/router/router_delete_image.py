from fastapi import Depends, Response

from typing import List
from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data
from app.utils import AppModel


class DeleteImagesRequest(AppModel):
    media: List[str]


@router.delete("/{id}/media")
def delete_images(
    shanyrak_id: str,
    filenames: DeleteImagesRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    svc.repository.delete_images(shanyrak_id, filenames.media)
    return Response(status_code=200)
