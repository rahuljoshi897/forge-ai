from contextlib import asynccontextmanager
from fastapi import FastAPI
import structlog
logger = structlog.get_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application starting...")

    yield

    logger.info("Application shutting down..")