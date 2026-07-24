"""
Repository ORM model.
"""
from __future__ import annotations
from datetime import datetime
from typing import Any
from sqlalchemy import Enum, ForeignKey, Index, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from forge_ai.infrastructure.database.base_model import BaseModel
from sqlalchemy.dialects.postgresql import UUID
import uuid
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from forge_ai.infrastructure.database.models.workspace import Workspace
from forge_ai.domain.enums.repository import (
    RepositoryProvider,
    RepositoryStatus,
)

class Repository(BaseModel):
    __tablename__ = "repositories"
    __table_args__ = (
        Index("ix_repositories_workspace_id", "workspace_id"),
        Index("ix_repositories_status", "status"),
    )
    workspace_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    provider: Mapped[RepositoryProvider] = mapped_column(
        Enum(RepositoryProvider),
        nullable=False,
    )
    url: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    default_branch: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="main",
    )
    status: Mapped[RepositoryStatus] = mapped_column(
        Enum(RepositoryStatus),
        nullable=False,
        default=RepositoryStatus.PENDING,
    )
    provider_metadata: Mapped[dict[str, Any] | None] = mapped_column(
        JSONB,
        nullable=True,
    )
    last_indexed_at: Mapped[datetime | None]
    workspace: Mapped[Workspace] = relationship(
        back_populates="repositories",
        lazy="selectin",
    )