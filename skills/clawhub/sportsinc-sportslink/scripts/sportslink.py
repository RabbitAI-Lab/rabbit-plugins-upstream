#!/usr/bin/env python3
"""Sports Inc SportsLink API adapter — pull dealer invoices ("documents") and
mark them consumed.

Sports Inc is a buying group that does NOT send individual vendor invoices;
instead its SportsLink REST API exposes the dealer's documents from the
SportsWeb Invoice Center. This module is the SOURCE adapter for that API: it
authenticates, pages, normalises each SI document into a common invoice shape
(the same shape a PDF-extracted invoice would have, so downstream matching is
source-agnostic), and marks documents historical once they've been imported.

It is **customer-agnostic** — every Sports Inc dealer uses this same API — so it
carries no BaconCo/Odoo specifics. The payable-matching workflow consumes its
output; this adapter never touches Odoo.

Actions
-------
    list            GET active documents (normalised). Auto-pages.
                    Input (all optional): {"active": true, "lines": true,
                      "ediOnly": true, "poNumber": "...", "siDocNumber": 123,
                      "siDocStartDate": "2024-01-01", "siDocEndDate": "...",
                      "supplierDocStartDate": "...", "supplierDocEndDate": "...",
                      "page": 1, "pageSize": 200, "all": true,
                      "orderBy": "SIDocDate", "orderByDescending": false}
                    Defaults: active=true, lines=true, all=true (page to the end).
    get             Convenience: one/few docs by identifier.
                    Input: {"poNumber": "P13189"}  or  {"siDocNumber": 12345}
    mark-historical Mark documents consumed (PATCH status isActive=false) AFTER
                    they've been billed. Input: {"siDocNumbers": [12345, 23456]}.
                    Honors dry_run / SPORTSINC_DRY_RUN.

Environment
-----------
    SPORTSINC_API_KEY   Required. Sent as the `X-API-KEY` header.
    SPORTSINC_API_URL   Optional. Default https://api.sportsinc.com/
    SPORTSINC_DRY_RUN   Optional. If truthy, `mark-historical` is simulated.

Operational notes
-----------------
    * Do not pull before ~10:30am ET — SI's internal processing runs first.
    * Line-item data is EDI-only; scanned/OCR documents have header totals but
      no `lines` (`has_lines: false`). Use `ediOnly: true` to fetch only
      documents that carry lines.
    * `is_credit: true` marks a credit memo — handle separately, never as a bill.
    * EXACTLY-ONCE: import first, mark-historical AFTER the bill is created.
      Never mark on read (the API's `moveToHistorical=true` GET flag is
      deliberately NOT used here) — a crash between read and bill would drop the
      invoice.

Every command prints one JSON object on stdout, or {"error": {...}} with a
non-zero exit. Args are the 2nd CLI arg or JSON on stdin.
"""

from __future__ import annotations

import json
import os
import sys
import time
from typing import Any

try:
    import requests
except ImportError:  # pragma: no cover - surfaced at runtime
    requests = None  # type: ignore


DOCUMENTS_PATH = "dealers/documents/"
STATUS_PATH = "dealers/documents/status"

# GET query params we pass straight through (SportsLink param name : type-ish).
_PASSTHROUGH = {
    "poNumber", "supplierDocNumber", "siDocNumber", "siDocDate",
    "siDocStartDate", "siDocEndDate", "supplierDocDate",
    "supplierDocStartDate", "supplierDocEndDate", "fields", "orderBy",
    "orderByDescending",
}


def _fail(error_type: str, message: str, code: int = 1, **extra: Any) -> int:
    print(json.dumps({"error": {"type": error_type, "message": message, **extra}}))
    return code


def _truthy(v: Any) -> bool:
    return str(v).strip().lower() in ("1", "true", "yes", "on")


def _config() -> tuple[str, str]:
    return (
        (os.environ.get("SPORTSINC_API_URL") or "https://api.sportsinc.com/").strip().rstrip("/") + "/",
        (os.environ.get("SPORTSINC_API_KEY") or "").strip(),
    )


class _Client:
    def __init__(self, base_url: str, api_key: str, timeout: int = 30) -> None:
        self._base = base_url
        self._timeout = timeout
        self._s = requests.Session()
        self._s.headers.update({"X-API-KEY": api_key, "Accept": "application/json"})

    def _request(self, method: str, path: str, *, params=None, json_body=None) -> Any:
        url = self._base + path.lstrip("/")
        last_exc = None
        for attempt in range(4):  # resilience: retry transient failures
            try:
                resp = self._s.request(method, url, params=params, json=json_body, timeout=self._timeout)
            except requests.RequestException as exc:  # type: ignore[union-attr]
                last_exc = exc
                time.sleep(2 ** attempt)
                continue
            if resp.status_code == 401:
                raise _ApiError("auth_error", "SportsLink rejected the API key (401).", 401)
            if resp.status_code in (429, 500, 502, 503, 504) and attempt < 3:
                time.sleep(2 ** attempt)
                continue
            if not resp.ok:
                raise _ApiError("api_error", f"{resp.status_code}: {resp.text[:300]}", resp.status_code)
            if resp.status_code == 204 or not resp.content:
                return {}
            try:
                return resp.json()
            except ValueError:
                raise _ApiError("bad_response", f"Non-JSON response: {resp.text[:200]}", resp.status_code)
        raise _ApiError("connection_error", f"SportsLink unreachable: {last_exc}")

    def get_documents(self, params: dict[str, Any]) -> dict[str, Any]:
        return self._request("GET", DOCUMENTS_PATH, params=params)

    def patch_status(self, si_doc_numbers: list[int], is_active: bool) -> Any:
        return self._request("PATCH", STATUS_PATH, json_body={"siDocNumbers": si_doc_numbers, "isActive": is_active})


class _ApiError(RuntimeError):
    def __init__(self, error_type: str, message: str, status: int | None = None) -> None:
        self.error_type = error_type
        self.status = status
        super().__init__(message)


# ── normalisation: SI document -> common invoice shape ───────────────────────


def _num(v: Any) -> Any:
    return v if isinstance(v, (int, float)) else v


def _normalise(item: dict[str, Any]) -> dict[str, Any]:
    lines = item.get("lines") or []
    return {
        "source": "sports_inc",
        "po_number": item.get("poNumber"),
        "si_doc_number": item.get("siDocNumber"),
        "invoice_number": item.get("supplierDocNumber") or (
            str(item["siDocNumber"]) if item.get("siDocNumber") is not None else None
        ),
        "supplier_doc_number": item.get("supplierDocNumber"),
        "invoice_date": item.get("supplierDocDate") or item.get("siDocDate"),
        "si_doc_date": item.get("siDocDate"),
        "due_date": item.get("dueDate"),
        "supplier": item.get("supplier"),
        "is_credit": bool(item.get("isCredit", False)),
        "has_lines": bool(lines),
        "total": item.get("docTotal"),
        "charges": {
            "merchandise": item.get("merchandiseTotal"),
            "freight": item.get("freightAmount"),
            "freight_allowance": item.get("freightAllowance"),
            "si_upcharge": item.get("siUpcharge"),
            "svc_handle": item.get("svcHandleCharge"),
            "sales_tax": item.get("salesTax"),
            "excise_tax": item.get("exciseTax"),
            "discount": item.get("discountAmount"),
        },
        "terms_of_payment": item.get("termsOfPayment"),
        "tracking_number": item.get("trackingNumber"),
        "lines": [
            {
                "item": ln.get("supplierItemNumber"),
                "upc": ln.get("upc"),
                "description": ln.get("description"),
                "size": ln.get("size"),
                "color": ln.get("color"),
                "unit": ln.get("unit"),
                "qty_ordered": ln.get("quantityOrdered"),
                "qty_shipped": ln.get("quantityShipped"),
                "qty_backordered": ln.get("quantityBackOrdered"),
                "list_price": ln.get("listPrice"),
                "discount_pct": ln.get("discountPercent"),
                "net_price": ln.get("netPrice"),
                "extension": ln.get("extension"),
            }
            for ln in lines
        ],
    }


# ── param building ───────────────────────────────────────────────────────────


def _build_params(args: dict[str, Any]) -> dict[str, Any]:
    params: dict[str, Any] = {}
    # Booleans default to the safe/typical values.
    params["active"] = "true" if args.get("active", True) else "false"
    params["lines"] = "true" if args.get("lines", True) else "false"
    if args.get("ediOnly", False):
        params["excludeScannedDocuments"] = "true"
    for key in _PASSTHROUGH:
        if args.get(key) is not None:
            val = args[key]
            params[key] = ("true" if val else "false") if isinstance(val, bool) else val
    return params


# ── actions ──────────────────────────────────────────────────────────────────


def _list(client: _Client, args: dict[str, Any]) -> dict[str, Any]:
    params = _build_params(args)
    page = int(args.get("page", 1))
    page_size = int(args.get("pageSize", 200))
    auto = bool(args.get("all", True))

    invoices: list[dict[str, Any]] = []
    total_count = None
    pages_read = 0
    while True:
        params["page"] = page
        params["pageSize"] = page_size
        payload = client.get_documents(params)
        items = payload.get("items") or []
        invoices.extend(_normalise(it) for it in items)
        total_count = payload.get("totalCount", len(invoices))
        pages_read += 1
        if not auto or not payload.get("hasNextPage") or not items or pages_read >= 50:
            break
        page += 1

    return {
        "source": "sports_inc",
        "count": len(invoices),
        "total_count": total_count,
        "pages_read": pages_read,
        "invoices": invoices,
    }


def _get(client: _Client, args: dict[str, Any]) -> dict[str, Any]:
    if not (args.get("poNumber") or args.get("siDocNumber") or args.get("supplierDocNumber")):
        raise ValueError("Pass an identifier: poNumber, siDocNumber, or supplierDocNumber.")
    # A specific-doc lookup shouldn't filter by active-only by default.
    q = dict(args)
    q.setdefault("active", False)
    return _list(client, q)


def _mark_historical(client: _Client, args: dict[str, Any]) -> dict[str, Any]:
    nums = args.get("siDocNumbers")
    if not isinstance(nums, list) or not nums:
        raise ValueError("`siDocNumbers` (a non-empty list of integers) is required.")
    nums = [int(n) for n in nums]
    dry = bool(args.get("dry_run")) or _truthy(os.environ.get("SPORTSINC_DRY_RUN", ""))
    if dry:
        return {"dry_run": True, "would_mark_historical": nums, "isActive": False}
    client.patch_status(nums, is_active=False)  # 204 No Content on success
    return {"marked_historical": nums, "isActive": False}


def _get_for_a2a(client: _Client, args: dict[str, Any]) -> dict[str, Any]:
    """A2A-safe action for structured inter-agent requests.

    Contract request (all fields optional):
    {
      "customer_ref": "DEALER-001",     # advisory only — echoed back, NOT a filter
      "date_range": {"start": "2024-01-01", "end": "2024-12-31"},
      "include_historical": false        # false (default) → active/un-imported only
    }

    Unlike the exit-code contract of the other actions, this action always exits
    0 and reports failure IN-BAND via `success: false` + `error`, so an A2A caller
    reads one structured envelope whether the call succeeded or not:
    {"success": true, "invoices": [...], "metadata": {...}, "error": null}
    {"success": false, "invoices": null, "metadata": null, "error": {...}}

    Note on `customer_ref`: the SportsLink API key is issued per dealer and the
    API has no customer filter, so `customer_ref` cannot scope the result. It is
    accepted for auditing and echoed back in `metadata.customer_ref`; downstream
    (Odoo/payable-matching) does any customer-specific handling.
    """
    def _err(error_type: str, message: str, retriable: bool) -> dict[str, Any]:
        return {
            "success": False,
            "invoices": None,
            "metadata": None,
            "error": {"type": error_type, "message": message, "retriable": retriable},
        }

    try:
        customer_ref = args.get("customer_ref")
        date_range = args.get("date_range") or {}
        # Historical inclusion is governed by `include_historical` (NOT by any
        # status string): active=False lifts the active-only filter and returns
        # historical/consumed docs too. Default keeps the safe un-imported inbox.
        include_historical = bool(args.get("include_historical", False))

        list_args: dict[str, Any] = {
            "active": not include_historical,
            "lines": True,
            "all": True,  # Auto-page through all results
        }
        if date_range.get("start"):
            list_args["siDocStartDate"] = date_range["start"]
        if date_range.get("end"):
            list_args["siDocEndDate"] = date_range["end"]

        result = _list(client, list_args)

        return {
            "success": True,
            "invoices": result.get("invoices", []),
            "metadata": {
                "count": result.get("count"),
                "total_count": result.get("total_count"),
                "pages_read": result.get("pages_read"),
                "source": result.get("source"),
                "customer_ref": customer_ref,        # echoed for the caller's audit
                "include_historical": include_historical,
            },
            "error": None,
        }
    except _ApiError as exc:
        return _err(
            exc.error_type,
            str(exc),
            exc.error_type in ("connection_error", "bad_response"),
        )
    except (KeyError, ValueError, TypeError) as exc:
        return _err("validation_error", str(exc), False)


ACTIONS = {
    "list": _list,
    "get": _get,
    "mark-historical": _mark_historical,
    "get-for-a2a": _get_for_a2a,
}

USAGE = "sportslink.py <" + "|".join(ACTIONS) + ">   # JSON args as 2nd arg or on stdin"


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
    if requests is None:
        return _fail("config_error", "The 'requests' package is required. Install it (see the skill's install deps).", 2)

    base_url, api_key = _config()
    if not api_key:
        return _fail("config_error", "Set SPORTSINC_API_KEY (request one from mhoerner@hq.sportsinc.com).", 2)

    args = _read_args()
    client = _Client(base_url, api_key)
    try:
        result = handler(client, args)
    except _ApiError as exc:
        return _fail(exc.error_type, str(exc), 1, status=exc.status)
    except (KeyError, ValueError, TypeError) as exc:
        return _fail("validation_error", str(exc), 2)
    print(json.dumps(result, default=str, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
