"""
Common API response schemas.

These schemas define the standard response format used by all API endpoints.
"""

from datetime import UTC, datetime
from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class MetaResponse(BaseModel):
    """
    Metadata included with every API response.
    """

    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="UTC timestamp when the response was generated.",
    )


class SuccessResponse(BaseModel, Generic[T]):
    """
    Standard success response wrapper.
    """

    success: bool = Field(
        default=True,
        description="Indicates whether the request was successful.",
    )

    message: str = Field(
        ...,
        description="Human-readable success message.",
        examples=["Health check completed successfully."],
    )

    data: T = Field(
        ...,
        description="Actual response payload.",
    )

    meta: MetaResponse = Field(
        default_factory=MetaResponse,
        description="Additional response metadata.",
    )


class ErrorDetail(BaseModel):
    """
    Detailed error information.
    """

    code: str = Field(
        ...,
        description="Application-specific error code.",
        examples=["REPOSITORY_NOT_FOUND"],
    )

    details: dict[str, Any] | None = Field(
        default=None,
        description="Optional additional error details.",
    )


class ErrorResponse(BaseModel):
    """
    Standard error response wrapper.
    """

    success: bool = Field(
        default=False,
        description="Indicates whether the request was successful.",
    )

    message: str = Field(
        ...,
        description="Human-readable error message.",
        examples=["Repository not found."],
    )

    error: ErrorDetail

    meta: MetaResponse = Field(
        default_factory=MetaResponse,
        description="Additional response metadata.",
    )