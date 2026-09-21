#!/usr/bin/env python3
"""token_optimizer.py — Token usage reduction & speed optimization for universal-maps-navigator v2.

Techniques:
- Compact output (numbers only, no filler)
- Structured JSON with minimal fields
- Prefix caching friendly (stable User-Agent, no timestamp at front)
- Decision tree table replaces prose
- Single example pattern
- Truncation guard (350 token budget)
- Streaming/chunking for large responses
- Parallel requests where possible

Stdlib only, Python 3.8+.

Usage:
    from token_optimizer import compact_route, compact_poi, minimal_json, estimate_tokens, truncate_if_needed
"""
from __future__ import annotations
import json
from typing import Dict, List

# Token estimation: ~4 chars = 1 token (OpenAI heuristic)
def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)

def truncate_if_needed(text: str, max_tokens: int = 350, suffix: str = "\n... [truncated, use --json for full]") -> str:
    """Truncate to token budget, preserving summary + links."""
    est = estimate_tokens(text)
    if est <= max_tokens:
        return text
    # Keep first 70% + last 10% (summary + links)
    chars_budget = max_tokens * 4
    keep_first = int(chars_budget * 0.7)
    keep_last = int(chars_budget * 0.1)
    return text[:keep_first] + suffix + (text[-keep_last:] if keep_last > 0 else "")

def compact_route(route: Dict, units: str = "metric") -> str:
    """Ultra-compact route representation: ~30 tokens vs 150+ verbose."""
    dist = route.get("distance_m", 0)
    dur = route.get("duration_s", 0)
    # Format distance/duration compact
    if dist >= 1000:
        dist_s = f"{dist/1000:.1f}km"
    else:
        dist_s = f"{dist:.0f}m"
    mins = int(dur // 60)
    if mins >= 60:
        dur_s = f"{mins//60}h{mins%60:02d}"
    else:
        dur_s = f"{mins}min"
    summary = route.get("summary", "")[:30]
    engine = route.get("engine", "")
    # Compact: "ROUTE 12.3km 15min via A1 [valhalla] conf:high"
    conf = route.get("confidence", "high")
    return f"ROUTE {dist_s} {dur_s} via {summary} [{engine}] conf:{conf}"

def compact_poi(poi: Dict) -> str:
    """Compact POI: ~15 tokens."""
    name = poi.get("name", "POI")[:20]
    dist = poi.get("distance_m", 0)
    if dist >= 1000:
        dist_s = f"{dist/1000:.1f}km"
    else:
        dist_s = f"{dist:.0f}m"
    lat = poi.get("lat", 0)
    lon = poi.get("lon", 0)
    return f"{name} {dist_s} [{lat:.4f},{lon:.4f}]"

def minimal_json(data: Dict, compact: bool = False) -> Dict:
    """Strip verbose fields for token saving. Keeps essential + survival fields."""
    if not compact:
        return data
    # If data is list, handle first element
    if isinstance(data, list):
        return [minimal_json(d, True) for d in data[:5]]
    # Keep only essential, but preserve survival and i18n fields
    minimal = {}
    # Generic geo
    if "distance_m" in data:
        minimal["dist_m"] = data["distance_m"]
    if "duration_s" in data:
        minimal["dur_s"] = data["duration_s"]
    if "lat" in data and "lon" in data:
        minimal["ll"] = [round(data["lat"], 5), round(data["lon"], 5)]
    if "name" in data:
        minimal["name"] = str(data["name"])[:30]
    if "confidence" in data:
        minimal["conf"] = data["confidence"]
    if "source" in data:
        minimal["src"] = data["source"]
    if "sources" in data:
        minimal["srcs"] = data["sources"][:3]
    # Survival
    if "text" in data:
        # Truncate text to 400 chars in compact (~100 tokens)
        txt = data["text"]
        minimal["text"] = txt[:400] + ("..." if len(txt) > 400 else "")
    if "terrain" in data and data["terrain"]:
        minimal["terrain"] = data["terrain"].get("terrain") if isinstance(data["terrain"], dict) else str(data["terrain"])[:100]
    if "disaster" in data and data["disaster"]:
        minimal["disaster"] = data["disaster"].get("disaster") if isinstance(data["disaster"], dict) else str(data["disaster"])[:100]
    if "situation" in data and data["situation"]:
        minimal["situation"] = str(data["situation"])[:80]
    if "sos" in data:
        sos_val = data["sos"]
        if isinstance(sos_val, dict):
            # sos dict contains sos list
            minimal["sos"] = sos_val.get("sos", [])[:3] if isinstance(sos_val.get("sos", []), list) else str(sos_val)[:100]
            if "navigation_sos" in sos_val:
                minimal["nav_sos"] = sos_val.get("navigation_sos", [])[:3]
        elif isinstance(sos_val, list):
            minimal["sos"] = sos_val[:3]
        else:
            minimal["sos"] = str(sos_val)[:100]
    if "navigation_sos" in data:
        nav = data["navigation_sos"]
        if isinstance(nav, list):
            minimal["nav_sos"] = nav[:3]
        else:
            minimal["nav_sos"] = str(nav)[:100]
    if "terrains" in data:
        minimal["terrains"] = data["terrains"]
    if "disasters" in data:
        minimal["disasters"] = data["disasters"]
    # i18n
    if "languages" in data:
        minimal["langs"] = len(data["languages"])
    if "detected" in data:
        minimal["detected"] = data["detected"]
    if "translated" in data:
        minimal["translated"] = data["translated"]
    if "original" in data:
        minimal["original"] = str(data["original"])[:30]
    # Routes
    if "routes" in data:
        minimal["routes"] = [
            {
                "dist_m": r.get("distance_m"),
                "dur_s": r.get("duration_s"),
                "engine": r.get("engine"),
                "conf": r.get("confidence", "high")
            } for r in data["routes"][:1]
        ]
    if "results" in data:
        minimal["results"] = [
            {"name": r.get("name", "")[:20], "dist_m": r.get("distance_m"), "ll": [round(r.get("lat",0),4), round(r.get("lon",0),4)]}
            for r in data["results"][:5]
        ]
    if "deep_links" in data and compact:
        minimal["links"] = {k: v["url"] for k, v in list(data["deep_links"].items())[:2]}
    # Fallback: if minimal empty, keep original truncated
    if not minimal:
        # Keep up to 5 keys truncated
        for k, v in list(data.items())[:5]:
            if isinstance(v, str):
                minimal[k] = v[:100]
            else:
                minimal[k] = v
    return minimal

def structured_output(data: Dict, mode: str = "human", max_tokens: int = 350) -> str:
    """Return structured output optimized for token usage."""
    if mode == "json":
        # Minimal JSON
        minimal = minimal_json(data, compact=True)
        text = json.dumps(minimal, ensure_ascii=False)
        return truncate_if_needed(text, max_tokens)
    elif mode == "compact":
        # Compact human
        if "routes" in data:
            routes = data["routes"]
            lines = [compact_route(r) for r in routes[:2]]
            if "deep_links" in data:
                # Add 2 links
                links = list(data["deep_links"].values())[:2]
                for l in links:
                    lines.append(f"LINK {l.get('label','')}: {l.get('url','')[:60]}")
            text = "\n".join(lines)
            return truncate_if_needed(text, max_tokens)
        elif "results" in data:
            lines = [compact_poi(r) for r in data["results"][:5]]
            text = "\n".join(lines)
            return truncate_if_needed(text, max_tokens)
        else:
            text = json.dumps(minimal_json(data, True), ensure_ascii=False)
            return truncate_if_needed(text, max_tokens)
    else:
        # Human verbose but still budget-guarded
        # This is handled by umn.py's emit
        return json.dumps(data, ensure_ascii=False)

def token_budget_guard(text: str, budget: int = 350) -> Dict:
    """Check if text exceeds budget, return metrics."""
    est = estimate_tokens(text)
    return {
        "tokens_est": est,
        "budget": budget,
        "exceeds": est > budget,
        "savings_needed": max(0, est - budget),
        "suggestion": "Use --compact --json to reduce" if est > budget else "OK"
    }

# System prompt snippet for AI agents to reduce token usage
SYSTEM_PROMPT_SNIPPET = """You are navigation agent. Use umn CLI with --compact --json for minimal tokens.
Prefer lat,lon > saved > geocode (save 1 req + 200 tokens).
Cache geocodes 7d, reuse.
Decision tree: latlon? direct : saved? direct : ambiguous? geocode limit 3.
If response >350 tokens, truncate to summary + 2 deep links.
Never hallucinate traffic/cameras. Cite source [src=valhalla|overpass].
Confidence: high=verified, med=fallback, low=uncertain → abstain.
"""

def get_system_prompt_snippet() -> str:
    return SYSTEM_PROMPT_SNIPPET
