from fastapi import APIRouter

api_router = APIRouter(
    prefix="/api",
)

from . import views, models # noqa
