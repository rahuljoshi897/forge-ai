from forge_ai.infrastructure.database.base import Base
from forge_ai.infrastructure.database.types import(
    CreatedTimestamp, PrimaryKey, UpdatedTimestamp
)
from __future__ import annotations
import uuid
from datetime import datetime
from sqlalchemy import DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

class BaseModel(Base):
    """
        Abstract base model containing fields shared by all entities.
    """
    __abstract__ = True
    id: Mapped[PrimaryKey]
    created_at: Mapped[CreatedTimestamp]
    updated_at: Mapped[UpdatedTimestamp]