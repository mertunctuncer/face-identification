import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info(f"Starting {get_settings().PROJECT_NAME}-{get_settings().ENVIRONMENT}-{get_settings().PROJECT_VERSION}.")
    yield
    logging.info(f"Shutting down {get_settings().PROJECT_NAME}-{get_settings().ENVIRONMENT}-{get_settings().PROJECT_VERSION}.")

def create_application() -> FastAPI:
    application = FastAPI(
        title=get_settings().PROJECT_NAME,
        version=get_settings().PROJECT_VERSION,
        docs_url= None if get_settings().ENVIRONMENT != "development" else "/docs",
        redoc_url= None if get_settings().ENVIRONMENT != "development" else "/redoc",
        lifespan=lifespan,
    )

    return application

application = create_application()