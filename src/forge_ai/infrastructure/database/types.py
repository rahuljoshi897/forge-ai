"""
Reusable SQLAlchemy column type aliases.
"""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Annotated

from sqlalchemy import DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapped_column

# ---------------------------------------------------------------------
# Primary Key
# ---------------------------------------------------------------------

PrimaryKey = Annotated[
    uuid.UUID,
    mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    ),
]

# ---------------------------------------------------------------------
# Created Timestamp
# ---------------------------------------------------------------------

CreatedTimestamp = Annotated[
    datetime,
    mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    ),
]

# ---------------------------------------------------------------------
# Updated Timestamp
# ---------------------------------------------------------------------

UpdatedTimestamp = Annotated[
    datetime,
    mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    ),
]