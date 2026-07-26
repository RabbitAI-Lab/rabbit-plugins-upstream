#!/usr/bin/env python3
"""Centralized LLM bridge client with retries."""

import time

import requests

from config import BRIDGE_URL, BRIDGE_API_KEY, BRIDGE_MODEL


def chat(
    messages: list,
    temperature: float = 0.6,
    max_tokens: int = 4000,
    retries: int = 2,
    timeout: int = 300,
) -> str:
    """Send a chat completion request to the bridge and return the text content."""
    if not BRIDGE_API_KEY:
        raise RuntimeError("BRIDGE_API_KEY not set. Cannot generate content.")

    url = f"{BRIDGE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {BRIDGE_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": BRIDGE_MODEL,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    last_error = None
    for attempt in range(retries + 1):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=timeout)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except Exception as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(2 ** attempt)
            continue

    raise RuntimeError(f"LLM bridge failed after {retries + 1} attempts: {last_error}")
