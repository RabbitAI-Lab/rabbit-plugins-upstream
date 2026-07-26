"""Test bootstrap.

Run the suite with (no local venv needed; ffmpeg not required for unit tests):

    cd podcast && uv run --default-index https://bytedpypi.byted.org/simple/ \
        --with pytest --with requests --with markdown \
        python -m pytest tests -q

Import order matters: the fake `tos` module MUST be registered before any
script module is imported, so every script transparently uses the in-memory
bucket. We never install the real tos SDK in the test env — the injection is
therefore guaranteed to be the only provider.
"""

import sys
from pathlib import Path

import pytest

TESTS_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = TESTS_DIR.parent / "scripts"
sys.path.insert(0, str(TESTS_DIR))
sys.path.insert(0, str(SCRIPTS_DIR))

import fake_tos  # noqa: E402

assert "tos" not in sys.modules or sys.modules["tos"].__name__ == "tos", "unexpected tos module"
sys.modules["tos"] = fake_tos.as_module()


@pytest.fixture()
def tos_bucket():
    """Fresh shared in-memory TOS bucket; yields the client class for assertions."""
    fake_tos.FakeTosClient.reset()
    yield fake_tos.FakeTosClient
    fake_tos.FakeTosClient.reset()


@pytest.fixture()
def tos_env(monkeypatch):
    monkeypatch.setenv("TOS_ACCESS_KEY", "test-ak")
    monkeypatch.setenv("TOS_SECRET_KEY", "test-sk")
    monkeypatch.setenv("TOS_BUCKET", "test-bucket")
    monkeypatch.setenv("TOS_REGION", "cn-test")


@pytest.fixture()
def no_sleep(monkeypatch):
    """Retry tests must not actually back off."""
    import script_synthesis
    monkeypatch.setattr(script_synthesis.time, "sleep", lambda *_: None)


@pytest.fixture()
def tts(monkeypatch):
    """A DoubaoTTS whose network is always faked by the test (api key irrelevant)."""
    from script_synthesis import DoubaoTTS
    return DoubaoTTS(api_key="test-key", host_voice="voice-host", guest_voice="voice-guest")
