from pydantic import BaseSettings

from app.config import database


from .adapters.s3_service import S3Service
from .adapters.jwt_service import JwtService
from .repository.repository import ShanyraksRepository


class AuthConfig(BaseSettings):
    JWT_ALG: str = "HS256"
    JWT_SECRET: str = "YOUR_SUPER_SECRET_STRING"
    JWT_EXP: int = 10_800


config = AuthConfig()


class Service:
    def __init__(
        self,
        repository: ShanyraksRepository,
        jwt_svc: JwtService,
    ):
        self.repository = repository
        self.jwt_svc = jwt_svc
        self.s3_service = S3Service()


def get_service():
    repository = ShanyraksRepository(database)
    jwt_svc = JwtService(config.JWT_ALG, config.JWT_SECRET, config.JWT_EXP)

    svc = Service(repository, jwt_svc)
    return svc
