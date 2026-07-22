from fastapi import Request
from fastapi.responses import JSONResponse

from forge_ai.core.exceptions import ForgeAIException
from forge_ai.api.schemas.common import ErrorDetail, ErrorResponse


async def forge_ai_exception_handler(
    request: Request,
    exc: ForgeAIException,
):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            message=exc.message,
            error=ErrorDetail(
                code=exc.code,
                details=exc.details,
            ),
        ).model_dump(mode="json"),
    )