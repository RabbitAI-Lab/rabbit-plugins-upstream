#!/usr/bin/env python3
"""Shared, dependency-light helpers for Persian PDF StudyGuide Forge.

No credentials are stored here. Provider keys are read from explicitly named
environment variables (or auto-discovered from the host agent's environment)
only when network-assisted editing is enabled.

v1.5.0 — model-agnostic core. The LLM plumbing now lives in
``model_adapters.py`` (OpenAI-compatible chat, OpenAI Responses, Gemini,
Anthropic messages, Cohere v2, Ollama, HuggingFace router, deterministic
offline mock). This module keeps the v1.3 function names and signatures so
existing pipelines, forks and other agents' glue code keep working, and adds
determinism helpers (canonical JSON, stable ordering, cross-model
deduplication, self-consistency voting) so different models reproduce the same
intended result.
"""
from __future__ import annotations
import hashlib, html, json, os, re, time, unicodedata, urllib.error, urllib.request
from pathlib import Path

BIDI_RE = re.compile(r"[\u200e\u200f\u202a-\u202e\u2066-\u2069]")
ARABIC_TO_PERSIAN = str.maketrans({"ي": "ی", "ك": "ک", "ۀ": "ه", "ة": "ه", "ى": "ی"})
FA_DIGITS = str.maketrans("0123456789٠١٢٣٤٥٦٧٨٩", "۰۱۲۳۴۵۶۷۸۹۰۱۲۳۴۵۶۷۸۹")


def normalize_persian(text: str, persian_digits: bool = True) -> str:
    """Normalize display/search Persian while preserving ZWNJ (U+200C)."""
    text = unicodedata.normalize("NFKC", text or "")
    text = BIDI_RE.sub("", text).translate(ARABIC_TO_PERSIAN)
    if persian_digits:
        text = text.translate(FA_DIGITS)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def search_normalize(text: str) -> str:
    text = normalize_persian(text, persian_digits=False).lower()
    text = text.translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789"))
    return re.sub(r"\s+", " ", text.replace("\u200c", " ")).strip()


def sha256(path: str | Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_json(text: str):
    """Model-agnostic JSON extraction (v1.5.0).

    Delegates to ``model_adapters.parse_json_loose``, which additionally
    survives: reasoning traces (`<think>` from R1/QwQ/extended-thinking),
    markdown prose around the payload, NDJSON, trailing commas, Python
    constants, smart quotes, BOM, RTL bidi marks and token-limit truncation.
    Falls back to the v1.3 behaviour if the adapter module is unavailable.
    """
    try:
        from model_adapters import parse_json_loose
    except Exception:
        pass
    else:
        return parse_json_loose(text)
    t = re.sub(r"^```(?:json)?\s*", "", (text or "").strip())
    t = re.sub(r"\s*```$", "", t)
    for left, right in (("[", "]"), ("{", "}")):
        a, b = t.find(left), t.rfind(right)
        if a >= 0 and b > a:
            try:
                return json.loads(t[a:b + 1])
            except json.JSONDecodeError:
                pass
    raise ValueError("provider response did not contain valid JSON")


# ── Determinism / reproducibility (added v1.5.0) ──────────────────────────
# Two agents on two different model families must be able to produce the same
# intended artifact. These helpers remove the three biggest sources of
# divergence: sampling randomness, ordering, and near-duplicate content.

DEFAULT_SEED = int(os.environ.get("FORGE_SEED", "7"))


def log_line(msg: str, **fields) -> None:
    """Structured log to STDERR only (stdout stays machine-readable)."""
    try:
        from model_adapters import log
        log(msg, **fields)
    except Exception:
        import sys as _s
        print("[forge] " + msg, file=_s.stderr)


def canonical_json(obj) -> str:
    """Deterministic serialization used for every artifact this skill writes:
    sorted keys, stable indentation, Unicode preserved. Byte-comparable across
    runs, machines and models."""
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2)


def write_json(path, obj) -> None:
    """Write an artifact deterministically (canonical JSON + trailing newline)."""
    Path(path).write_text(canonical_json(obj) + "\n", "utf-8")


def content_key(text: object) -> str:
    """Normalized similarity key for deduplication across models.

    Persian normalization + digit folding + ZWNJ/punctuation removal, so
    «کدام‌یک از موارد زیر…؟» from model A and «کدام یک از موارد زیر ...» from
    model B collapse to the same key.
    """
    t = search_normalize(str(text or ""))
    # Drop Arabic combining marks so «حافظهٔ» == «حافظه» and «مطالعهٔ» == «مطالعه»
    # (models differ on whether they write the ezafe hamza), plus harakat.
    t = re.sub(r"[\u0640\u064b-\u0652\u0653\u0654\u0655\u0670]", "", t)
    t = re.sub(r"[\u060c\u061b\u061f.,;:!?()\[\]{}«»\"'\-–—/\\]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def dedupe_items(items, keys=("q", "text", "title", "caption")):
    """Stable, order-preserving near-duplicate removal for enrichment items."""
    seen, out = set(), []
    for it in items or []:
        if isinstance(it, dict):
            probe = next((it[k] for k in keys if it.get(k)), json.dumps(it, sort_keys=True))
        else:
            probe = it
        k = content_key(probe)
        if not k or k in seen:
            continue
        seen.add(k)
        out.append(it)
    return out


def stable_sort_items(items, order_key="ref"):
    """Deterministic ordering: by source reference, then by content key.
    Guarantees the same artifact ordering regardless of which model or thread
    produced which item."""
    def sk(it):
        if not isinstance(it, dict):
            return (0, content_key(it))
        try:
            ref = int(it.get(order_key, 0) or 0)
        except (TypeError, ValueError):
            ref = 0
        probe = next((it[k] for k in ("q", "text", "title", "caption") if it.get(k)), "")
        return (ref, content_key(probe))
    return sorted(items or [], key=sk)


STOPWORDS_FA = {"از", "به", "در", "که", "را", "با", "این", "آن", "و", "یا", "است",
                "هست", "برای", "های", "ها", "می", "چه", "کدام", "چقدر", "چند",
                "شود", "کند", "دارد", "بر", "تا", "یک", "the", "a", "of", "is"}


def _tokens(text: object) -> set:
    return {w for w in content_key(text).split() if len(w) > 2 and w not in STOPWORDS_FA}


def similarity(a: object, b: object) -> float:
    """Jaccard overlap of content words — a cheap, dependency-free proxy for
    'these two items say the same thing'. Used to merge near-duplicates that
    different models phrase differently."""
    ta, tb = _tokens(a), _tokens(b)
    if not ta or not tb:
        return 1.0 if content_key(a) == content_key(b) else 0.0
    return len(ta & tb) / float(len(ta | tb))


def consensus_pick(candidates, keys=("q", "text", "title", "caption"),
                   threshold=0.6, min_votes=1):
    """n-way self-consistency across model families.

    Given the SAME request answered by several models, group items that mean
    the same thing (exact key match, or Jaccard similarity above ``threshold``)
    and rank them by how many independent models produced them. The best-worded
    representative of each group is kept — by default the one from the
    highest-ranked model, preferring the more complete answer.

    This is the mechanism that makes the *intended result* reproducible even
    though GPT, Claude, Gemini, Mistral and Llama never phrase a flashcard
    identically: agreement across families is treated as evidence, and
    single-model idiosyncrasies sink to the bottom (or are dropped entirely
    with ``min_votes=2``).
    """
    def probe_of(it):
        if isinstance(it, dict):
            return next((it[k] for k in keys if it.get(k)), json.dumps(it, sort_keys=True))
        return it

    groups = []  # [{votes, models, rank, item, probe, key}]
    for rank, batch in enumerate(candidates or []):
        for it in batch or []:
            probe = probe_of(it)
            k = content_key(probe)
            if not k:
                continue
            hit = None
            for g in groups:
                if g["key"] == k or similarity(probe, g["probe"]) >= threshold:
                    hit = g
                    break
            if hit is None:
                groups.append({"votes": 1, "models": {rank}, "rank": rank,
                               "item": it, "probe": probe, "key": k})
            else:
                hit["models"].add(rank)
                hit["votes"] = len(hit["models"])
                # keep the most informative representative from the best model
                better = (rank < hit["rank"]) or (
                    rank == hit["rank"] and len(str(probe)) > len(str(hit["probe"])))
                if better:
                    hit["item"], hit["probe"], hit["rank"] = it, probe, rank
    kept = [g for g in groups if g["votes"] >= min_votes]
    kept.sort(key=lambda g: (-g["votes"], g["rank"], g["key"]))
    return [g["item"] for g in kept]


def load_provider_config(path: str | Path | None = None) -> list:
    """Load the provider chain (v1.5.0: model-agnostic, config-optional).

    Resolution order:
      1. the given providers.json (v1.x ``kind`` and v1.4 ``dialect`` shapes
         are both accepted);
      2. environment auto-discovery — OPENAI/ANTHROPIC/GEMINI/GROQ/OPENROUTER/
         MISTRAL/COHERE/DEEPSEEK/TOGETHER/FIREWORKS/XAI/ZAI/HF keys,
         ``OLLAMA_HOST`` and ``LOCAL_OPENAI_BASE_URL`` for local runtimes;
      3. the deterministic offline ``mock`` provider when ``FORGE_MOCK=1``.

    This is what lets a foreign agent runtime (Claude Code, Codex CLI, Gemini
    CLI, LangChain, CrewAI, n8n, cron) run the skill with nothing but the API
    key it already has in its environment.

    Returns ``ProviderInfo`` objects, which still behave like the old dicts for
    the two keys the legacy code read (``p["name"]``, ``p["model"]``).
    """
    from model_adapters import discover_providers  # local import: keeps common.py importable standalone
    provs = discover_providers(str(path) if path else None)
    if not provs:
        raise RuntimeError(
            "no usable model provider found. Set one of OPENAI_API_KEY, "
            "ANTHROPIC_API_KEY, GEMINI_API_KEY, GROQ_API_KEY, OPENROUTER_API_KEY, "
            "MISTRAL_API_KEY, COHERE_API_KEY, DEEPSEEK_API_KEY, OLLAMA_HOST, … "
            "or pass a providers.json, or export FORGE_MOCK=1 for an offline dry run.")
    return provs


def call_provider(provider, prompt: str, system: str,
                  max_tokens: int = 12000, timeout: int = 360,
                  json_mode: bool = True, seed: int | None = None) -> str:
    """Call ANY supported model dialect and return the raw assistant text.

    v1.5.0: this is a thin, backwards-compatible wrapper over
    ``model_adapters.call_model`` — the same signature as v1.3 so existing
    pipelines and forks keep working, but now backed by adapters for
    OpenAI-compatible chat, the OpenAI Responses API, Gemini, Anthropic
    messages, Cohere v2, Ollama, HuggingFace router, and a deterministic
    offline mock.

    Every started request is allowed to complete (retry + backoff + failover);
    keys are never logged; responses are cached by content hash.
    """
    from model_adapters import call_model
    reply = call_model(provider, prompt, system, max_tokens=max_tokens,
                       timeout=timeout, json_mode=json_mode,
                       seed=DEFAULT_SEED if seed is None else seed)
    if reply.truncated:
        # Surfaced, not hidden: callers shrink the batch and retry rather than
        # silently shipping half a study guide.
        log_line("truncated response", provider=reply.provider, model=reply.model,
                 chars=len(reply.text))
    return reply.text


def call_provider_reply(provider, prompt: str, system: str, **kw):
    """Same as :func:`call_provider` but returns the full normalized
    ``ModelReply`` (text, finish reason, provider, model, usage, timing)."""
    from model_adapters import call_model
    kw.setdefault("seed", DEFAULT_SEED)
    return call_model(provider, prompt, system, **kw)


def esc(text: object) -> str:
    return html.escape(str(text), quote=True)


# ── Robust provider-JSON coercion helpers (added v1.3.0) ──────────────────
# Free-tier providers frequently return Persian/Arabic digit or word page
# references («صفحهٔ ۳»), Persian/Arabic answer labels («الف/ب/ج/د»), bare JSON
# arrays instead of objects, and option text prefixed with duplicate «الف) »
# style labels. These helpers coerce those shapes into the strict internal
# contract instead of discarding otherwise-valid content.

# Persian/Arabic digits -> ASCII (note: do NOT reuse the name FA_DIGITS, which
# normalizes the opposite direction and is used by normalize_persian above).
ASCII_DIGITS = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")

# Persian/Arabic letters and digits that models emit instead of A-D.
ARABIC_ANSWER_MAP = {
    "الف": "A", "ا": "A", "أ": "A", "۱": "A", "1": "A",
    "ب": "B", "۲": "B", "2": "B",
    "ج": "C", "۳": "C", "3": "C",
    "د": "D", "۴": "D", "4": "D",
}

_OPTION_PREFIX_RE = re.compile(
    r"^\s*(?:الف|آ|ا|ب|پ|ج|ت|ث|د|[۱-۴1-4]|[A-Da-d])\s*[).\-:]\s*", re.UNICODE)


def coerce_ref(value, session_start: int, session_end: int) -> int:
    """Clamp a provider-supplied page reference into the session range.

    Understands integers, floats and strings such as «صفحهٔ ۳» or «5»; Persian
    digits are translated first. Never raises — an unparseable or out-of-range
    reference falls back to the session start page.
    """
    s, e = int(session_start), int(session_end)
    if isinstance(value, bool):
        return s
    if isinstance(value, (int, float)):
        return min(e, max(s, int(value)))
    if isinstance(value, str):
        m = re.findall(r"\d+", value.translate(ASCII_DIGITS))
        if m:
            return min(e, max(s, int(m[0])))
    return s


def coerce_answer(value) -> str:
    """Normalize a model answer label to 'A'-'D' (or '' if unrecognized).

    Accepts ASCII letters plus the Persian/Arabic letters and digits models
    commonly emit (e.g. «الف», «ج», «۲»).
    """
    a = str(value or "").strip()
    if len(a) == 1 and a.upper() in "ABCD":
        return a.upper()
    return ARABIC_ANSWER_MAP.get(a, ARABIC_ANSWER_MAP.get(a.upper(), ""))


def is_bare_answer(value) -> bool:
    """True when an answer carries no real content (empty, a single letter, or
    a 1-2 character token with no digits). Used to drop multiple-choice-style
    flashcards that ended up with a bare 'A'/'ب' instead of a statement."""
    a = str(value or "").strip()
    if not a:
        return True
    if re.fullmatch(r"[A-Da-d]", a):
        return True
    return len(a) <= 2 and not any(ch.isdigit() for ch in a)


def strip_option_prefix(text) -> str:
    """Remove a duplicated «الف) » / «A) » style prefix from an option so the
    HTML shell's own A-D labels do not repeat."""
    return _OPTION_PREFIX_RE.sub("", str(text or "")).strip()
