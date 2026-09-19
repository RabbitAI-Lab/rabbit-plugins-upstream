"""Configuration loader: YAML file + environment-variable overrides.

Layered config:
  1. config.yaml (defaults, committed)
  2. environment variables (IRANCHEM__SECTION__KEY) override anything above
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml

_DEFAULTS: dict[str, Any] = {
    "httrack": {
        "base_mirror_dir": "/var/lib/iran_chem_db/mirrors",
        "default_depth": 5,
        "default_ext_depth": 0,
        "default_connections_per_second": 2.0,
        "default_sockets": 4,
        "default_max_rate": 50000,
        "default_max_time": 7200,
        "default_robots_txt": 2,
        "user_agent": "IranChemDB/1.0 (Research Chemical Database crawler)",
        "supplier_overrides": {},
    },
    "playwright": {"enabled": True, "headless": True, "timeout_ms": 30000, "max_scroll_iterations": 50},
    # Inclusion policy for catalogue entries (remediation §5):
    #   research_only               — only explicit research/analytical-grade signals
    #   lab_or_research             — strict entries + ambiguous items from lab suppliers
    #   all_identifiable_catalogue  — every identifiable chemical entry (default);
    #                                 grade and confidence are retained as data, and
    #                                 excluded items are preserved in the audit table
    "parsing": {
        "inclusion_mode": "all_identifiable_catalogue",
        "retain_rejections": True,
        "reparse_failure_threshold": 0.05,   # fraction of sync/parse failures tolerated
        "resolve_cas_structures": True,      # CAS-only records -> PubChem structure (dedup)
    },
    "database": {"host": "localhost", "port": 5432, "name": "iran_chem_db", "user": "chemdb", "password": ""},
    "redis": {"url": "redis://localhost:6379/0"},
    "discovery": {
        "search_api_key": "",
        "auto_discover_interval_hours": 168,
        "min_verification_score": 60,
        "initial_directory_discovery": False,   # opt-in; slow, must never block seeding
        "directory_timeout_seconds": 120,       # per-directory budget
        "max_directories_per_run": 3,
        "max_new_candidates_per_run": 100,
    },
    "sync": {
        "high_priority_interval_hours": 6,
        "medium_priority_interval_hours": 24,
        "low_priority_interval_hours": 72,
        "force_full_remirror_after_days": 30,
        "mark_discontinued_after_missing": 3,
        "alert_unreachable_after_days": 7,
    },
    "logging": {"level": "INFO", "file": "/var/log/iran_chem_db/app.log", "max_size_mb": 100, "backup_count": 10},
    "storage": {"max_mirror_storage_gb": 500, "compress_old_mirrors": True, "compression_after_days": 30},
}


def _deep_merge(base: dict, override: dict) -> dict:
    out = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = _deep_merge(out[key], value)
        else:
            out[key] = value
    return out


def _expand_env(value: Any) -> Any:
    """Recursively expand ${VAR} placeholders in string values."""
    if isinstance(value, str):
        return os.path.expandvars(value)
    if isinstance(value, dict):
        return {k: _expand_env(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_expand_env(v) for v in value]
    return value


def _apply_env_overrides(cfg: dict) -> dict:
    """IRANCHEM__SECTION__KEY=value overrides."""
    prefix = "IRANCHEM__"
    for env_key, env_val in os.environ.items():
        if not env_key.startswith(prefix):
            continue
        parts = env_key[len(prefix):].lower().split("__")
        node = cfg
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        # best-effort type coercion
        if env_val.lower() in ("true", "false"):
            env_val_typed: Any = env_val.lower() == "true"
        elif env_val.isdigit():
            env_val_typed = int(env_val)
        else:
            try:
                env_val_typed = float(env_val)
            except ValueError:
                env_val_typed = env_val
        node[parts[-1]] = env_val_typed
    return cfg


def load_config(path: str | None = None) -> dict:
    """Load merged configuration."""
    cfg = dict(_DEFAULTS)
    config_path = Path(path) if path else Path(__file__).resolve().parent.parent / "config.yaml"
    if config_path.exists():
        with open(config_path, encoding="utf-8") as fh:
            file_cfg = yaml.safe_load(fh) or {}
        cfg = _deep_merge(cfg, file_cfg)
    cfg = _apply_env_overrides(cfg)
    return _expand_env(cfg)


class Config:
    """Singleton-ish accessor with attribute style access."""

    _instance: "Config | None" = None

    def __init__(self, data: dict):
        object.__setattr__(self, "_data", data)

    def __getattr__(self, key: str) -> Any:
        data = object.__getattribute__(self, "_data")
        if key in data:
            value = data[key]
            if isinstance(value, dict):
                return Config(value)
            return value
        raise AttributeError(key)

    @classmethod
    def load(cls, path: str | None = None) -> "Config":
        if cls._instance is None:
            cls._instance = cls(load_config(path))
        return cls._instance

    def as_dict(self) -> dict:
        return object.__getattribute__(self, "_data")


def get_config() -> Config:
    return Config.load()
