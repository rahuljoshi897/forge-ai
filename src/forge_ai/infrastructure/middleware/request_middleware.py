"""
Application request middleware.

Responsibilities:
- Generate a unique request ID.
- Measure request execution time.
- Log incoming requests.
- Log outgoing responses.
- Add request metadata to response headers..
"""

from __future__ import annotations
import time
import uuid
import structlog
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
logger = structlog.getLogger()

class RequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next)-> Response:
        request_id = uuid.uuid4().hex
        start_time = time.perf_counter()
        request.state.request_id = request_id
        logger.info(
            "Request started",
            request_id=request_id,
            method=request.method,
            path=request.url.path,
            client=request.client.host if request.client else "unknown",
        )
        response = await call_next(request)
        duration_ms = round(
            (time.perf_counter() - start_time) * 1000,
            2,
        )
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Process-Time"] = f"{duration_ms} ms"
        logger.info(
            "Request completed",
            request_id=request_id,
            method=request.method,
            path=request.url.path,
            status_code=response.status_code,
            duration_ms=duration_ms,
        )
        return response


        # return await super().dispatch(request, call_next)
