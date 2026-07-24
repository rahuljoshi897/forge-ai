"""
Workspace ORM model.
"""
from __future__ import annotations
from sqlalchemy import Boolean,Index,String,Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column,relationship
from forge_ai.infrastructure.database.base_model import BaseModel
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from forge_ai.infrastructure.database.models.repository import Repository
class Workspace(BaseModel):
    """
    Represents a logical workspace within ForgeAI.

    A workspace is the top-level container for repositories,
    conversations, knowledge bases, documents, and AI agents.
    """
    __tablename__ = "workspaces"
    __table_args__ = (
        UniqueConstraint("slug", name="uq_workspace_slug"),
        Index("ix_workspace_name", "name"),
        Index("ix_workspace_slug", "slug"),
    )
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    slug: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default="true",
    )
    repositories: Mapped[list[Repository]] = relationship(
        back_populates="workspace",
        cascade="all, delete-orphan",
        lazy="selectin",
    )
