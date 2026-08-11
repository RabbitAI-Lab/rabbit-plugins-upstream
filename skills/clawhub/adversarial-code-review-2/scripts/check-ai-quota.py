#!/usr/bin/env python3
"""Quota checker for Claude, Codex, Gemini, GLM, and DeepSeek APIs.

The CLI itself uses only the Python standard library. Actual checks lazily load
``quota_api`` from the optional ``hermes-quota-status`` plugin. Without that
plugin, importing this module and ``--help`` still work, while checks return a
normal per-provider error.

Endpoints, credentials, status, and privacy notes (full details in
``references/ai-quota-apis.md``):

* Claude: ``https://api.anthropic.com/api/oauth/usage``; OAuth token from
  ``~/.claude/.credentials.json``; first-party but undocumented and
  community-discovered; sends the OAuth token and exposes account usage.
* Codex: ``https://chatgpt.com/backend-api/wham/usage``; OAuth token from
  ``~/.codex/auth.json``; first-party/official service but not a documented
  public API; sends the OAuth token and exposes ChatGPT account usage.
* Gemini: official ``https://generativelanguage.googleapis.com/v1beta/models``
  and
  ``https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent``
  endpoints; API key from ``GOOGLE_API_KEY`` or ``~/.hermes/.env``; the probe
  sends "ok" to Google and consumes a small amount of quota because no
  real-time quota API exists.
* GLM: ``https://api.z.ai`` then ``https://open.bigmodel.cn``, both with
  ``/api/monitor/usage/quota/limit``; key from ``GLM_API_KEY`` or
  ``ZHIPU_API_KEY``; undocumented/community endpoints; fallback can send the
  same credential and account-usage request to both Z.AI/Zhipu hosts.
* DeepSeek: official ``https://api.deepseek.com/user/balance``; key from
  ``DEEPSEEK_API_KEY``; sends the key and exposes the account balance.

Every check discloses the caller's IP, timing, and account association to the
target provider. Credentials are sent in request headers and are not printed.
"""
from __future__ import annotations

import argparse
import importlib
import json
import math
import os
import sys
from concurrent.futures import Future, ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock
from types import ModuleType
from typing import Any, Callable, Sequence

# Hermes may sandbox HOME for a run while retaining the user's credential/plugin
# root in HERMES_REAL_HOME. Outside Hermes, Path.home() remains the default. The
# directory is not added to sys.path until a provider check needs the adapter.
PLUGIN_DIR = (
    Path(os.environ.get("HERMES_REAL_HOME", str(Path.home())))
    / ".hermes"
    / "plugins"
    / "hermes-quota-status"
)

_QUOTA_API: ModuleType | None = None
_QUOTA_API_LOCK = Lock()
_QUOTA_API_ERROR = (
    "quota_api dependency unavailable; install the hermes-quota-status plugin"
)

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
GRAY = "\033[90m"
RESET = "\033[0m"

QuotaResult = dict[str, Any]
QuotaFetcher = Callable[[], QuotaResult]
ProviderSpec = tuple[str, QuotaFetcher]


def json_object(value: Any) -> dict[str, Any]:
    """Return a JSON object or an empty compatibility value."""
    return value if isinstance(value, dict) else {}


def json_number(value: Any) -> float:
    """Return a finite JSON number, matching the adapter's rendering helper."""
    if value is None or isinstance(value, bool):
        return 0.0
    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError):
        return 0.0
    return number if math.isfinite(number) else 0.0


def _quota_api() -> ModuleType:
    """Load the optional external adapter only when a check is requested."""
    global _QUOTA_API
    if _QUOTA_API is not None:
        return _QUOTA_API

    with _QUOTA_API_LOCK:
        if _QUOTA_API is not None:
            return _QUOTA_API

        plugin_path = str(PLUGIN_DIR)
        if plugin_path not in sys.path:
            sys.path.insert(0, plugin_path)
        try:
            _QUOTA_API = importlib.import_module("quota_api")
        except Exception as exc:
            raise RuntimeError(_QUOTA_API_ERROR) from exc
        return _QUOTA_API


def _adapter_fetcher(name: str) -> Callable[[], dict[str, Any] | None]:
    """Resolve a named plugin fetcher with a concise compatibility failure."""
    fetcher = getattr(_quota_api(), name, None)
    if not callable(fetcher):
        raise RuntimeError(f"{_QUOTA_API_ERROR} ({name} is missing)")
    return fetcher


def fetch_claude_quota() -> dict[str, Any] | None:
    return _adapter_fetcher("fetch_claude_quota")()


def fetch_codex_quota() -> dict[str, Any] | None:
    return _adapter_fetcher("fetch_codex_quota")()


def fetch_gemini_quota() -> dict[str, Any] | None:
    return _adapter_fetcher("fetch_gemini_quota")()


def fetch_glm_quota() -> dict[str, Any] | None:
    return _adapter_fetcher("fetch_glm_quota")()


def fetch_deepseek_balance() -> dict[str, Any] | None:
    return _adapter_fetcher("fetch_deepseek_balance")()

_FRENCH_TEXT = {
    "AI CLI quota checker": "Vérificateur de quota des CLI d'IA",
    "show this help message and exit": "afficher cette aide et quitter",
    "emit machine-readable JSON": "produire du JSON lisible par machine",
    "check Claude quota": "vérifier le quota Claude",
    "check Codex quota": "vérifier le quota Codex",
    "check Gemini quota": "vérifier le quota Gemini",
    "check GLM (Z.AI) quota": "vérifier le quota GLM (Z.AI)",
    "check DeepSeek USD balance": "vérifier le solde DeepSeek en USD",
    "check all providers": "vérifier tous les fournisseurs",
    "Errors": "Erreurs",
    "GLM API key not found (set GLM_API_KEY or ZHIPU_API_KEY)": (
        "clé API GLM introuvable (définissez GLM_API_KEY ou ZHIPU_API_KEY)"
    ),
    "DEEPSEEK_API_KEY not found": "DEEPSEEK_API_KEY introuvable",
}


def _session_language() -> str:
    """Resolve the process/session language without changing the global locale."""
    for variable in ("HERMES_SESSION_LANGUAGE", "LANGUAGE", "LC_ALL", "LC_MESSAGES", "LANG"):
        value = os.environ.get(variable, "").strip().lower()
        if value:
            return value.split(":", 1)[0].split("_", 1)[0].split("-", 1)[0]
    return "en"


def human_text(message: str) -> str:
    """Translate human-only text; JSON paths deliberately never call this."""
    if _session_language() == "fr":
        return _FRENCH_TEXT.get(message, message)
    return message


def human_error(error: str) -> str:
    """Translate known CLI diagnostics while retaining provider and API details."""
    if _session_language() != "fr":
        return error
    provider, separator, message = error.partition(": ")
    if not separator:
        return human_text(error)
    return f"{provider}: {human_text(message)}"


def codex_quota() -> dict[str, Any]:
    quota = fetch_codex_quota()
    if quota is None:
        raise RuntimeError("Codex OAuth token not found")
    return {
        "provider": "codex",
        "plan": "unknown",
        "session": {
            "used_pct": quota.get("session_pct"),
            "reset_iso": quota.get("session_reset", ""),
        },
        "weekly": {
            "used_pct": quota.get("weekly_pct"),
            "reset_iso": quota.get("weekly_reset", ""),
        },
    }


def claude_quota() -> dict[str, Any]:
    quota = fetch_claude_quota()
    if quota is None:
        raise RuntimeError("Claude OAuth token not found")
    return {
        "provider": "claude",
        "plan": "pro",
        "session": {
            "used_pct": quota.get("session_pct"),
            "reset_iso": quota.get("session_reset", ""),
        },
        "weekly": {
            "used_pct": quota.get("weekly_pct"),
            "reset_iso": quota.get("weekly_reset", ""),
        },
    }


def gemini_quota() -> dict[str, Any]:
    quota = fetch_gemini_quota()
    if quota is None:
        raise RuntimeError("GOOGLE_API_KEY not found")
    return {
        "provider": "gemini",
        "plan": "google-ai-studio",
        "key_valid": bool(quota.get("key_valid")),
        "available_models": quota.get("available_models", []),
        "model_count": quota.get("model_count", 0),
        "probe": quota.get("probe"),
        "error": quota.get("error", ""),
    }


def _optional_number(value: Any) -> float | None:
    """Return a finite JSON-compatible number without treating booleans as numbers."""
    if value is None or isinstance(value, bool):
        return None
    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError):
        return None
    return number if math.isfinite(number) else None


def glm_quota() -> dict[str, Any]:
    quota = fetch_glm_quota()
    if quota is None:
        raise RuntimeError("GLM API key not found (set GLM_API_KEY or ZHIPU_API_KEY)")

    result: dict[str, Any] = {
        "provider": "glm",
        "plan": "z.ai",
        "session": {
            "used_pct": _optional_number(quota.get("session_pct")),
            "reset_iso": quota.get("session_reset", quota.get("reset_iso", "")),
        },
    }
    # Preserve the provider-specific normalized metrics used by registry rules.
    for key in ("available_limit_pct", "remaining_fraction", "balance", "host"):
        if key in quota:
            result[key] = quota[key]
    return result


def _deepseek_usd_balance(quota: dict[str, Any]) -> tuple[float, dict[str, Any]]:
    raw_balances = quota.get("balances")
    balances = raw_balances if isinstance(raw_balances, list) else []
    for raw_balance in balances:
        balance = json_object(raw_balance)
        currency = balance.get("currency")
        if not isinstance(currency, str) or currency.upper() != "USD":
            continue
        amount = _optional_number(balance.get("total_balance"))
        if amount is not None:
            return amount, balance

    # Older quota_api releases returned only the preferred balance. A missing
    # currency in that shape is USD by contract; an explicit non-USD currency
    # must not be mislabeled as dollars.
    currency = quota.get("currency")
    amount = _optional_number(quota.get("balance", quota.get("total_balance")))
    if amount is not None and (not isinstance(currency, str) or currency.upper() == "USD"):
        return amount, quota
    raise RuntimeError("DeepSeek API response did not include a USD balance")


def deepseek_quota() -> dict[str, Any]:
    quota = fetch_deepseek_balance()
    if quota is None:
        raise RuntimeError("DEEPSEEK_API_KEY not found")

    balance, usd_details = _deepseek_usd_balance(quota)
    result: dict[str, Any] = {
        "provider": "deepseek",
        "plan": "pay-as-you-go",
        "balance": balance,
        "currency": "USD",
        "is_available": quota.get("is_available", True),
    }
    for key in (
        "granted_balance",
        "topped_up_balance",
        "total_balance_display",
        "granted_balance_display",
        "topped_up_balance_display",
    ):
        if key in usd_details:
            result[key] = usd_details[key]
    return result


def fmt_duration(seconds: float) -> str:
    if seconds <= 0:
        return "now"
    h, rem = divmod(int(seconds), 3600)
    m, s = divmod(rem, 60)
    if h > 0:
        return f"{h}h{m:02d}m"
    return f"{m}m{s:02d}s"


def fmt_reset(iso_str: str) -> tuple[str, str]:
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        diff = (dt - now).total_seconds()
        if diff <= 0:
            return "RESET NOW", ""
        local = dt.astimezone()
        return local.strftime("%a %H:%M"), f" ({fmt_duration(diff)})"
    except Exception:
        return iso_str or "?", ""


def bar(pct: Any, width: int = 10) -> str:
    if pct is None:
        return f"{GRAY}{'░' * width} ?%{RESET}"
    pct_num = max(0.0, min(100.0, json_number(pct)))
    filled = int(pct_num / 100 * width)
    empty = width - filled
    if pct_num >= 80:
        color = RED
    elif pct_num >= 50:
        color = YELLOW
    else:
        color = GREEN
    return f"{color}{'█' * filled}{'░' * empty} {pct_num:.0f}%{RESET}"


def render_quota(provider: str, data: dict[str, Any]) -> None:
    if provider == "gemini":
        render_gemini(data)
        return
    if provider == "glm":
        render_glm(data)
        return
    if provider == "deepseek":
        render_deepseek(data)
        return

    session = json_object(data.get("session"))
    weekly = json_object(data.get("weekly"))
    session_reset, session_countdown = fmt_reset(str(session.get("reset_iso", "")))
    weekly_reset, weekly_countdown = fmt_reset(str(weekly.get("reset_iso", "")))

    print(f"\n{'=' * 55}")
    print(f"  {provider.upper()} ({data.get('plan', 'unknown')})")
    print(f"{'=' * 55}")
    print(
        f"  5h session:  {bar(session.get('used_pct'))} used  -> "
        f"resets {session_reset}{session_countdown}"
    )
    if weekly:
        print(
            f"  7d weekly:   {bar(weekly.get('used_pct'))} used  -> "
            f"resets {weekly_reset}{weekly_countdown}"
        )


def render_glm(data: dict[str, Any]) -> None:
    session = json_object(data.get("session"))
    reset, countdown = fmt_reset(str(session.get("reset_iso", "")))

    print(f"\n{'=' * 55}")
    print(f"  GLM ({data.get('plan', 'unknown')})")
    print(f"{'=' * 55}")
    print(
        f"  quota period: {bar(session.get('used_pct'))} used  -> "
        f"resets {reset}{countdown}"
    )


def render_deepseek(data: dict[str, Any]) -> None:
    print(f"\n{'=' * 55}")
    print("  DEEPSEEK (pay-as-you-go)")
    print(f"{'=' * 55}")
    print(f"  balance:      ${json_number(data.get('balance')):.2f} USD")
    availability = (
        f"{GREEN}available{RESET}"
        if data.get("is_available")
        else f"{RED}unavailable{RESET}"
    )
    print(f"  API:          {availability}")


def render_gemini(data: dict[str, Any]) -> None:
    probe = json_object(data.get("probe"))
    status = probe.get("status")
    available_models = data.get("available_models")
    models = (
        [model for model in available_models if isinstance(model, str)]
        if isinstance(available_models, list)
        else []
    )

    print(f"\n{'=' * 55}")
    print("  GEMINI (google-ai-studio)")
    print(f"{'=' * 55}")
    if not data.get("key_valid"):
        print(f"  key:          {RED}invalid{RESET}")
        if data.get("error"):
            print(f"  error:        {data['error']}")
        return

    print(f"  key:          {GREEN}valid{RESET}")
    print(f"  models:       {len(models)} generateContent-capable Gemini models")
    if models:
        print(f"  examples:     {', '.join(models[:4])}")

    if status == 429 or probe.get("rate_limited") is True:
        print(f"  probe:        {RED}rate limited (HTTP 429){RESET}")
    elif status == 403:
        print(f"  probe:        {YELLOW}HTTP 403 (quota exhausted or model unavailable){RESET}")
    elif status == "error":
        print(f"  probe:        {YELLOW}error: {probe.get('error', 'unknown')}{RESET}")
    elif status is None:
        print(f"  probe:        {GRAY}not available{RESET}")
    else:
        print(f"  probe:        {GREEN}HTTP {int(json_number(status))}{RESET}")


def provider_status(provider: str, data: dict[str, Any]) -> str:
    if provider == "gemini":
        if not data.get("key_valid"):
            return "KEY INVALID"
        probe = json_object(data.get("probe"))
        status = probe.get("status")
        if status == 429 or probe.get("rate_limited") is True:
            return "RATE-LIMITED"
        if status in (403, "error"):
            return "DRAINING"
        return "OK"

    if provider == "deepseek":
        if not data.get("is_available"):
            return "UNAVAILABLE"
        return "OK" if json_number(data.get("balance")) > 0 else "DRAINING"

    session = json_object(data.get("session"))
    used_pct = session.get("used_pct")
    if used_pct is None:
        return "UNKNOWN"
    pct = json_number(used_pct)
    if pct >= 100:
        return "RATE-LIMITED"
    if pct < 50:
        return "OK"
    return "DRAINING"


def provider_registry() -> dict[str, ProviderSpec]:
    """Build the unified registry lazily so callers can replace fetchers."""
    return {
        "claude": ("Claude", claude_quota),
        "codex": ("Codex", codex_quota),
        "gemini": ("Gemini", gemini_quota),
        "glm": ("GLM", glm_quota),
        "deepseek": ("DeepSeek", deepseek_quota),
    }


def provider_checks() -> dict[str, QuotaFetcher]:
    """Return the fetcher-only compatibility view of the provider registry."""
    return {name: fetcher for name, (_, fetcher) in provider_registry().items()}


def provider_label(name: str, registry: dict[str, ProviderSpec] | None = None) -> str:
    """Return a registered label, with a readable fallback for unknown providers."""
    spec = (registry if registry is not None else provider_registry()).get(name)
    return spec[0] if spec is not None else name.replace("_", " ").title()


def run_checks(providers: Sequence[str]) -> tuple[dict[str, QuotaResult], list[str]]:
    """Run provider checks concurrently with deterministic result/error ordering."""
    registry = provider_registry()
    requested = list(dict.fromkeys(providers))
    if not requested:
        return {}, []

    futures: dict[str, Future[QuotaResult]] = {}
    setup_errors: dict[str, str] = {}
    with ThreadPoolExecutor(max_workers=len(requested), thread_name_prefix="quota") as executor:
        for name in requested:
            spec = registry.get(name)
            if spec is None:
                setup_errors[name] = "provider is not registered"
                continue
            futures[name] = executor.submit(spec[1])

        results: dict[str, QuotaResult] = {}
        errors: list[str] = []
        for name in requested:
            if name in setup_errors:
                errors.append(f"{provider_label(name, registry)}: {setup_errors[name]}")
                continue
            try:
                results[name] = futures[name].result()
            except Exception as exc:
                detail = str(exc).strip() or type(exc).__name__
                errors.append(f"{provider_label(name, registry)}: {detail}")
    return results, errors


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=human_text("AI CLI quota checker"),
        add_help=False,
    )
    parser.add_argument(
        "-h",
        "--help",
        action="help",
        help=human_text("show this help message and exit"),
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help=human_text("emit machine-readable JSON"),
    )
    parser.add_argument("--all", action="store_true", help=human_text("check all providers"))
    parser.add_argument("--claude", action="store_true", help=human_text("check Claude quota"))
    parser.add_argument("--codex", action="store_true", help=human_text("check Codex quota"))
    parser.add_argument("--gemini", action="store_true", help=human_text("check Gemini quota"))
    parser.add_argument("--glm", action="store_true", help=human_text("check GLM (Z.AI) quota"))
    parser.add_argument(
        "--deepseek",
        action="store_true",
        help=human_text("check DeepSeek USD balance"),
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)

    provider_names = tuple(provider_registry())
    requested = [name for name in provider_names if getattr(args, name)]
    if args.all or not requested:
        requested = list(provider_names)

    results, errors = run_checks(requested)

    if args.json:
        print(json.dumps({"results": results, "errors": errors}, indent=2))
        return 1 if errors else 0

    for provider, data in results.items():
        render_quota(provider, data)

    if errors:
        print(
            f"\n  {human_text('Errors')}: "
            f"{'; '.join(human_error(error) for error in errors)}",
        )

    if results:
        print(f"\n{'-' * 55}")
        for name, result in results.items():
            status = provider_status(name, result)
            session = json_object(result.get("session"))
            pct = session.get("used_pct")
            suffix = f" ({json_number(pct):.0f}%)" if pct is not None else ""
            print(f"  {provider_label(name)}: {status}{suffix}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
