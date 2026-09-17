"""Provider-resilient AI normalization hop chain (v2.16, strategy P5.1).

Normalizes Persian/English product-listing text into English molecule
identities by hopping across providers with automatic failover, adaptive
token budgets, jittered pacing, and a live NONE-rate metric for model
degradation detection.

Hop order (first working hop wins; a dead hop is skipped for the rest of
the process):
  1. Arena workspace ``router.py`` (if present — it already implements
     provider failover + key management; ``$ICDB_ROUTER`` or
     ``/home/user/tools/router.py``).
  2. Direct free-tier provider endpoints from environment keys
     (GEMINI_API_KEY, MISTRAL_API_KEY, OPENROUTER_API_KEY, LLM7_API_KEY).
  3. No hops available -> ``NoHopError`` (callers must degrade gracefully).

Batch normalization uses strict numbered-line parsing and reports the
per-batch NONE rate so callers can detect model degradation live
(F8: in one session groq 404'd, zai/cohere 429'd, gemini 404'd at high
max_tokens — the hop chain + adaptive budget is the fix).

Stdlib only. No keys are shipped in the skill; keys come from the
environment or the arena router.
"""
from __future__ import annotations

import json
import os
import random
import re
import subprocess
import time
import urllib.parse
import urllib.request
from typing import Dict, List, Optional

DEFAULT_TIMEOUT = 120
DEFAULT_BATCH = 6


class NoHopError(RuntimeError):
    """No AI hop is available (no router.py and no provider keys)."""


# --------------------------------------------------------------------------
# Arena router.py hop
# --------------------------------------------------------------------------

def _router_path() -> Optional[str]:
    env = os.environ.get("ICDB_ROUTER")
    if env and os.path.exists(env):
        return env
    for cand in ("/home/user/tools/router.py",):
        if os.path.exists(cand):
            return cand
    return None


def _hop_router(texts: List[str], system: str, timeout: int) -> List[str]:
    """Call the arena router with the numbered prompt; return raw answers."""
    router = _router_path()
    if not router:
        raise NoHopError("router.py not found")
    items = "\n".join(f"{i + 1}) {t[:700]}" for i, t in enumerate(texts))
    prompt = system + "\n\nItems:\n" + items
    try:
        r = subprocess.run(
            ["python3", router, prompt, "--task", "general"],
            capture_output=True, text=True, timeout=timeout)
        return [r.stdout or ""]
    except subprocess.TimeoutExpired:
        raise RuntimeError("router.py timed out")


# --------------------------------------------------------------------------
# Direct provider hops (env keys, stdlib urllib)
# --------------------------------------------------------------------------

def _http_post_json(url: str, payload: dict, headers: dict,
                    timeout: int) -> dict:
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", **headers},
        method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", "ignore"))


def _hop_gemini(texts, system, timeout, max_tokens=1024):
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise NoHopError("no GEMINI_API_KEY")
    items = "\n".join(f"{i + 1}) {t[:700]}" for i, t in enumerate(texts))
    d = _http_post_json(
        "https://generativelanguage.googleapis.com/v1beta/models/"
        "gemini-2.0-flash:generateContent",
        {"contents": [{"parts": [{"text": system + "\n\nItems:\n" + items}]}],
         "generationConfig": {"maxOutputTokens": max_tokens}},
        {"x-goog-api-key": key}, timeout)
    parts = d.get("candidates", [{}])[0].get("content", {})
    return ["".join(p.get("text", "") for p in parts.get("parts", []))]


def _hop_mistral(texts, system, timeout, max_tokens=1024):
    key = os.environ.get("MISTRAL_API_KEY")
    if not key:
        raise NoHopError("no MISTRAL_API_KEY")
    items = "\n".join(f"{i + 1}) {t[:700]}" for i, t in enumerate(texts))
    d = _http_post_json(
        "https://api.mistral.ai/v1/chat/completions",
        {"model": "mistral-small-latest",
         "messages": [{"role": "user",
                       "content": system + "\n\nItems:\n" + items}],
         "max_tokens": max_tokens},
        {"Authorization": f"Bearer {key}"}, timeout)
    return [d["choices"][0]["message"]["content"]]


def _hop_openrouter(texts, system, timeout, max_tokens=1024):
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise NoHopError("no OPENROUTER_API_KEY")
    items = "\n".join(f"{i + 1}) {t[:700]}" for i, t in enumerate(texts))
    d = _http_post_json(
        "https://openrouter.ai/api/v1/chat/completions",
        {"model": "meta-llama/llama-3.1-70b-instruct",
         "messages": [{"role": "user",
                       "content": system + "\n\nItems:\n" + items}],
         "max_tokens": max_tokens},
        {"Authorization": f"Bearer {key}"}, timeout)
    return [d["choices"][0]["message"]["content"]]


def _hop_llm7(texts, system, timeout, max_tokens=1024):
    key = os.environ.get("LLM7_API_KEY")
    base = os.environ.get("LLM7_BASE_URL", "https://api.llm7.io/v1")
    if not key:
        raise NoHopError("no LLM7_API_KEY")
    items = "\n".join(f"{i + 1}) {t[:700]}" for i, t in enumerate(texts))
    d = _http_post_json(
        base.rstrip("/") + "/chat/completions",
        {"model": "default",
         "messages": [{"role": "user",
                       "content": system + "\n\nItems:\n" + items}],
         "max_tokens": max_tokens},
        {"Authorization": f"Bearer {key}"}, timeout)
    return [d["choices"][0]["message"]["content"]]


HOPS = [
    ("arena-router", _hop_router),
    ("gemini", _hop_gemini),
    ("mistral", _hop_mistral),
    ("openrouter", _hop_openrouter),
    ("llm7", _hop_llm7),
]

# dead hops are remembered for the life of the process (F8: don't re-pay
# the timeout cost for a provider that just died)
_DEAD_HOPS: set = set()


def _call_hop(name: str, fn, texts: List[str], system: str,
              timeout: int, max_tokens: int) -> List[str]:
    try:
        return fn(texts, system, timeout, max_tokens=max_tokens)
    except TypeError:
        return fn(texts, system, timeout)


def hop_chain_call(texts: List[str], system: str, *,
                   timeout: int = DEFAULT_TIMEOUT,
                   max_tokens: int = 1024,
                   backoff: float = 1.5) -> Dict:
    """Try each hop until one returns text. Adaptive token budget: on a
    4xx-class failure (HTTP 400/404/413) the budget halves (gemini 404s
    at high max_tokens); transient 429/5xx waits with backoff then
    moves to the next hop.

    Returns {"text": str, "hop": name, "failures": [(hop, err), ...]}.
    Raises NoHopError when every hop is unavailable/failed.
    """
    failures: List[tuple] = []
    budget = max_tokens
    for name, fn in HOPS:
        if name in _DEAD_HOPS:
            continue
        try:
            out = _call_hop(name, fn, texts, system, timeout, budget)
            # hops return either [text] or a bare text — handle both
            if isinstance(out, (list, tuple)):
                text = (out[0] if out else "").strip()
            else:
                text = (out or "").strip()
            if not text:
                raise RuntimeError("empty response")
            return {"text": text, "hop": name, "failures": failures}
        except NoHopError as exc:
            failures.append((name, f"unavailable: {exc}"))
            continue
        except Exception as exc:  # noqa: BLE001 - hop failover by design
            msg = str(exc)
            failures.append((name, f"{type(exc).__name__}: {msg[:120]}"))
            if "HTTP Error 429" in msg or "HTTP Error 5" in msg:
                # transient overload — brief backoff, then next hop
                time.sleep(min(backoff + random.uniform(0, 1), 10))
                continue
            # 4xx-class: shrink the budget (adaptive), mark hop dead for
            # this process if it persists
            if "HTTP Error 4" in msg:
                budget = max(256, budget // 2)
                _DEAD_HOPS.add(name)
                continue
            # other errors (timeout, parse) — try next hop
            continue
    raise NoHopError(f"all hops failed: {failures}")


# --------------------------------------------------------------------------
# Batch normalization with strict parsing + NONE-rate metric
# --------------------------------------------------------------------------

NORMALIZE_SYSTEM = (
    "You are a chemical-identification assistant for academic procurement "
    "research. Below are product-ad texts (Persian and/or English) from "
    "Iranian chemical supplier listings that could not be resolved by a "
    "dictionary/CAS lookup. For EACH item, decide whether ONE primary "
    "chemical product (a single molecule or clearly named single substance) "
    "is being offered.\n\n"
    "Respond with ONLY a JSON array, one object per item, same order:\n"
    '[{"item": 1, "name": "common English product name" or null, '
    '"cas": "NNNNN-NN-N" or null, "confidence": 0.0-1.0}]\n\n'
    'Rules: name = the substance itself (not a brand, package, or mixture); '
    "use \"NONE\" as name when the text is about services/equipment/a mixed "
    "basket or no single substance can be identified; give a CAS only if "
    "certain. Do not invent molecules."
)

_JSON_ARR = re.compile(r"\[[\s\S]*\]")


def _extract_json_array(txt: str) -> Optional[list]:
    start = txt.find("[")
    while start != -1:
        depth, in_str, esc = 0, False, False
        for i in range(start, len(txt)):
            c = txt[i]
            if in_str:
                if esc:
                    esc = False
                elif c == "\\":
                    esc = True
                elif c == '"':
                    in_str = False
                continue
            if c == '"':
                in_str = True
            elif c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
                if depth == 0:
                    try:
                        v = json.loads(txt[start:i + 1])
                        if isinstance(v, list):
                            return v
                    except ValueError:
                        pass
                    break
        start = txt.find("[", start + 1)
    return None


def normalize_batch(texts: List[str], *,
                    system: Optional[str] = None,
                    batch: int = DEFAULT_BATCH,
                    timeout: int = DEFAULT_TIMEOUT,
                    max_tokens: int = 1024,
                    pacing: float = 0.4,
                    value_field: str = "name") -> Dict:
    """Normalize a list of texts into structured values via the hop chain.

    ``value_field`` is the JSON field the prompt asks the model for
    ("name" for molecule identity; e.g. "category" when the prompt is a
    classification task). Returns {"results": [{index, name, cas,
    confidence, hop} ...] (the value is always mirrored into "name"),
    "none_rate": float, "hops_used": [...], "failed_batches": int}.
    """
    system = system or NORMALIZE_SYSTEM
    results: List[dict] = []
    hops_used: List[str] = []
    failed_batches = 0
    total_none = 0
    for i in range(0, len(texts), batch):
        chunk = texts[i:i + batch]
        try:
            out = hop_chain_call(chunk, system, timeout=timeout,
                                 max_tokens=max_tokens)
        except NoHopError:
            # no AI available: mark every item unresolved, never invent
            for j in range(len(chunk)):
                results.append({"index": i + j, "name": None, "cas": None,
                                "confidence": None, "hop": None})
            total_none += len(chunk)
            failed_batches += len(chunk) // batch + (1 if len(chunk) % batch else 0)
            continue
        hops_used.append(out["hop"])
        arr = _extract_json_array(out["text"]) or []
        matched = 0
        for j in range(len(chunk)):
            m = next((a for a in arr
                      if str(a.get("item")) == str(j + 1)), None)
            name = (m or {}).get(value_field, (m or {}).get("name"))
            cas = (m or {}).get("cas")
            if not m or not name or str(name).strip().upper() == "NONE":
                results.append({"index": i + j, "name": None, "cas": None,
                                "confidence": None, "hop": out["hop"]})
                total_none += 1
            else:
                matched += 1
                if cas and not re.match(r"^\d{2,7}-\d{2}-\d$", str(cas)):
                    cas = None
                results.append({"index": i + j,
                                "name": str(name).strip(),
                                "cas": str(cas) if cas else None,
                                "confidence": (m or {}).get("confidence"),
                                "hop": out["hop"]})
        if not matched and chunk:
            # live degradation signal (F8): a whole batch came back empty
            failed_batches += 1
        if pacing and i + batch < len(texts):
            time.sleep(pacing + random.uniform(0, 0.3))
    n = len(texts)
    return {"results": results,
            "none_rate": (total_none / n) if n else 0.0,
            "hops_used": hops_used,
            "failed_batches": failed_batches}
