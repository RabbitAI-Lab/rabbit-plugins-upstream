"""Tests for the standalone quota CLI provider registry and JSON contract."""
from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import threading
import time
from pathlib import Path
from types import ModuleType

import pytest


@pytest.fixture
def quota_cli() -> ModuleType:
    script = Path(__file__).parents[1] / "scripts" / "check-ai-quota.py"
    spec = importlib.util.spec_from_file_location("check_ai_quota", script)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_glm_flag_normalizes_percentage_payload(quota_cli, monkeypatch, capsys):
    monkeypatch.setattr(
        quota_cli,
        "fetch_glm_quota",
        lambda: {
            "session_pct": 37.5,
            "session_reset": "2026-07-17T00:00:00Z",
            "available_limit_pct": 62.5,
        },
    )

    code = quota_cli.main(["--json", "--glm"])

    payload = json.loads(capsys.readouterr().out)
    assert code == 0
    assert payload["errors"] == []
    assert payload["results"]["glm"] == {
        "provider": "glm",
        "plan": "z.ai",
        "session": {
            "used_pct": 37.5,
            "reset_iso": "2026-07-17T00:00:00Z",
        },
        "available_limit_pct": 62.5,
    }


def test_glm_human_output_does_not_claim_five_hour_window(quota_cli, monkeypatch, capsys):
    monkeypatch.setattr(
        quota_cli,
        "fetch_glm_quota",
        lambda: {
            "session_pct": 40,
            "session_reset": "2026-08-01T00:00:00Z",
        },
    )

    code = quota_cli.main(["--glm"])

    output = capsys.readouterr().out
    assert code == 0
    assert "quota period:" in output
    assert "5h session:" not in output


def test_deepseek_flag_selects_usd_balance(quota_cli, monkeypatch, capsys):
    monkeypatch.setattr(
        quota_cli,
        "fetch_deepseek_balance",
        lambda: {
            "is_available": True,
            "currency": "CNY",
            "balance": 100.0,
            "balances": [
                {"currency": "CNY", "total_balance": 100.0},
                {
                    "currency": "USD",
                    "total_balance": 14.25,
                    "granted_balance": 4.25,
                },
            ],
        },
    )

    code = quota_cli.main(["--json", "--deepseek"])

    payload = json.loads(capsys.readouterr().out)
    result = payload["results"]["deepseek"]
    assert code == 0
    assert result["provider"] == "deepseek"
    assert result["plan"] == "pay-as-you-go"
    assert result["currency"] == "USD"
    assert result["balance"] == 14.25
    assert result["granted_balance"] == 4.25


def test_no_flags_runs_all_providers_concurrently(quota_cli, monkeypatch, capsys):
    provider_names = ("claude", "codex", "gemini", "glm", "deepseek")
    barrier = threading.Barrier(len(provider_names), timeout=2)

    def make_fetcher(name):
        def fetch():
            barrier.wait()
            return {"provider": name, "plan": "test"}

        return fetch

    for name in provider_names:
        monkeypatch.setattr(quota_cli, f"{name}_quota", make_fetcher(name))

    code = quota_cli.main(["--json"])

    payload = json.loads(capsys.readouterr().out)
    assert code == 0
    assert list(payload["results"]) == list(provider_names)
    assert payload["errors"] == []


def test_lazy_adapter_preserves_all_plugin_fetchers(quota_cli, monkeypatch):
    calls = []
    adapter = ModuleType("quota_api")
    fetcher_names = (
        "fetch_claude_quota",
        "fetch_codex_quota",
        "fetch_gemini_quota",
        "fetch_glm_quota",
        "fetch_deepseek_balance",
    )

    def make_fetcher(name):
        def fetch():
            calls.append(name)
            return {"source": name}

        return fetch

    for name in fetcher_names:
        setattr(adapter, name, make_fetcher(name))
    monkeypatch.setattr(
        quota_cli.importlib,
        "import_module",
        lambda name: adapter if name == "quota_api" else None,
    )
    quota_cli._QUOTA_API = None

    results = [getattr(quota_cli, name)() for name in fetcher_names]

    assert calls == list(fetcher_names)
    assert results == [{"source": name} for name in fetcher_names]


def test_lazy_adapter_initialization_is_thread_safe(quota_cli, monkeypatch):
    worker_count = 5
    start = threading.Barrier(worker_count, timeout=2)
    adapter = ModuleType("quota_api")
    import_calls = []

    class RaceAmplifyingPath(list):
        def __contains__(self, item):
            if item == str(quota_cli.PLUGIN_DIR):
                return False
            return super().__contains__(item)

    plugin_path = str(quota_cli.PLUGIN_DIR)
    test_path = RaceAmplifyingPath(
        entry for entry in quota_cli.sys.path if entry != plugin_path
    )

    def import_adapter(name):
        import_calls.append(name)
        time.sleep(0.05)
        return adapter

    def load_adapter():
        start.wait()
        return quota_cli._quota_api()

    monkeypatch.setattr(quota_cli.sys, "path", test_path)
    monkeypatch.setattr(quota_cli.importlib, "import_module", import_adapter)
    quota_cli._QUOTA_API = None

    with quota_cli.ThreadPoolExecutor(max_workers=worker_count) as executor:
        loaded = list(executor.map(lambda _index: load_adapter(), range(worker_count)))

    assert loaded == [adapter] * worker_count
    assert import_calls == ["quota_api"]
    assert test_path.count(plugin_path) == 1


def test_lazy_adapter_wraps_module_load_errors(quota_cli, monkeypatch):
    def fail_import(_name):
        raise SyntaxError("broken adapter")

    monkeypatch.setattr(quota_cli.importlib, "import_module", fail_import)
    quota_cli._QUOTA_API = None

    with pytest.raises(RuntimeError, match="^quota_api dependency unavailable") as error:
        quota_cli._quota_api()

    assert isinstance(error.value.__cause__, SyntaxError)


def test_failure_isolated_and_exit_one(quota_cli, monkeypatch, capsys):
    monkeypatch.setattr(
        quota_cli,
        "claude_quota",
        lambda: {
            "provider": "claude",
            "plan": "pro",
            "session": {"used_pct": 12.0, "reset_iso": ""},
        },
    )
    monkeypatch.setattr(
        quota_cli,
        "fetch_glm_quota",
        lambda: None,
    )

    code = quota_cli.main(["--json", "--claude", "--glm"])

    payload = json.loads(capsys.readouterr().out)
    assert code == 1
    assert payload["results"]["claude"]["provider"] == "claude"
    assert "glm" not in payload["results"]
    assert payload["errors"] == [
        "GLM: GLM API key not found (set GLM_API_KEY or ZHIPU_API_KEY)",
    ]


def test_unknown_provider_is_reported_without_registry_key_error(quota_cli):
    results, errors = quota_cli.run_checks(["future_provider"])

    assert results == {}
    assert errors == ["Future Provider: provider is not registered"]


def test_each_requested_result_has_common_schema(quota_cli, monkeypatch, capsys):
    monkeypatch.setattr(
        quota_cli,
        "fetch_glm_quota",
        lambda: {"session_pct": 80},
    )
    monkeypatch.setattr(
        quota_cli,
        "fetch_deepseek_balance",
        lambda: {"balance": "3.50", "currency": "USD"},
    )

    code = quota_cli.main(["--json", "--glm", "--deepseek"])

    payload = json.loads(capsys.readouterr().out)
    assert code == 0
    for result in payload["results"].values():
        assert isinstance(result["provider"], str)
        assert isinstance(result["plan"], str)
    assert payload["results"]["glm"]["session"]["used_pct"] == 80.0
    assert payload["results"]["deepseek"]["balance"] == 3.5


def test_provider_flags_are_exposed_in_help(quota_cli):
    parser_args = quota_cli.parse_args(["--glm", "--deepseek", "--all"])
    assert parser_args.glm is True
    assert parser_args.deepseek is True
    assert parser_args.all is True


def test_french_human_errors_do_not_localize_json(quota_cli, monkeypatch, capsys):
    monkeypatch.setenv("HERMES_SESSION_LANGUAGE", "fr-FR")
    monkeypatch.setattr(quota_cli, "fetch_glm_quota", lambda: None)

    human_code = quota_cli.main(["--glm"])
    human_output = capsys.readouterr().out
    json_code = quota_cli.main(["--json", "--glm"])
    payload = json.loads(capsys.readouterr().out)

    assert human_code == json_code == 1
    assert "Erreurs: GLM: clé API GLM introuvable" in human_output
    assert payload["errors"] == [
        "GLM: GLM API key not found (set GLM_API_KEY or ZHIPU_API_KEY)",
    ]


def test_cli_without_external_plugin_reports_clean_errors(tmp_path):
    script = Path(__file__).parents[1] / "scripts" / "check-ai-quota.py"
    isolated_home = tmp_path / "home"
    isolated_home.mkdir()
    env = os.environ.copy()
    env.update(
        {
            "HOME": str(isolated_home),
            "HERMES_REAL_HOME": str(isolated_home),
            "HERMES_SESSION_LANGUAGE": "en",
        }
    )

    def run(*args):
        return subprocess.run(
            [sys.executable, "-I", str(script), *args],
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )

    help_run = run("--help")
    assert help_run.returncode == 0
    assert "AI CLI quota checker" in help_run.stdout
    assert "Traceback" not in help_run.stderr

    human_run = run("--claude")
    assert human_run.returncode == 1
    assert "Claude: quota_api dependency unavailable" in human_run.stdout
    assert "Traceback" not in human_run.stdout + human_run.stderr

    json_run = run("--json", "--claude")
    assert json_run.returncode == 1
    assert json.loads(json_run.stdout) == {
        "results": {},
        "errors": [
            "Claude: quota_api dependency unavailable; "
            "install the hermes-quota-status plugin"
        ],
    }
    assert "Traceback" not in json_run.stdout + json_run.stderr


def test_french_help_uses_session_language(quota_cli, monkeypatch, capsys):
    monkeypatch.setenv("HERMES_SESSION_LANGUAGE", "fr")

    with pytest.raises(SystemExit) as exit_info:
        quota_cli.parse_args(["--help"])

    assert exit_info.value.code == 0
    help_output = capsys.readouterr().out
    assert "Vérificateur de quota" in help_output
    assert "vérifier le quota GLM" in help_output
