"""HTTrack mirror status endpoints."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.schemas import MirrorOut
from src.database.models import HTTrackMirror
from src.database.session import get_db_session

router = APIRouter(prefix="/api/v1/mirrors", tags=["mirrors"])


def get_db() -> Session:
    db = get_db_session()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def mirrors(db: Session = Depends(get_db)):
    rows = db.execute(select(HTTrackMirror)).scalars().all()
    return {"mirrors": [
        MirrorOut(
            mirror_id=m.mirror_id, supplier_id=m.supplier_id, mirror_path=m.mirror_path,
            project_name=m.project_name, total_files=m.total_files,
            html_files=m.html_files, pdf_files=m.pdf_files, excel_files=m.excel_files,
            mirror_size_bytes=m.mirror_size_bytes,
            last_update_date=m.last_update_date.isoformat() if m.last_update_date else None,
            files_new_last_run=m.files_new_last_run,
            files_modified_last_run=m.files_modified_last_run,
            files_removed_last_run=m.files_removed_last_run,
            httrack_return_code=m.httrack_return_code,
            uses_playwright_fallback=m.uses_playwright_fallback,
        ) for m in rows
    ]}


@router.get("/{mirror_id}/changes")
def mirror_changes(mirror_id: int, db: Session = Depends(get_db)):
    mirror = db.get(HTTrackMirror, mirror_id)
    if mirror is None:
        raise HTTPException(status_code=404, detail="Mirror not found")
    return {
        "mirror_id": mirror_id,
        "changes": mirror.last_changes_json or {},
    }
