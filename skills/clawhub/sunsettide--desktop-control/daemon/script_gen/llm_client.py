"""
LLM client with pluggable provider architecture.

Supports:
  - OpenAI-compatible API (DeepSeek, OpenAI, Ollama, etc.)
  - Disabled mode (no LLM configured)

Configuration is via environment variables to keep dependencies minimal.
No additional pip packages required beyond `requests` (standard HTTP).

Usage:
    client = get_llm_client()
    if client:
        text = client.chat(system_prompt, user_prompt)
    else:
        print("LLM not configured. See env vars below.")
"""

import json
import logging
import os
import re
import sys

logger = logging.getLogger(__name__)

# ── Configuration ──────────────────────────────────────────────────────────

LLM_PROVIDER = os.environ.get("LLM_PROVIDER", "").strip().lower()
LLM_BASE_URL = os.environ.get("LLM_BASE_URL", "").strip().rstrip("/")
LLM_API_KEY  = os.environ.get("LLM_API_KEY", "").strip()
LLM_MODEL    = os.environ.get("LLM_MODEL", "").strip()

# Fallback: if only LLM_API_KEY is set, try OpenAI format
_FALLBACK_URL  = "https://api.openai.com/v1"
_FALLBACK_MODEL = "gpt-4o-mini"


def is_configured() -> bool:
    """Check if any LLM backend is configured."""
    if LLM_API_KEY and LLM_BASE_URL:
        return True
    if LLM_API_KEY and not LLM_BASE_URL:
        return True  # fallback to OpenAI
    return False


def config_help() -> str:
    """Return a human-friendly help string on how to configure LLM."""
    return (
        "To enable AI-powered script generation, set any of these environment variables:\n\n"
        "  LLM_API_KEY=<your-api-key>     (required)\n"
        "  LLM_BASE_URL=<api-endpoint>    (optional, defaults to OpenAI API)\n"
        "  LLM_MODEL=<model-name>         (optional, defaults to gpt-4o-mini)\n"
        "  LLM_PROVIDER=deepseek|openai   (optional, auto-detected from URL)\n\n"
        "Examples:\n"
        "  # DeepSeek\n"
        "  set LLM_API_KEY=sk-xxx\n"
        "  set LLM_BASE_URL=https://api.deepseek.com/v1\n"
        "  set LLM_MODEL=deepseek-chat\n\n"
        "  # OpenAI\n"
        "  set LLM_API_KEY=sk-xxx\n"
        "  set LLM_MODEL=gpt-4o-mini\n\n"
        "  # Ollama (local)\n"
        "  set LLM_BASE_URL=http://localhost:11434/v1\n"
        "  set LLM_MODEL=qwen2.5:7b\n"
        "  set LLM_API_KEY=ollama              (Ollama ignores API key but requires non-empty)\n"
    )


# ── HTTP Client ────────────────────────────────────────────────────────────

def _chat_completion(system_prompt: str, user_prompt: str,
                     temperature: float = 0.3, max_tokens: int = 4096) -> str:
    """Send a chat completion request to an OpenAI-compatible API.

    Returns the assistant's response text.
    Raises RuntimeError on failure.
    """
    import requests  # only imported when actually used

    base_url = LLM_BASE_URL or _FALLBACK_URL
    model = LLM_MODEL or _FALLBACK_MODEL
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LLM_API_KEY}",
    }

    # Build provider-appropriate endpoint
    url = f"{base_url}/chat/completions"

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": False,
    }

    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.Timeout:
        raise RuntimeError("LLM request timed out after 60 seconds.")
    except requests.exceptions.ConnectionError as e:
        raise RuntimeError(f"Cannot connect to LLM endpoint: {base_url}. {e}")
    except requests.exceptions.HTTPError as e:
        detail = ""
        try:
            detail = f": {resp.text[:300]}"
        except Exception:
            pass
        raise RuntimeError(f"LLM API returned HTTP {resp.status_code}{detail}")
    except Exception as e:
        raise RuntimeError(f"LLM request failed: {e}")

    choices = data.get("choices", [])
    if not choices:
        raise RuntimeError("LLM returned no choices.")

    content = choices[0].get("message", {}).get("content", "")
    return content.strip()


# ── Script generation helper ───────────────────────────────────────────────

def generate_script(system_prompt: str, user_prompt: str) -> str:
    """Call LLM to generate a script definition from prompts.

    Returns raw JSON text. Caller is responsible for parsing and validation.
    """
    if not is_configured():
        raise RuntimeError(
            "LLM is not configured. " + config_help()
        )
    return _chat_completion(system_prompt, user_prompt)


def extract_json(text: str) -> str:
    """Extract JSON block from LLM response text.

    Handles:
      - Fenced code blocks ```json ... ```
      - Fenced code blocks ``` ... ```
      - Bare JSON (starts with {)
    """
    # Try json code fence first
    m = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", text, re.DOTALL)
    if m:
        return m.group(1).strip()

    # Try bare JSON
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if m:
        return m.group(0)

    return text.strip()
