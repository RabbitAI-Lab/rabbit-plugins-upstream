#!/usr/bin/env python3
"""Configuration loader for igamingreviews automation."""

import json
import os
from pathlib import Path

ROOT = Path(__file__).parent


def load_json(path: Path, default=None):
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default if default is not None else {}


def save_json(path: Path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# LLM bridge
BRIDGE_URL = os.environ.get("BRIDGE_URL", "http://127.0.0.1:5555/v1")
BRIDGE_API_KEY = os.environ.get("BRIDGE_API_KEY")
BRIDGE_MODEL = os.environ.get("BRIDGE_MODEL", "kimi-cli")

# SEO / generation
SEO_PASSES = int(os.environ.get("SEO_PASSES", "1"))
DRY_RUN = os.environ.get("DRY_RUN", "false").lower() in ("1", "true", "yes")
HUMANIZER_ENABLED = os.environ.get("HUMANIZER_ENABLED", "true").lower() in ("1", "true", "yes")

# WordPress credentials
CREDENTIALS_PATH = ROOT / "credentials.json"

# Data files
TOPICS_PATH = ROOT / "topics.json"
REVIEWS_PATH = ROOT / "reviews.json"
STATE_PATH = ROOT / "state.json"
SOCIAL_CREDENTIALS_PATH = ROOT / "social_credentials.json"

# Site settings
SITE_URL = "https://igamingreviews.org"

# Operators we never promote (Trevor's rule, 15/07/2026): worked there, bad actors.
OPERATOR_BLACKLIST = ["betway", "jackpot city", "jackpotcity", "super group"]
