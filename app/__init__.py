from fastapi import FastAPI

from app.config import settings


def create_app() -> FastAPI:
    app = FastAPI()

    from app.logging import configure_logging
    configure_logging()

    # do this before loading routes
    from app.celery_utils import create_celery
    app.celery_app = create_celery()

    from app.api import api_router
    app.include_router(api_router)


    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    return app
