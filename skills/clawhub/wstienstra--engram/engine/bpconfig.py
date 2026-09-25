#!/usr/bin/env python3
"""
bpconfig.py — shared config loader for Engram engine scripts.

All Engram engine files import this to resolve paths and model settings
from engram/engram.json instead of hardcoding them. This is the SINGLE
source of truth for every path/model in the package.

Resolution order:
  1. If ENGRAM_CONFIG env var is set, load that JSON file.
  2. Otherwise look for engram/engram.json relative to this file's parent
     (engine/ is inside engram/ after staging).
  3. Fall back to deriving paths from this file's location if no JSON found.
"""

import json
import os
import sys

_CACHE = {}


def _find_config_path():
    """Locate engram.json."""
    # 1. Env var
    env_p = os.environ.get("ENGRAM_CONFIG")
    if env_p and os.path.isfile(env_p):
        return env_p

    # 2. Relative to this file: engine/bpconfig.py → engram/bpconfig.py after staging
    #    or engine/bpconfig.py → ../engram/engram.json in package layout
    here = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(here, "engram.json"),           # engine/ next to engram.json (staged in engram/)
        os.path.join(os.path.dirname(here), "engram", "engram.json"),  # engine/ one level above engram/
        os.path.join(os.path.dirname(here), "templates", "engram.json"),  # package layout
    ]
    for c in candidates:
        if os.path.isfile(c):
            return c

    return None


def load_config():
    """Load and cache the engram.json config. Returns a dict."""
    if "cfg" in _CACHE:
        return _CACHE["cfg"]

    path = _find_config_path()
    if path:
        with open(path, "r") as f:
            cfg = json.load(f)
        # Expand __WORKSPACE__ placeholder if present
        ws = cfg.get("workspace", "")
        if "__WORKSPACE__" in ws:
            # Derive workspace from config file location: engram/engram.json → parent
            cfg["workspace"] = os.path.dirname(os.path.dirname(os.path.abspath(path)))
            for k in ("db_path", "engram_dir", "scripts_dir", "logs_dir", "backups_dir"):
                if k in cfg and isinstance(cfg[k], str):
                    cfg[k] = cfg[k].replace("__WORKSPACE__", cfg["workspace"])
        _CACHE["cfg"] = cfg
        return cfg

    # Fallback: derive everything from this file's location
    here = os.path.dirname(os.path.abspath(__file__))
    # If we're in engine/ inside engram/, workspace is two levels up
    # If we're in engine/ in the package, workspace can't be derived
    engram_dir = here
    # Check if we're inside a engram/ dir (staged)
    if os.path.basename(here) == "engine":
        # Could be engram/engine/ or package/engine/
        parent = os.path.dirname(here)
        if os.path.basename(parent) == "engram":
            engram_dir = parent
        else:
            engram_dir = os.path.join(parent, "engram")
    workspace = os.path.dirname(engram_dir) if os.path.basename(engram_dir) == "engram" else os.path.dirname(here)

    cfg = {
        "workspace": workspace,
        "db_path": os.path.join(engram_dir, "engram.db"),
        "engram_dir": engram_dir,
        "scripts_dir": os.path.join(workspace, "scripts"),
        "logs_dir": os.path.join(workspace, "logs"),
        "backups_dir": os.path.join(workspace, "backups", "engram"),
        "socket_path": "/tmp/engram-serve.sock",
        "pid_path": "/tmp/engram-serve.pid",
        "embed_model": "multilingual-e5-small",
        "embed_dim": 384,
        "sleep_model": "local",
        "ollama_url": "http://localhost:11434",
        "ollama_embed_model": "nomic-embed-text",
        "semantic_mode": "onnx",
        "flashrank_model": "ms-marco-TinyBERT-L-2-v2",
    }
    _CACHE["cfg"] = cfg
    return cfg


def get(key, default=None):
    """Get a single config value."""
    return load_config().get(key, default)


def engram_dir():
    return load_config()["engram_dir"]


def db_path():
    return load_config()["db_path"]


def workspace():
    return load_config()["workspace"]


def socket_path():
    return load_config()["socket_path"]


def pid_path():
    return load_config()["pid_path"]


def scripts_dir():
    return load_config()["scripts_dir"]


def logs_dir():
    return load_config()["logs_dir"]


def backups_dir():
    return load_config()["backups_dir"]


def semantic_mode():
    return load_config().get("semantic_mode", "onnx")


def ollama_url():
    return load_config().get("ollama_url", "http://localhost:11434")


def ollama_embed_model():
    return load_config().get("ollama_embed_model", "nomic-embed-text")