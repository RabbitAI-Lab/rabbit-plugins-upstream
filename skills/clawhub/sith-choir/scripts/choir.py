#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sith-choir — cross-model intellect relay across a mesh of API keys.

A "conductor" farms work out to a *choir* of heterogeneous models reachable via
stored API keys, then harvests the best intelligence back. Designed as a
ClawHub skill.

The choir is a MESH, not a single key: every stored credential
(`api_key` + every `alt_api_keys` entry, across every provider) becomes its own
voice. Voices are health-tracked with per-key cooldowns and automatic failover,
so a request that starts on one provider's key can be served by, or ask help
from, the keys of other providers (e.g. a Mistral-key model that needs help
consults Gemini keys and llm7.io keys).

Research foundations (see references/design.md for full citations):
  * Mixture-of-Agents (arXiv:2406.04692)  -> `moa` / proposer->aggregator.
  * LLM cascades / FrugalGPT (arXiv:2305.05176) -> cheap-first `ask`, escalate
    only when confidence is low (`escalate`).
  * LLM-as-a-Judge (arXiv:2306.05685)     -> `judge` reward/punish panel with
    bias mitigations (multi-judge mean, no-self-enhancement, verbosity warning).
  * Test-time compute (arXiv:2408.03314)  -> spend reasoning budget adaptively.
  * Weak-to-strong (arXiv:2312.09390 + trust functions arXiv:2606.01000)
    -> weak/cheap models propose raw material; a strong model aggregates.
  * Vision asymmetry across vendors (arXiv:2502.16428) -> `vision` relay.

Sith-choir flavour: the choir sings (weak/cheap models produce candidates),
the Sith listens, judges, and drains the best intelligence from the room.

Usage examples:
  choir.py list --credentials creds.json
  choir.py fleet --credentials creds.json
  choir.py ask "2+2?" --from groq/openai/gpt-oss-120b --credentials creds.json
  choir.py ask "hi" --from mistral/mistral-small-latest#2   # force key #2
  choir.py moa "hard question" --aggregator gemini --credentials creds.json
  choir.py escalate "prove pythagoras" --from mistral/mistral-small-latest \
           --helpmates gemini,llm7 --force --credentials creds.json
  choir.py vision --image chart.png --question "summarize" --synthesize
  choir.py harvest "hard question" --json --credentials creds.json
  choir.py ledger --credentials creds.json

Credentials file format (JSON):  {"providers": {name: {"api_key": "..."}}}
  Multi-key: add "alt_api_keys": ["k2", ...] for additional accounts of the
  same provider. Optional per provider: "base" (override endpoint), "kind"
  ("openai"|"gemini"), "default_model", "tags": ["vision", ...].
  In an arena.ai workspace the file usually lives at
  /home/user/secrets/api_credentials.json and is auto-loaded with --use-workspace.

Never prints, logs or persists API keys. State (reward ledger + key health) is
written only under the state dir (default ~/.cache/sith-choir/).
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
json_mod = json
import mimetypes
import os
import re
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.request

VERSION = "1.3.0"

# --------------------------------------------------------------------------
# Provider endpoint defaults (override per provider via the credentials file)
# --------------------------------------------------------------------------
DEFAULT_BASE = {
    "openai":       "https://api.openai.com/v1",
    "anthropic":    "https://api.anthropic.com/v1",
    "google":       "https://generativelanguage.googleapis.com/v1beta",
    "gemini":       "https://generativelanguage.googleapis.com/v1beta",
    "openrouter":   "https://openrouter.ai/api/v1",
    "groq":         "https://api.groq.com/openai/v1",
    "mistral":      "https://api.mistral.ai/v1",
    "cohere":       "https://api.cohere.com/compatibility/v1",
    "huggingface":  "https://router.huggingface.co/v1",
    "zai":          "https://api.z.ai/api/paas/v4",
    "llm7":         "https://api.llm7.io/v1",
    "cerebras":     "https://api.cerebras.io/v1",
    "xai":          "https://api.x.ai/v1",
    "kimi":         "https://api.moonshot.ai/v1",
}
# Per-provider fallback model when the credentials file does not name one.
# These mirror tools/router.py PROVIDER_DEFS — the model ids this fleet's keys
# are *live-verified* against (free-tier aware; retired ids like
# gemini-2.5-flash / llama-3.3-70b-versatile are deliberately absent). They are
# preferred over catalog ids: a catalog (GET /models) lists public ids the key
# may not actually be granted (e.g. Gemini "not available to new users"), so a
# proven default must never be clobbered by catalog entry [0].
DEFAULT_MODEL = {
    "gemini": "gemini-3.1-flash-lite", "groq": "openai/gpt-oss-120b",
    "mistral": "mistral-small-latest", "cohere": "command-a-03-2025",
    "huggingface": "meta-llama/Llama-3.1-8B-Instruct", "zai": "glm-4.7-flash",
    "llm7": "default", "openrouter": "nvidia/nemotron-3-super-120b-a12b:free",
    "cerebras": "gpt-oss-120b", "openai": "default",
    "xai": "grok-4", "kimi": "kimi-k2.5",
}
# Providers that store a credential but that this skill cannot call directly
# (different auth / URL scheme than the openai & gemini kinds used here).
NON_CALLABLE = {"cloudflare", "kaggle"}

# --------------------------------------------------------------------------
# Heuristic capability classification. This is a *router hint*, not ground
# truth: the true capability of an endpoint is decided by the user's key and
# the vendor's docs. Every heuristic can be overridden in the credentials
# file via a "tags": [...] list on a provider entry.
# --------------------------------------------------------------------------
VISION_RE = re.compile(
    r"vision|multimodal|image|4o|pixtral|gemini|claude|fable|opus|sonnet|grok|"
    r"kimi-k3|k2\.5|-vl\b|glm-4\.1v|glm-4\.5v|glm-4v|aya-vision|"
    r"command-a-vision|janus|llama-4|omni|gpt-4o|gpt-5|gpt-6|gemma", re.I)
REASONING_RE = re.compile(
    r"reason|think|devstral|codestral|deepseek|r1|v4-pro|kimi|k3|o1|o3|o4|"
    r"command-a-reason|glm-4\.7|glm-5|minimax|opus|sol|terra|pro$|gpt-oss|"
    r"grok|nova|qwen3\.8|nemotron", re.I)
FAST_RE = re.compile(
    r"flash|fast|lite|mini|tiny|small|8b|7b|3b|turbo|speed|low|scout|nano", re.I)
LONGCTX_RE = re.compile(
    r"long|1m|128k|256k|pro$|gemini|claude|grok|k3|k2|opus", re.I)

CANDIDATE_JSON = re.compile(r"\{.*\}|SCORE\s*[:=]\s*(\d+(?:\.\d+)?)", re.S | re.I)
CONF_RE = re.compile(r"(?:^|\n)\s*CONF\s*[:=]\s*(\d{1,3}(?:\.\d+)?)\s*%?", re.I)
HTTP_CODE_RE = re.compile(r"HTTP (\d{3})")


def classify(model: str, provider: str = "") -> set:
    """Return a set of tags for a model id: reasoning/vision/fast/longctx."""
    tags = set()
    s = f"{provider}/{model}".lower()
    if VISION_RE.search(s):
        tags.add("vision")
    if REASONING_RE.search(s):
        tags.add("reasoning")
    if FAST_RE.search(s):
        tags.add("fast")
    if LONGCTX_RE.search(s) or "1m" in s:
        tags.add("longctx")
    if not tags:
        tags.add("general")
    return tags


def provider_keys(block: dict) -> list[str]:
    """Ordered distinct stored keys for one provider: primary first, then
    `alt_api_keys` in order. Each distinct VALUE is a separate voice/account.
    Identical values collapse; placeholders are skipped. Key material is never
    printed — voices are labelled by their 1-based index (`k1`, `k2`, ...)."""
    keys: list[str] = []
    primary = block.get("api_key") or block.get("api_token")
    alts = block.get("alt_api_keys") or []
    if isinstance(alts, str):
        alts = [alts]
    for k in [primary, *alts]:
        if not isinstance(k, str):
            continue
        v = k.strip()
        if not v or "placeholder" in v.lower() or v.startswith("YOUR_"):
            continue
        if v not in keys:
            keys.append(v)
    return keys


# --------------------------------------------------------------------------
# Credentials / roster loading (multi-key mesh)
# --------------------------------------------------------------------------
def _write_private(path: str, obj: object, indent: int | None = None,
                 sort_keys: bool = True) -> None:
    """Atomically write JSON to a file that is private from the very first
    byte (mkstemp creates mode 0600): no world-readable window between create
    and chmod, and os.replace makes concurrent readers never see a partial
    file. Used for every state writer."""
    d = os.path.dirname(path) or "."
    os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".sith-", suffix=".tmp", dir=d)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=indent,
                      sort_keys=sort_keys)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


class Fleet:
    """Per-key health store. Every key (voice) is tracked independently so a
    throttled/dead key is cooled and the provider's other keys take over."""

    def __init__(self, state_dir: str):
        self.state_dir = state_dir
        self.path = os.path.join(state_dir, "fleet.json")
        os.makedirs(state_dir, exist_ok=True)
        self.data: dict[str, dict] = {}
        if os.path.isfile(self.path):
            try:
                self.data = json.load(open(self.path, encoding="utf-8"))
            except Exception:
                self.data = {}

    @staticmethod
    def vid(provider: str, kid: int) -> str:
        return f"{provider}#k{kid}"

    def rec(self, provider: str, kid: int) -> dict:
        v = self.vid(provider, kid)
        r = self.data.get(v)
        if r is None:
            r = {"ok": 0, "fail": 0, "cool_until": 0.0, "last": "",
                 "tokens": 0, "cached": 0, "ms": 0.0, "calls": 0}
            self.data[v] = r
        return r

    def add_tokens(self, provider: str, kid: int, n: int,
                   cached: int = 0) -> None:
        if n or cached:
            self.rec(provider, kid)
            key = self.vid(provider, kid)
            self.data[key]["tokens"] = self.data[key].get("tokens", 0) + n
            self.data[key]["cached"] = self.data[key].get("cached", 0) + cached
            self.save()

    def note_call(self, provider: str, kid: int, ms: float) -> None:
        """Fold one call's wall-clock latency into the voice's EWMA."""
        self.rec(provider, kid)
        key = self.vid(provider, kid)
        r = self.data[key]
        n = r.get("calls", 0)
        prev = r.get("ms", 0.0)
        r["ms"] = round((prev * n + ms) / (n + 1), 1) if n else round(ms, 1)
        r["calls"] = n + 1
        self.save()

    def cooled(self, provider: str, kid: int) -> float:
        """Seconds remaining on the cooldown (>0 => cooled)."""
        return max(0.0, self.rec(provider, kid).get("cool_until", 0.0) - time.time())

    def usable(self, provider: str, nkeys: int) -> list[int]:
        """Kid indices in health order: uncooled first, then by fewest fails."""
        kids = range(1, nkeys + 1)
        uncooled = [k for k in kids if self.cooled(provider, k) == 0]
        return sorted(uncooled, key=lambda k: self.rec(provider, k).get("fail", 0)) + \
            sorted((k for k in kids if k not in uncooled),
                   key=lambda k: self.cooled(provider, k))

    @staticmethod
    def _cool(code: int | None, fails: int) -> float:
        if code == 429:
            return min(300.0, 60.0 * (fails + 1))
        if code in (401, 403, 402):
            return 3600.0  # bad/empty credential — needs human action
        if code in (408, 500, 502, 503, 504) or code is None:
            return 30.0 * (fails + 1)
        return 5.0

    def record(self, provider: str, kid: int, ok: bool, err: str = "") -> None:
        r = self.rec(provider, kid)
        if ok:
            r["ok"] = r.get("ok", 0) + 1
            r["fail"] = 0
            r["cool_until"] = 0.0
            r["last"] = ""
        else:
            r["fail"] = r.get("fail", 0) + 1
            m = HTTP_CODE_RE.search(err or "")
            code = int(m.group(1)) if m else None
            r["cool_until"] = time.time() + self._cool(code, r["fail"])
            r["last"] = (err or "network")[:80]
        self.save()

    def save(self) -> None:
        _write_private(self.path, self.data, indent=2)


class Roster:
    """Read-only view of the available models: every provider and every stored
    key, with a health-aware voice picker (per-provider failover)."""

    def __init__(self, creds_path: str | None, state_dir: str,
                 catalog_path: str | None = None, allow_workspace: bool = False):
        self.creds_path = creds_path or os.environ.get("SITH_CREDENTIALS", "")
        self.state_dir = state_dir or os.environ.get(
            "SITH_STATE", os.path.expanduser("~/.cache/sith-choir"))
        self.fleet = Fleet(self.state_dir)
        self.providers: dict[str, dict] = {}
        self.catalog: dict[str, list[str]] = {}
        self._load(allow_workspace)
        if catalog_path:
            self._load_catalog(catalog_path)
        elif allow_workspace:
            self._load_catalog(os.path.expanduser(
                "~/out/models_by_provider.json"))

    def _resolve_creds(self, allow_workspace: bool) -> str:
        cands = [self.creds_path]
        if allow_workspace:
            cands += ["/home/user/secrets/api_credentials.json",
                      os.path.expanduser("~/secrets/api_credentials.json")]
        for c in cands:
            if c and os.path.isfile(c):
                return c
        raise SystemExit(
            "no credentials file found. Pass --credentials <path> (JSON "
            '{"providers":{name:{"api_key":...}}}), set SITH_CREDENTIALS, or '
            "--use-workspace in an arena.ai workspace.")

    def _load(self, allow_workspace: bool) -> None:
        p = self._resolve_creds(allow_workspace)
        data = json.load(open(p, encoding="utf-8"))
        for name, cfg in (data.get("providers") or {}).items():
            if not isinstance(cfg, dict):
                continue
            keys = provider_keys(cfg)
            if not keys:
                continue
            base = cfg.get("base") or DEFAULT_BASE.get(name, "")
            kind = cfg.get("kind") or ("gemini" if name in ("gemini", "google") else "openai")
            model = cfg.get("model") or cfg.get("default_model") or DEFAULT_MODEL.get(name, "")
            tags = set(cfg.get("tags", []) or [])
            self.providers[name] = {
                "keys": keys, "base": base, "kind": kind,
                "model": model, "tags": tags,
                "note": ("stored but not directly callable by this skill"
                         if name in NON_CALLABLE else ""),
            }
        if not self.providers:
            raise SystemExit("credentials file contains no usable provider keys.")

    def _load_catalog(self, path: str) -> None:
        if not path or not os.path.isfile(path):
            return
        try:
            raw = json.load(open(path, encoding="utf-8"))
        except Exception:
            return
        items = raw.get("providers", raw) if isinstance(raw, dict) else raw
        for p in items if isinstance(items, list) else []:
            if not isinstance(p, dict):
                continue
            name = p.get("provider") or p.get("name")
            ids = p.get("models_list") or p.get("models") or []
            ids = [m.get("id") if isinstance(m, dict) else str(m) for m in ids]
            if name:
                self.catalog[name] = ids
        # Fill only providers that still have NO model. Never clobber a model
        # that is set (credentials or proven DEFAULT_MODEL) with catalog[0].
        for name, prov in self.providers.items():
            if not prov["model"]:
                ids = self.catalog.get(name, [])
                if ids:
                    prov["model"] = ids[0]

    # -- voices: one per stored key -----------------------------------------
    def voices_for(self, name: str) -> list[dict]:
        """Every stored key of one provider as an independent voice member."""
        p = self.providers.get(name)
        if not p or p["note"] or not p["model"] or not p["base"]:
            return []
        out = []
        for i, key in enumerate(p["keys"], start=1):
            tags = set(p["tags"])
            tags |= classify(p["model"], name) - tags
            out.append({"provider": name, "kid": i, "key": key,
                        "base": p["base"], "kind": p["kind"],
                        "model": p["model"], "tags": tags})
        return out

    def all_voices(self) -> list[dict]:
        out: list[dict] = []
        for name in self.providers:
            out.extend(self.voices_for(name))
        return out

    def voice(self, name: str, kid: int | None = None) -> dict | None:
        """Healthiest usable key of a provider (or a specific key by index).
        Fails over: cooled keys are skipped in favour of live ones."""
        voices = self.voices_for(name)
        if not voices:
            return None
        if kid is not None:
            for v in voices:
                if v["kid"] == kid:
                    return v
            raise SystemExit(f"unknown key index: {name}#k{kid} "
                             f"(provider has {len(voices)} keys)")
        for kidx in self.fleet.usable(name, len(voices)):
            for v in voices:
                if v["kid"] == kidx:
                    return v
        return voices[0]  # all cooled — still allow (call will re-cool)

    # -- members: one voice per provider (distinct models) ------------------
    def members(self) -> list[dict]:
        out = []
        for name in self.providers:
            v = self.voice(name)
            if v:
                out.append(v)
        return out

    def member_key(self, prov: str, model: str | None = None,
                   kid: int | None = None) -> dict:
        """Resolve provider[#kid][/model] to a live voice. model may be None
        to use the provider default."""
        voices = self.voices_for(prov)
        if not voices:
            raise SystemExit(f"provider '{prov}' has no callable voice "
                             f"(keys, model, base and kind all required).")
        if model:
            cands = [v for v in voices if v["model"] == model]
            if not cands:
                raise SystemExit(f"unknown member: {prov}/{model} "
                                 f"(default for provider: {voices[0]['model']})")
        else:
            cands = [v for v in voices if v["model"] == voices[0]["model"]]
        if kid is not None:
            for v in cands:
                if v["kid"] == kid:
                    return v
            raise SystemExit(f"unknown key index: {prov}#k{kid} "
                             f"(provider has {len(cands)} callable keys)")
        for kidx in self.fleet.usable(prov, len(self.providers[prov]["keys"])):
            for v in cands:
                if v["kid"] == kidx:
                    return v
        return cands[0]

    def pick(self, want: set[str] | None = None, exclude: set[str] | None = None,
             n: int = 1) -> list[dict]:
        ms = self.members()
        if want:
            ms = [m for m in ms if want & m["tags"]]
        if exclude:
            ms = [m for m in ms if not (exclude & m["tags"])]
        ms = sorted(ms, key=lambda m: (m["provider"], m["model"]))
        return ms[:n] if n else ms

    def voice_count(self, name: str) -> int:
        p = self.providers.get(name)
        return len(p["keys"]) if p else 0


# --------------------------------------------------------------------------
# State / reward ledger
# --------------------------------------------------------------------------
LEDGER_FILE = "ledger.json"


class Ledger:
    def __init__(self, state_dir: str):
        self.path = os.path.join(state_dir, LEDGER_FILE)
        os.makedirs(state_dir, exist_ok=True)
        self.data: dict[str, dict] = {}
        if os.path.isfile(self.path):
            try:
                self.data = json.load(open(self.path, encoding="utf-8"))
            except Exception:
                self.data = {}

    def key(self, m: dict) -> str:
        return f"{m['provider']}/{m['model']}"

    def update_label(self, label: str, score: float) -> dict:
        """Update ledger from a voice label like 'gemini#k1/model' (keys by
        provider/model, pooling a provider's keys as before)."""
        pk, _, model = label.partition("/")
        prov = pk.partition("#")[0]
        return self.update({"provider": prov, "model": model}, score)

    def update(self, m: dict, score: float) -> dict:
        k = self.key(m)
        rec = self.data.get(k, {"uses": 0, "sum": 0.0, "ewma": None,
                                "rewards": 0, "punishments": 0, "best": 0.0})
        rec["uses"] += 1
        rec["sum"] += score
        rec["ewma"] = round((rec["ewma"] * (rec["uses"] - 1) + score) / rec["uses"]
                            if rec["ewma"] is not None else score, 3)
        rec["best"] = max(rec.get("best", 0.0), score)
        if score >= 7.5:
            rec["rewards"] += 1
        elif score <= 4.0:
            rec["punishments"] += 1
        rec["last"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        self.data[k] = rec
        self.save()
        return rec

    def save(self) -> None:
        _write_private(self.path, self.data, indent=2)

    def best(self, ms: list[dict], min_uses: int = 1) -> list[dict]:
        def score(m):
            rec = self.data.get(self.key(m), {})
            if rec.get("uses", 0) < min_uses:
                return -1.0
            return rec.get("ewma", -1.0)
        ranked = sorted(ms, key=lambda m: -score(m))
        return [m for m in ranked if score(m) >= 0]


# --------------------------------------------------------------------------
# Sessions (multi-turn memory), answer cache, provenance runs
# --------------------------------------------------------------------------
# Privacy rule that also keeps the code simple: session transcripts, the
# answer cache and provenance runs store NO raw prompts or model answer bodies
# anywhere except inside a session file the user explicitly opens (see
# Session.add). Question-derived cache keys are sha256 digests, provenance
# records voice labels + verdicts + token counts only.


class Sessions:
    """Bounded multi-turn memory. Transcript kept under
    state/sessions/<name>.json (chmod 600). Each stored turn only records the
    last ~TRIM_TURNS exchanges so memory cannot balloon."""

    TRIM_TURNS = 12

    def __init__(self, state_dir: str):
        self.dir = os.path.join(state_dir, "sessions")
        os.makedirs(self.dir, exist_ok=True)
        try:
            os.chmod(self.dir, 0o700)
        except OSError:
            pass

    def _path(self, name: str) -> str:
        safe = re.sub(r"[^A-Za-z0-9._-]", "_", name)
        return os.path.join(self.dir, f"{safe}.json")

    def load(self, name: str) -> list[dict]:
        p = self._path(name)
        if not os.path.isfile(p):
            return []
        try:
            turns = json.load(open(p, encoding="utf-8"))
            return turns if isinstance(turns, list) else []
        except Exception:
            return []

    def append(self, name: str, q: str, answer: str, member: str) -> None:
        turns = self.load(name)
        turns.append({"role": "user", "content": q[:800]})
        turns.append({"role": "assistant", "content": answer[:2000],
                      "member": member})
        # bounded memory
        if len(turns) > self.TRIM_TURNS:
            turns = turns[-self.TRIM_TURNS:]
        p = self._path(name)
        _write_private(p, turns, indent=1, sort_keys=False)

    def reset(self, name: str) -> None:
        p = self._path(name)
        if os.path.isfile(p):
            os.remove(p)

    def list(self) -> list[str]:
        try:
            return sorted(f[:-5] for f in os.listdir(self.dir)
                          if f.endswith(".json"))
        except FileNotFoundError:
            return []

    def context(self, name: str, k: int = 6,
                budget_chars: int = 2600) -> str:
        """Render the last k exchanges for the model, bounded by a rolling
        character budget (deterministic, no extra model call): the newest two
        exchanges keep up to ~600 chars each, older ones are truncated harder
        so a long session's prefix cannot balloon the token cost of every
        turn."""
        turns = self.load(name)
        if not turns:
            return ""
        recent = turns[-k * 2:]
        lines = []
        used = 0
        n = len(recent)
        for i, t in enumerate(recent):
            who = "User" if t.get("role") == "user" else "Assistant"
            content = t.get("content", "") or ""
            is_new = i >= n - 4
            per = 600 if is_new else 220
            room = budget_chars - used
            if room <= 40:
                break
            cap = min(per, room)
            chunk = content[:cap]
            if len(content) > cap:
                chunk = chunk.rstrip() + " ..."
            lines.append(f"{who}: {chunk}")
            used += len(chunk) + len(who) + 3
        return "\n".join(lines)


def session_wrap(ctx: str, q: str) -> str:
    if not ctx:
        return q
    return (f"[Conversation so far]\n{ctx}\n\n"
            f"[New question]\n{q}")


class AnswerCache:
    """Exact-match response cache (sha256 of the question). Repeated identical
    questions cost zero tokens — very valuable when free-tier keys are
    rate-limited. `--no-cache` bypasses; answers are stored (they are the
    point of a cache) but never keys or prompts."""

    def __init__(self, state_dir: str):
        self.path = os.path.join(state_dir, "cache.json")
        self.data: dict[str, dict] = {}
        if os.path.isfile(self.path):
            try:
                self.data = json.load(open(self.path, encoding="utf-8"))
            except Exception:
                self.data = {}
        self.hits = 0

    @staticmethod
    def key(q: str) -> str:
        return hashlib.sha256(q.encode("utf-8")).hexdigest()

    def get(self, q: str) -> dict | None:
        k = self.key(q)
        hit = self.data.get(k)
        if hit and hit.get("answer"):
            self.hits += 1
            return hit
        return None

    def put(self, q: str, answer: str, member: str) -> None:
        self.data[self.key(q)] = {"answer": answer, "member": member,
                                  "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                                      time.gmtime())}
        _write_private(self.path, self.data, indent=1, sort_keys=False)


class Runs:
    """Provenance: one small record per command. Stores voice labels, verdict,
    mean score, token spend, cache hits, error lines — never the question or
    answer bodies (so state stays free of your content)."""

    def __init__(self, state_dir: str):
        self.path = os.path.join(state_dir, "runs.jsonl")
        os.makedirs(state_dir, exist_ok=True)

    def add(self, rec: dict) -> None:
        rec.setdefault("ts", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
        try:
            with open(self.path, "a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            os.chmod(self.path, 0o600)
        except OSError:
            pass

    def read(self) -> list[dict]:
        if not os.path.isfile(self.path):
            return []
        out = []
        for line in open(self.path, encoding="utf-8"):
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except Exception:
                    continue
        return out


# --------------------------------------------------------------------------
# Calibration (self-improvement): a small frozen question set re-scored
# periodically so the choir learns which voices are accurate, and the results
# adapt routing/voting weights (a cheap offline eval loop — no fine-tuning).
# --------------------------------------------------------------------------
CALIBRATION_QUESTIONS = [
    ("What is the capital of France?", "paris"),
    ("What is 7 times 6?", "42"),
    ("Write 1/8 as a decimal.", "0.125"),
    ("What planet is known as the Red Planet?", "mars"),
    ("What does the Python expression len('hello') evaluate to?", "5"),
    ("A train leaves at 09:15 and arrives at 11:45. How many minutes did the "
     "journey take?", "150"),
    ("What is the chemical symbol for gold?", "au"),
    ("Is 2024 a leap year? Answer yes or no.", "yes"),
]


def score_calibration(answer: str, gold: str) -> bool:
    """True when a calibration answer matches the gold (normalized tokens,
    either direction — fuzzy enough for fact/short-answer questions)."""
    a = normalize_answer(answer)
    g = normalize_answer(gold)
    if not a or not g:
        return False
    return a == g or g in a or a in g


class Calibration:
    """Per-voice accuracy store (state/calibration.json, chmod 600). Keyed by
    the same provider#k<idx> label as the fleet store so report can join."""

    def __init__(self, state_dir: str):
        self.path = os.path.join(state_dir, "calibration.json")
        self.data: dict[str, dict] = {}
        if os.path.isfile(self.path):
            try:
                self.data = json.load(open(self.path, encoding="utf-8"))
            except Exception:
                self.data = {}

    def record(self, provider: str, kid: int, correct: int, n: int) -> dict:
        key = Fleet.vid(provider, kid)
        old = self.data.get(key, {})
        old_n = old.get("n", 0)
        total_n = old_n + n
        total_c = old.get("correct", 0) + correct
        rec = {"acc": round(total_c / total_n, 3) if total_n else 0.0,
               "correct": total_c, "n": total_n,
               "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        self.data[key] = rec
        self.save()
        return rec

    def save(self) -> None:
        _write_private(self.path, self.data, indent=1)

    def for_voice(self, provider: str, kid: int) -> dict:
        return self.data.get(Fleet.vid(provider, kid), {})


def voice_weight(ledger: "Ledger", calibration: Calibration | None,
                 member: dict) -> float:
    """Vote/routing weight for a voice: calibration accuracy (when >=2 scored
    questions) > reward-ledger EWMA (when judged before) > 1.0. Accuracy is
    bounded to [0.2, 3.0] so a single strong voice cannot dominate plurality,
    and honest-but-weak voices still count."""
    if calibration:
        cal = calibration.for_voice(member["provider"], member["kid"])
        if cal.get("n", 0) >= 2 and cal.get("acc") is not None:
            return max(0.2, min(3.0, cal["acc"]))
    if ledger:
        rec = ledger.data.get(ledger.key(member), {})
        if rec.get("uses", 0) > 0 and rec.get("ewma") is not None:
            return max(0.1, rec["ewma"] / 10.0)
    return 1.0


# --------------------------------------------------------------------------
# HTTP / model calls (parallel, never aborted mid-flight)
# --------------------------------------------------------------------------
class ProviderError(Exception):
    pass


def _http_json(url: str, headers: dict, payload: dict, timeout: float) -> dict:
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"),
                                 headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")[:300]
        raise ProviderError(f"HTTP {e.code}: {body}") from None
    except urllib.error.URLError as e:
        raise ProviderError(f"network: {e.reason}") from None


def _api_kw(kw: dict) -> dict:
    """Forward only the api call kwargs (drop CLI-only keys like json)."""
    return {k: v for k, v in kw.items() if k in ("timeout", "max_tokens")}


_FLEET_LOCK = threading.Lock()
# Per-run accounting: {(provider, kid): {"in":int,"out":int,"cached":int,
# "ms":float,"n":int}}. Populated inside the _call_* helpers from each
# provider's own usage report. Providers differ in shape:
#   openai:  usage.prompt_tokens / completion_tokens /
#            usage.prompt_tokens_details.cached_tokens
#   gemini:  usageMetadata.promptTokenCount / candidatesTokenCount /
#            cachedContentTokenCount
#   anthropic-style: usage.input_tokens / output_tokens /
#            cache_read_input_tokens / cache_creation_input_tokens
# Flushed into the fleet state at the end of a command so budgets and
# reports work without printing prompts. Budget/net spend excludes cached
# reads (cache-read tokens are billed at ~10-50% and are the point of
# prompt caching, so a repeat session prefix must not eat the budget).
_RUN_USAGE: dict[tuple[str, int], dict[str, int]] = {}


def _split_usage(data: dict) -> dict | None:
    """Pull (input, output, cached_read) token counts out of ANY provider's
    usage report. Returns None when nothing parseable is present. Unit-tested
    offline with per-provider fixture shapes (selftest)."""
    if not isinstance(data, dict):
        return None
    usage = data.get("usage")
    if isinstance(usage, dict):
        pin = usage.get("prompt_tokens")
        pout = usage.get("completion_tokens")
        if isinstance(pin, int) and isinstance(pout, int):
            cached = 0
            det = usage.get("prompt_tokens_details")
            if isinstance(det, dict) and isinstance(det.get("cached_tokens"), int):
                cached = det["cached_tokens"]
            return {"in": pin, "out": pout, "cached": cached}
        iin = usage.get("input_tokens")
        oout = usage.get("output_tokens")
        if isinstance(iin, int) and isinstance(oout, int):
            cached = (usage.get("cache_read_input_tokens")
                      or usage.get("cache_creation_input_tokens") or 0)
            if not isinstance(cached, int):
                cached = 0
            return {"in": iin, "out": oout, "cached": cached}
    um = data.get("usageMetadata")
    if isinstance(um, dict):
        pin = um.get("promptTokenCount")
        pout = um.get("candidatesTokenCount")
        if isinstance(pin, int) and isinstance(pout, int):
            cached = um.get("cachedContentTokenCount") or 0
            if not isinstance(cached, int):
                cached = 0
            return {"in": pin, "out": pout, "cached": cached}
    # last resort: a single total (counted as output for backwards compat)
    if isinstance(usage, dict) and isinstance(usage.get("total_tokens"), int):
        return {"in": 0, "out": usage["total_tokens"], "cached": 0}
    return None


def _note_usage(provider: str, kid: int, data: dict, ms: float = 0.0) -> None:
    try:
        u = _split_usage(data)
        if not u:
            return
        with _FLEET_LOCK:
            rec = _RUN_USAGE.setdefault(
                (provider, kid), {"in": 0, "out": 0, "cached": 0,
                                  "ms": 0.0, "n": 0})
            rec["in"] = rec.get("in", 0) + u["in"]
            rec["out"] = rec.get("out", 0) + u["out"]
            rec["cached"] = rec.get("cached", 0) + u["cached"]
            rec["ms"] = rec.get("ms", 0.0) + ms
            rec["n"] = rec.get("n", 0) + 1
    except Exception:
        pass


def run_tokens_spent() -> int:
    """Net tokens consumed this run: outputs + freshly-processed inputs
    (cache-read inputs are excluded — they are billed at a large discount)."""
    with _FLEET_LOCK:
        total = 0
        for r in _RUN_USAGE.values():
            fresh_in = max(0, r.get("in", 0) - r.get("cached", 0))
            total += r.get("out", 0) + fresh_in
        return total


def run_usage_rows() -> list[tuple[str, int, dict]]:
    """Snapshot of this run's accounting (for provenance/latency)."""
    with _FLEET_LOCK:
        return [((p, k), dict(r)) for (p, k), r in _RUN_USAGE.items()]


def flush_run_usage(fleet: "Fleet") -> None:
    """Fold this run's accounting into the persistent fleet state."""
    with _FLEET_LOCK:
        items = list(_RUN_USAGE.items())
        _RUN_USAGE.clear()
    for (provider, kid), rec in items:
        if not fleet:
            continue
        net = rec.get("out", 0) + max(0, rec.get("in", 0) - rec.get("cached", 0))
        fleet.add_tokens(provider, kid, net, cached=rec.get("cached", 0))
        n = rec.get("n", 0)
        if n:
            fleet.note_call(provider, kid, ms=rec.get("ms", 0.0) / n)


def call(m: dict, prompt: str, system: str = "", max_tokens: int = 2000,
         timeout: float = 90.0, image_path: str | None = None,
         fleet: Fleet | None = None) -> str:
    """One call to one voice (provider+key). Records health in the fleet store
    so per-key failover is learned, and retries a single 429 once (backoff)."""
    try:
        if m["kind"] == "gemini":
            text = _call_gemini(m, prompt, system, max_tokens, timeout, image_path)
        else:
            text = _call_openai(m, prompt, system, max_tokens, timeout, image_path)
        if fleet:
            with _FLEET_LOCK:
                fleet.record(m["provider"], m["kid"], ok=True)
        return text
    except ProviderError as e:
        if fleet:
            with _FLEET_LOCK:
                fleet.record(m["provider"], m["kid"], ok=False, err=str(e))
        raise


def _image_data_uri(path: str) -> tuple[str, str]:
    mime = mimetypes.guess_type(path)[0] or "image/png"
    b64 = base64.b64encode(open(path, "rb").read()).decode("ascii")
    return mime, b64


def _call_openai(m, prompt, system, max_tokens, timeout, image_path):
    base = m["base"] or DEFAULT_BASE.get(m["provider"], "")
    url = base.rstrip("/") + "/chat/completions"
    headers = {"Authorization": "Bearer " + m["key"],
               "Content-Type": "application/json",
               "User-Agent": f"sith-choir/{VERSION}"}
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    if image_path:
        mime, b64 = _image_data_uri(image_path)
        messages.append({"role": "user", "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url",
             "image_url": {"url": f"data:{mime};base64,{b64}"}}]})
    else:
        messages.append({"role": "user", "content": prompt})
    body = {"model": m["model"], "messages": messages,
            "max_tokens": max_tokens, "temperature": 0.4}
    for attempt in (1, 2):
        try:
            t0 = time.monotonic()
            data = _http_json(url, headers, body, timeout)
            _note_usage(m["provider"], m["kid"], data,
                        (time.monotonic() - t0) * 1000.0)
            content = data.get("choices", [{}])[0].get("message", {}).get("content")
            if not content or not str(content).strip():
                raise ProviderError("empty completion")
            return str(content)
        except ProviderError as e:
            if attempt == 1 and "HTTP 429" in str(e):
                time.sleep(1.2)
                continue
            raise


def _call_gemini(m, prompt, system, max_tokens, timeout, image_path):
    base = m["base"] or DEFAULT_BASE.get(m["provider"], "")
    mdl = m["model"]
    url = f"{base.rstrip('/')}/models/{mdl}:generateContent"
    headers = {"X-goog-api-key": m["key"], "Content-Type": "application/json"}
    parts = []
    if image_path:
        mime, b64 = _image_data_uri(image_path)
        parts.append({"inline_data": {"mime_type": mime, "data": b64}})
    parts.append({"text": prompt})
    body = {"contents": [{"parts": parts}]}
    if system:
        body["systemInstruction"] = {"parts": [{"text": system}]}
    body["generationConfig"] = {"maxOutputTokens": max_tokens,
                                "temperature": 0.4}
    for attempt in (1, 2):
        try:
            t0 = time.monotonic()
            data = _http_json(url, headers, body, timeout)
            _note_usage(m["provider"], m["kid"], data,
                        (time.monotonic() - t0) * 1000.0)
            text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
            if not text or not str(text).strip():
                raise ProviderError("empty completion")
            return str(text)
        except ProviderError as e:
            if attempt == 1 and "HTTP 429" in str(e):
                time.sleep(1.2)
                continue
            raise


def call_failover(m: dict, prompt: str, system: str = "", max_tokens: int = 2000,
                  timeout: float = 90.0, image_path: str | None = None,
                  fleet: Fleet | None = None,
                  provider_obj: dict | None = None,
                  attempts: int = 3) -> tuple[str, dict]:
    """Call a voice with per-key failover across its provider's keys: if one
    key is throttled/bad we try the next stored key, up to `attempts` tries.
    Attempts are bounded so a rate-limited provider (e.g. 17 mistral keys on a
    shared quota) cannot burn minutes; cooldowns then rotate to fresh keys on
    the next call."""
    nkeys = len(provider_obj["keys"]) if provider_obj else 1
    tries = max(1, min(attempts, nkeys))
    tried: list[int] = []
    kid_start = m["kid"]
    for _ in range(tries):
        order = fleet.usable(m["provider"], nkeys) if fleet else list(range(1, nkeys + 1))
        if not order:
            order = list(range(1, nkeys + 1))
        kid = next((k for k in order if k not in tried), None)
        if kid is None:
            kid = kid_start
        tried.append(kid)
        voice = dict(m)
        voice["kid"] = kid
        if provider_obj:
            voice["key"] = provider_obj["keys"][kid - 1]
        try:
            text = call(voice, prompt, system, max_tokens, timeout,
                        image_path, fleet=fleet)
            return text, voice
        except ProviderError:
            if len(tried) >= tries:
                raise
    raise ProviderError("no keys left to try")  # pragma: no cover


def parallel_calls(tasks: list[tuple], fleet: Fleet | None = None) -> list[dict]:
    """tasks: (member, prompt, system[, image_path[, max_tokens]]). Run all in
    parallel, join all, never abort mid-flight. max_tokens lets micro-tasks
    (judges, votes, verifiers) carry a tight per-call output cap so they stay
    cheap and fast."""
    results = [None] * len(tasks)

    def run(i, m, prompt, system, image_path, cap):
        try:
            results[i] = {"member": m, "ok": True,
                          "text": call(m, prompt, system,
                                       max_tokens=cap or 2000,
                                       image_path=image_path, fleet=fleet)}
        except Exception as e:
            results[i] = {"member": m, "ok": False, "error": str(e)[:200]}

    normed = [t if len(t) == 5 else t + (None,) * (5 - len(t))
              for t in tasks]
    threads = [threading.Thread(target=run, args=(i, m, p, s, ip, cap),
                                daemon=True)
               for i, (m, p, s, ip, cap) in enumerate(normed)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return results


# --------------------------------------------------------------------------
# Orchestration primitives (the Sith's moves)
# --------------------------------------------------------------------------
PROPOSER_SYS = ("You are one independent member of a choir of AI models "
                "answering the user's question. Be correct, concise and "
                "honest. Never fabricate: if you cannot determine the answer, "
                "say UNKNOWN instead of guessing. Do not invent citations, "
                "numbers, URLs or API names. Do not claim you can see images "
                "unless you truly can.")
AGGREGATOR_SYS = ("You are the lead model merging candidate answers produced "
                  "by several other AI models. Produce the single best, most "
                  "correct, most complete final answer. Keep the strongest "
                  "parts, drop wrong parts, and resolve contradictions. Do "
                  "NOT invent details: if candidates disagree about a fact, "
                  "attribute the claim to the candidate that made it rather "
                  "than asserting it as new truth. If the candidates cannot "
                  "answer, answer UNKNOWN. Be concise.")
JUDGE_SYS = ("You are a strict independent judge on a review panel. Grade the "
             "ANSWER for the QUESTION on correctness, faithfulness, "
             "completeness and clarity from 0 to 10. Never reward length or "
             "order; punish invented or unsupported claims. If the answer "
             "says UNKNOWN, score the honesty (do not punish a refusal). "
             "Reply with exactly one line: SCORE: <0-10> then a short REASON "
             "line naming the single biggest flaw if score <= 7.")
CONSENSUS_SYS = PROPOSER_SYS + (
    " End with exactly one final line: ANSWER: <your concise final answer>. "
    "If you cannot determine the answer, end with exactly: ANSWER: UNKNOWN "
    "(an honest abstention beats a confident guess).")
REVISOR_SYS = AGGREGATOR_SYS + (
    " You receive critiques of a previous draft. Produce a REVISED final "
    "answer fixing every concrete point raised while keeping what was "
    "correct. Never remove a correct part just to satisfy a critique; never "
    "add unverifiable detail to look more complete.")
VERIFIER_SYS = ("You are an independent adversarial verifier. Check the "
                "ANSWER against the QUESTION for factual errors, "
                "hallucinated claims, non-sequiturs and unsupported detail. "
                "Do not guess about facts: if a claim cannot be checked from "
                "the answer itself or general knowledge, flag it as "
                "unverifiable rather than confirming it. Reply with exactly "
                "one line: VERDICT: PASS | FAIL | PARTIAL then a numbered "
                "list of the specific flaws you found (or one line saying "
                "no flaws).")
ARBITER_SYS = ("You are the final arbiter in a disagreement between AI "
               "models. Two answer groups conflict. Choose the one that is "
               "more correct, better grounded and more faithful to the "
               "question. If both are wrong or you cannot tell, say "
               "ANSWER: UNKNOWN. Reply with exactly one line: "
               "ANSWER: <your chosen answer or UNKNOWN>, then one short "
               "reason line.")


def resolve_label(roster: Roster, label: str) -> dict:
    """Resolve a voice label like 'gemini#k1/gemini-3.1-flash-lite' back to a
    live voice object."""
    prov_k, _, model = label.partition("/")
    prov, _, ks = prov_k.partition("#")
    kid = None
    if ks and ks.lower().startswith("k") and ks[1:].isdigit():
        kid = int(ks[1:])
    return roster.member_key(prov, model or None, kid)


def _parse_score(text: str) -> float | None:
    m = re.search(r"SCORE\s*[:=]\s*(\d{1,2}(?:\.\d+)?)", text or "", re.I)
    if not m:
        return None
    try:
        s = float(m.group(1))
        return s if 0 <= s <= 10 else None
    except ValueError:
        return None


def _parse_conf(text: str) -> float | None:
    m = CONF_RE.search(text or "")
    if not m:
        return None
    raw = m.group(1).strip()
    try:
        if raw.endswith("%"):
            return float(raw[:-1]) / 100.0
        return float(raw)
    except ValueError:
        return None


def parse_src(src: str) -> tuple[str, str | None, int | None]:
    """Parse --from "provider[/model[#k<idx>]]" -> (provider, model, kid)."""
    prov, sep, rest = src.partition("/")
    if not sep:
        return prov, None, None
    model, _, ks = rest.partition("#")
    kid = None
    if ks and ks.lower().startswith("k") and ks[1:].isdigit():
        kid = int(ks[1:])
    return prov, model or None, kid


def vlabel(m: dict) -> str:
    """Human label for a voice: provider#k<kid>/model"""
    return f"{m['provider']}#k{m['kid']}/{m['model']}"


# -- structured answer extraction (consensus / machine-consumable outputs) ---
ANSWER_RE = re.compile(r"(?:^|\n)\s*ANSWER\s*[:=]\s*(.+)$", re.M | re.I)


def extract_final_answer(text: str) -> str:
    """Pull the model's concise final answer from the trailing `ANSWER: ...`
    line. Returns the raw text if no tag is present (lenient)."""
    matches = ANSWER_RE.findall(text or "")
    if not matches:
        return (text or "").strip()
    return matches[-1].strip()


def normalize_answer(s: str) -> str:
    """Normalize an answer for vote equality (case, punctuation, spaces)."""
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()

_ABSTAIN_PHRASES = {
    "unknown", "unsure", "not sure", "not certain", "don't know", "dont know",
    "do not know", "cannot determine", "can't determine", "cannot answer",
    "can't answer", "unable to answer", "no idea", "no answer", "abstain",
    "i don't know", "i do not know", "i am not sure", "i'm not sure",
    "i am unsure", "cannot tell", "can't tell", "n/a", "na",
}


def is_abstention(text: str) -> bool:
    """True when a model explicitly abstained instead of guessing. Matches:
    (1) the full normalized answer equals an abstention phrase; (2) the answer
    starts with an unambiguous dodge phrase ("i don't know", "not sure",
    "cannot determine", ...) followed by a short clause (<= 3 words); or (3) it begins with
    a bare single-token dodge ("unknown", "unsure") and is only a few words
    long. Real answers that merely contain the word 'unknown' (e.g. "unknown
    kingdom of fungi") are NOT treated as abstentions."""
    norm = normalize_answer(text)
    if not norm:
        return True  # empty ballot
    if norm in _ABSTAIN_PHRASES:
        return True
    words = norm.split()
    if words[0] in ("unknown", "unsure", "abstain", "na") and len(words) <= 3:
        return True
    for ph in ("i don t know", "i do not know", "i m not sure", "i am not sure",
               "not sure", "not certain", "do not know", "dont know",
               "don t know", "cannot determine", "can t determine",
               "cannot answer", "can t answer", "unable to answer",
               "cannot say", "can t say", "no idea", "cannot tell",
               "can t tell"):
        if norm.startswith(ph):
            tail = norm[len(ph):].strip()
            return len(tail.split()) <= 3
    return False


def _crop(text: str, n: int = 2400) -> str:
    """Cap a candidate block for the aggregator input: shorter prefill = less
    TTFT + fewer input tokens. Adds a marker when trimmed."""
    t = (text or "").strip()
    if len(t) <= n:
        return t
    return t[:n].rstrip() + "\n\u2026[trimmed by sith-choir]"


def _parse_verdict(text: str) -> str | None:
    m = re.search(r"VERDICT\s*[:=]\s*(PASS|FAIL|PARTIAL)", text or "", re.I)
    return m.group(1).upper() if m else None


def plurality_vote(votes: list[dict], weights: list[float]) -> dict:
    """Weighted plurality vote over `votes` = [{member, answer}].
    weights parallel to votes; default weight 1.0. Returns the winning answer,
    its label list, tally and the tally of the runner-up (consensus strength).
    This is confidence-weighted majority voting, the Self-Consistency
    (arXiv:2203.11171) + CISC (arXiv:2502.06233) selection rule."""
    buckets: dict[str, dict] = {}
    for vote, w in zip(votes, weights):
        a = vote["answer"] or ""
        norm = normalize_answer(a)
        if not norm:
            norm = "<empty>"
        b = buckets.setdefault(norm, {"label": a, "weight": 0.0, "votes": 0,
                                      "members": []})
        b["weight"] += w
        b["votes"] += 1
        b["members"].append(vote["member"])
    ranked = sorted(buckets.values(), key=lambda b: (-b["weight"], -b["votes"]))
    win = ranked[0]
    tally = [{"answer": b["label"], "votes": b["votes"],
              "weight": round(b["weight"], 3), "members": b["members"]}
             for b in ranked]
    return {"answer": win["label"], "tally": tally, "votes": win["votes"],
            "weight": round(win["weight"], 3),
            "members": win["members"]}


def judge_critiques(judged: dict) -> str:
    """Turn judge notes into critique bullets a revisor can act on."""
    parts = []
    for j in judged.get("judges", []):
        note = (j.get("note") or "").strip()
        if note:
            score = j.get("score")
            line = (f"- {j.get('member')} "
                    f"({score if score is not None else 'n/a'}/10): "
                    f"{note.splitlines()[-1][:300]}")
            parts.append(line)
    return "\n".join(parts)


def cmd_list(roster: Roster, ledger: Ledger, json: bool = False) -> None:
    rows = []
    for v in roster.members():
        rec = ledger.data.get(ledger.key(v), {})
        nk = roster.voice_count(v["provider"])
        good = sum(1 for i in range(1, nk + 1)
                   if roster.fleet.cooled(v["provider"], i) == 0) if nk else 0
        rows.append({"provider": v["provider"], "model": v["model"],
                     "keys_healthy": good, "keys_total": nk,
                     "tags": sorted(v["tags"]) or ["general"],
                     "ledger_ewma": rec.get("ewma"),
                     "ledger_uses": rec.get("uses", 0)})
    if json:
        print(json_mod.dumps(rows, indent=2, ensure_ascii=False))
        return
    for r in rows:
        print(f"{r['provider']:12s} {r['model']:40s} "
              f"keys={r['keys_healthy']}/{r['keys_total']}  "
              f"tags={','.join(r['tags']):22s} "
              f"ledger={r['ledger_ewma'] if r['ledger_ewma'] is not None else '-'} "
              f"(uses={r['ledger_uses']})")
    print(f"\n{len(rows)} provider voice(s) · "
          f"{len(roster.all_voices())} API keys · state: {roster.fleet.state_dir}")


def cmd_fleet(roster: Roster, json: bool = False) -> None:
    rows = []
    for name in roster.providers:
        p = roster.providers[name]
        if p["note"]:
            rows.append({"provider": name, "model": p["model"] or "-",
                         "note": p["note"], "keys": []})
            continue
        voices = roster.voices_for(name)
        keys = []
        for v in voices:
            fr = roster.fleet.rec(v["provider"], v["kid"])
            cool = roster.fleet.cooled(v["provider"], v["kid"])
            keys.append({"kid": v["kid"], "model": v["model"],
                         "health": "cool" if cool > 0 else "ok",
                         "cool_seconds": int(cool),
                         "ok": fr.get("ok", 0), "fail": fr.get("fail", 0),
                         "tokens": fr.get("tokens", 0),
                         "avg_ms": fr.get("ms"),
                         "last_error": fr.get("last", "")})
        rows.append({"provider": name, "model": p["model"], "keys": keys})
    if json:
        print(json_mod.dumps(rows, indent=2, ensure_ascii=False))
        return
    for r in rows:
        if r.get("note"):
            print(f"{r['provider']:14s} {r['model']:40s} {r['note']}")
            continue
        print(f"{r['provider']:14s} model={r['model']:38s} "
              f"voices={len(r['keys'])}")
        for k in r["keys"]:
            err = f" last={k['last_error'][:44]}" if k["last_error"] else ""
            print(f"    k{k['kid']}  {k['health'].upper():12s} "
                  f"ok={k['ok']:3d} fail={k['fail']:3d} "
                  f"tokens={k['tokens']:7d}{err}")
    print(f"\n{len(roster.providers)} provider(s) · "
          f"{len(roster.all_voices())} stored keys "
          f"(state dir {roster.fleet.state_dir})")


def cmd_ask(roster: Roster, q: str, src: str, **kw) -> dict:
    fleet = roster.fleet
    cache: AnswerCache | None = kw.get("_cache")
    session: str | None = kw.get("_session")
    sess: Sessions | None = kw.get("_sessions")
    lane: str = kw.get("lane", "")
    LANES = {"general": None, "fast": {"fast"}, "reasoning": {"reasoning"},
             "longctx": {"longctx"}, "code": {"reasoning"}}
    if lane:
        if lane not in LANES:
            raise SystemExit(f"unknown --lane '{lane}' "
                             f"(general|code|reasoning|fast|longctx)")
        want = LANES[lane]
        pool = (roster.pick(want=want, n=5) if want else roster.members())
        pool = pool or roster.pick(n=1)
    elif src:
        prov, model, kid = parse_src(src)
        pool = [roster.member_key(prov, model, kid)]
    else:
        pool = roster.pick(n=1)
    m = pool[0]
    ctx = sess.context(session) if (sess and session) else ""
    question = session_wrap(ctx, q)
    # cache (exact-question dedupe) unless disabled
    if cache and not kw.get("no_cache"):
        hit = cache.get(question)
        if hit:
            out = {"member": hit.get("member", "cache"),
                   "answer": hit["answer"], "cache": True}
            if kw.get("json"):
                print(json_mod.dumps(out, indent=2, ensure_ascii=False))
            else:
                print(f"── {out['member']} (cached) ──\n{out['answer']}")
            return out
    try:
        text, used = call_failover(
            m, question, system=PROPOSER_SYS,
            max_tokens=kw.get("max_tokens", 2000),
            timeout=kw.get("timeout", 90.0), fleet=fleet,
            provider_obj=roster.providers.get(m["provider"]))
    except ProviderError as e:
        raise SystemExit(f"all {roster.voice_count(m['provider'])} keys of "
                         f"{m['provider']} failed: {e}") from None
    if cache and not kw.get("no_cache"):
        cache.put(question, text, vlabel(used))
    if sess and session:
        sess.append(session, q, text, vlabel(used))
    verify_out = None
    if kw.get("verify"):
        try:
            verify_out = cmd_verify(roster, q, text, quiet=True,
                                    json=False,
                                    _author_provider=used["provider"])
        except SystemExit:
            verify_out = {"verdict": "UNVERIFIED", "error": True}
    out = {"member": vlabel(used), "answer": text, "cache": False,
           "verify": verify_out}
    if kw.get("json"):
        print(json_mod.dumps(out, indent=2, ensure_ascii=False))
    else:
        print(f"── {vlabel(used)} ──\n{text}")
        if verify_out and not verify_out.get("error"):
            print(f"── verified: {verify_out.get('verdict')} ──")
        elif verify_out:
            print("── verify stage failed (answer returned unverified) ──")
    return out


def cmd_moa(roster: Roster, q: str, n_proposers: int, quiet: bool = False,
            aggregator: str = "", **kw) -> dict:
    """Weak/cheap choir proposes in parallel; best reasoning model aggregates.
    The proposers are drawn from DISTINCT providers (and each of their
    healthiest keys) so one account's quota cannot gate the choir."""
    props = roster.pick(want={"fast"}, exclude={"reasoning"}, n=n_proposers)
    if len(props) < n_proposers:
        extra = roster.pick(exclude={"reasoning"}, n=n_proposers * 2)
        props = extra[:n_proposers] if len(extra) >= n_proposers else extra
    if not props:
        props = roster.pick(n=n_proposers)
    if aggregator:
        prov, _, _ = parse_src(aggregator)
        ag = roster.voice(prov)
        if not ag:
            raise SystemExit(f"--aggregator provider '{prov}' not callable")
        agg = [ag]
    else:
        agg = roster.pick(want={"reasoning"}, n=1)
        if not agg:
            agg = roster.pick(n=1)
    tasks = [(m, q, PROPOSER_SYS) for m in props]
    res = parallel_calls(tasks, fleet=roster.fleet)
    candidates = [r["text"] for r in res if r["ok"]]
    if not candidates:
        errs = "\n".join(f"  {vlabel(r['member'])}: {r['error']}"
                         for r in res if not r['ok'])
        raise SystemExit("all proposers failed:\n" + errs)
    budget = kw.get("_budget")
    if budget and run_tokens_spent() > budget:
        raise SystemExit(f"[budget] {run_tokens_spent()} tokens already spent "
                         f"(> --budget {budget}); stopping before the "
                         f"aggregator stage.")
    block = "\n\n".join(f"--- candidate from {vlabel(r['member'])} ---\n"
                        f"{_crop(r['text'], 2200)}" for r in res if r["ok"])
    prompt = (f"QUESTION: {q}\n\nBelow are candidate answers from several "
              f"models.\n{block}\n\nProduce the best final answer.")
    agg_m = agg[0]
    final = call(agg_m, prompt, system=AGGREGATOR_SYS,
                 max_tokens=kw.get("max_tokens", 2000),
                 timeout=kw.get("timeout", 90.0), fleet=roster.fleet)
    out = {"aggregator": vlabel(agg_m),
           "proposers": [vlabel(m) for m in props],
           "answer": final}
    if not quiet:
        if kw.get("json"):
            print(json_mod.dumps(out, indent=2, ensure_ascii=False))
        else:
            print(f"═══ {vlabel(agg_m)} (aggregated {len(candidates)} "
                  f"proposals from {len(set(p['provider'] for p in props))} "
                  f"provider(s)) ═══\n{final}")
    return out


def cmd_vision(roster: Roster, image: str, q: str, synth: bool, **kw) -> dict:
    """A caller/model that cannot see the image asks vision-capable voices to
    perform the job (arXiv:2502.16428: vision ability is vendor-specific).
    Optional second pass: a text reasoning model synthesizes the reports."""
    seers = roster.pick(want={"vision"}, n=3)
    if not seers:
        raise SystemExit("no vision-capable member configured. Add one whose "
                         "model supports image input and tag it 'vision'.")
    tasks = [(m, q, "You have been handed an image to perform the job on. "
                    "Describe/OCR/answer precisely from the image.", image)
             for m in seers]
    res = parallel_calls(tasks, fleet=roster.fleet)
    reports = [r for r in res if r["ok"]]
    if not reports:
        errs = "\n".join(f"  {vlabel(r['member'])}: {r['error']}"
                         for r in res if not r['ok'])
        raise SystemExit("all vision members failed (endpoint may not accept "
                         f"images):\n{errs}")
    final = None
    if synth:
        budget = kw.get("_budget")
        if budget and run_tokens_spent() > budget:
            raise SystemExit(f"[budget] {run_tokens_spent()} tokens spent "
                             f"(> --budget {budget}); stopping before the "
                             f"synthesis stage.")
        thinker = roster.pick(want={"reasoning"}, n=1) or roster.pick(n=1)
        block = "\n\n".join(f"--- {vlabel(r['member'])} (vision) ---\n"
                            f"{_crop(r['text'], 2000)}" for r in reports)
        t0 = thinker[0]
        final = call(t0, f"QUESTION: {q}\n\nVisual reports from vision models:\n"
                     f"{block}\n\nSynthesize the most accurate final answer.",
                     system=AGGREGATOR_SYS, max_tokens=kw.get("max_tokens", 2000),
                     timeout=kw.get("timeout", 90.0), fleet=roster.fleet)
    out = {"image": image,
           "seers": [vlabel(r["member"]) for r in reports],
           "reports": [r["text"] for r in reports],
           "synthesized": final,
           "failed": [f"{vlabel(r['member'])}: {r['error']}"
                      for r in res if not r["ok"]]}
    if kw.get("json"):
        print(json_mod.dumps(out, indent=2, ensure_ascii=False))
    else:
        for r in reports:
            print(f"═══ {vlabel(r['member'])} ═══\n{r['text']}\n")
        if synth:
            print(f"═══ synthesized by {vlabel(thinker[0])} ═══\n{final}")
    return out


def cmd_escalate(roster: Roster, q: str, src: str, force: bool,
                 require_conf: bool, helpmates: str, **kw) -> dict:
    """Primary answers; if confidence is low (or --force), it is MANDATORY to
    ask the best reasoning models — drawn across OTHER providers' keys
    (--helpmates) so a primary on one provider is helped by other providers."""
    fleet = roster.fleet
    if src:
        prov, model, kid = parse_src(src)
        primary_m = roster.member_key(prov, model, kid)
    else:
        fast_pool = roster.pick(want={"fast"}, n=1)
        primary_m = (fast_pool or roster.pick(n=1))[0]
    inst = (PROPOSER_SYS + " End your answer with one line: "
            "CONF: <0.0-1.0> estimating how confident you are in the answer.")
    try:
        first, used = call_failover(
            primary_m, q, system=inst, max_tokens=kw.get("max_tokens", 2000),
            timeout=kw.get("timeout", 90.0), fleet=fleet,
            provider_obj=roster.providers.get(primary_m["provider"]))
        primary_m = used
    except ProviderError as e:
        first, force = "", True
        print(f"[escalate] all keys of {primary_m['provider']} failed ({e}); "
              f"escalating to the reasoning court.", file=sys.stderr)
    conf = _parse_conf(first) if first else None
    escalate = (force or conf is None and require_conf or
                conf is not None and conf < 0.7)
    if not escalate:
        out = {"member": vlabel(primary_m),
               "answer": first, "confidence": conf, "escalated": False}
        if kw.get("json"):
            print(json_mod.dumps(out, indent=2, ensure_ascii=False))
        else:
            print(f"── {vlabel(primary_m)} (CONF={conf}) ──\n{first}")
        return out
    # court = explicitly requested helpmate providers first, then top-up with
    # reasoning voices from other providers.
    court: list[dict] = []
    seen: set[str] = {primary_m["provider"]}
    if helpmates:
        for h in helpmates.split(","):
            h = h.strip()
            if not h:
                continue
            v = roster.voice(h)
            if v and h not in seen:
                court.append(v)
                seen.add(h)
    for v in roster.pick(want={"reasoning"}, n=3):
        if v["provider"] not in seen:
            court.append(v)
            seen.add(v["provider"])
    if not court:
        for v in roster.members():
            if v["provider"] not in seen:
                court.append(v)
                seen.add(v["provider"])
    if not court:
        raise SystemExit("no court available: every other provider failed.")
    ccap = max(256, min(kw.get("max_tokens", 2000), 1600))
    tasks = [(m, q, AGGREGATOR_SYS + " Answer the question yourself first, then "
                    "if needed revise.", None, ccap) for m in court]
    res = parallel_calls(tasks, fleet=fleet)
    panel = [r for r in res if r["ok"]]
    if not panel:
        errs = "\n".join(f"  {vlabel(r['member'])}: {r['error']}"
                         for r in res if not r['ok'])
        raise SystemExit("escalation court empty:\n" + errs)
    merged = "\n\n".join(f"--- {vlabel(r['member'])} ---\n{_crop(r['text'], 1800)}"
                         for r in panel)
    lead = panel[0]["member"]
    budget = kw.get("_budget")
    if budget and run_tokens_spent() > budget:
        raise SystemExit(f"[budget] {run_tokens_spent()} tokens already spent "
                         f"(> --budget {budget}); stopping before the lead "
                         f"synthesis stage.")
    prompt = (f"QUESTION: {q}\n\nReasoning members' answers:\n{merged}\n\n"
              "Produce the single best final answer (MoA synthesis).")
    final = call(lead, prompt, system=AGGREGATOR_SYS,
                 max_tokens=kw.get("max_tokens", 2000),
                 timeout=kw.get("timeout", 90.0), fleet=fleet)
    out = {"escalated": True,
           "primary": vlabel(primary_m),
           "primary_conf": conf,
           "panel": [vlabel(r["member"]) for r in panel],
           "lead": vlabel(lead),
           "answer": final}
    if kw.get("json"):
        print(json_mod.dumps(out, indent=2, ensure_ascii=False))
    else:
        print(f"🔺 escalated (conf={conf}; court of {len(panel)} from "
              f"{sorted(set(p['member']['provider'] for p in panel))})\n"
              f"═══ {vlabel(lead)} ═══\n{final}")
    return out


def cmd_judge(roster: Roster, q: str, answer: str,
              members: list[str] | None = None, quiet: bool = False,
              **kw) -> dict:
    """Judge panel rewards good answers / punishes bad ones and updates the
    ledger. Uses several independent judges from different providers and takes
    the mean (LLM-as-a-Judge with bias mitigation: the answer's own provider is
    excluded so no model grades its own work)."""
    author_prov = (kw.get("_author_provider") or "").lower()
    if members:
        judges: list[dict] = []
        for mm in members:
            prov, model, kid = parse_src(mm)
            judges.append(roster.member_key(prov, model, kid))
    else:
        judges = roster.pick(want={"reasoning"}, n=3)
        if not judges:
            judges = roster.pick(n=3)
        if author_prov:
            others = [v for v in judges if v["provider"] != author_prov]
            if others:
                judges = others
    block = f"QUESTION: {q}\n\nANSWER:\n{_crop(answer, 4000)}"
    jcap = max(256, min(kw.get("max_tokens", 2000), 700))
    res = parallel_calls([(m, block, JUDGE_SYS, None, jcap) for m in judges],
                         fleet=roster.fleet)
    scored = []
    for r in res:
        if not r["ok"]:
            continue
        s = _parse_score(r["text"])
        scored.append({"member": vlabel(r["member"]),
                       "score": s, "note": r["text"][:400]})
        if s is not None:
            ledger_here = kw.get("_ledger")
            if ledger_here:
                ledger_here.update(r["member"], s)
    if not scored:
        raise SystemExit("judge panel produced no scores.")
    vals = [x["score"] for x in scored if x["score"] is not None]
    mean = round(sum(vals) / len(vals), 2) if vals else None
    out = {"mean_score": mean, "verdict": ("REWARD" if (mean or 0) >= 7.5
                                           else "PUNISH" if (mean or 0) <= 4
                                           else "NEUTRAL"),
           "judges": scored}
    if not quiet:
        if kw.get("json"):
            print(json_mod.dumps(out, indent=2, ensure_ascii=False))
        else:
            for x in scored:
                print(f"  judge {x['member']}: {x['score']} — "
                      f"{x['note'].splitlines()[-1][:120] if x['note'] else ''}")
            print(f"── verdict: {out['verdict']} (mean {mean}/10) ──")
    return out


def cmd_harvest(roster: Roster, ledger: Ledger, q: str, **kw) -> dict:
    """The full Sith move: weak choir proposes in parallel -> strong model
    aggregates (MoA) -> judge panel rewards/punishes -> ledger updated. The
    judge's author provider is excluded from judging itself."""
    quiet = bool(kw.get("json"))
    api_kw = _api_kw(kw)
    bud = kw.get("_budget")
    res_moa = cmd_moa(roster, q, n_proposers=kw.get("n_proposers", 3),
                      json=False, quiet=quiet,
                      aggregator=kw.get("aggregator", ""),
                      **{**api_kw, "_budget": bud})
    answer = res_moa["answer"]
    author_prov = res_moa["aggregator"].split("#", 1)[0].split("/", 1)[0]
    judged = cmd_judge(roster, q, answer, json=False, quiet=quiet,
                       _ledger=ledger, _author_provider=author_prov, **api_kw)
    out = {"question": q, **res_moa, "verdict": judged["verdict"],
           "mean_score": judged["mean_score"],
           "judges": judged.get("judges", [])}
    if kw.get("json"):
        print(json_mod.dumps(out, indent=2, ensure_ascii=False))
    else:
        print(f"\n🦞 verdict: {judged['verdict']} — the choir sang, the Sith "
              f"harvested ({judged['mean_score']}/10).")
    return out


def cmd_consensus(roster: Roster, ledger: Ledger, q: str, samples: int,
                  **kw) -> dict:
    """Self-consistency: sample several voices on the SAME question, extract
    each voice's concise final `ANSWER:` line, and choose by weighted
    plurality vote. Weights come from each voice's ledger EWMA when it has
    been judged before (confidence-weighted majority — CISC-style), else 1.
    This complements MoA: MoA *synthesizes*, consensus *votes*."""
    n = max(2, samples)
    pool = roster.members()
    if len(pool) < 2:
        raise SystemExit("consensus needs at least 2 distinct providers; "
                         "only %d callable." % len(pool))
    pool = pool[:n]
    scap = max(256, min(kw.get("max_tokens", 2000), 1000))
    tasks = [(m, q, CONSENSUS_SYS, None, scap) for m in pool]
    res = parallel_calls(tasks, fleet=roster.fleet)
    ok = [r for r in res if r["ok"]]
    if len(ok) < 2:
        errs = "\n".join(f"  {vlabel(r['member'])}: {r['error']}"
                         for r in res if not r['ok'])
        raise SystemExit("consensus needs >=2 successful voices:\n" + errs)
    ballots = []
    abstained = []
    weights = []
    for r in ok:
        ans = extract_final_answer(r["text"])
        w = voice_weight(ledger, kw.get("_calibration"), r["member"])
        if is_abstention(ans):
            abstained.append(vlabel(r["member"]))
        else:
            ballots.append({"member": vlabel(r["member"]), "answer": ans})
            weights.append(w)
    votes = ballots
    if not votes:
        raise SystemExit("consensus: every voice abstained (honest UNKNOWN); "
                         "no answer can be asserted. Try a different question "
                         "or `moa`.")
    result = plurality_vote(votes, weights)
    # thin-margin / conflict arbitration: if the top two answer groups are
    # within 1.5 weighted points, a reasoning voice arbitrates (one bounded
    # extra call) instead of returning a coin-flip winner.
    arbiter = None
    if len(result["tally"]) >= 2:
        top1 = result["tally"][0]
        top2 = result["tally"][1]
        if top1["weight"] - top2["weight"] < 1.5:
            arb = roster.pick(want={"reasoning"}, n=1) or roster.pick(n=1)
            if arb:
                prompt = (f"QUESTION: {q}\n\nAnswer group A:\n{top1['answer']}"
                          f"\n\nAnswer group B:\n{top2['answer']}")
                try:
                    txt = call(arb[0], prompt, system=ARBITER_SYS,
                               max_tokens=300, timeout=60.0, fleet=roster.fleet)
                    pick = extract_final_answer(txt)
                    if not is_abstention(pick):
                        norm_pick = normalize_answer(pick)
                        if normalize_answer(top1["answer"]) == norm_pick:
                            result["answer"] = top1["answer"]
                            arbiter = vlabel(arb[0])
                        elif normalize_answer(top2["answer"]) == norm_pick:
                            result["answer"] = top2["answer"]
                            arbiter = vlabel(arb[0])
                except ProviderError:
                    arbiter = None
    out = {"question": q, "samples": len(ok), "voting": len(votes),
           "abstained": abstained, "arbiter": arbiter,
           "voices": [v["member"] for v in ballots],
           "answer": result["answer"], "weight": result["weight"],
           "tally": result["tally"]}
    if kw.get("json"):
        print(json_mod.dumps(out, indent=2, ensure_ascii=False))
    else:
        note = (f", {len(abstained)} abstained" if abstained else "")
        print(f"🗳️ consensus of {len(ok)} voices{note} "
              f"(weighted plurality, score {result['weight']:.2f})\n"
              f"═══ WINNER ═══\n{result['answer']}\n")
        for t in result["tally"]:
            mark = "◀ winner" if t["answer"] == result["answer"] else ""
            print(f"  · {t['votes']} vote(s) weight {t['weight']:<6} "
                  f"[{', '.join(t['members'])}] {mark}")
        if abstained:
            print(f"  (abstained: {', '.join(abstained)})")
        if arbiter:
            print(f"  (arbiter: {arbiter} broke the near-tie)")
    return out


def cmd_refine(roster: Roster, ledger: Ledger, q: str, rounds: int,
               target: float, helpmates: str, **kw) -> dict:
    """Propose -> aggregate -> judge -> (critique -> revise)*, a bounded
    verifier/revision loop (Reflexion arXiv:2303.11366 + adaptive test-time
    compute arXiv:2408.03314). Each round the judges grade the current draft;
    if the mean is below `--target` (default 7.5) and rounds remain, a revisor
    voice rewrites the draft against the judges' critiques and the loop
    repeats. Ledger is updated only by the FINAL judge panel."""
    api_kw = _api_kw(kw)
    budget = kw.get("_budget")
    max_tokens = kw.get("max_tokens", 2000)
    timeout = kw.get("timeout", 90.0)
    fleet = roster.fleet
    # round 0: MoA draft
    cur = cmd_moa(roster, q, n_proposers=kw.get("n_proposers", 3),
                  json=False, quiet=True, aggregator=kw.get("aggregator", ""),
                  **{**api_kw, "_budget": budget})
    author_prov = cur["aggregator"].split("#", 1)[0].split("/", 1)[0]
    trace = []
    answer = cur["answer"]
    lead_label = cur["aggregator"]
    last_judged = None
    n_rounds = max(1, rounds)
    for rnd in range(n_rounds):
        judged = cmd_judge(roster, q, answer, json=False, quiet=True,
                           _author_provider=author_prov, **api_kw)
        last_judged = judged
        mean = judged["mean_score"]
        trace.append({"round": rnd, "mean": mean,
                      "verdict": judged["verdict"]})
        if mean is not None and mean >= target:
            break
        if rnd == n_rounds - 1:
            break
        if budget and run_tokens_spent() > budget:
            raise SystemExit(f"[budget] {run_tokens_spent()} tokens spent "
                             f"(> --budget {budget}); stopping the revision "
                             f"loop.")
        critiques = judge_critiques(judged)
        # revisor: --helpmates provider first, else the aggregator's provider
        rev_prov = ""
        if helpmates:
            rev_prov = helpmates.split(",")[0].strip()
        if not rev_prov:
            rev_prov = author_prov
        revisor = roster.voice(rev_prov) or roster.pick(want={"reasoning"},
                                                        n=1)[0]
        prompt = (f"QUESTION: {q}\n\nPRIOR DRAFT:\n{answer}\n\n"
                  f"JUDGE CRITIQUES:\n{critiques}\n\n"
                  "Produce the revised final answer addressing every critique.")
        answer = call(revisor, prompt, system=REVISOR_SYS,
                      max_tokens=max_tokens, timeout=timeout, fleet=fleet)
        lead_label = vlabel(revisor)
    # ledger updated from the FINAL judge panel (no extra judge call)
    for j in (last_judged or {}).get("judges", []):
        s = j.get("score")
        if s is not None and j.get("member"):
            ledger.update_label(j["member"], s)
    judged = last_judged or {}
    out = {"question": q, "answer": answer, "lead": lead_label,
           "rounds": trace,
           "verdict": judged.get("verdict"), "mean_score": judged.get("mean_score"),
           "judges": judged.get("judges", [])}
    if kw.get("json"):
        print(json_mod.dumps(out, indent=2, ensure_ascii=False))
    else:
        history = " → ".join(f"r{r['round']}:{r['mean']}" for r in trace)
        print(f"🔁 refine rounds [{history}]\n"
              f"═══ {lead_label} (final) ═══\n{answer}\n"
              f"── verdict: {out['verdict']} (mean {out['mean_score']}/10) ──")
    return out


def cmd_verify(roster: Roster, q: str, answer: str,
              verifiers: list[str] | None = None, quiet: bool = False,
              **kw) -> dict:
    """Independent adversarial verifier round (arXiv-backed: external verifier
    gives binary feedback before an answer is trusted). Two reasoning voices
    check the answer for hallucinated/unsupported claims and reply VERDICT:
    PASS | FAIL | PARTIAL. Cheap (one parallel round, tight output caps)."""
    if verifiers:
        chosen: list[dict] = []
        for mm in verifiers:
            prov, model, kid = parse_src(mm)
            chosen.append(roster.member_key(prov, model, kid))
    else:
        chosen = roster.pick(want={"reasoning"}, n=2)
        if not chosen:
            chosen = roster.pick(n=2)
        # never let the voice that produced the answer verify itself
        author = (kw.get("_author_provider") or "").lower()
        if author:
            others = [v for v in chosen if v["provider"] != author]
            if len(others) >= 1:
                chosen = others
    block = f"QUESTION: {q}\n\nANSWER:\n{_crop(answer, 5000)}"
    vcap = max(256, min(kw.get("max_tokens", 2000), 700))
    res = parallel_calls([(m, block, VERIFIER_SYS, None, vcap) for m in chosen],
                         fleet=roster.fleet)
    verdicts = []
    for r in res:
        if not r["ok"]:
            continue
        v = _parse_verdict(r["text"])
        verdicts.append({"member": vlabel(r["member"]),
                         "verdict": v or "INCONCLUSIVE",
                         "note": r["text"][:500]})
    if not verdicts:
        raise SystemExit("verify: no verifier produced a verdict.")
    order = {"FAIL": 0, "PARTIAL": 1, "PASS": 2, "INCONCLUSIVE": 3}
    final = min((x["verdict"] for x in verdicts), key=lambda v: order.get(v, 3))
    out = {"verdict": final, "verifiers": verdicts}
    if not quiet:
        if kw.get("json"):
            print(json_mod.dumps(out, indent=2, ensure_ascii=False))
        else:
            marks = {"PASS": "✔ PASS", "FAIL": "✘ FAIL",
                     "PARTIAL": "◐ PARTIAL", "INCONCLUSIVE": "? INCONCLUSIVE"}
            for x in verdicts:
                note = (x["note"] or "").splitlines()
                last = note[-1][:140] if note else ""
                print(f"  verifier {x['member']}: "
                      f"{marks.get(x['verdict'], x['verdict'])}"
                      + (f" — {last}" if last else ""))
            print(f"── verify verdict: {final} ──")
    return out


def cmd_calibrate(roster: Roster, questions: int = 3,
                  only: str = "", **kw) -> dict:
    """Self-improvement eval: score one voice per provider on a frozen set of
    calibration questions (default 3 of 8) and store per-voice accuracy in
    state/calibration.json. Later `consensus` voting weights and `report`
    win-rates read this store. Deterministic, cheap, and gated behind
    --plan/--questions so the operator controls the cost."""
    voices = roster.members()
    if only:
        keep = {x.strip() for x in only.split(",") if x.strip()}
        voices = [v for v in voices if v["provider"] in keep]
    if not voices:
        raise SystemExit("calibrate: no voices to score (--providers filter "
                         "matched nothing).")
    qs = CALIBRATION_QUESTIONS[:max(1, min(questions, len(CALIBRATION_QUESTIONS)))]
    calib = kw.get("_calibration") or Calibration(roster.fleet.state_dir)
    inst = "Answer in a few words only. No explanation."
    scored: dict[tuple[str, int], dict] = {}
    for q, gold in qs:
        tasks = [(v, q, inst, None, 80) for v in voices]
        res = parallel_calls(tasks, fleet=roster.fleet)
        for r, v in zip(res, voices):
            if not r["ok"]:
                continue
            key = (v["provider"], v["kid"])
            e = scored.setdefault(key, {"voice": v, "correct": 0,
                                        "answered": 0})
            e["answered"] += 1
            e["correct"] += int(score_calibration(r["text"], gold))
    n_asked = len(qs)
    out_rows = []
    for key, e in scored.items():
        v = e["voice"]
        rec = calib.record(v["provider"], v["kid"], e["correct"], e["answered"])
        out_rows.append({"voice": vlabel(v),
                         "accuracy": rec["acc"], "correct": e["correct"],
                         "questions": e["answered"],
                         "total_scored": rec["n"]})
    out = {"questions": n_asked, "voices": out_rows}
    if kw.get("json"):
        print(json_mod.dumps(out, indent=2, ensure_ascii=False))
    else:
        print(f"== calibration: {len(qs)} question(s) x {len(scored)} voice(s) ==")
        for r in sorted(out_rows, key=lambda x: -x["accuracy"]):
            print(f"  {r['voice']:56s} acc={r['accuracy']:.2f} "
                  f"({r['correct']}/{r['questions']}, {r['total_scored']} scored)")
    return out


def cmd_sessions(sessions: Sessions, name: str = "", reset: bool = False,
                 json: bool = False) -> None:
    if reset:
        if not name:
            raise SystemExit("--reset needs a session name (--name <name>)")
        sessions.reset(name)
        if json:
            print(json_mod.dumps({"reset": name}, ensure_ascii=False))
        else:
            print(f"session '{name}' reset.")
        return
    names = sessions.list()
    out = [{"session": n,
            "exchanges": len(sessions.load(n)) // 2} for n in names]
    if json:
        print(json_mod.dumps(out, indent=2, ensure_ascii=False))
        return
    if not out:
        print("(no sessions yet — use ask/moa/... --session <name>)")
        return
    for r in out:
        print(f"{r['session']:24s} {r['exchanges']} exchange(s)")


def cmd_runs(runs: Runs, last: int = 10, json: bool = False) -> None:
    rows = runs.read()
    if json:
        print(json_mod.dumps(rows[-max(1, last):], indent=2, ensure_ascii=False))
        return
    if not rows:
        print("(no provenance runs recorded yet)")
        return
    for r in rows[-max(1, last):]:
        vs = r.get("voices") or []
        tok = r.get("tokens") or 0
        verdict = r.get("verdict") or "-"
        mean = r.get("mean_score")
        ms = r.get("ms")
        tail = f" {ms:.0f}ms" if isinstance(ms, (int, float)) else ""
        print(f"{r.get('ts', '?')}  {str(r.get('cmd', '?'))[:12]:12s} "
              f"voices={len(vs):2d} tok={tok:6d} "
              f"verdict={str(verdict):7s} mean={mean if mean is not None else '-'}"
              f"{tail}")


def cmd_report(roster: Roster, runs: Runs, cache: AnswerCache,
               calibration: Calibration | None = None,
               json: bool = False) -> None:
    rows = []
    for name in roster.providers:
        p = roster.providers[name]
        if p["note"]:
            continue
        for v in roster.voices_for(name):
            fr = roster.fleet.rec(v["provider"], v["kid"])
            if fr.get("tokens") or fr.get("ok") or fr.get("fail"):
                cal = calibration.for_voice(v["provider"], v["kid"]) \
                    if calibration else {}
                ms = fr.get("ms") or 0.0
                calls = fr.get("calls") or 0
                tps = round(fr.get("tokens", 0) / ms * 1000.0, 1) \
                    if ms and calls else None
                rows.append({
                    "voice": f"{name}#k{v['kid']}",
                    "ok": fr.get("ok", 0), "fail": fr.get("fail", 0),
                    "tokens": fr.get("tokens", 0),
                    "cached_tokens": fr.get("cached", 0),
                    "avg_ms": round(ms, 0) if ms else None,
                    "calls": calls,
                    "tokens_per_s": tps,
                    "accuracy": cal.get("acc") if cal else None,
                    "scored": (cal or {}).get("n", 0)})
    if json:
        print(json_mod.dumps({"voices": rows, "cache_hits": cache.hits},
                         indent=2, ensure_ascii=False))
        return
    print("== token spend / latency per voice (provider usage reports) ==")
    if not rows:
        print("(no usage recorded yet — run a command first)")
    for r in rows:
        tps = f"{r['tokens_per_s']:.0f} tok/s" if r["tokens_per_s"] else "-"
        acc = f" acc={r['accuracy']:.2f}" if r.get("accuracy") is not None else ""
        print(f"  {r['voice']:16s} ok={r['ok']:3d} fail={r['fail']:3d} "
              f"tokens={r['tokens']:7d} cached={r['cached_tokens']:6d}"
              f" {tps:>12s}{acc}")
    allr = runs.read()
    rewards = sum(1 for r in allr if r.get("verdict") == "REWARD")
    pun = sum(1 for r in allr if r.get("verdict") == "PUNISH")
    print(f"\n== runs: {len(allr)} recorded | REWARD {rewards} | "
          f"PUNISH {pun} | cache hits this process: {cache.hits} ==")


def cmd_ledger(ledger: Ledger, reset: bool, json: bool = False) -> None:
    if reset:
        ledger.data = {}
        ledger.save()
        if json:
            print(json_mod.dumps({"reset": True}))
        else:
            print("ledger reset.")
        return
    rows = sorted(ledger.data.items(), key=lambda kv: -(kv[1].get("ewma") or -1))
    out = [{"member": k, "ewma": rec.get("ewma"), "uses": rec.get("uses", 0),
            "rewards": rec.get("rewards", 0),
            "punishments": rec.get("punishments", 0)} for k, rec in rows]
    if json:
        print(json_mod.dumps(out, indent=2, ensure_ascii=False))
        return
    if not out:
        print("(empty ledger)")
        return
    for x in out:
        print(f"{x['member']:60s} ewma={x['ewma']:6} uses={x['uses']:3d} "
              f"rewards={x['rewards']} pun={x['punishments']}")


def cmd_selftest(creds_path: str, state_dir: str) -> int:
    """Offline self-test: multi-key roster + fleet failover + capability tags +
    ledger + parsing. No network and no real user state touched."""
    import shutil
    import tempfile
    ok = True

    def check(name: str, cond: bool, extra: str = "") -> None:
        nonlocal ok
        print((("  PASS  " if cond else "  FAIL  ") + name) +
              ("  " + extra if extra else ""))
        ok = ok and cond

    tmp = tempfile.mkdtemp(prefix="sith-selftest-")
    try:
        fixture = {"providers": {
            "gemini": {"api_key": "test", "alt_api_keys": ["test"],
                       "default_model": "gemini-2.5-flash", "tags": ["vision"]},
            "groq": {"api_key": "test", "alt_api_keys": ["test2"],
                     "default_model": "openai/gpt-oss-120b"},
            "cohere": {"api_key": "test",
                       "default_model": "command-a-reasoning-08-2025",
                       "tags": ["reasoning"]},
            "mistral": {"api_key": "test", "default_model": "mistral-small-latest"},
        }}
        creds = os.path.join(tmp, "creds.json")
        json.dump(fixture, open(creds, "w"))
        state = os.path.join(tmp, "st")
        roster = Roster(creds_path=creds, state_dir=state)
        check("multi-key roster: 4 providers", len(roster.members()) == 4)
        # gemini: duplicate alt collapses to 1 voice; groq: 2 distinct keys
        check("gemini voices == 1 (dedupe)",
              len(roster.voices_for("gemini")) == 1)
        check("groq voices == 2 (primary+alt)",
              len(roster.voices_for("groq")) == 2)
        check("all voices == 5", len(roster.all_voices()) == 5)
        v = roster.voice("groq")
        check("healthiest voice starts at k1", v["kid"] == 1)
        # cool k1 with a fake 429 -> voice() must fail over to k2
        roster.fleet.record("groq", 1, ok=False, err="HTTP 429: rate")
        v2 = roster.voice("groq")
        check("failover to k2 after k1 cooled", v2["kid"] == 2)
        check("k1 cooldown recorded", roster.fleet.cooled("groq", 1) > 0)
        # member resolution with explicit key index
        vm = roster.member_key("groq", None, 2)
        check("member_key(prov,None,k2) == k2", vm["kid"] == 2)
        tags = {f"{m['provider']}/{m['model']}": m["tags"] for m in roster.members()}
        check("gemini classified vision",
              "vision" in tags["gemini/gemini-2.5-flash"])
        check("cohere classified reasoning",
              "reasoning" in tags["cohere/command-a-reasoning-08-2025"])
        check("confidence parse", _parse_conf("answer\nCONF: 0.35") == 0.35)
        check("confidence missing -> None", _parse_conf("no conf") is None)
        check("score parse", _parse_score("SCORE: 8.5") == 8.5)
        # -- new v1.2 features (offline): extraction, vote, sessions, cache ---
        check("extract ANSWER: line",
              extract_final_answer("reasoning\nANSWER: 42") == "42")
        check("extract lenient (no tag)", "plain" in extract_final_answer("plain text"))
        res = plurality_vote(
            [{"member": "a/m1", "answer": "alpha"},
             {"member": "b/m2", "answer": "alpha"},
             {"member": "c/m3", "answer": "beta"}],
            [1.0, 1.0, 10.0])
        check("weighted plurality (beta wins on weight)",
              res["answer"] == "beta" and res["votes"] == 1
              and res["tally"][0]["weight"] == 10.0)
        res2 = plurality_vote(
            [{"member": "a/m1", "answer": "X"}, {"member": "b/m2", "answer": "X"}],
            [1.0, 1.0])
        check("plurality picks majority (X)", res2["answer"] == "X")
        sess = Sessions(state)
        sess.append("demo", "hello?", "hi", "p/m")
        sess.append("demo", "2nd?", "yo", "p/m")
        check("session persists 2 exchanges",
              len(sess.load("demo")) == 4 and "demo" in sess.list())
        ctx = sess.context("demo")
        check("session context mentions prior q", "hello?" in ctx)
        sess.reset("demo")
        check("session reset", sess.load("demo") == [] and "demo" not in sess.list())
        ac = AnswerCache(state)
        ac.put("repeat q", "answer one", "p/m")
        h1 = ac.get("repeat q")
        check("cache hit returns answer", h1 and h1["answer"] == "answer one")
        check("cache miss is None", ac.get("other q") is None)
        check("cache key is sha256 digest", len(AnswerCache.key("q")) == 64)
        # -- new v1.3 helpers (offline) --------------------------------
        check("abstention: UNKNOWN", is_abstention("unknown"))
        check("abstention: unsure clause", is_abstention("unsure, cannot say"))
        check("abstention: i don't know", is_abstention("I don't know what this is"))
        check("not abstention (real answer)", not is_abstention(
            "unknown kingdom of fungi"))
        check("not abstention (empty guard)", is_abstention("") is True)
        # provider usage shapes -> (input, output, cached)
        u1 = _split_usage({"usage": {"prompt_tokens": 100, "completion_tokens": 20,
                                     "prompt_tokens_details": {"cached_tokens": 40}}})
        check("usage parse (openai cached)", u1 == {"in": 100, "out": 20,
                                                    "cached": 40})
        u2 = _split_usage({"usageMetadata": {"promptTokenCount": 90,
                                             "candidatesTokenCount": 10,
                                             "cachedContentTokenCount": 50}})
        check("usage parse (gemini cached)", u2 == {"in": 90, "out": 10,
                                                    "cached": 50})
        u3 = _split_usage({"usage": {"input_tokens": 60, "output_tokens": 5,
                                     "cache_read_input_tokens": 30}})
        check("usage parse (anthropic-style)", u3 == {"in": 60, "out": 5,
                                                      "cached": 30})
        check("usage parse (none) is None", _split_usage({}) is None)
        check("verdict parse", _parse_verdict("VERDICT: FAIL\n- wrong") == "FAIL")
        longtxt = "x" * 3000
        cut = _crop(longtxt, 100)
        check("crop shortens + marks", len(cut) < 3000 and "trimmed" in cut)
        check("crop passes through small text", _crop("hi", 100) == "hi")
        check("calibration score exact", score_calibration("Paris", "paris"))
        check("calibration score fuzzy", score_calibration("the capital is Paris, "
                                                           "France", "paris"))
        check("calibration score wrong", not score_calibration("London", "paris"))
        cal = Calibration(state)
        first_m = roster.members()[0]
        cal.record(first_m["provider"], first_m["kid"], 3, 3)
        w = voice_weight(None, cal, first_m)
        check("voice_weight uses calibration acc", abs(w - 1.0) < 1e-6)
        led = Ledger(state)
        w2 = voice_weight(led, None, first_m)
        check("voice_weight falls back to 1.0", w2 == 1.0)
        # session compaction: context stays within a bounded char budget
        big = Sessions(state)
        for i in range(8):
            big.append("wide", f"question {i}", "answer " + "y" * 900, "p/m")
        ctx = big.context("wide")
        check("session context budget-bounded", len(ctx) <= 2800)
        check("session context keeps newest", "question 7" in ctx)
        mem = roster.members()[0]
        led.update(mem, 9)
        led.update(mem, 2)
        led2 = Ledger(state)  # persisted reload
        rec = led2.data[led2.key(mem)]
        check("ledger persists + ewma", abs(rec["ewma"] - 5.5) < 0.01
              and rec["rewards"] == 1 and rec["punishments"] == 1)
        blob = json_mod.dumps(led2.data) + json_mod.dumps(roster.fleet.data)
        check("no key leakage in state", "test" not in blob
              and "test2" not in blob)
        # value present in state must not be the raw key, and files are 0600
        mode_ok = True
        for f in (os.path.join(state, "ledger.json"),
                  os.path.join(state, "fleet.json"),
                  os.path.join(state, "cache.json"),
                  os.path.join(state, "calibration.json")):
            if os.path.isfile(f):
                mode_ok = mode_ok and (os.stat(f).st_mode & 0o777) == 0o600
        check("state files 0600", mode_ok)
        print("── selftest " + ("ALL PASS" if ok else "FAILED") + " ──")
        return 0 if ok else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _plan_only(roster: Roster, args) -> int:
    """--plan: show exactly which voices each stage would use and exit without
    calling any API (budget transparency)."""
    def names(ms: list) -> list[str]:
        return [vlabel(m) for m in ms]
    plan: list[str] = []
    cmd = args.cmd
    if cmd in ("ask",):
        plan.append("1. direct answer  -> " +
                    ", ".join(names([roster.pick(n=1)[0]])))
    if cmd == "moa" or cmd == "harvest" or cmd == "refine" or cmd == "consensus":
        n = getattr(args, "proposers", 3)
        props = roster.pick(want={"fast"}, exclude={"reasoning"}, n=n)
        if len(props) < n:
            props = roster.pick(exclude={"reasoning"}, n=n * 2)[:n] or props
        plan.append(f"1. proposers ({len(props)}) -> "
                    + ", ".join(names(props)))
        if cmd == "consensus":
            plan.append("2. plurality vote on the extracted ANSWER: lines "
                        "(no aggregator call)")
        else:
            agg = (roster.voice(getattr(args, "aggregator", ""))
                   if getattr(args, "aggregator", "")
                   else (roster.pick(want={"reasoning"}, n=1) or roster.pick(n=1))[0])
            plan.append("2. aggregator     -> " + vlabel(agg))
    if cmd in ("harvest", "refine"):
        plan.append("3. judge panel    -> " +
                    ", ".join(names(roster.pick(want={"reasoning"}, n=3))))
    if cmd == "refine":
        plan.append(f"4. revision rounds -> up to {getattr(args, 'rounds', 2)} "
                    f"(revisor from {'--helpmates' if getattr(args,'helpmates','') else 'aggregator provider'})")
    if cmd == "escalate":
        if args.src:
            prov, model, kid = parse_src(args.src)
            prim = [roster.member_key(prov, model, kid)]
        else:
            prim = roster.pick(want={"fast"}, n=1) or roster.pick(n=1)
        plan.append("1. primary       -> " + ", ".join(names(prim)))
        plan.append("2. reasoning court -> " +
                    ", ".join(names(roster.pick(want={"reasoning"}, n=3))))
    if cmd == "vision":
        plan.append("1. vision voices -> " +
                    ", ".join(names(roster.pick(want={"vision"}, n=3))))
        if getattr(args, "synthesize", False):
            plan.append("2. synthesize    -> " +
                        ", ".join(names(roster.pick(want={"reasoning"}, n=1))))
    if cmd == "verify":
        verifiers = roster.pick(want={"reasoning"}, n=2) or roster.pick(n=2)
        plan.append("1. verifiers     -> " + ", ".join(names(verifiers)))
        plan.append("2. verdict       -> PASS/FAIL/PARTIAL majority")
    if cmd == "calibrate":
        qn = getattr(args, "questions", 3)
        voices = roster.members()
        if getattr(args, "providers", ""):
            keep = {x.strip() for x in args.providers.split(",") if x.strip()}
            voices = [v for v in voices if v["provider"] in keep]
        plan.append("1. voices to score -> " +
                    ", ".join(names(voices)) or "(none)")
        plan.append(f"2. frozen questions -> {qn} of "
                    f"{len(CALIBRATION_QUESTIONS)} (facts/arithmetic/code)")
        plan.append(f"3. est. API calls  -> ~{len(voices) * qn} "
                    f"(bounded; scores stored in calibration.json)")
    is_json = bool(getattr(args, "json", False))
    if is_json:
        import json as _json
        print(_json_mod.dumps({"plan": plan, "dry_run": True,
                           "note": "no API keys were called"},
                          indent=2, ensure_ascii=False))
    else:
        print("\n".join(plan) or f"(no plan for {cmd})")
        print("(plan only — no API keys were called)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(prog="sith-choir",
                                 description="Cross-model intellect relay across "
                                             "a mesh of stored API keys (all "
                                             "providers, multi-key failover).")
    ap.add_argument("--credentials", help="JSON creds path")
    ap.add_argument("--catalog", help="model list JSON (models_list per provider)")
    ap.add_argument("--use-workspace", action="store_true",
                    help="auto-load arena.ai workspace secrets + catalog")
    ap.add_argument("--state", help="state dir (ledger + key health)")
    ap.add_argument("--json", action="store_true", dest="json",
                    help="machine-readable JSON output")
    ap.add_argument("--timeout", type=float, default=90.0)
    ap.add_argument("--max-tokens", type=int, default=2000)
    # cross-cutting feature options
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--session", default="",
                        help="multi-turn memory session name")
    common.add_argument("--no-cache", action="store_true",
                        help="disable the exact-question answer cache")
    common.add_argument("--budget", type=int, default=0,
                        help="stop before later stages if this many tokens "
                             "have already been spent (provider-reported)")
    common.add_argument("--plan", action="store_true",
                        help="print the exact voices each stage would use, "
                             "then exit (calls no API)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    # --json must also work AFTER the subcommand (as the README documents), so
    # each subparser inherits it too. default=SUPPRESS means an absent flag
    # never clobbers a --json given before the subcommand.
    json_opt = argparse.ArgumentParser(add_help=False)
    json_opt.add_argument("--json", action="store_true", dest="json",
                          default=argparse.SUPPRESS,
                          help="machine-readable JSON output")

    def sp(*a, **kw):
        kw.setdefault("parents", [json_opt, common])
        return sub.add_parser(*a, **kw)

    sp("list", help="show roster: one voice per provider + ledger")
    sp("fleet", help="show EVERY stored API key and its health (the mesh)")
    p = sp("ask", help="single direct question (per-key failover)")
    p.add_argument("question")
    p.add_argument("--from", dest="src", default="",
                   help="provider[/model[#k<idx>]]")
    p.add_argument("--lane", default="",
                   help="general|fast|reasoning|longctx|code (voice routing)")
    p.add_argument("--verify", action="store_true",
                   help="after a fresh answer, run an independent adversarial "
                        "verifier round (hallucination check)")
    p = sp("moa", help="proposers -> aggregator (Mixture-of-Agents)")
    p.add_argument("question")
    p.add_argument("--proposers", type=int, default=3)
    p.add_argument("--aggregator", default="",
                   help="force the aggregating provider (e.g. gemini)")
    p = sp("vision", help="ask vision-capable models to do the job")
    p.add_argument("--image", required=True)
    p.add_argument("--question", required=True, dest="question")
    p.add_argument("--synthesize", action="store_true",
                   help="second pass: reasoning model fuses the reports")
    p = sp("escalate", help="cheap first; mandatory escalation on low confidence")
    p.add_argument("question")
    p.add_argument("--from", dest="src", default="")
    p.add_argument("--force", action="store_true")
    p.add_argument("--require-conf", action="store_true")
    p.add_argument("--helpmates", default="",
                   help="comma-separated providers whose keys join the court "
                        "(e.g. gemini,llm7)")
    p = sp("judge", help="reward/punish an answer with a judge panel")
    p.add_argument("--question", required=True, dest="question")
    p.add_argument("--answer", required=True, dest="answer")
    p.add_argument("--members", default="",
                   help="comma-separated provider[/model[#k]] list")
    p = sp("harvest", help="propose -> aggregate -> judge -> ledger")
    p.add_argument("question")
    p.add_argument("--proposers", type=int, default=3)
    p.add_argument("--aggregator", default="")
    p = sp("consensus",
           help="self-consistency: sample voices, weighted plurality vote "
                "(no aggregator)")
    p.add_argument("question")
    p.add_argument("--samples", type=int, default=4)
    p = sp("refine", help="verifier loop: propose->judge->critique->revise "
                          "(Reflexion)")
    p.add_argument("question")
    p.add_argument("--proposers", type=int, default=3)
    p.add_argument("--aggregator", default="")
    p.add_argument("--rounds", type=int, default=2)
    p.add_argument("--target", type=float, default=7.5,
                   help="stop revising once mean judge score >= target")
    p.add_argument("--helpmates", default="",
                   help="provider whose voice does the revisions")
    p = sp("verify", help="independent verifier: PASS/FAIL/PARTIAL on an answer")
    p.add_argument("--question", default="", dest="question")
    p.add_argument("--answer", default="", dest="answer",
                   help="answer text, @file, or - to read stdin")
    p.add_argument("--members", default="",
                   help="comma-separated provider[/model[#k]] verifiers")
    p = sp("calibrate", help="self-improvement: score voices on a frozen "
                             "calibration set (writes calibration.json)")
    p.add_argument("--questions", type=int, default=3,
                   help="how many calibration questions (1-8, default 3)")
    p.add_argument("--providers", default="",
                   help="only score these providers (comma-separated)")
    p = sp("sessions", help="list / reset multi-turn memory sessions")
    p.add_argument("--name", default="")
    p.add_argument("--reset", action="store_true")
    p = sp("runs", help="show recent provenance run records")
    p.add_argument("--last", type=int, default=10)
    sp("report", help="aggregate token usage per voice + run verdicts")
    p = sp("ledger")
    p.add_argument("--reset", action="store_true")
    sp("selftest", help="offline self-test (no network)")
    args = ap.parse_args()

    kw = {"timeout": args.timeout, "max_tokens": args.max_tokens, "json": args.json}
    state_dir = args.state or os.environ.get(
        "SITH_STATE", os.path.expanduser("~/.cache/sith-choir"))

    if args.cmd == "selftest":
        rc = cmd_selftest(args.credentials or "/nonexistent", state_dir)
        return 3 if rc else 0  # exit-code contract: 3 = invariant failure

    roster = Roster(args.credentials, state_dir, args.catalog, args.use_workspace)
    ledger = Ledger(state_dir)
    sessions = Sessions(state_dir)
    cache = AnswerCache(state_dir)
    runs = Runs(state_dir)
    calibration = Calibration(state_dir)
    kw["_calibration"] = calibration

    # --plan prints who would sing and exits before any API call
    if args.plan and args.cmd in ("ask", "moa", "vision", "escalate",
                                  "harvest", "consensus", "refine",
                                  "verify", "calibrate"):
        return _plan_only(roster, args)

    # cross-cutting state plumbing shared by network commands
    kw["_cache"] = cache
    kw["no_cache"] = args.no_cache
    kw["_budget"] = args.budget or None
    kw["lane"] = getattr(args, "lane", "")
    kw["verify"] = getattr(args, "verify", False)
    kw["_author_provider"] = getattr(args, "author_provider", "")

    # multi-turn memory: wrap the question with prior context at the OUTER
    # edge (single point of wrapping), store the exchange after the command.
    session_name = args.session or None
    sess_q = getattr(args, "question", "") or ""
    if args.cmd in ("ask", "moa", "harvest", "consensus", "refine",
                    "escalate", "vision") and session_name:
        ctx = sessions.context(session_name)
        sess_q = session_wrap(ctx, sess_q)

    t0 = time.monotonic()
    result = None
    try:
        if args.cmd == "list":
            cmd_list(roster, ledger, json=args.json)
        elif args.cmd == "fleet":
            cmd_fleet(roster, json=args.json)
        elif args.cmd == "sessions":
            cmd_sessions(sessions, args.name, args.reset, json=args.json)
        elif args.cmd == "runs":
            cmd_runs(runs, args.last, json=args.json)
        elif args.cmd == "report":
            cmd_report(roster, runs, cache, calibration=calibration,
                       json=args.json)
        elif args.cmd == "ledger":
            cmd_ledger(ledger, args.reset, json=args.json)
        elif args.cmd == "ask":
            result = cmd_ask(roster, sess_q, args.src, **kw)
        elif args.cmd == "moa":
            result = cmd_moa(roster, sess_q, args.proposers,
                             aggregator=args.aggregator, **kw)
        elif args.cmd == "vision":
            result = cmd_vision(roster, args.image, sess_q,
                                args.synthesize, **kw)
        elif args.cmd == "escalate":
            result = cmd_escalate(roster, sess_q, args.src, args.force,
                                  args.require_conf, args.helpmates, **kw)
        elif args.cmd == "judge":
            answer = args.answer
            if answer.startswith("@"):
                answer = open(answer[1:], encoding="utf-8").read()
            members = [x.strip() for x in args.members.split(",")
                       if x.strip()] or None
            result = cmd_judge(roster, args.question, answer, members,
                               _ledger=ledger, **kw)
        elif args.cmd == "harvest":
            result = cmd_harvest(roster, ledger, sess_q,
                                 n_proposers=args.proposers,
                                 aggregator=args.aggregator, **kw)
        elif args.cmd == "consensus":
            result = cmd_consensus(roster, ledger, sess_q,
                                   args.samples, **kw)
        elif args.cmd == "refine":
            result = cmd_refine(roster, ledger, sess_q, args.rounds,
                                args.target, args.helpmates, **kw)
        elif args.cmd == "verify":
            if not (getattr(args, "question", "") and args.answer):
                raise SystemExit("verify needs --question Q and --answer "
                                 "TEXT|@file|- (or use --plan)")
            answer = args.answer
            if answer == "-":
                answer = sys.stdin.read()
            elif answer.startswith("@"):
                answer = open(answer[1:], encoding="utf-8").read()
            members = [x.strip() for x in args.members.split(",")
                       if x.strip()] or None
            result = cmd_verify(roster, args.question, answer, members, **kw)
        elif args.cmd == "calibrate":
            result = cmd_calibrate(roster, args.questions, args.providers,
                                   **kw)
    except BaseException:
        flush_run_usage(roster.fleet)
        raise

    spent = run_tokens_spent()
    flush_run_usage(roster.fleet)

    # provenance: labels + verdict + token spend + latency only (never content)
    ms = (time.monotonic() - t0) * 1000.0
    if result and (result.get("answer") or result.get("voices")
                   or args.cmd in ("verify", "calibrate")):
        voices = ((result.get("proposers") or []) +
                  (result.get("voices") or []) +
                  ([result.get("aggregator")] if result.get("aggregator") else []) +
                  (result.get("panel") or []) +
                  ([result.get("member")] if result.get("member") else []) +
                  ([result.get("lead")] if result.get("lead") else []) +
                  (result.get("seers") or []))
        voices = [v for v in voices if isinstance(v, str) and v]
        # calibrate rows carry their label under "voice"; verify rows carry
        # theirs under "verifiers"
        if args.cmd == "calibrate":
            voices = [x.get("voice") for x in result.get("voices", [])
                      if isinstance(x, dict) and x.get("voice")]
        elif args.cmd == "verify":
            voices = [x.get("member") for x in result.get("verifiers", [])
                      if isinstance(x, dict) and x.get("member")]
        voices = list(dict.fromkeys(voices))
        rec = {"cmd": args.cmd, "voices": voices,
               "verdict": result.get("verdict") or (result.get("verify") or {}).get("verdict"),
               "mean_score": result.get("mean_score"),
               "tokens": spent, "ms": round(ms, 0)}
        runs.add(rec)
        if session_name:
            label = (result.get("member") or result.get("lead")
                     or result.get("aggregator") or "choir")
            q0 = getattr(args, "question", "") or ""
            if q0:
                sessions.append(session_name, q0,
                                result["answer"][:2000], label)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception as e:  # never fake a silent success
        print(f"error: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
