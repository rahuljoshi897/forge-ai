from datetime import UTC, datetime
from typing import Generic, TypeVar
from pydantic import BaseModel, Field
T = TypeVar("T")

class MetaResponse(BaseModel):
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )

class SuccessResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str
    data: T
    meta: MetaResponse = Field(default_factory=MetaResponse)

