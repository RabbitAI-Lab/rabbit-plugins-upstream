"""FastAPI application."""
from __future__ import annotations

from fastapi import FastAPI

from src.api.routes import (coverage, export, mirrors, molecules,
                               observability, search, social, stats, suppliers)

app = FastAPI(
    title="Iran Chemical Database API",
    description="HTTrack-powered best-effort index of Iranian chemical supplier offerings (crawled from public catalogues). Coverage is measured, not assumed.",
    version="1.0.0",
)

app.include_router(molecules.router)
app.include_router(suppliers.router)
app.include_router(search.router)
app.include_router(mirrors.router)
app.include_router(stats.router)
app.include_router(coverage.router)
app.include_router(observability.router)
app.include_router(export.router)
app.include_router(social.router)


@app.get("/api/v1/health", tags=["health"])
def health() -> dict:
    return {"ok": True, "service": "iran-chem-db"}
