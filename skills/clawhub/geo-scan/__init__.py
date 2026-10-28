"""Hermes plugin: geo_scan — answer-engine readiness audit (no API key, stdlib).

The engine is `geo_scan.py` next to this file; the repo root IS the plugin
directory, so there is exactly one copy of the scoring code. The engine path is
fixed; there is no override and no fallback location.
"""
from __future__ import annotations

import json
import time
import urllib.parse
from pathlib import Path

__version__ = "1.2.3"

_MAX_PAGES = 25
_DEFAULT_PAGES = 8
_BUDGET_SECONDS = 90  # the scan runs synchronously inside an agent turn


def _load_engine():
    """Import the engine as a plain submodule of this plugin package.

    A static relative import — no file-path spec, no exec_module, no fallback
    locations — so nothing outside the installed plugin package can be executed.
    Hermes loads this directory as a package (it sets __path__ to the plugin
    dir), which is what makes `from . import geo_scan` resolve.
    """
    from . import geo_scan  # noqa: PLC0415 - the engine is this package's submodule
    return geo_scan


def _normalise(url: str) -> str:
    url = (url or "").strip()
    if not url:
        raise ValueError("url is required")
    return url if "://" in url else "https://" + url


def _handle_geo_scan(params: dict) -> str:
    try:
        engine = _load_engine()
    except Exception as e:  # noqa: BLE001
        return json.dumps({"ok": False, "error": f"engine load failed: {e}"})

    try:
        root = _normalise(params.get("url", ""))
    except ValueError as e:
        return json.dumps({"ok": False, "error": str(e)})

    try:
        pages = int(params.get("pages", _DEFAULT_PAGES))
    except (TypeError, ValueError):
        pages = _DEFAULT_PAGES
    pages = max(1, min(_MAX_PAGES, pages))

    try:
        # public_only: refuse private/loopback/link-local hosts (redirects included), so a
        # prompt-injected agent cannot use the tool to probe the LAN
        findings = engine.scan(root, max_pages=pages, budget=_BUDGET_SECONDS, public_only=True)
    except Exception as e:  # noqa: BLE001
        return json.dumps({"ok": False, "error": f"scan failed for {root}: {e}",
                           "hint": "site unreachable, blocked, private address, or not a URL"})

    result = {
        "ok": True,
        "tool": "geo_scan",
        "version": findings.get("version"),
        "root": findings.get("root", root),
        "score": findings.get("score"),
        "grade": findings.get("grade"),
        "axes": [
            {"id": c["id"], "name": c["name"], "score": c["score"], "max": c["max"],
             "status": c["status"], "evidence": c["evidence"]}
            for c in findings.get("checks", [])
        ],
        "actions": [{"priority": p, "action": a} for p, a in findings.get("actions", [])],
        "pages_sampled": len(findings.get("pages", [])),
        "pages": [
            {"url": p.get("url"), "words": p.get("words"), "h1": p.get("h1"),
             "schema": p.get("schema_types"), "figures": p.get("stat_hits"),
             "quotable": p.get("quotable_hits")}
            for p in findings.get("pages", [])[:12]
        ],
        "signals": findings.get("signals", {}),
        "notes": findings.get("notes", [])[:10],
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
    }

    if params.get("save"):
        try:
            out_dir = Path(params.get("out_dir")
                           or Path.home() / ".hermes" / "cache" / "scratch" / "geo-scan")
            out_dir.mkdir(parents=True, exist_ok=True)
            slug = urllib.parse.urlparse(root).netloc.replace("www.", "_")
            stamp = time.strftime("%Y%m%d-%H%M")
            md_path = out_dir / f"geo-scan-{slug}-{stamp}.md"
            json_path = out_dir / f"geo-scan-{slug}-{stamp}.json"
            md_path.write_text(engine.to_md(findings), encoding="utf-8")
            slim = {k: v for k, v in findings.items() if k != "pages"}
            slim["pages"] = [{k: v for k, v in p.items() if k != "title"}
                             for p in findings.get("pages", [])]
            json_path.write_text(json.dumps(slim, indent=1), encoding="utf-8")
            result["report_md"] = str(md_path)
            result["report_json"] = str(json_path)
        except Exception as e:  # noqa: BLE001
            result["save_error"] = str(e)

    return json.dumps(result, ensure_ascii=False)


def register(ctx):
    description = (
        "Audit a public website's answer-engine readiness (ChatGPT search / Perplexity / "
        "Claude / Gemini / AI Overviews): 0-100 across crawler access for search agents, "
        "machine readability, snippet permissions, structure, quotability and freshness, "
        "each with its evidence, plus a prioritised fix list. No API key. Scanning is "
        "read-only: robots.txt-obedient HTTP GETs at about one per second, max 90 s, "
        "public hosts only. When save=true the tool additionally writes two report "
        "files (Markdown + JSON) to out_dir (default ~/.hermes/cache/scratch/geo-scan)."
    )
    ctx.register_tool(
        name="geo_scan",
        toolset="geo_scan",
        description=description,
        # the registry shows the model {**schema, "name": name}: name/description/parameters
        schema={
            "name": "geo_scan",
            "description": description,
            "parameters": {
                "type": "object",
                "required": ["url"],
                "properties": {
                    "url": {"type": "string",
                            "description": "Site or page to audit (https://example.com)"},
                    "pages": {"type": "integer",
                              "description": f"Pages to sample, 1-{_MAX_PAGES} (default {_DEFAULT_PAGES})"},
                    "save": {"type": "boolean",
                             "description": "Also write the full Markdown + JSON report to disk"},
                    "out_dir": {"type": "string",
                                "description": "Directory for saved reports (default: scratch/geo-scan)"},
                },
            },
        },
        handler=_handle_geo_scan,
    )
