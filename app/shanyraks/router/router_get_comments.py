from fastapi import Depends

from ..service import Service, get_service
from . import router


@router.get("/{id}/comments")
def get_comments(shanyrak_id: str, svc: Service = Depends(get_service)):
    comments = svc.repository.get_comments_by_id(shanyrak_id)
    return comments
