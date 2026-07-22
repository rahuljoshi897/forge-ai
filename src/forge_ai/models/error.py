from datetime import UTC, datetime
from pydantic import BaseModel, Field
class ErrorDetail(BaseModel):
    code: str
    details: dict | None = None


class MetaResponse(BaseModel):
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )

class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    error: ErrorDetail
    meta: MetaResponse = Field(default_factory=MetaResponse)


    
