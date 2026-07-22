from fastapi import FastAPI
from forge_ai.api.routes import api_router
from forge_ai.core.config import get_settings
from forge_ai.infrastructure.logging.logging import configure_logging
from forge_ai.core.lifespan import lifespan
from forge_ai.core.exception_handlers import forge_ai_exception_handler
from forge_ai.core.exceptions import ForgeAIException
from forge_ai.infrastructure.middleware.request_middleware import (
    RequestMiddleware
)
settings = get_settings()


def create_app() -> FastAPI:
    """
    Application Factory.
    Responsible for creating and configuring
    the FastAPI application.
    """
    configure_logging()
    app = FastAPI(
        title= settings.app_name,
        description=settings.app_description,
        version= settings.app_version,
        lifespan=lifespan,
    )
    app.add_middleware(RequestMiddleware)
    app.add_exception_handler(
        ForgeAIException,
        forge_ai_exception_handler,
    )
    app.include_router(api_router)
    return app