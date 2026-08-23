#!/usr/bin/env python3
"""Shared, dependency-light helpers for Persian PDF StudyGuide Forge.
No credentials are stored here. Provider keys are read from explicitly named
environment variables only when network-assisted editing is enabled.
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
    text = re.sub(r"^```(?:json)?\s*", "", (text or "").strip())
    text = re.sub(r"\s*```$", "", text)
    for left, right in (("[", "]"), ("{", "}")):
        a, b = text.find(left), text.rfind(right)
        if a >= 0 and b > a:
            try:
                return json.loads(text[a:b + 1])
            except json.JSONDecodeError:
                pass
    raise ValueError("provider response did not contain valid JSON")


def load_provider_config(path: str | Path) -> list[dict]:
    """Load provider descriptors; API key values remain in env vars.

    Example descriptor:
      {"name":"gemini","kind":"gemini","model":"gemini-2.5-flash",
       "api_key_env":"GEMINI_API_KEY"}
    """
    data = json.loads(Path(path).read_text("utf-8"))
    providers = data.get("providers", data)
    if not isinstance(providers, list):
        raise ValueError("provider config must contain a providers list")
    out = []
    for p in providers:
        env = p.get("api_key_env", "")
        if env and os.environ.get(env):
            out.append(p)
    if not out:
        raise RuntimeError("no configured provider has its api_key_env set")
    return out


def _post_json(url: str, headers: dict, body: dict, timeout: int = 360) -> dict:
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")
    last = None
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code not in (408, 409, 429, 500, 502, 503, 504):
                raise
            retry = int(exc.headers.get("Retry-After", "0") or 0)
            time.sleep(max(retry, min(2 ** attempt, 60)))
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last = exc
            time.sleep(min(2 ** attempt, 60))
    raise RuntimeError(f"provider call failed after retries: {last}")


def call_provider(provider: dict, prompt: str, system: str, max_tokens: int = 12000, timeout: int = 360) -> str:
    """Call Gemini-native or OpenAI-compatible endpoint.

    Every started request is allowed to complete. Retries use backoff; callers
    should cache successful results and never log headers or keys.
    """
    key = os.environ[provider["api_key_env"]]
    kind = provider.get("kind", "openai")
    model = provider["model"]
    if kind == "gemini":
        base = provider.get("base_url", "https://generativelanguage.googleapis.com/v1beta")
        url = f"{base}/models/{model}:generateContent?key={key}"
        body = {"systemInstruction": {"parts": [{"text": system}]},
                "contents": [{"role": "user", "parts": [{"text": prompt}]}],
                "generationConfig": {"maxOutputTokens": max_tokens, "temperature": 0.15}}
        data = _post_json(url, {"Content-Type": "application/json"}, body, timeout)
        return "".join(p.get("text", "") for c in data.get("candidates", [])
                       for p in c.get("content", {}).get("parts", []))
    base = provider["base_url"].rstrip("/")
    body = {"model": model, "messages": [{"role": "system", "content": system},
            {"role": "user", "content": prompt}], "max_tokens": max_tokens, "temperature": 0.15}
    data = _post_json(base + "/chat/completions",
                      {"Authorization": "Bearer " + key, "Content-Type": "application/json"}, body, timeout)
    return data["choices"][0]["message"]["content"]


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
