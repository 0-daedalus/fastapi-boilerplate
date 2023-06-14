from fastapi import Depends, Response

from ..service import Service, get_service
from . import router


@router.delete("/{id}/comments/{comment_id}")
def delete_comment(
    shanyrak_id: str,
    comment_id: str,
    svc: Service = Depends(get_service),
):
    svc.repository.delete_comment(shanyrak_id, comment_id)
    return Response(status_code=200)
