from fastapi import FastAPI
from forge_ai.api.router import api_router
from forge_ai.core.config import get_settings
from forge_ai.core.logging import configure_logging
from forge_ai.core.lifespan import lifespan
from forge_ai.core.exception_handlers import forge_ai_exception_handler
from forge_ai.core.exceptions import ForgeAIException
configure_logging()
settings = get_settings()


def create_app() -> FastAPI:
    """
    Application Factory.
    Responsible for creating and configuring
    the FastAPI application.
    """
    app = FastAPI(
        title= settings.app_name,
        description=settings.app_description,
        version= settings.app_version,
        lifespan=lifespan,
    )
    app.include_router(api_router)
    app.add_exception_handler(
        ForgeAIException,
        forge_ai_exception_handler,
    )
    return app