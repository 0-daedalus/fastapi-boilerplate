from fastapi import Depends, UploadFile
from typing import List

from ..service import Service, get_service
from . import router


@router.post("/{id}/media")
def add_images(
    shanyrak_id: str, files: List[UploadFile], svc: Service = Depends(get_service)
):
    result = []
    for file in files:
        url = svc.s3_service.upload_file(file.file, file.filename)
        status = svc.repository.add_image_to_shanyrak(shanyrak_id, url)
        if status == -1:
            return {"message": "Image is already present!"}
        result.append(url)
    return result
