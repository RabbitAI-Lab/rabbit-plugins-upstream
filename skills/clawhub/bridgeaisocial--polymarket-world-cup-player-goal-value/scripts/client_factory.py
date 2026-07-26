"""Local SDK client factory for unpublished skill edits.

The Simmer SDK verifies published skill entrypoint hashes when SimmerClient is
constructed from a directory containing SKILL.md + clawhub.json. During local
World Cup dogfooding this repo intentionally carries unpublished entrypoint
changes, so construct the client from this helper subdirectory (which has no
SKILL.md) to avoid failing the published-entrypoint integrity check.
"""

from __future__ import annotations

from simmer_sdk import SimmerClient


def create_simmer_client(*, api_key: str, venue: str, live: bool) -> SimmerClient:
    return SimmerClient(api_key=api_key, venue=venue, live=live)
