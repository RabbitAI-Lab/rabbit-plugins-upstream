#!/usr/bin/env python3
"""self_test.py — offline verification. No API keys, no network, no PDF needed.

Any agent runtime should run this first: it proves the skill is intact and that
the model-agnostic layer behaves identically wherever it is installed.

Checks
  1. every script compiles
  2. required files exist (including the v1.4 interop manifests)
  3. SKILL.md frontmatter carries the required publishing metadata
  4. the JSON tool spec is valid and matches the manifest
  5. app.js syntax (when node is available)
  6. the unit suite in tests/ (pytest if present, else a built-in runner)
  7. the model-agnostic layer: all dialects have adapters, the mock provider is
     deterministic, and the tolerant JSON parser survives every known model quirk
  8. the CLI contract: describe/doctor emit exactly one JSON document on stdout
"""
import json
import os
import py_compile
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
errors: list = []
checks = 0


def check(name, fn):
    global checks
    checks += 1
    try:
        fn()
    except Exception as exc:
        errors.append(f"{name}: {type(exc).__name__}: {exc}")


# 1. compile
def _compile():
    for p in sorted((ROOT / "scripts").glob("*.py")):
        py_compile.compile(str(p), doraise=True)
    for p in sorted((ROOT / "integrations").glob("*.py")):
        py_compile.compile(str(p), doraise=True)


check("compile", _compile)


# 2. files
REQUIRED = [
    "SKILL.md", "README.md", "AGENT_DISCOVERY.md", "CHANGELOG.md",
    "agent-manifest.json", "docs/WORKFLOW_PLAYBOOK.md", "docs/MODEL_COMPATIBILITY.md",
    "integrations/tool-spec.json", "integrations/mcp_server.py", "integrations/adapters.py",
    "integrations/README.md",
    "scripts/forge.py", "scripts/model_adapters.py", "scripts/common.py",
    "templates/guide.css", "templates/app.js", "templates/providers.example.json",
]
check("files", lambda: [_ for _ in REQUIRED if not (ROOT / _).is_file()] and
      (_ for _ in ()).throw(AssertionError(
          "missing: " + ", ".join(x for x in REQUIRED if not (ROOT / x).is_file()))))


# 3. frontmatter
def _frontmatter():
    text = (ROOT / "SKILL.md").read_text("utf-8")
    for token in ("name: persian-pdf-studyguide-forge", "version: 1.5.1",
                  "categories:", "topics:", "requires:", "emoji:"):
        assert token in text, f"SKILL.md frontmatter missing {token!r}"


check("frontmatter", _frontmatter)


# 4. manifests agree
def _manifests():
    man = json.loads((ROOT / "agent-manifest.json").read_text("utf-8"))
    spec = json.loads((ROOT / "integrations/tool-spec.json").read_text("utf-8"))
    assert man["version"] == "1.5.1", "agent-manifest version mismatch"
    cmds = {c["name"] for c in man["commands"]}
    enum = set(spec["input_schema"]["properties"]["command"]["enum"])
    assert cmds == enum, f"manifest/tool-spec command drift: {cmds ^ enum}"
    assert spec["input_schema"]["required"] == ["command"]


check("manifests", _manifests)


# 5. app.js
def _appjs():
    if shutil.which("node"):
        r = subprocess.run(["node", "--check", str(ROOT / "templates/app.js")],
                           capture_output=True)
        assert r.returncode == 0, r.stderr.decode()[:200]


check("app.js", _appjs)


# 6. unit suite
def _units():
    if shutil.which("pytest") or _has("pytest"):
        r = subprocess.run([sys.executable, "-m", "pytest", "-q", str(ROOT / "tests")],
                           capture_output=True, text=True, cwd=str(ROOT))
        assert r.returncode == 0, (r.stdout + r.stderr)[-600:]
    else:                                    # built-in runner, no pytest needed
        import tests.test_common as tc       # noqa
        fns = [v for k, v in vars(tc).items() if k.startswith("test_") and callable(v)]
        for fn in fns:
            fn()
        assert fns, "no tests discovered"


def _has(mod):
    import importlib.util
    return importlib.util.find_spec(mod) is not None


sys.path.insert(0, str(ROOT))
check("unit tests", _units)


# 7. model-agnostic layer
def _agnostic():
    import model_adapters as MA
    assert set(MA.DIALECTS) == set(MA._ADAPTERS), "a dialect has no adapter"
    p = MA.ProviderInfo(name="mock", dialect="mock", model="deterministic-mock")
    prompt = 'صفحه 1 — تست\n{"flash":[2 objects q,a,ref],"quiz":[1 item]}'
    a = MA.call_model(p, prompt, "sys", max_tokens=800, use_cache=False)
    b = MA.call_model(p, prompt, "sys", max_tokens=800, use_cache=False)
    assert a.text == b.text, "mock provider is not deterministic"
    doc = a.json()
    assert len(doc["flash"]) == 2 and len(doc["quiz"]) == 1, "mock contract broken"
    # tolerant parsing of every known model quirk
    for raw, want in (
        ('```json\n{"a":1}\n```', {"a": 1}),
        ('<think>reasoning</think>{"a":1}', {"a": 1}),
        ('\ufeff\u200f{"a":1}', {"a": 1}),
        ('{"a":[1,2,],}', {"a": [1, 2]}),
        ('prose before {"a":1} prose after', {"a": 1}),
    ):
        assert MA.parse_json_loose(raw) == want, f"parser failed on {raw!r}"
    assert MA.parse_json_loose('{"a":[1,2')["a"] == [1, 2], "truncation repair failed"
    assert MA._finish("end_turn") == "stop" and MA._finish("MAX_TOKENS") == "length"


check("model-agnostic layer", _agnostic)


# 8. CLI contract
def _cli():
    env = dict(os.environ, FORGE_MOCK="1", FORGE_VERBOSE="0")
    for cmd, allowed in (("describe", (0,)), ("doctor", (0, 3, 4))):
        r = subprocess.run([sys.executable, str(ROOT / "scripts/forge.py"), cmd],
                           capture_output=True, text=True, cwd=str(ROOT), env=env)
        assert r.returncode in allowed, f"{cmd} exit {r.returncode}"
        doc = json.loads(r.stdout)           # exactly one JSON document on stdout
        assert isinstance(doc, dict) and doc, f"{cmd} produced no JSON object"


check("CLI contract", _cli)


report = {
    "pass": not errors,
    "checks": checks,
    "python_scripts": len(list((ROOT / "scripts").glob("*.py"))),
    "version": "1.5.1",
    "network_used": False,
    "errors": errors,
}
print(json.dumps(report, indent=2, ensure_ascii=False))
raise SystemExit(0 if not errors else 1)
