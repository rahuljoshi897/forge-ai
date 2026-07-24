"""
SQLAlchemy async session factory.
"""
from sqlalchemy.ext.asyncio import AsyncSession,async_sessionmaker
from forge_ai.infrastructure.database.engine import get_engine
session_factory = async_sessionmaker(
        bind=get_engine(),
        class_=AsyncSession,
        autoflush=False,
        expire_on_commit=False,
)

def get_session_factory()->async_sessionmaker[AsyncSession]:
    return session_factory

"""
    Explaination
async_sessionmaker: This is SQLAlchemy's recommended way to create sessions.
session_factory = async_sessionmaker(...)
We're not creating a session. We're creating something that knows how to create sessions.
A: bind=get_engine()
    This tells SQLAlchemy:
        Every session created by this factory should use this Engine.

B: class_=AsyncSession
    Explicitly tells SQLAlchemy:
    Create asynchronous sessions.

C: autoflush=False:
    Only send SQL when we decide.Much more predictable.

D: expire_on_commit=False
    Without it:
        await session.commit()
        print(workspace.name)
        SQLAlchemy may automatically reload the object from the database.That often causes unexpected queries.
    With this setting: expire_on_commit=False
        Objects remain usable after a commit.This avoids unnecessary database round trips.
        
Note: we won't do session = session_factory() here
    - Because sessions are request-scoped.
    - Creating one globally would be incorrect.
    - The factory stays global.
    - The sessions are short-lived.
"""