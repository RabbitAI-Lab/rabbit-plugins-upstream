"""SQLAlchemy engine/session factory bound to the configured PostgreSQL."""
from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.config import get_config

_engine = None
_SessionLocal = None


def database_url() -> str:
    cfg = get_config().database
    user = cfg.user
    password = cfg.password
    host = cfg.host
    port = int(cfg.port)
    name = cfg.name
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"


def get_engine():
    global _engine
    if _engine is None:
        _engine = create_engine(database_url(), pool_pre_ping=True)
    return _engine


def get_session_factory() -> sessionmaker:
    global _SessionLocal
    if _SessionLocal is None:
        _SessionLocal = sessionmaker(bind=get_engine(), autoflush=False, expire_on_commit=False)
    return _SessionLocal


def get_db_session() -> Session:
    return get_session_factory()()


def init_db() -> None:
    """Create all tables (dev convenience; production uses alembic)."""
    from src.database import models  # noqa: F401
    from src.database.models import Base
    Base.metadata.create_all(get_engine())
