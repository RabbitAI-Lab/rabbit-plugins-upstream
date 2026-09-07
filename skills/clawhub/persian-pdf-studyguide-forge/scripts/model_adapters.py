#!/usr/bin/env python3
"""model_adapters.py — model-agnostic LLM access layer (added v1.5.0).

Pure standard library (urllib only). No SDKs, no `requests`, no vendored
dependencies, Python 3.9+. It exists so that *every* script in this skill can
talk to *any* model family through one normalized call, and so that different
agent runtimes (OpenClaw, Claude Code, Codex/Agents CLI, Gemini CLI, Cursor,
LangChain/LangGraph, CrewAI, AutoGen, n8n, MCP hosts, plain cron) reproduce the
same intended results.

Supported API dialects
----------------------
  openai      OpenAI-compatible POST {base}/chat/completions
              (OpenAI, Azure-style gateways, OpenRouter, Groq, Mistral,
               DeepSeek, Together, Fireworks, xAI, Z.AI, llm7, LM Studio,
               vLLM, llama.cpp server, LiteLLM, any proxy)
  responses   OpenAI Responses API POST {base}/responses
  gemini      Google generativelanguage POST {base}/models/{m}:generateContent
  anthropic   Anthropic POST {base}/v1/messages (x-api-key, anthropic-version)
  cohere      Cohere POST {base}/v2/chat
  ollama      Ollama POST {base}/api/chat (stream disabled)
  hf          HuggingFace router (OpenAI-compatible shape, separate default base)
  mock        Deterministic offline provider used by tests/--dry-run. Never
              touches the network and always satisfies the JSON contract.

Design rules
------------
* One normalized return value: ModelReply(text, finish, provider, model, usage,
  raw_len, attempts, elapsed). Callers never inspect vendor payloads.
* Every started request is allowed to finish; transient failures back off and
  fail over (see API_CALLS_NEVER_STOP).
* Keys are read from environment variables only, are never logged, and are
  redacted from error text.
* Determinism first: temperature 0, top_p 1, fixed seed where the dialect
  supports it, canonical JSON everywhere, on-disk response cache keyed by a
  hash of (dialect, model, system, prompt, max_tokens, json_mode, seed).
* Capability quirks are *probed and remembered*, never assumed: unsupported
  parameters (`temperature`, `seed`, `response_format`, `max_tokens` vs
  `max_completion_tokens`, system role) are detected from the provider's own
  4xx body and retried without them, then cached in
  ``~/.cache/persian-pdf-studyguide-forge/capabilities.json``.
"""
from __future__ import annotations

import hashlib
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

__all__ = [
    "ModelReply", "ProviderInfo", "ModelError", "TransientError", "ContractError",
    "call_model", "discover_providers", "load_providers", "probe_provider",
    "compat_matrix", "canonical_json", "sanitize_model_text", "parse_json_loose",
    "DIALECTS", "cache_dir", "log",
]

DIALECTS = ("openai", "responses", "gemini", "anthropic", "cohere", "ollama", "hf", "mock")
SCHEMA_VERSION = "1.5.1"
USER_AGENT = f"persian-pdf-studyguide-forge/{SCHEMA_VERSION} (+stdlib-urllib)"


# ──────────────────────────────────────────────────────────────────────────
# logging: ALWAYS stderr, so stdout stays a clean machine-readable channel
# ──────────────────────────────────────────────────────────────────────────
_VERBOSE = os.environ.get("FORGE_VERBOSE", "1") not in ("0", "false", "no")


def log(msg: str, **fields: Any) -> None:
    """Structured single-line log to stderr (stdout is reserved for data)."""
    if not _VERBOSE:
        return
    if fields:
        msg = msg + " " + " ".join(f"{k}={_short(v)}" for k, v in fields.items())
    print("[forge] " + msg, file=sys.stderr, flush=True)


def _short(v: Any, n: int = 120) -> str:
    s = str(v).replace("\n", " ")
    return s if len(s) <= n else s[: n - 1] + "…"


# ──────────────────────────────────────────────────────────────────────────
# errors
# ──────────────────────────────────────────────────────────────────────────
class ModelError(RuntimeError):
    """Base class for adapter failures."""


class TransientError(ModelError):
    """Retryable: timeout, network, 408/409/429/5xx, empty completion."""


class ContractError(ModelError):
    """The model answered but the answer violated the requested contract."""


class RefusalError(ContractError):
    """The model declined to answer (safety/refusal)."""


# ──────────────────────────────────────────────────────────────────────────
# provider descriptors
# ──────────────────────────────────────────────────────────────────────────
@dataclass
class ProviderInfo:
    name: str
    dialect: str = "openai"
    model: str = ""
    base_url: str = ""
    api_key_env: str = ""
    alt_models: List[str] = field(default_factory=list)
    headers: Dict[str, str] = field(default_factory=dict)
    # capability hints; None means "unknown, probe it"
    supports_system: Optional[bool] = None
    supports_temperature: Optional[bool] = None
    supports_seed: Optional[bool] = None
    supports_json_mode: Optional[bool] = None
    max_tokens_field: Optional[str] = None     # "max_tokens" | "max_completion_tokens"
    context: int = 0
    weight: int = 50                            # higher = preferred earlier
    notes: str = ""

    # ── derived ──
    @property
    def key(self) -> str:
        if self.dialect in ("mock", "ollama"):
            return os.environ.get(self.api_key_env, "") if self.api_key_env else ""
        return os.environ.get(self.api_key_env, "")

    @property
    def usable(self) -> bool:
        if self.dialect == "mock":
            return True
        if self.dialect == "ollama":
            return bool(self.base_url)
        return bool(self.key)

    # Backwards compatibility: v1.3 code treated providers as plain dicts
    # (p["name"], p["model"], p.get("kind")). Keep that working.
    def __getitem__(self, item: str) -> Any:
        if item == "kind":
            return self.dialect
        return getattr(self, item)

    def get(self, item: str, default: Any = None) -> Any:
        if item == "kind":
            return self.dialect
        return getattr(self, item, default)

    def to_dict(self) -> dict:
        d = asdict(self)
        d.pop("headers", None) if not self.headers else None
        return d


# Default base URLs per well-known provider name.
_DEFAULT_BASES = {
    "openai": "https://api.openai.com/v1",
    "openrouter": "https://openrouter.ai/api/v1",
    "groq": "https://api.groq.com/openai/v1",
    "mistral": "https://api.mistral.ai/v1",
    "deepseek": "https://api.deepseek.com/v1",
    "together": "https://api.together.xyz/v1",
    "fireworks": "https://api.fireworks.ai/inference/v1",
    "xai": "https://api.x.ai/v1",
    "zai": "https://api.z.ai/api/paas/v4",
    "llm7": "https://api.llm7.io/v1",
    "cerebras": "https://api.cerebras.ai/v1",
    "nvidia": "https://integrate.api.nvidia.com/v1",
    "perplexity": "https://api.perplexity.ai",
    "hf": "https://router.huggingface.co/v1",
    "gemini": "https://generativelanguage.googleapis.com/v1beta",
    "anthropic": "https://api.anthropic.com",
    "cohere": "https://api.cohere.com",
    "ollama": "http://localhost:11434",
}

# name → (dialect, [env var candidates], default model, weight)
_AUTODISCOVER = [
    ("openai",     "openai",    ["OPENAI_API_KEY"],                     "gpt-4o-mini",                     70),
    ("anthropic",  "anthropic", ["ANTHROPIC_API_KEY"],                  "claude-3-5-haiku-latest",         75),
    ("gemini",     "gemini",    ["GEMINI_API_KEY", "GOOGLE_API_KEY"],   "gemini-flash-latest",             75),
    ("groq",       "openai",    ["GROQ_API_KEY"],                       "llama-3.3-70b-versatile",         65),
    ("openrouter", "openai",    ["OPENROUTER_API_KEY", "OPENROUTER_KEY"], "openrouter/auto",               72),
    ("deepseek",   "openai",    ["DEEPSEEK_API_KEY"],                   "deepseek-chat",                   66),
    ("mistral",    "openai",    ["MISTRAL_API_KEY"],                    "mistral-small-latest",            64),
    ("cohere",     "cohere",    ["COHERE_API_KEY", "CO_API_KEY"],       "command-r-plus",                  55),
    ("together",   "openai",    ["TOGETHER_API_KEY"],                   "meta-llama/Llama-3.3-70B-Instruct-Turbo", 58),
    ("fireworks",  "openai",    ["FIREWORKS_API_KEY"],                  "accounts/fireworks/models/llama-v3p3-70b-instruct", 56),
    ("xai",        "openai",    ["XAI_API_KEY", "GROK_API_KEY"],        "grok-2-latest",                   60),
    ("zai",        "openai",    ["ZAI_API_KEY", "ZHIPU_API_KEY"],       "glm-4.5-flash",                   52),
    ("cerebras",   "openai",    ["CEREBRAS_API_KEY"],                   "llama3.3-70b",                    54),
    ("nvidia",     "openai",    ["NVIDIA_API_KEY"],                     "meta/llama-3.3-70b-instruct",     50),
    ("perplexity", "openai",    ["PERPLEXITY_API_KEY"],                 "sonar",                           40),
    ("llm7",       "openai",    ["LLM7_API_KEY", "LLM7_TOKEN"],         "default",                         45),
    ("hf",         "hf",        ["HF_TOKEN", "HUGGINGFACE_API_KEY", "HUGGINGFACEHUB_API_TOKEN"],
                                                                        "meta-llama/Llama-3.3-70B-Instruct", 42),
]


def _env_first(names: Iterable[str]) -> str:
    for n in names:
        if os.environ.get(n):
            return n
    return ""


def discover_providers(config: Optional[str] = None,
                       include_mock: bool = False,
                       only: Optional[List[str]] = None) -> List[ProviderInfo]:
    """Build the provider chain from (1) an optional providers.json and
    (2) environment variables. Nothing is required: if a config is absent the
    environment alone is enough, which is what lets a foreign agent runtime
    drop this skill in and have it work.

    Order: explicit config entries first (operator intent wins), then
    auto-discovered providers by descending weight. Duplicates by
    (dialect, model, base_url) are removed.
    """
    found: List[ProviderInfo] = []
    if config:
        found.extend(load_providers(config))

    generic_base = os.environ.get("OPENAI_BASE_URL") or os.environ.get("OPENAI_API_BASE") or ""
    for name, dialect, envs, model, weight in _AUTODISCOVER:
        env = _env_first(envs)
        if not env:
            continue
        base = os.environ.get(f"{name.upper()}_BASE_URL", "") or _DEFAULT_BASES.get(name, "")
        if name == "openai" and generic_base:
            base = generic_base
        found.append(ProviderInfo(
            name=name, dialect=dialect,
            model=os.environ.get(f"{name.upper()}_MODEL", model),
            base_url=base, api_key_env=env, weight=weight,
            notes="auto-discovered from environment"))

    # Local runtimes: Ollama / LM Studio / vLLM need no key at all.
    ollama = os.environ.get("OLLAMA_HOST") or os.environ.get("OLLAMA_BASE_URL")
    if ollama:
        if not ollama.startswith("http"):
            ollama = "http://" + ollama
        found.append(ProviderInfo(name="ollama", dialect="ollama",
                                  model=os.environ.get("OLLAMA_MODEL", "llama3.1"),
                                  base_url=ollama.rstrip("/"), weight=48,
                                  notes="local Ollama runtime"))
    local_oai = os.environ.get("LOCAL_OPENAI_BASE_URL")
    if local_oai:
        found.append(ProviderInfo(name="local-openai", dialect="openai",
                                  model=os.environ.get("LOCAL_OPENAI_MODEL", "local-model"),
                                  base_url=local_oai.rstrip("/"),
                                  api_key_env="LOCAL_OPENAI_API_KEY", weight=46,
                                  notes="local OpenAI-compatible server (vLLM/LM Studio/llama.cpp)"))

    if include_mock or os.environ.get("FORGE_MOCK") == "1":
        found.append(ProviderInfo(name="mock", dialect="mock", model="deterministic-mock",
                                  weight=1, notes="offline deterministic provider"))

    usable, seen = [], set()
    for p in found:
        if not p.usable:
            continue
        sig = (p.dialect, p.model, p.base_url)
        if sig in seen:
            continue
        seen.add(sig)
        usable.append(p)

    if only:
        wanted = {x.strip().lower() for x in only}
        usable = [p for p in usable if p.name.lower() in wanted or p.dialect.lower() in wanted]

    usable.sort(key=lambda p: -p.weight)
    return usable


def load_providers(path: str | Path) -> List[ProviderInfo]:
    """Load providers.json. Accepts both the legacy v1.x shape
    ({"providers":[{"name","kind","model","api_key_env","base_url"}]}) and the
    v1.4 shape (``dialect`` instead of ``kind``, plus capability hints).
    """
    data = json.loads(Path(path).read_text("utf-8"))
    raw = data.get("providers", data)
    if not isinstance(raw, list):
        raise ValueError("provider config must contain a providers list")
    out: List[ProviderInfo] = []
    for p in raw:
        dialect = p.get("dialect") or p.get("kind") or "openai"
        if dialect == "openai" and p.get("name", "").startswith("hf"):
            dialect = "hf"
        if dialect not in DIALECTS:
            log("unknown dialect, treating as openai", provider=p.get("name"), dialect=dialect)
            dialect = "openai"
        base = p.get("base_url") or _DEFAULT_BASES.get(p.get("name", ""), "")
        info = ProviderInfo(
            name=p.get("name") or dialect,
            dialect=dialect,
            model=p.get("model", ""),
            base_url=base,
            api_key_env=p.get("api_key_env", ""),
            alt_models=list(p.get("alt_models", []) or []),
            headers=dict(p.get("headers", {}) or {}),
            supports_system=p.get("supports_system"),
            supports_temperature=p.get("supports_temperature"),
            supports_seed=p.get("supports_seed"),
            supports_json_mode=p.get("supports_json_mode"),
            max_tokens_field=p.get("max_tokens_field"),
            context=int(p.get("context", 0) or 0),
            weight=int(p.get("weight", 60) or 60),
            notes=p.get("notes", ""),
        )
        out.append(info)
    return out


# ──────────────────────────────────────────────────────────────────────────
# cache + capability memory
# ──────────────────────────────────────────────────────────────────────────
def cache_dir() -> Path:
    root = os.environ.get("FORGE_CACHE_DIR")
    if root:
        p = Path(root)
    else:
        p = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "persian-pdf-studyguide-forge"
    p.mkdir(parents=True, exist_ok=True)
    return p


_CAP_PATH = None
_CAPS: Optional[dict] = None


def _caps() -> dict:
    global _CAPS, _CAP_PATH
    if _CAPS is None:
        _CAP_PATH = cache_dir() / "capabilities.json"
        try:
            _CAPS = json.loads(_CAP_PATH.read_text("utf-8"))
        except Exception:
            _CAPS = {}
    return _CAPS


def _cap_key(p: ProviderInfo, model: str) -> str:
    return f"{p.dialect}::{p.base_url}::{model}"


def _cap_get(p: ProviderInfo, model: str) -> dict:
    return _caps().setdefault(_cap_key(p, model), {})


def _cap_set(p: ProviderInfo, model: str, **kw: Any) -> None:
    _cap_get(p, model).update(kw)
    try:
        (cache_dir() / "capabilities.json").write_text(
            canonical_json(_caps()), "utf-8")
    except Exception:
        pass


def canonical_json(obj: Any) -> str:
    """Deterministic JSON: sorted keys, stable separators, UTF-8 preserved.
    Used for cache keys, manifests and every artifact this skill writes, so two
    runs on two different models produce byte-comparable structure."""
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2)


def _cache_path(sig: str) -> Path:
    d = cache_dir() / "responses"
    d.mkdir(parents=True, exist_ok=True)
    return d / (sig + ".json")


# ──────────────────────────────────────────────────────────────────────────
# text sanitation (the part that actually makes models interchangeable)
# ──────────────────────────────────────────────────────────────────────────
_THINK_RE = re.compile(
    r"<(think|thinking|reasoning|scratchpad|antthinking)>.*?</\1>", re.S | re.I)
_OPEN_THINK_RE = re.compile(r"<(think|thinking|reasoning)>.*\Z", re.S | re.I)
_FENCE_RE = re.compile(r"^\s*```(?:json|jsonc|json5|javascript|js|python|text)?\s*|\s*```\s*$",
                       re.I | re.M)
_BIDI_RE = re.compile(r"[\u200e\u200f\u202a-\u202e\u2066-\u2069\ufeff]")
_REFUSAL_RE = re.compile(
    r"(i'?m sorry|i can'?t (help|assist|comply)|i cannot (help|assist|comply)|"
    r"as an ai language model|نمی\u200cتوانم کمک کنم|متأسفم، نمی\u200cتوانم)", re.I)
_TRAILING_COMMA_RE = re.compile(r",\s*([}\]])")
_PY_CONST_RE = re.compile(r"(?<![\"\w])(None|True|False)(?![\"\w])")


def sanitize_model_text(text: str) -> str:
    """Strip everything model families add around the payload.

    Handles: reasoning tags (<think>, DeepSeek-R1 / QwQ / Claude extended
    thinking transcripts), unterminated reasoning blocks from truncation,
    markdown code fences, byte-order marks, and bidi control characters that
    Persian-capable models love to emit around JSON punctuation.
    """
    t = text or ""
    t = t.replace("\ufeff", "")
    t = _THINK_RE.sub("", t)
    t = _OPEN_THINK_RE.sub("", t)
    t = _FENCE_RE.sub("", t)
    t = _BIDI_RE.sub("", t)
    return t.strip()


def _close_truncated(s: str) -> str:
    """Best-effort repair of a JSON document cut off by a token limit.

    Walks the text tracking string/bracket state, then retries from the longest
    possible prefix backwards, closing whatever is still open. This keeps the
    LAST complete value (``{"a":[1,2`` → ``{"a":[1,2]}``) instead of discarding
    it, while never inventing content: only structural brackets are added.
    """
    # Record every index at which the document is in a valid, un-escaped,
    # outside-a-string position, i.e. a place we could legally cut.
    cuts, depth_c, depth_s, in_str, esc = [], 0, 0, False, False
    for i, ch in enumerate(s):
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
                cuts.append((i + 1, depth_c, depth_s))
            continue
        if ch == '"':
            in_str = True
            continue
        if ch == "{":
            depth_c += 1
        elif ch == "}":
            depth_c -= 1
        elif ch == "[":
            depth_s += 1
        elif ch == "]":
            depth_s -= 1
        if ch not in " \t\r\n,":
            cuts.append((i + 1, depth_c, depth_s))

    if not (in_str or depth_c > 0 or depth_s > 0):
        return s

    for end, d_c, d_s in reversed(cuts):
        if d_c < 0 or d_s < 0:
            continue
        core = s[:end].rstrip().rstrip(",")
        candidate = core + "]" * d_s + "}" * d_c
        try:
            json.loads(candidate)
            return candidate
        except Exception:
            continue
    return s


def parse_json_loose(text: str) -> Any:
    """Tolerant JSON extraction that still refuses to invent content.

    Order of attempts (each strictly more forgiving than the last):
      1. strict json.loads on the sanitized text;
      2. widest {...} / [...] slice;
      3. NDJSON / JSON-Lines concatenation;
      4. syntax repair: trailing commas, Python constants, smart quotes,
         single-quoted keys;
      5. truncation repair (auto-closing brackets left open by finish=length).
    Raises ContractError when no valid JSON survives.
    """
    t = sanitize_model_text(text)
    if not t:
        raise ContractError("empty model response")
    if _REFUSAL_RE.search(t[:400]) and not t.lstrip().startswith(("{", "[")):
        raise RefusalError("model refused: " + _short(t, 160))

    def _try(s: str):
        try:
            return json.loads(s)
        except Exception:
            return None

    got = _try(t)
    if got is not None:
        return got

    # Truncation repair on the WHOLE document first. Slicing a cut-off document
    # would otherwise return an inner fragment (e.g. `{"a":[1,2,3],"b":"cut`
    # collapsing to just `[1,2,3]`) and silently lose the outer keys.
    repaired = _close_truncated(t)
    if repaired != t:
        got = _try(repaired)
        if got is not None:
            return got

    # Widest slice. Order matters: try the bracket type the document actually
    # STARTS with first, otherwise '{"a":[1,2,]}' gets mis-sliced to '[1,2,]'.
    pairs = [("[", "]"), ("{", "}")]
    first = next((c for c in t if c in "[{"), "")
    if first == "{":
        pairs.reverse()
    cands = []
    for left, right in pairs:
        a, b = t.find(left), t.rfind(right)
        if a >= 0 and b > a:
            cands.append(t[a: b + 1])
    for c in cands:
        got = _try(c)
        if got is not None:
            return got

    # NDJSON / JSON-Lines
    lines = [ln.strip() for ln in t.splitlines() if ln.strip().startswith(("{", "["))]
    if len(lines) > 1:
        items = [x for x in (_try(ln) for ln in lines) if x is not None]
        if items:
            return items

    # syntax repair
    for c in cands + [t]:
        r = c.replace("\u201c", '"').replace("\u201d", '"').replace("\u2018", "'").replace("\u2019", "'")
        r = _TRAILING_COMMA_RE.sub(r"\1", r)
        r = _PY_CONST_RE.sub(lambda m: {"None": "null", "True": "true", "False": "false"}[m.group(1)], r)
        r = re.sub(r"(?m)^\s*//.*$", "", r)
        got = _try(r)
        if got is not None:
            return got
        got = _try(_close_truncated(r))
        if got is not None:
            return got

    raise ContractError("provider response did not contain valid JSON")


# ──────────────────────────────────────────────────────────────────────────
# normalized reply
# ──────────────────────────────────────────────────────────────────────────
@dataclass
class ModelReply:
    text: str
    finish: str = "stop"           # stop | length | refusal | filter | unknown
    provider: str = ""
    model: str = ""
    dialect: str = ""
    usage: Dict[str, int] = field(default_factory=dict)
    attempts: int = 1
    elapsed: float = 0.0
    cached: bool = False

    @property
    def truncated(self) -> bool:
        return self.finish == "length"

    def json(self) -> Any:
        return parse_json_loose(self.text)


_FINISH_MAP = {
    "stop": "stop", "end_turn": "stop", "complete": "stop", "COMPLETE": "stop",
    "eos": "stop", "STOP": "stop", "stop_sequence": "stop",
    "length": "length", "max_tokens": "length", "MAX_TOKENS": "length",
    "model_length": "length", "MAX_TOKENS_REACHED": "length", "token_limit": "length",
    "content_filter": "filter", "SAFETY": "filter", "safety": "filter",
    "RECITATION": "filter", "blocklist": "filter",
    "refusal": "refusal", "tool_use": "stop", "function_call": "stop",
}


def _finish(raw: Any) -> str:
    if raw is None:
        return "stop"
    return _FINISH_MAP.get(str(raw), _FINISH_MAP.get(str(raw).lower(), "unknown"))


# ──────────────────────────────────────────────────────────────────────────
# HTTP
# ──────────────────────────────────────────────────────────────────────────
def _redact(text: str, *secrets: str) -> str:
    out = text
    for s in secrets:
        if s and len(s) > 6:
            out = out.replace(s, "***")
    return re.sub(r"(sk-[A-Za-z0-9_\-]{6})[A-Za-z0-9_\-]+", r"\1***", out)


def _http_post(url: str, headers: dict, body: dict, timeout: int,
               secret: str = "") -> dict:
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    hdrs = {"Content-Type": "application/json", "Accept": "application/json",
            "User-Agent": USER_AGENT}
    hdrs.update(headers)
    req = urllib.request.Request(url, data=data, headers=hdrs, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = resp.read().decode("utf-8", "replace")
        # Ollama and some gateways may answer NDJSON even with stream:false.
        try:
            return json.loads(payload)
        except json.JSONDecodeError:
            merged: dict = {}
            for line in payload.splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    chunk = json.loads(line)
                except json.JSONDecodeError:
                    continue
                merged = _merge_stream_chunk(merged, chunk)
            if merged:
                return merged
            raise
    except urllib.error.HTTPError as exc:
        detail = ""
        try:
            detail = exc.read().decode("utf-8", "replace")[:1200]
        except Exception:
            pass
        raise _HTTPFail(exc.code, _redact(detail, secret),
                        int(exc.headers.get("Retry-After", "0") or 0)) from None
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise TransientError(f"network: {type(exc).__name__}: {_short(exc)}") from None


def _merge_stream_chunk(merged: dict, chunk: dict) -> dict:
    if not merged:
        merged = {"message": {"content": ""}, "done_reason": None}
    msg = chunk.get("message") or {}
    merged["message"]["content"] += msg.get("content", "")
    if chunk.get("done_reason"):
        merged["done_reason"] = chunk["done_reason"]
    for k in ("prompt_eval_count", "eval_count"):
        if k in chunk:
            merged[k] = chunk[k]
    return merged


class _HTTPFail(ModelError):
    def __init__(self, code: int, body: str, retry_after: int = 0):
        super().__init__(f"HTTP {code}: {_short(body, 300)}")
        self.code, self.body, self.retry_after = code, body, retry_after

    @property
    def transient(self) -> bool:
        return self.code in (408, 409, 425, 429, 500, 502, 503, 504, 520, 522, 524)


# Parameter-rejection detection: providers disagree about which knobs exist.
_UNSUPPORTED_PATTERNS = {
    "max_tokens_field": re.compile(
        r"max_tokens.*(not supported|unsupported|use\s+'?max_completion_tokens)|"
        r"unsupported_parameter.*max_tokens", re.I),
    "temperature": re.compile(
        r"temperature.*(not supported|unsupported|does not support|only the default|"
        r"must be|fixed)", re.I),
    "seed": re.compile(r"\bseed\b.*(not supported|unsupported|unrecognized|unknown)", re.I),
    "json_mode": re.compile(
        r"response_format.*(not supported|unsupported|invalid|unknown)|"
        r"json_schema.*(not supported|unsupported)", re.I),
    "system": re.compile(
        r"(system).*(role.*not supported|not supported|unsupported|must be user|"
        r"developer instead)", re.I),
    "top_p": re.compile(r"top_p.*(not supported|unsupported)", re.I),
}


def _classify_rejection(body: str) -> Optional[str]:
    """Which knob did the provider reject? Verified live against Mistral,
    Gemini, Groq, Cohere, OpenRouter, Z.AI and HuggingFace error bodies."""
    b = body or ""
    for name, rx in _UNSUPPORTED_PATTERNS.items():
        if rx.search(b):
            return name
    # Pydantic-style rejection used by Mistral/vLLM/LiteLLM:
    #   {"detail":[{"type":"extra_forbidden","loc":["body","seed"], ...}]}
    m = re.search(r'"extra_forbidden".{0,80}?"loc"\s*:\s*\[[^\]]*?"(\w+)"\s*\]', b, re.S)
    if not m:
        m = re.search(r'"loc"\s*:\s*\[\s*"body"\s*,\s*"(\w+)"\s*\].{0,120}?extra_forbidden', b, re.S)
    if m:
        return {"seed": "seed", "temperature": "temperature", "top_p": "top_p",
                "response_format": "json_mode", "max_tokens": "max_tokens_field",
                "stream": "stream"}.get(m.group(1))
    return None


# Providers retire models and often name the replacement in the 404 body
# (observed live on Gemini: "no longer available … Please update your code to
# use models/gemini-3.6-flash"). Follow the provider's own advice once.
_SUGGESTED_MODEL_RES = (
    re.compile(r"use\s+models/([A-Za-z0-9._\-]+)", re.I),
    re.compile(r"use\s+[`'\"]?([A-Za-z0-9._\-/:]{3,})[`'\"]?\s+instead", re.I),
    re.compile(r"replaced by\s+[`'\"]?([A-Za-z0-9._\-/:]{3,})", re.I),
)


def _suggested_model(body: str) -> Optional[str]:
    for rx in _SUGGESTED_MODEL_RES:
        m = rx.search(body or "")
        if m:
            cand = m.group(1).strip().rstrip(".,;")
            if 2 < len(cand) < 80:
                return cand
    return None


def _usage(u: Any) -> Dict[str, int]:
    """Normalize the many usage shapes into {prompt, completion, total}."""
    if not isinstance(u, dict):
        return {}
    def pick(*names):
        for n in names:
            v = u.get(n)
            if isinstance(v, (int, float)):
                return int(v)
        return 0
    p = pick("prompt_tokens", "input_tokens", "promptTokenCount", "prompt_eval_count")
    c = pick("completion_tokens", "output_tokens", "candidatesTokenCount", "eval_count")
    t = pick("total_tokens", "totalTokenCount") or (p + c)
    return {"prompt": p, "completion": c, "total": t}


# ──────────────────────────────────────────────────────────────────────────
# dialect adapters — each returns (text, finish, usage)
# ──────────────────────────────────────────────────────────────────────────
def _b_openai(p, model, prompt, system, max_tokens, json_mode, seed, caps):
    field_name = caps.get("max_tokens_field") or p.max_tokens_field or "max_tokens"
    msgs = []
    if system and caps.get("supports_system", p.supports_system) is not False:
        msgs.append({"role": "system", "content": system})
        user = prompt
    else:
        user = (system + "\n\n" + prompt) if system else prompt
    msgs.append({"role": "user", "content": user})
    body: Dict[str, Any] = {"model": model, "messages": msgs, field_name: max_tokens}
    if caps.get("supports_stream_field", True) is not False:
        body["stream"] = False
    if caps.get("supports_temperature", p.supports_temperature) is not False:
        body["temperature"] = 0
        if caps.get("supports_top_p", True) is not False:
            body["top_p"] = 1
    # `seed` is rejected outright by Mistral and some vLLM/LiteLLM builds
    # (HTTP 422 extra_forbidden); the rejection is parsed, cached and the call
    # is retried without it, so determinism degrades gracefully per provider.
    if seed is not None and caps.get("supports_seed", p.supports_seed) is not False:
        body["seed"] = seed
    if json_mode and caps.get("supports_json_mode", p.supports_json_mode) is not False:
        body["response_format"] = {"type": "json_object"}
    base = (p.base_url or _DEFAULT_BASES.get(p.name, "")).rstrip("/")
    hdrs = dict(p.headers)
    if p.key:
        hdrs["Authorization"] = "Bearer " + p.key
    if p.name == "openrouter":
        hdrs.setdefault("HTTP-Referer", "https://hub.openclaw.ai/orionshaowswmw")
        hdrs.setdefault("X-Title", "persian-pdf-studyguide-forge")
    data = _http_post(base + "/chat/completions", hdrs, body, p_timeout(), p.key)
    ch = (data.get("choices") or [{}])[0]
    msg = ch.get("message") or {}
    text = msg.get("content") or ch.get("text") or ""
    if isinstance(text, list):   # some gateways return content parts
        text = "".join(x.get("text", "") for x in text if isinstance(x, dict))
    if not text and msg.get("reasoning_content"):
        text = msg["reasoning_content"]
    if msg.get("refusal"):
        raise RefusalError(str(msg["refusal"])[:200])
    return text, _finish(ch.get("finish_reason") or ch.get("native_finish_reason")), _usage(data.get("usage"))


def _b_responses(p, model, prompt, system, max_tokens, json_mode, seed, caps):
    base = (p.base_url or _DEFAULT_BASES["openai"]).rstrip("/")
    body: Dict[str, Any] = {"model": model, "input": prompt,
                            "max_output_tokens": max_tokens}
    if system:
        body["instructions"] = system
    if caps.get("supports_temperature", p.supports_temperature) is not False:
        body["temperature"] = 0
    if json_mode and caps.get("supports_json_mode", p.supports_json_mode) is not False:
        body["text"] = {"format": {"type": "json_object"}}
    hdrs = dict(p.headers)
    if p.key:
        hdrs["Authorization"] = "Bearer " + p.key
    data = _http_post(base + "/responses", hdrs, body, p_timeout(), p.key)
    text = data.get("output_text") or ""
    if not text:
        parts = []
        for item in data.get("output", []) or []:
            for c in item.get("content", []) or []:
                if c.get("type") in ("output_text", "text"):
                    parts.append(c.get("text", ""))
        text = "".join(parts)
    return text, _finish(data.get("status") if data.get("status") != "completed" else "stop"), _usage(data.get("usage"))


def _b_gemini(p, model, prompt, system, max_tokens, json_mode, seed, caps):
    base = (p.base_url or _DEFAULT_BASES["gemini"]).rstrip("/")
    gen: Dict[str, Any] = {"maxOutputTokens": max_tokens, "temperature": 0, "topP": 1}
    if json_mode and caps.get("supports_json_mode", p.supports_json_mode) is not False:
        gen["responseMimeType"] = "application/json"
    if seed is not None and caps.get("supports_seed", p.supports_seed) is not False:
        gen["seed"] = seed
    body: Dict[str, Any] = {"contents": [{"role": "user", "parts": [{"text": prompt}]}],
                            "generationConfig": gen}
    if system and caps.get("supports_system", p.supports_system) is not False:
        body["systemInstruction"] = {"parts": [{"text": system}]}
    elif system:
        body["contents"][0]["parts"][0]["text"] = system + "\n\n" + prompt
    hdrs = dict(p.headers)
    hdrs["x-goog-api-key"] = p.key            # header form; keeps key out of URLs/logs
    data = _http_post(f"{base}/models/{model}:generateContent", hdrs, body, p_timeout(), p.key)
    cands = data.get("candidates") or []
    if not cands:
        fb = (data.get("promptFeedback") or {}).get("blockReason")
        if fb:
            raise RefusalError(f"gemini blocked: {fb}")
        return "", "unknown", _usage(data.get("usageMetadata"))
    c = cands[0]
    text = "".join(part.get("text", "") for part in (c.get("content", {}).get("parts") or []))
    um = data.get("usageMetadata") or {}
    return text, _finish(c.get("finishReason")), {
        "prompt": um.get("promptTokenCount", 0), "completion": um.get("candidatesTokenCount", 0)}


def _b_anthropic(p, model, prompt, system, max_tokens, json_mode, seed, caps):
    base = (p.base_url or _DEFAULT_BASES["anthropic"]).rstrip("/")
    body: Dict[str, Any] = {"model": model, "max_tokens": max_tokens,
                            "temperature": 0,
                            "messages": [{"role": "user", "content": prompt}]}
    if system:
        body["system"] = system                # Anthropic: top-level, not a message
    if json_mode:
        # No response_format on /v1/messages: prefill the assistant turn so the
        # model must continue a JSON document.
        body["messages"].append({"role": "assistant", "content": "{"})
    hdrs = dict(p.headers)
    hdrs["x-api-key"] = p.key
    hdrs.setdefault("anthropic-version", os.environ.get("ANTHROPIC_VERSION", "2023-06-01"))
    data = _http_post(base + "/v1/messages", hdrs, body, p_timeout(), p.key)
    text = "".join(b.get("text", "") for b in (data.get("content") or [])
                   if b.get("type") == "text")
    if json_mode and text and not text.lstrip().startswith(("{", "[")):
        text = "{" + text            # restore the prefilled brace
    u = data.get("usage") or {}
    return text, _finish(data.get("stop_reason")), {
        "prompt": u.get("input_tokens", 0), "completion": u.get("output_tokens", 0)}


def _b_cohere(p, model, prompt, system, max_tokens, json_mode, seed, caps):
    base = (p.base_url or _DEFAULT_BASES["cohere"]).rstrip("/")
    msgs = []
    if system:
        msgs.append({"role": "system", "content": system})
    msgs.append({"role": "user", "content": prompt})
    body: Dict[str, Any] = {"model": model, "messages": msgs,
                            "max_tokens": max_tokens, "temperature": 0}
    if json_mode and caps.get("supports_json_mode", p.supports_json_mode) is not False:
        body["response_format"] = {"type": "json_object"}
    if seed is not None and caps.get("supports_seed", p.supports_seed) is not False:
        body["seed"] = seed
    hdrs = dict(p.headers)
    hdrs["Authorization"] = "Bearer " + p.key
    data = _http_post(base + "/v2/chat", hdrs, body, p_timeout(), p.key)
    content = ((data.get("message") or {}).get("content")) or []
    text = "".join(c.get("text", "") for c in content if isinstance(c, dict))
    u = (data.get("usage") or {}).get("tokens") or {}
    return text, _finish(data.get("finish_reason")), {
        "prompt": int(u.get("input_tokens", 0) or 0),
        "completion": int(u.get("output_tokens", 0) or 0)}


def _b_ollama(p, model, prompt, system, max_tokens, json_mode, seed, caps):
    base = (p.base_url or _DEFAULT_BASES["ollama"]).rstrip("/")
    msgs = []
    if system:
        msgs.append({"role": "system", "content": system})
    msgs.append({"role": "user", "content": prompt})
    opts: Dict[str, Any] = {"temperature": 0, "top_p": 1, "num_predict": max_tokens}
    if seed is not None:
        opts["seed"] = seed
    body: Dict[str, Any] = {"model": model, "messages": msgs, "stream": False,
                            "options": opts}
    if json_mode:
        body["format"] = "json"
    data = _http_post(base + "/api/chat", dict(p.headers), body, p_timeout(), "")
    text = ((data.get("message") or {}).get("content")) or ""
    return text, _finish(data.get("done_reason")), {
        "prompt": data.get("prompt_eval_count", 0), "completion": data.get("eval_count", 0)}


def _b_hf(p, model, prompt, system, max_tokens, json_mode, seed, caps):
    if not p.base_url:
        p = ProviderInfo(**{**asdict(p), "base_url": _DEFAULT_BASES["hf"]})
    return _b_openai(p, model, prompt, system, max_tokens, json_mode, seed, caps)


def _b_mock(p, model, prompt, system, max_tokens, json_mode, seed, caps):
    """Deterministic offline provider.

    It never invents study content: it echoes a contract-shaped skeleton derived
    from the prompt via a seeded PRNG, so tests, --dry-run, CI and the
    reproducibility harness all run without network or keys and produce byte
    identical output for identical input.
    """
    rnd = random.Random(f"{seed}:{model}:{hashlib.sha256(prompt.encode()).hexdigest()}")
    pages = [int(x) for x in re.findall(r"صفحه\s*(\d+)", prompt)] or \
            [int(x) for x in re.findall(r"\bpage\s*(\d+)", prompt, re.I)] or [1]
    lo, hi = min(pages), max(pages)
    want = {k: int(v) for k, v in re.findall(r'"(tables|flash|mnemonics|review|quiz|bank)"\s*:\s*\[\s*(\d+)', prompt)}
    if "page" in prompt and '"text"' in prompt and not want:
        out = [{"page": pg, "title": f"صفحهٔ {pg}", "text": f"متن بازسازی‌شدهٔ آزمایشی صفحهٔ {pg}."}
               for pg in sorted(set(pages))]
        return json.dumps(out, ensure_ascii=False), "stop", {"prompt": len(prompt) // 4, "completion": 64}
    if '"answer"' in prompt and '"tables"' not in prompt and "flash" not in want:
        return json.dumps({"answer": "پاسخ آزمایشی مستند از متن صفحه."}, ensure_ascii=False), "stop", {}
    doc: Dict[str, Any] = {}
    for key, n in (want or {"flash": 2}).items():
        items = []
        for i in range(n):
            ref = rnd.randint(lo, hi)
            if key == "tables":
                items.append({"caption": f"جدول آزمایشی {i+1}",
                              "headers": ["مفهوم", "توضیح"],
                              "rows": [[f"مفهوم {j+1}", f"توضیح {j+1}"] for j in range(4)]})
            elif key == "flash":
                items.append({"q": f"پرسش آزمایشی {i+1}؟", "a": f"پاسخ کامل آزمایشی {i+1}.", "ref": ref})
            elif key == "mnemonics":
                items.append({"title": f"یادیار {i+1}", "text": f"متن یادیار {i+1}.", "ref": ref})
            elif key == "review":
                items.append({"text": f"نکتهٔ مرور {i+1}.", "ref": ref})
            else:
                items.append({"q": f"سؤال {i+1}؟",
                              "options": [f"گزینه {j+1}" for j in range(4)],
                              "answer": "ABCD"[rnd.randrange(4)],
                              "why": f"دلیل {i+1}.", "ref": ref})
        doc[key] = items
    return json.dumps(doc, ensure_ascii=False), "stop", {"prompt": len(prompt) // 4, "completion": 128}


_ADAPTERS = {"openai": _b_openai, "responses": _b_responses, "gemini": _b_gemini,
             "anthropic": _b_anthropic, "cohere": _b_cohere, "ollama": _b_ollama,
             "hf": _b_hf, "mock": _b_mock}


def p_timeout() -> int:
    return int(os.environ.get("FORGE_TIMEOUT", "360"))


# ──────────────────────────────────────────────────────────────────────────
# the one public call
# ──────────────────────────────────────────────────────────────────────────
def call_model(provider: ProviderInfo | dict,
               prompt: str,
               system: str = "",
               max_tokens: int = 8000,
               timeout: Optional[int] = None,
               json_mode: bool = True,
               seed: Optional[int] = 7,
               retries: int = 5,
               use_cache: bool = True,
               model: Optional[str] = None) -> ModelReply:
    """Call one provider and return a normalized reply.

    Behaviour that makes models interchangeable:
      * unsupported parameters are removed and remembered (capability probe);
      * transient failures retry with exponential backoff + jitter, honouring
        Retry-After; every started request is allowed to finish;
      * `finish=length` is reported, not hidden — callers can shrink the batch;
      * responses are cached on disk by content hash so a re-run of the same
        pipeline with the same model is free and byte-identical.
    """
    p = provider if isinstance(provider, ProviderInfo) else _coerce(provider)
    models = [model] if model else ([p.model] + [m for m in p.alt_models if m != p.model])
    timeout = timeout or p_timeout()
    started = time.time()
    last: Optional[Exception] = None
    attempts = 0

    queue = list(models)
    seen_models = set()
    while queue:
        mdl = queue.pop(0)
        if mdl in seen_models:
            continue
        seen_models.add(mdl)
        caps = dict(_cap_get(p, mdl))
        if caps.get("renamed_to") and caps["renamed_to"] not in seen_models:
            queue.insert(0, caps["renamed_to"])
        sig = hashlib.sha256(canonical_json({
            "d": p.dialect, "b": p.base_url, "m": mdl, "s": system, "p": prompt,
            "t": max_tokens, "j": json_mode, "seed": seed, "v": SCHEMA_VERSION,
        }).encode()).hexdigest()[:40]
        cpath = _cache_path(sig)
        if use_cache and cpath.exists():
            try:
                blob = json.loads(cpath.read_text("utf-8"))
                return ModelReply(text=blob["text"], finish=blob.get("finish", "stop"),
                                  provider=p.name, model=mdl, dialect=p.dialect,
                                  usage=blob.get("usage", {}), attempts=0,
                                  elapsed=0.0, cached=True)
            except Exception:
                pass

        for attempt in range(retries):
            attempts += 1
            try:
                text, finish, usage = _ADAPTERS[p.dialect](
                    p, mdl, prompt, system, max_tokens, json_mode, seed, caps)
                if not (text or "").strip():
                    raise TransientError("empty completion (HTTP 200)")
                reply = ModelReply(text=text, finish=finish, provider=p.name, model=mdl,
                                   dialect=p.dialect, usage=usage, attempts=attempts,
                                   elapsed=round(time.time() - started, 2))
                if use_cache:
                    try:
                        cpath.write_text(canonical_json(
                            {"text": text, "finish": finish, "usage": usage,
                             "provider": p.name, "model": mdl}), "utf-8")
                    except Exception:
                        pass
                if caps:
                    _cap_set(p, mdl, **caps)
                log("ok", provider=p.name, model=mdl, finish=finish,
                    chars=len(text), tries=attempts)
                return reply
            except _HTTPFail as exc:
                last = exc
                which = _classify_rejection(exc.body)
                if which and exc.code in (400, 404, 422):
                    if which == "max_tokens_field":
                        caps["max_tokens_field"] = ("max_completion_tokens"
                                                    if caps.get("max_tokens_field") != "max_completion_tokens"
                                                    else "max_tokens")
                    elif which == "temperature":
                        caps["supports_temperature"] = False
                    elif which == "seed":
                        caps["supports_seed"] = False
                    elif which == "json_mode":
                        caps["supports_json_mode"] = False
                    elif which == "system":
                        caps["supports_system"] = False
                    elif which == "top_p":
                        caps["supports_top_p"] = False
                    elif which == "stream":
                        caps["supports_stream_field"] = False
                    _cap_set(p, mdl, **caps)
                    log("quirk learned, retrying", provider=p.name, model=mdl, quirk=which)
                    continue
                if exc.code in (401, 403):
                    log("auth failure — skipping provider", provider=p.name)
                    break
                if exc.code in (402, 413):
                    log("quota/credits exhausted — skipping provider",
                        provider=p.name, detail=_short(exc.body, 90))
                    break
                if exc.code in (400, 404, 422):
                    # Model retired? Providers frequently name the replacement.
                    sug = _suggested_model(exc.body)
                    if sug and sug not in seen_models:
                        _cap_set(p, mdl, renamed_to=sug)
                        queue.insert(0, sug)
                        log("model retired — following provider's suggestion",
                            provider=p.name, was=mdl, now=sug)
                    else:
                        log("bad request — trying next model", provider=p.name,
                            model=mdl, detail=_short(exc.body, 90))
                    break
                if exc.transient:
                    _sleep(attempt, exc.retry_after)
                    continue
                break
            except RefusalError as exc:
                last = exc
                log("refusal", provider=p.name, model=mdl)
                break
            except TransientError as exc:
                last = exc
                _sleep(attempt, 0)
                continue
            except Exception as exc:                      # unknown → one backoff
                last = exc
                _sleep(attempt, 0)
                continue

    raise ModelError(f"{p.name}: all attempts failed ({type(last).__name__}: {_short(last)})")


def _sleep(attempt: int, retry_after: int) -> None:
    delay = max(retry_after, min(2 ** attempt, 60))
    delay += random.random() * 0.4 * delay      # jitter: avoid synchronized retries
    time.sleep(min(delay, 90))


def _coerce(d: dict) -> ProviderInfo:
    if isinstance(d, ProviderInfo):
        return d
    dialect = d.get("dialect") or d.get("kind") or "openai"
    return ProviderInfo(name=d.get("name", dialect), dialect=dialect,
                        model=d.get("model", ""), base_url=d.get("base_url", ""),
                        api_key_env=d.get("api_key_env", ""),
                        alt_models=list(d.get("alt_models", []) or []),
                        headers=dict(d.get("headers", {}) or {}))


# ──────────────────────────────────────────────────────────────────────────
# capability probe + compatibility matrix
# ──────────────────────────────────────────────────────────────────────────
_PROBE_PROMPT = ('Reply with exactly this JSON and nothing else: '
                 '{"ok": true, "n": 3, "fa": "سلام"}')
_PROBE_SYSTEM = "You are a strict JSON generator. Output only JSON."


def probe_provider(p: ProviderInfo, timeout: int = 60) -> dict:
    """One cheap round-trip that records what a provider/model actually does.

    Returns a row for the compatibility matrix: reachability, JSON discipline,
    Persian round-trip, which parameters were rejected, latency.
    """
    row: Dict[str, Any] = {"provider": p.name, "dialect": p.dialect, "model": p.model,
                           "reachable": False, "json_ok": False, "persian_ok": False,
                           "finish": "", "latency_s": 0.0, "quirks": {}, "error": ""}
    t0 = time.time()
    try:
        r = call_model(p, _PROBE_PROMPT, _PROBE_SYSTEM, max_tokens=200,
                       timeout=timeout, json_mode=True, seed=7, retries=2,
                       use_cache=False)
        row["reachable"] = True
        row["finish"] = r.finish
        row["model"] = r.model
        try:
            doc = r.json()
            row["json_ok"] = isinstance(doc, dict) and doc.get("ok") is True
            row["persian_ok"] = "سلام" in json.dumps(doc, ensure_ascii=False)
        except Exception as exc:
            row["error"] = f"json: {_short(exc, 90)}"
    except Exception as exc:
        row["error"] = f"{type(exc).__name__}: {_short(exc, 120)}"
    row["latency_s"] = round(time.time() - t0, 2)
    row["quirks"] = dict(_cap_get(p, row["model"] or p.model))
    return row


def compat_matrix(providers: List[ProviderInfo], timeout: int = 60,
                  workers: int = 6) -> dict:
    """Probe every provider in parallel and return a machine-readable report."""
    import concurrent.futures as cf
    rows: List[dict] = []
    with cf.ThreadPoolExecutor(max_workers=max(1, workers)) as ex:
        for row in ex.map(lambda p: probe_provider(p, timeout), providers):
            rows.append(row)
    usable = [r for r in rows if r["reachable"] and r["json_ok"]]
    return {
        "schema": "forge.compat-matrix/1",
        "skill_version": SCHEMA_VERSION,
        "generated_at": int(time.time()),
        "counts": {"configured": len(rows), "reachable": sum(r["reachable"] for r in rows),
                   "contract_ready": len(usable)},
        "verdict": "READY" if usable else "NO_USABLE_PROVIDER",
        "providers": sorted(rows, key=lambda r: (not r["json_ok"], r["latency_s"])),
    }


# ──────────────────────────────────────────────────────────────────────────
# CLI: `python3 scripts/model_adapters.py --list | --probe | --matrix out.json`
# ──────────────────────────────────────────────────────────────────────────
def _main(argv: List[str]) -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Model adapter layer / provider doctor")
    ap.add_argument("--providers", help="optional providers.json")
    ap.add_argument("--list", action="store_true", help="list discovered providers")
    ap.add_argument("--probe", action="store_true", help="probe every provider")
    ap.add_argument("--matrix", help="write the compatibility matrix to this path")
    ap.add_argument("--only", help="comma-separated provider/dialect filter")
    ap.add_argument("--mock", action="store_true", help="include the offline mock provider")
    ap.add_argument("--timeout", type=int, default=60)
    a = ap.parse_args(argv)

    provs = discover_providers(a.providers, include_mock=a.mock,
                               only=a.only.split(",") if a.only else None)
    if a.list or not (a.probe or a.matrix):
        print(canonical_json({"count": len(provs),
                              "providers": [{"name": p.name, "dialect": p.dialect,
                                             "model": p.model, "base_url": p.base_url,
                                             "api_key_env": p.api_key_env,
                                             "weight": p.weight} for p in provs]}))
        return 0 if provs else 1
    report = compat_matrix(provs, timeout=a.timeout)
    text = canonical_json(report)
    if a.matrix:
        Path(a.matrix).write_text(text, "utf-8")
    print(text)
    return 0 if report["verdict"] == "READY" else 1


if __name__ == "__main__":
    raise SystemExit(_main(sys.argv[1:]))
