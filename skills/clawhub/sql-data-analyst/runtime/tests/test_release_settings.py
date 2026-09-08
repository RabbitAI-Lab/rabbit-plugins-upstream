from __future__ import annotations

import base64
import hashlib
import json

import pytest

import sql_data_analyst_local.settings as settings
import sql_data_analyst_local.tickets as tickets
from sql_data_analyst_local.settings import SettingsError


def test_stamped_release_settings_accept_real_https_origin_and_digest(monkeypatch):
    monkeypatch.setattr(settings, "PLATFORM_API_ORIGIN", "https://ai-skills.open-idea.net")
    monkeypatch.setattr(settings, "TRUSTED_KEYS_SHA256", "a" * 64)

    settings.validate_release_settings()


@pytest.mark.parametrize(
    "origin",
    [
        "http://ai-skills.open-idea.net",
        "https://sql-data-analyst.invalid",
        "https://localhost",
        "https://127.0.0.1",
        "https://ai-skills.open-idea.net/path",
    ],
)
def test_release_settings_reject_placeholder_or_non_origin_urls(monkeypatch, origin):
    monkeypatch.setattr(settings, "PLATFORM_API_ORIGIN", origin)
    monkeypatch.setattr(settings, "TRUSTED_KEYS_SHA256", "a" * 64)

    with pytest.raises(SettingsError, match="^configuration_invalid$"):
        settings.validate_release_settings()


def test_default_ticket_verifier_pins_stamped_bundle_sha256(monkeypatch):
    encoded = base64.b64encode(b"k" * 32).decode("ascii")
    bundle = json.dumps(
        {"release-2026-01": encoded},
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )

    class Resource:
        def joinpath(self, _name):
            return self

        def read_text(self, *, encoding):
            assert encoding == "utf-8"
            return bundle

    monkeypatch.setattr(tickets, "files", lambda _package: Resource())
    monkeypatch.setattr(
        tickets,
        "TRUSTED_KEYS_SHA256",
        hashlib.sha256(bundle.encode("utf-8")).hexdigest(),
    )
    verifier = tickets.TicketVerifier()
    assert verifier is not None

    monkeypatch.setattr(tickets, "TRUSTED_KEYS_SHA256", "0" * 64)
    with pytest.raises(tickets.TicketError, match="^authorization_invalid$"):
        tickets.TicketVerifier()
