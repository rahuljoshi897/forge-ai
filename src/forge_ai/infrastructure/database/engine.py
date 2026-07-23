"""
SQLAlchemy async engine configuration.
"""
from __future__ import annotations
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from forge_ai.core.config import get_settings
settings = get_settings()

engine: AsyncEngine = create_async_engine(
    settings.database_url,
    echo = settings.is_development,
    pool_pre_ping = True,
    pool_recycle = 3600
)

def get_engine()->AsyncEngine:
    return engine

"""
pool_pre_ping=True
Imagine:
    Connection Pool -> Connection #2 -> Idle for 2 hours -> Database closed it
Without pre-ping:
Application -> Dead connection -> 500 Internal Server Error
with pool_pre_ping=True
SQLAlchemy checks the connection before using it.If it's dead...
It transparently opens another one.Production applications almost always enable this.
"""

"""
 Next step:
 The engine alone can't execute queries. It still needs a Session.
It will be like :
FastAPI -> Engine-> Session-> Database

"""