"""
school_calendar_sync.py — School Email Attachment Extraction Utility

Refactored: LLM logic removed. This script now focuses on extracting text from
PDF attachments and downloading inline images to provide raw data to the
OpenClaw agent.
"""

from __future__ import annotations

import base64
import io
import logging
import os
import re
import time
from typing import Dict, List

logger = logging.getLogger(__name__)


# ─── PDF Extraction ───────────────────────────────────────────────────────────

def extract_pdf_text_from_bytes(pdf_bytes: bytes) -> str:
    """Extract plain text from raw PDF bytes using pypdf."""
    try:
        from pypdf import PdfReader  # type: ignore
        reader = PdfReader(io.BytesIO(pdf_bytes))
        pages = []
        for page in reader.pages:
            text = page.extract_text() or ""
            if text.strip():
                pages.append(text)
        return "\n".join(pages)
    except Exception as exc:
        logger.warning(f"[pdf_extract] pypdf failed: {exc}")
        return ""


def _collect_pdf_parts(payload: Dict, out: list) -> None:
    """Recursively collect application/pdf parts from a Gmail message payload."""
    mime = payload.get("mimeType", "")
    if mime == "application/pdf":
        out.append(payload)
    elif mime.startswith("multipart/"):
        for part in payload.get("parts", []):
            _collect_pdf_parts(part, out)


def extract_pdf_attachments(service, msg_id: str, payload: Dict) -> List[str]:
    """Download and extract text from all PDF attachments in a Gmail message."""
    pdf_parts: list = []
    _collect_pdf_parts(payload, pdf_parts)

    texts: List[str] = []
    for part in pdf_parts:
        filename = part.get("filename", "attachment.pdf")
        body = part.get("body", {})
        attachment_id = body.get("attachmentId")
        inline_data = body.get("data")

        try:
            if attachment_id:
                att = service.users().messages().attachments().get(
                    userId="me", messageId=msg_id, id=attachment_id
                ).execute()
                pdf_bytes = base64.urlsafe_b64decode(att["data"])
            elif inline_data:
                pdf_bytes = base64.urlsafe_b64decode(inline_data)
            else:
                continue

            text = extract_pdf_text_from_bytes(pdf_bytes)
            if text:
                texts.append(text)
        except Exception:
            continue

    return texts


# ─── Image Extraction ────────────────────────────────────────────────────────

def _collect_image_parts(payload: Dict, out: list) -> None:
    """Recursively collect image/* parts from a Gmail message payload."""
    mime = payload.get("mimeType", "")
    if mime.startswith("image/"):
        out.append(payload)
    elif mime.startswith("multipart/"):
        for part in payload.get("parts", []):
            _collect_image_parts(part, out)


def _mime_to_ext(mime: str) -> str:
    """Map image MIME type to file extension."""
    mapping = {
        "image/jpeg": ".jpg",
        "image/png": ".png",
        "image/gif": ".gif",
        "image/webp": ".webp",
        "image/bmp": ".bmp",
    }
    return mapping.get(mime.lower(), ".jpg")


def download_image_attachments(
    service, msg_id: str, payload: Dict, save_dir: str
) -> List[str]:
    """Download all image attachments from a Gmail message and save to disk.

    Returns list of absolute file paths for saved images.
    """
    image_parts: list = []
    _collect_image_parts(payload, image_parts)

    os.makedirs(save_dir, exist_ok=True)
    paths: List[str] = []

    for idx, part in enumerate(image_parts):
        filename = part.get("filename", "")
        mime = part.get("mimeType", "image/jpeg")
        ext = _mime_to_ext(mime)

        if filename:
            safe_name = re.sub(r'[^\w.\-]', '_', filename)
        else:
            safe_name = f"inline_{idx}{ext}"
        save_name = f"{msg_id}_{idx}_{safe_name}"
        save_path = os.path.join(save_dir, save_name)

        body = part.get("body", {})
        attachment_id = body.get("attachmentId")
        inline_data = body.get("data")

        try:
            if attachment_id:
                att = service.users().messages().attachments().get(
                    userId="me", messageId=msg_id, id=attachment_id
                ).execute()
                img_bytes = base64.urlsafe_b64decode(att["data"])
            elif inline_data:
                img_bytes = base64.urlsafe_b64decode(inline_data)
            else:
                continue

            with open(save_path, "wb") as f:
                f.write(img_bytes)
            paths.append(os.path.abspath(save_path))
        except Exception:
            continue

    return paths


def cleanup_old_attachments(save_dir: str, max_age_days: int = 7) -> None:
    """Remove attachment files older than max_age_days."""
    if not os.path.isdir(save_dir):
        return
    cutoff = time.time() - (max_age_days * 86400)
    for fname in os.listdir(save_dir):
        fpath = os.path.join(save_dir, fname)
        try:
            if os.path.isfile(fpath) and os.path.getmtime(fpath) < cutoff:
                os.unlink(fpath)
        except OSError:
            pass
