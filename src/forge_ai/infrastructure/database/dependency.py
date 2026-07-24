"""
Database session dependency.
"""
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from forge_ai.infrastructure.database.session import get_session_factory

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Provide a database session for a single request.

    A new session is created for each request.
    The session is automatically rolled back if an exception occurs
    and always closed before the request completes.
    """
    async with get_session_factory()() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise

"""
    async with get_session_factory() as session
        - This guarantees that the session is closed, even if an exception occurs.
        - It is cleaner, safer, and is the recommended SQLAlchemy pattern.
    why yeild instead of return?
        - If we wrote "return session".
        - FastAPI would have no opportunity to clean up after the endpoint finishes.
         with "yield session":
        - FastAPI pauses the dependency, executes the endpoint, and then resumes the dependency to perform cleanup.
    why we have rollback only here, and not commit?
        - Transactions should be committed only when the business operation has completed successfully.
        - The service layer decides when data becomes permanent.
        - The dependency only guarantees that failed transactions are rolled back.
"""