#!/usr/bin/env python3
"""Resolve the client-name registry without shipping private names in the package."""

from __future__ import annotations

import os
from pathlib import Path


ENV_NAME = "OMNI_ECOM_CLIENT_REGISTRY"


def resolve_client_registry(package_root: Path) -> Path:
    """Prefer an explicit or user-private registry, then fall back to package examples."""
    explicit = os.environ.get(ENV_NAME, "").strip()
    if explicit:
        return Path(explicit).expanduser().resolve()

    private_registry = (
        Path.home()
        / ".workbuddy"
        / "private"
        / "omni-ecom"
        / "client-brand-registry.json"
    )
    if private_registry.is_file():
        return private_registry.resolve()

    return (package_root / "config" / "client-brand-registry.json").resolve()
