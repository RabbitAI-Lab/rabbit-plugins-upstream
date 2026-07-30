#!/usr/bin/env python3
"""Payable matching — the efficient engine for reconciling Purchasing-folder
documents against their purchase orders in Odoo.

Self-contained: talks to the Odoo `drivethru_mcp` MCP endpoint (Streamable
HTTP) directly, so this skill has no dependency on any sibling skill.

WHY THIS EXISTS — context economy. The naive way to "check the docs in the
Purchasing folder against the POs" is to pull each file with `documents_get`
(returns base64) and read the PDF through a multimodal reader (adds a page
image). Across many documents, many times a day, that floods the agent's
context window with bytes and renders instead of the few hundred characters of
text that matter — and drives token cost (and latency) through the roof.

This CLI keeps the heavy, deterministic work OUT of the model's context:

  * `extract`  fetches every file in a folder, decodes + extracts the TEXT
               locally (PyMuPDF, else poppler `pdftotext -layout`, else `pypdf`)
               and returns compact JSON — text only, never base64 or an image.
               Extraction is quality-gated: a document whose text is empty OR
               unreliable (e.g. a Type3-font / custom-encoded PDF that renders
               fine but extracts as garbage) is flagged `needs_vision: true`
               instead of returning junk the model would fail to match.
  * `render`   rasterises a `needs_vision` document to PNG page image(s) with
               PyMuPDF (no system poppler needed) so the model can read it with
               vision; if `tesseract` is installed it also returns OCR text.
               This is the fallback that rescues a doc the text pass can't read.
  * `po-lines` returns a purchase order trimmed to just the fields matching
               needs (line_id / style / color / size / qty / price_unit, plus
               qty_received / qty_invoiced for shipment-coverage checks).
  * `notes`    reads a PO's prior chatter (log notes) so a partial-shipment
               match can see which lines earlier shipments already checked.
  * `apply`    corrects PO line prices (and optional freight/fees) in one call.
  * `bill`     creates the DRAFT vendor bill from a reconciled PO (never posts).
  * `post`     posts a DRAFT vendor bill once it MATCHES — gated on the bill's
               total reconciling to the vendor invoice's `expected_total`
               within tolerance (a mismatch is refused, never posted blind).
  * `matched`  posts the "checked" LOG NOTE on the PO and files the document
               into the `Matched` subfolder — the clean-result tail in one call.
  * `questions` raises a reviewer activity on the document and files it into
               the `Questions` subfolder — the escalation tail in one call.
  * `move`     files a document into any sibling subfolder by name or id.

The model orchestrates these; it never sees a byte of base64. Every command
prints one JSON object on stdout, or `{"error": {"type", "message"}}` with a
non-zero exit.

LOG NOTES ONLY. Every note this tool posts to a PO or document (`matched`,
`questions`) is an internal Odoo **log note** — never a "Send message" — so it
stays internal and is never emailed to the vendor or customer.

Usage
-----
    python3 scripts/paymatch.py extract   '{"folder": "Purchasing"}'
    python3 scripts/paymatch.py render    '{"document_id": 485}'
    python3 scripts/paymatch.py po-lines  '{"po": "P13189"}'
    python3 scripts/paymatch.py notes     '{"po": "P13137"}'
    python3 scripts/paymatch.py apply     '{"po_id": 13145, "lines": [{"line_id": 40941, "price_unit": 11.94}]}'
    python3 scripts/paymatch.py bill      '{"po_id": 13145, "vendor_bill_number": "INV-98765", "invoice_date": "2026-07-22", "expected_total": 1041.90, "tolerance": 0.02}'
    python3 scripts/paymatch.py post      '{"bill_id": 8842, "expected_total": 1041.90, "tolerance": 0.02, "note": "Matched INV-98765; totals reconcile."}'
    python3 scripts/paymatch.py matched   '{"po_id": 13145, "body": "Pricing checked ...", "document_id": 481}'
    python3 scripts/paymatch.py questions '{"document_id": 485, "question": "Can't reconcile total ...", "reviewer": "Zach Tucker"}'
    python3 scripts/paymatch.py move      '{"document_id": 481, "to": "Matched"}'

Environment
-----------
    ODOO_MCP_URL     Full MCP endpoint, e.g. https://odoo.example.com/drivethru_mcp/v1
    ODOO_MCP_TOKEN   The drivethru.mcp_key value, sent as `Authorization: Bearer`.

Text extraction prefers PyMuPDF (honours ToUnicode CMaps and Type3 / custom-
encoded fonts, and needs no system binary), then poppler's `pdftotext -layout`,
then `pypdf`; a document none of them read reliably is flagged for the `render`
vision/OCR fallback. Args are the 2nd CLI arg or JSON on stdin.
"""

from __future__ import annotations

import base64
import io
import json
import mimetypes
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

# Runtime deps (the mcp/anyio MCP transport + the PyMuPDF/pypdf PDF stack) are
# declared in SKILL.md's install.uv, but not every OpenClaw host honors that —
# where it isn't honored the bare imports below would die with e.g.
# `ModuleNotFoundError: No module named 'anyio'`. Self-bootstrap first: on a
# missing dep, _bootstrap builds a cached uv venv, installs, and re-execs into
# it (a no-op on hosts that already pre-installed). Must run BEFORE anyio/mcp.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _bootstrap  # noqa: E402

_bootstrap.ensure()

import anyio  # noqa: E402
from mcp import ClientSession  # noqa: E402
from mcp.client.streamable_http import streamablehttp_client  # noqa: E402


# ── error contract ───────────────────────────────────────────────────────────


def _fail(error_type: str, message: str, code: int = 1) -> int:
    print(json.dumps({"error": {"type": error_type, "message": message}}))
    return code


def _config() -> tuple[str, str]:
    return (
        (os.environ.get("ODOO_MCP_URL") or "").strip(),
        (os.environ.get("ODOO_MCP_TOKEN") or "").strip(),
    )


def _root_cause(exc: BaseException) -> BaseException:
    """Drill through anyio/ExceptionGroup wrappers to the most useful cause."""
    seen: set[int] = set()
    while True:
        if id(exc) in seen:
            return exc
        seen.add(id(exc))
        inner = getattr(exc, "exceptions", None)
        if inner:
            exc = inner[0]
            continue
        return exc


# ── MCP session + call ───────────────────────────────────────────────────────


async def _with_session(fn: Any) -> Any:
    url, token = _config()
    if not url or not token:
        return _fail("config_error", "Set ODOO_MCP_URL and ODOO_MCP_TOKEN before using this skill.", 2)
    headers = {"Authorization": f"Bearer {token}"}
    try:
        async with streamablehttp_client(url, headers=headers) as (read, write, _):
            async with ClientSession(read, write) as session:
                await session.initialize()
                return await fn(session)
    except Exception as exc:  # noqa: BLE001 - normalise transport/auth errors
        cause = _root_cause(exc)
        return _fail("connection_error", f"{type(cause).__name__}: {cause}")


def _tool_json(result: Any) -> dict[str, Any]:
    """Pull the JSON payload out of an MCP CallToolResult (structured or text)."""
    sc = getattr(result, "structuredContent", None)
    if isinstance(sc, dict) and sc:
        if set(sc.keys()) == {"result"} and isinstance(sc["result"], dict):
            return sc["result"]
        return sc
    for block in getattr(result, "content", None) or []:
        text = getattr(block, "text", None)
        if text:
            try:
                parsed = json.loads(text)
            except (json.JSONDecodeError, TypeError):
                continue
            if isinstance(parsed, dict):
                return parsed
    return {}


async def _call(session: Any, name: str, args: dict[str, Any]) -> dict[str, Any]:
    result = await session.call_tool(name, args)
    if getattr(result, "isError", False):
        raise RuntimeError(f"{name} failed: {_tool_json(result) or result}")
    return _tool_json(result)


# ── local PDF/text extraction (no bytes leave this process) ──────────────────


def _pdftotext(data: bytes) -> str | None:
    exe = shutil.which("pdftotext")
    if not exe:
        return None
    with tempfile.NamedTemporaryFile(suffix=".pdf") as tmp:
        tmp.write(data)
        tmp.flush()
        try:
            out = subprocess.run(
                [exe, "-layout", "-nopgbrk", tmp.name, "-"],
                capture_output=True,
                timeout=60,
            )
        except (subprocess.SubprocessError, OSError):
            return None
    return out.stdout.decode("utf-8", "replace") if out.returncode == 0 else None


def _fitz():
    """Import PyMuPDF under either module name (`fitz` classic, `pymupdf` new)."""
    try:
        import fitz  # PyMuPDF
        return fitz
    except ImportError:
        try:
            import pymupdf  # PyMuPDF >= 1.24 module alias
            return pymupdf
        except ImportError:
            return None


def _pymupdf_text(data: bytes) -> str | None:
    """Extract with PyMuPDF. Honours ToUnicode CMaps and reads Type3 / custom-
    encoded fonts that pypdf mis-reads (renders fine but extracts as garbage),
    and needs no system binary — so it is tried first."""
    fitz = _fitz()
    if fitz is None:
        return None
    try:
        with fitz.open(stream=data, filetype="pdf") as doc:
            return "\n".join(page.get_text("text") for page in doc)
    except Exception:  # noqa: BLE001 - malformed PDF; hand back to caller
        return None


def _pypdf_text(data: bytes) -> str | None:
    try:
        from pypdf import PdfReader
    except ImportError:
        return None
    try:
        reader = PdfReader(io.BytesIO(data))
        return "\n".join((page.extract_text() or "") for page in reader.pages)
    except Exception:  # noqa: BLE001 - malformed PDF; hand back to caller
        return None


def _tesseract_ocr(png_path: str) -> str | None:
    """OCR a rendered page with tesseract if it is installed; else None."""
    exe = shutil.which("tesseract")
    if not exe:
        return None
    try:
        out = subprocess.run(
            [exe, png_path, "-", "--psm", "6"],
            capture_output=True,
            timeout=120,
        )
    except (subprocess.SubprocessError, OSError):
        return None
    if out.returncode != 0:
        return None
    text = out.stdout.decode("utf-8", "replace")
    return text if text.strip() else None


def _is_reliable(text: str | None) -> bool:
    """True if extracted text looks like real content, not empty or garbled.

    A Type3-font / custom-encoded PDF with no usable ToUnicode renders fine but
    extracts as a few control/replacement chars or spaced-out noise. Trusting
    that junk yields a false "no PO number" and a needless escalation — so gate
    on it and route the document to the `render` vision/OCR fallback instead."""
    if not text:
        return False
    t = text.strip()
    if len(t) < 20:
        return False
    non_space = [c for c in t if not c.isspace()]
    if len(non_space) < 12:
        return False
    if sum(c.isalpha() for c in non_space) < 8:
        return False
    bad = sum(1 for c in non_space if c == "�" or (ord(c) < 32 and c != "\t"))
    if bad / len(non_space) > 0.10:
        return False
    printable = sum(1 for c in non_space if c.isprintable())
    return printable / len(non_space) >= 0.85


def _squeeze(text: str) -> str:
    lines = [ln.rstrip() for ln in text.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    out: list[str] = []
    blanks = 0
    for ln in lines:
        if ln.strip():
            blanks = 0
            out.append(ln)
        else:
            blanks += 1
            if blanks <= 1:
                out.append("")
    return "\n".join(out).strip()


def _extract_text(data: bytes, mimetype: str) -> tuple[str, bool]:
    """Return (text, needs_vision).

    Try each available extractor (PyMuPDF → poppler pdftotext → pypdf) and use
    the FIRST result that passes the reliability gate. If none do — an
    image-only scan, or a custom-encoded PDF whose text layer won't decode —
    return ("", True) so the caller routes the document to the `render`
    vision/OCR fallback rather than handing the model unusable text."""
    if "pdf" in (mimetype or "").lower() or data[:5] == b"%PDF-":
        for extractor in (_pymupdf_text, _pdftotext, _pypdf_text):
            text = extractor(data)
            if _is_reliable(text):
                return _squeeze(text), False
        return "", True  # scanned/image-only or undecodable text layer → vision
    if (mimetype or "").lower().startswith("image/"):
        return "", True
    return _squeeze(data.decode("utf-8", "replace")), False


# ── folder resolution ────────────────────────────────────────────────────────


async def _resolve_folder(session: Any, name: str, parent_id: int | None = None) -> dict[str, Any]:
    args: dict[str, Any] = {"name": name}
    if parent_id is not None:
        args["parent_id"] = parent_id
    payload = await _call(session, "documents_list_folders", args)
    folders = payload.get("folders") or []
    if not folders:
        where = f" under folder {parent_id}" if parent_id is not None else ""
        raise ValueError(f"No Documents folder matching {name!r}{where}.")
    exact = [f for f in folders if (f.get("name") or "").strip().lower() == name.strip().lower()]
    return (exact or folders)[0]


async def _folder_id_for(session: Any, args: dict[str, Any]) -> tuple[int, int]:
    """Resolve (destination_folder_id, parent_folder_id) for a filing action."""
    to = args.get("to_folder_id", args.get("to"))
    under = args.get("under", "Purchasing")
    parent = await _resolve_folder(session, str(under))
    parent_id = int(parent["id"])
    if to is None:
        raise ValueError("Pass `to` ('Matched'/'Questions') or `to_folder_id`.")
    if isinstance(to, int) or (isinstance(to, str) and str(to).isdigit()):
        return int(to), parent_id
    child = await _resolve_folder(session, str(to), parent_id=parent_id)
    return int(child["id"]), parent_id


# ── lean shapers ─────────────────────────────────────────────────────────────


def _lean_line(line: dict[str, Any]) -> dict[str, Any]:
    return {
        "line_id": line.get("id"),
        "sku": line.get("product_sku"),
        "style": line.get("style_number"),
        "description": line.get("description") or line.get("product_name"),
        "qty": line.get("product_qty"),
        "qty_received": line.get("qty_received"),
        "qty_invoiced": line.get("qty_invoiced"),
        "price_unit": line.get("price_unit"),
        "price_subtotal": line.get("price_subtotal"),
    }


def _lean_po(po: dict[str, Any]) -> dict[str, Any]:
    return {
        "po_id": po.get("id"),
        "name": po.get("name"),
        "vendor": po.get("partner_name"),
        "partner_ref": po.get("partner_ref"),
        "state": po.get("state"),
        "amount_untaxed": po.get("amount_untaxed"),
        "amount_total": po.get("amount_total"),
        "freight_cost": po.get("freight_cost"),
        "fees_cost": po.get("fees_cost"),
        "receipt_status": po.get("receipt_status"),
        "invoice_count": po.get("invoice_count"),
        "lines": [_lean_line(ln) for ln in po.get("lines", [])],
    }


# ── actions ──────────────────────────────────────────────────────────────────


async def _extract(session: Any, args: dict[str, Any]) -> dict[str, Any]:
    folder_id = args.get("folder_id")
    folder_name = args.get("folder")
    if folder_id is None:
        if not folder_name:
            raise ValueError("Pass `folder` (name) or `folder_id`.")
        folder = await _resolve_folder(session, str(folder_name))
        folder_id, folder_name = folder["id"], folder.get("name")
    folder_id = int(folder_id)

    limit = int(args.get("limit", 200))
    include_subfolders = bool(args.get("include_subfolders", False))

    metas: list[dict[str, Any]] = []
    offset, total = 0, None
    while True:
        page = await _call(
            session,
            "documents_search",
            {
                "folder_id": folder_id,
                "limit": limit,
                "offset": offset,
                "include_subfolders": include_subfolders,
            },
        )
        docs = page.get("documents") or []
        metas.extend(docs)
        total = page.get("total_matched", len(metas))
        offset += len(docs)
        if not docs or offset >= total:
            break

    out: list[dict[str, Any]] = []
    for meta in metas:
        if meta.get("type") not in (None, "binary"):
            continue  # folders / URL bookmarks carry no bytes
        doc_id = meta["id"]
        full = await _call(session, "documents_get", {"document_id": doc_id})
        b64 = full.get("data_base64")
        if not b64:
            out.append(
                {
                    "document_id": doc_id,
                    "name": meta.get("name"),
                    "mimetype": meta.get("mimetype"),
                    "file_size": meta.get("file_size"),
                    "chars": 0,
                    "text": "",
                    "needs_vision": True,
                    "note": "no inline bytes (over transport guard or non-binary); fetch directly",
                    "open_activities": full.get("open_activities") or [],
                }
            )
            continue
        data = base64.b64decode(b64)
        text, needs_vision = _extract_text(data, meta.get("mimetype", ""))
        out.append(
            {
                "document_id": doc_id,
                "name": meta.get("name"),
                "mimetype": meta.get("mimetype"),
                "file_size": meta.get("file_size"),
                "chars": len(text),
                "text": text,
                "needs_vision": needs_vision,
                "open_activities": full.get("open_activities") or [],
            }
        )

    return {
        "folder": {"id": folder_id, "name": folder_name},
        "count": len(out),
        "total_matched": total if total is not None else len(out),
        "documents": out,
    }


async def _po_lines(session: Any, args: dict[str, Any]) -> dict[str, Any]:
    po_id = args.get("po_id")
    if po_id is None:
        po = str(args.get("po") or "").strip()
        if not po:
            raise ValueError("Pass `po` (PO number) or `po_id`.")
        found = await _call(session, "ap_search_purchase_orders", {"search": po, "limit": 10})
        pos = found.get("purchase_orders") or []
        exact = [p for p in pos if (p.get("name") or "").strip().lower() == po.lower()]
        chosen = (exact or pos)
        if not chosen:
            return {"found": False, "searched": po, "candidates": []}
        po_id = chosen[0]["id"]
        if len(chosen) > 1 and not exact:
            return {
                "found": False,
                "searched": po,
                "ambiguous": True,
                "candidates": [
                    {"po_id": p["id"], "name": p.get("name"), "vendor": p.get("partner_name")}
                    for p in chosen
                ],
            }
    detail = await _call(session, "ap_get_purchase_order", {"po_id": int(po_id)})
    return {"found": True, "po": _lean_po(detail)}


async def _apply(session: Any, args: dict[str, Any]) -> dict[str, Any]:
    if "po_id" not in args:
        raise ValueError("`po_id` is required.")
    payload: dict[str, Any] = {"po_id": int(args["po_id"])}
    if args.get("lines"):
        payload["lines"] = [
            {"line_id": int(ln["line_id"]), "price_unit": float(ln["price_unit"])}
            for ln in args["lines"]
        ]
    if "freight_cost" in args:
        payload["freight_cost"] = float(args["freight_cost"])
    if "fees_cost" in args:
        payload["fees_cost"] = float(args["fees_cost"])
    if "lines" not in payload and "freight_cost" not in payload and "fees_cost" not in payload:
        raise ValueError("Nothing to update — pass `lines` and/or `freight_cost`/`fees_cost`.")
    return await _call(session, "ap_update_po_lines", payload)


async def _bill(session: Any, args: dict[str, Any]) -> dict[str, Any]:
    """Create a DRAFT vendor bill from a reconciled PO. This command never posts
    — posting is the separate `post` command (or a human via the scheduled
    review activity). `expected_total` (the invoice docTotal) is recorded for
    the total check; keep the same value for the `post` step, which is what
    actually gates posting on the bill matching within `tolerance`.
    """
    if "po_id" not in args:
        raise ValueError("`po_id` is required.")
    payload: dict[str, Any] = {"po_id": int(args["po_id"])}
    for key in ("vendor_bill_number", "invoice_date", "review_note"):
        if args.get(key):
            payload[key] = str(args[key])
    if args.get("expected_total") is not None:
        payload["expected_total"] = float(args["expected_total"])
    if args.get("tolerance") is not None:
        payload["tolerance"] = float(args["tolerance"])
    if args.get("reviewer_user_id") is not None:
        payload["reviewer_user_id"] = int(args["reviewer_user_id"])
    if args.get("line_ids"):
        payload["line_ids"] = [int(x) for x in args["line_ids"]]
    return await _call(session, "ap_create_vendor_bill", payload)


async def _post(session: Any, args: dict[str, Any]) -> dict[str, Any]:
    """Post a DRAFT vendor bill once it MATCHES — the 'match & post' tail.

    Only reach here for a bill whose total reconciles to the vendor invoice.
    `expected_total` (the vendor invoice total) is REQUIRED and passed to the
    guarded `ap_post_vendor_bill` tool, which REFUSES to post a bill whose total
    misses it beyond `tolerance` (an absolute currency amount) — a mismatch
    comes back success:false/error, so you escalate rather than post blind.
    Pass `post: false` for a dry-run that reports `would_post` + `total_check`
    without posting; the default is to post. `vendor_bill_number` / `invoice_date`
    set the bill's ref/date first if unset; `note` is logged as an internal note.
    """
    if "bill_id" not in args:
        raise ValueError("`bill_id` is required.")
    if args.get("expected_total") is None:
        raise ValueError(
            "`expected_total` (the vendor invoice total) is required — posting is "
            "gated on the bill matching it within tolerance."
        )
    payload: dict[str, Any] = {
        "bill_id": int(args["bill_id"]),
        "post": bool(args.get("post", True)),
        "expected_total": float(args["expected_total"]),
    }
    if args.get("tolerance") is not None:
        payload["tolerance"] = float(args["tolerance"])
    for key in ("vendor_bill_number", "invoice_date", "note"):
        if args.get(key):
            payload[key] = str(args[key])
    return await _call(session, "ap_post_vendor_bill", payload)


async def _matched(session: Any, args: dict[str, Any]) -> dict[str, Any]:
    """Clean-result tail: post the 'checked' LOG NOTE on the PO (internal — never
    a 'Send message', so it is not emailed to the vendor) and file the doc to
    Matched. For a partial shipment, first read prior notes with `notes` and, if
    this shipment completes the PO's remaining lines, say so in `body`."""
    if "po_id" not in args or "document_id" not in args:
        raise ValueError("`po_id`, `body`, and `document_id` are required.")
    body = args.get("body")
    if not body:
        raise ValueError("`body` (the checked-note text) is required.")
    msg = await _call(session, "po_post_message", {"po_id": int(args["po_id"]), "body": str(body)})
    folder_id, _ = await _folder_id_for(session, {"to": args.get("to", "Matched"), "under": args.get("under", "Purchasing")})
    moved = await _call(
        session,
        "documents_update",
        {"document_id": int(args["document_id"]), "fields": {"folder_id": folder_id}},
    )
    return {
        "po_message_id": msg.get("message_id"),
        "document_id": int(args["document_id"]),
        "filed_to": "Matched",
        "folder_id": folder_id,
        "moved": bool(moved.get("updated", True)),
    }


async def _questions(session: Any, args: dict[str, Any]) -> dict[str, Any]:
    """Escalation tail: raise a reviewer activity on the doc (an internal log
    note plus a To-Do — never emailed externally) and file it to Questions."""
    if "document_id" not in args:
        raise ValueError("`document_id` is required.")
    question = args.get("question") or args.get("body")
    if not question:
        raise ValueError("`question` (what the reviewer must resolve) is required.")
    doc_id = int(args["document_id"])

    po_result = None
    if args.get("po_id") and args.get("po_note"):
        po_result = await _call(session, "po_post_message", {"po_id": int(args["po_id"]), "body": str(args["po_note"])})

    doc_msg_args: dict[str, Any] = {
        "document_id": doc_id,
        "body": str(question),
        "activity_user": str(args.get("reviewer", "Zach Tucker")),
    }
    if args.get("summary"):
        doc_msg_args["activity_summary"] = str(args["summary"])
    if args.get("deadline"):
        doc_msg_args["activity_date_deadline"] = str(args["deadline"])
    activity = await _call(session, "documents_post_message", doc_msg_args)

    folder_id, _ = await _folder_id_for(session, {"to": args.get("to", "Questions"), "under": args.get("under", "Purchasing")})
    moved = await _call(
        session,
        "documents_update",
        {"document_id": doc_id, "fields": {"folder_id": folder_id}},
    )
    return {
        "document_id": doc_id,
        "activity_id": activity.get("activity_id"),
        "reviewer": doc_msg_args["activity_user"],
        "po_message_id": (po_result or {}).get("message_id"),
        "filed_to": "Questions",
        "folder_id": folder_id,
        "moved": bool(moved.get("updated", True)),
    }


async def _move(session: Any, args: dict[str, Any]) -> dict[str, Any]:
    if "document_id" not in args:
        raise ValueError("`document_id` is required.")
    folder_id, _ = await _folder_id_for(session, args)
    moved = await _call(
        session,
        "documents_update",
        {"document_id": int(args["document_id"]), "fields": {"folder_id": folder_id}},
    )
    doc = moved.get("document") or {}
    return {
        "document_id": int(args["document_id"]),
        "folder_id": folder_id,
        "folder_name": (doc.get("folder") or {}).get("name"),
        "moved": bool(moved.get("updated", True)),
    }


async def _notes(session: Any, args: dict[str, Any]) -> dict[str, Any]:
    """Read a PO's prior chatter (log notes), newest first, plus open activities.

    Use before posting a partial-shipment 'checked' note: it shows which lines
    earlier shipments already checked, so you can tell whether this shipment is
    the last piece and the PO is now fully checked."""
    po_id = args.get("po_id")
    if po_id is None:
        po = str(args.get("po") or "").strip()
        if not po:
            raise ValueError("Pass `po_id` or `po` (PO number).")
        found = await _call(session, "ap_search_purchase_orders", {"search": po, "limit": 10})
        pos = found.get("purchase_orders") or []
        exact = [p for p in pos if (p.get("name") or "").strip().lower() == po.lower()]
        chosen = exact or pos
        if not chosen:
            return {"found": False, "searched": po, "messages": []}
        po_id = chosen[0]["id"]
    payload = await _call(
        session, "po_get_messages", {"po_id": int(po_id), "limit": int(args.get("limit", 20))}
    )
    return {"found": True, "po_id": int(po_id), **payload}


async def _render(session: Any, args: dict[str, Any]) -> dict[str, Any]:
    """Vision/OCR fallback for a document `extract` flagged `needs_vision: true`.

    Rasterises the document to PNG page image(s) with PyMuPDF (no system poppler
    needed) so the model can read it with vision; if `tesseract` is installed,
    also returns OCR text. This is what rescues a Type3-font / scanned document
    the text pass could not decode — read the returned image(s) to pull the PO
    number and line items, then continue the normal match."""
    if "document_id" not in args:
        raise ValueError("`document_id` is required.")
    fitz = _fitz()
    if fitz is None:
        raise RuntimeError("PyMuPDF is required for render; add `pymupdf` to the skill's install deps.")
    doc_id = int(args["document_id"])
    full = await _call(session, "documents_get", {"document_id": doc_id})
    b64 = full.get("data_base64")
    if not b64:
        return {
            "document_id": doc_id,
            "name": full.get("name"),
            "images": [],
            "note": "no inline bytes (over transport guard); fetch via download_url",
            "download_url": full.get("download_url"),
        }
    data = base64.b64decode(b64)
    dpi = int(args.get("dpi", 150))
    want = args.get("pages")  # optional list of 1-based page numbers
    out_dir = str(args.get("out_dir") or tempfile.mkdtemp(prefix="paymatch_render_"))
    os.makedirs(out_dir, exist_ok=True)
    mimetype = (full.get("mimetype") or "").lower()

    images: list[str] = []
    ocr_chunks: list[str] = []
    if data[:5] == b"%PDF-" or mimetype.endswith("pdf"):
        with fitz.open(stream=data, filetype="pdf") as pdf:
            for i, page in enumerate(pdf):
                if want and (i + 1) not in want:
                    continue
                path = os.path.join(out_dir, f"doc{doc_id}_p{i + 1}.png")
                page.get_pixmap(dpi=dpi).save(path)
                images.append(path)
                ocr = _tesseract_ocr(path)
                if ocr:
                    ocr_chunks.append(ocr)
    else:
        # already an image (e.g. a scanned upload) — hand it straight to vision/OCR
        ext = mimetypes.guess_extension(mimetype) or ".img"
        path = os.path.join(out_dir, f"doc{doc_id}{ext}")
        with open(path, "wb") as fh:
            fh.write(data)
        images.append(path)
        ocr = _tesseract_ocr(path)
        if ocr:
            ocr_chunks.append(ocr)

    ocr_text = "\n\n".join(ocr_chunks) or None
    return {
        "document_id": doc_id,
        "name": full.get("name"),
        "images": images,
        "dpi": dpi,
        "ocr_text": ocr_text,
        "ocr_engine": "tesseract" if ocr_chunks else None,
        "hint": None
        if ocr_text
        else "Read the PNG(s) with a vision reader to pull the PO number and line items.",
    }


ACTIONS = {
    "extract": _extract,
    "render": _render,
    "po-lines": _po_lines,
    "notes": _notes,
    "apply": _apply,
    "bill": _bill,
    "post": _post,
    "matched": _matched,
    "questions": _questions,
    "move": _move,
}

USAGE = "paymatch.py <" + "|".join(ACTIONS) + ">   # JSON args as 2nd arg or on stdin"


def _read_args() -> dict[str, Any]:
    raw = None
    if len(sys.argv) >= 3:
        raw = sys.argv[2]
    elif not sys.stdin.isatty():
        raw = sys.stdin.read().strip()
    raw = (raw or "").strip() or "{}"
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        sys.exit(_fail("invalid_arguments", f"Arguments must be valid JSON: {exc}", 2))
    if not isinstance(parsed, dict):
        sys.exit(_fail("invalid_arguments", "Arguments must be a JSON object.", 2))
    return parsed


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        return _fail("usage", USAGE, 2)
    handler = ACTIONS.get(sys.argv[1])
    if handler is None:
        return _fail("unknown_action", f"Unknown action {sys.argv[1]!r}. Use: {', '.join(ACTIONS)}", 2)

    args = _read_args()

    async def fn(session: Any) -> dict[str, Any]:
        try:
            return await handler(session, args)
        except (KeyError, ValueError, TypeError) as exc:
            return {"__error__": ("validation_error", str(exc))}

    res = anyio.run(lambda: _with_session(fn))
    if isinstance(res, int):  # config/connection error already printed
        return res
    if isinstance(res, dict) and "__error__" in res:
        etype, emsg = res["__error__"]
        return _fail(etype, emsg, 2)
    print(json.dumps(res, default=str, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
