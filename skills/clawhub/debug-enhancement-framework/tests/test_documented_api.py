#!/usr/bin/env python3
"""Executes what the documentation promises, so the docs cannot drift.

WHY THIS EXISTS (v2.1.0)

v1.0.6 documented an API that did not exist. Measured before the fix:

  * 4 of 5 documented Python imports raised ModuleNotFoundError - every example
    said ``from debug_enhancement import ...`` and no such module shipped;
  * 5 documented shell helpers were missing (``profile_command``,
    ``monitor_memory``, ``dbg_reproduce``, ``dbg_fix``, ``dbg_verify``), three
    of them steps in the published 5-step bug-fixing workflow;
  * 2 documented CLI flags (``--diagnose``, ``--simulate-network-error``) did
    not exist - the real CLI uses subcommands;
  * a documented health endpoint had no server behind it.

An agent reading that documentation writes code that has never worked. The
skill was, in effect, a hallucination generator. Fixing the text once would not
stop it happening again, so this module makes the documentation *executable*:
every import, every shell helper and every CLI line named in SKILL.md is run
here. If the docs promise something the code does not provide, this fails.

Only names the docs actually claim are exercised, and every filesystem effect is
confined to a temporary directory.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_MD = ROOT / "SKILL.md"
DEBUGGER_SH = ROOT / "scripts" / "debugger.sh"


def sh(body: str, timeout: int = 120) -> subprocess.CompletedProcess:
    """Run a bash snippet with the framework sourced."""
    script = f'source "{DEBUGGER_SH}" >/dev/null 2>&1\n{body}\n'
    return subprocess.run(["bash", "-c", script], capture_output=True,
                          text=True, timeout=timeout)


class FrontmatterTest(unittest.TestCase):
    """v1.0.6 had NO YAML frontmatter at all - it faked it with bold markdown,
    so the skill could not be discovered by the Agent Skills standard."""

    def setUp(self) -> None:
        self.text = SKILL_MD.read_text(encoding="utf-8")

    def test_starts_with_yaml_frontmatter(self) -> None:
        self.assertTrue(self.text.startswith("---\n"),
                        "SKILL.md must open with a YAML frontmatter block")

    def test_has_required_fields(self) -> None:
        fm = self.text.split("---")[1]
        for field in ("name:", "description:", "version:"):
            self.assertIn(field, fm)

    def test_name_is_slug_safe_and_short(self) -> None:
        fm = self.text.split("---")[1]
        name = re.search(r"^name:\s*(\S+)", fm, re.M).group(1)
        self.assertRegex(name, r"^[a-z0-9][a-z0-9-]{0,63}$")

    def test_description_within_1024_chars(self) -> None:
        fm = self.text.split("---")[1]
        desc = re.search(r"description:\s*>\n(.*?)\nversion:", fm, re.S).group(1)
        self.assertLessEqual(len(" ".join(desc.split())), 1024)

    def test_version_matches_package(self) -> None:
        """v1.0.6 said 'Version: 2.0.0' in the body while the registry had 1.0.6."""
        sys.path.insert(0, str(ROOT))
        import debug_enhancement
        fm = self.text.split("---")[1]
        version = re.search(r"^version:\s*(\S+)", fm, re.M).group(1)
        self.assertEqual(version, debug_enhancement.__version__)


class DocumentedPythonImportsTest(unittest.TestCase):
    """Every `from debug_enhancement import ...` in SKILL.md must actually run."""

    def test_every_documented_import_executes(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8")
        imports = re.findall(r"^\s*from\s+(debug_enhancement)\s+import\s+([^\n]+)",
                             text, re.M)
        self.assertGreater(len(imports), 0, "expected documented imports to check")
        for module, names in imports:
            with self.subTest(names=names):
                r = subprocess.run(
                    [sys.executable, "-c",
                     f"import sys; sys.path.insert(0, {str(ROOT)!r})\n"
                     f"from {module} import {names}"],
                    capture_output=True, text=True, timeout=120)
                self.assertEqual(r.returncode, 0,
                                 f"documented import failed: from {module} import {names}\n{r.stderr}")

    def test_every_name_in_the_api_table_is_importable(self) -> None:
        sys.path.insert(0, str(ROOT))
        import debug_enhancement
        for name in debug_enhancement.__all__:
            with self.subTest(name=name):
                self.assertTrue(hasattr(debug_enhancement, name))


class DocumentedShellHelpersTest(unittest.TestCase):
    """The five helpers that used to be documented but missing."""

    HELPERS = ["dbg_log", "dbg_info", "dbg_warn", "dbg_error", "dbg_retry",
               "dbg_with_timeout", "dbg_time_command", "profile_command",
               "monitor_memory", "dbg_capture_state", "dbg_diagnose",
               "dbg_reproduce", "dbg_fix", "dbg_verify", "dbg_simulate_error"]

    def test_every_documented_helper_is_defined(self) -> None:
        for fn in self.HELPERS:
            with self.subTest(fn=fn):
                r = sh(f"declare -F {fn} >/dev/null && echo yes")
                self.assertIn("yes", r.stdout, f"{fn} is documented but not defined")

    def test_profile_command_emits_valid_json(self) -> None:
        r = sh('profile_command "sleep 0.01" 2>/dev/null | tail -1')
        payload = json.loads(r.stdout.strip())
        self.assertEqual(payload["exit_code"], 0)
        self.assertGreaterEqual(payload["elapsed_s"], 0.0)

    def test_monitor_memory_emits_valid_json(self) -> None:
        r = sh("monitor_memory --threshold 999999 2>/dev/null | tail -1")
        payload = json.loads(r.stdout.strip())
        self.assertFalse(payload["over_threshold"])
        self.assertEqual(payload["threshold_mb"], 999999)

    def test_reproduce_fix_verify_workflow(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "app.sh"
            target.write_text("#!/bin/bash\nexit 3\n", encoding="utf-8")
            rep = json.loads(sh(f'dbg_reproduce "bash {target}" 2>/dev/null | tail -1').stdout)
            self.assertEqual(rep["exit_code"], 3)
            fix = json.loads(sh(f"cd {td} && dbg_fix {target.name} 's/exit 3/exit 0/' 2>/dev/null | tail -1").stdout)
            self.assertTrue(fix["fixed"])
            self.assertTrue(Path(fix["backup"]).exists(), "dbg_fix must leave a backup")
            ver = json.loads(sh(f'dbg_verify "bash {target}" 0 2>/dev/null | tail -1').stdout)
            self.assertEqual(ver["verdict"], "FIXED")

    def test_dbg_fix_rolls_back_on_failure(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "f.txt"
            target.write_text("original\n", encoding="utf-8")
            sh(f"cd {td} && dbg_fix {target.name} 's/unclosed' 2>/dev/null")
            self.assertEqual(target.read_text(encoding="utf-8"), "original\n")


class CallerTrapPreservationTest(unittest.TestCase):
    """dbg_with_timeout used to run `trap - EXIT`, deleting the EXIT trap of the
    shell that sourced this library - silently disabling the caller's cleanup."""

    def test_caller_exit_trap_survives(self) -> None:
        script = (
            'cleanup(){ echo CALLER_CLEANUP_RAN; }\n'
            'trap cleanup EXIT\n'
            f'source "{DEBUGGER_SH}" >/dev/null 2>&1\n'
            'dbg_with_timeout 2 "true" >/dev/null 2>&1\n'
        )
        r = subprocess.run(["bash", "-c", script], capture_output=True,
                           text=True, timeout=120)
        self.assertIn("CALLER_CLEANUP_RAN", r.stdout,
                      "the caller's EXIT trap was destroyed by dbg_with_timeout")


class DocumentedCLITest(unittest.TestCase):
    """v1.0.6 documented --diagnose and --simulate-network-error; neither existed."""

    def _cli(self, script: str, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, str(ROOT / "scripts" / script), *args],
                              capture_output=True, text=True, timeout=300)

    def test_every_documented_cli_line_runs(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8")
        lines = [ln.strip() for blk in re.findall(r"```bash\n(.*?)```", text, re.S)
                 for ln in blk.splitlines()
                 if ln.strip().startswith("python3 scripts/")]
        self.assertGreater(len(lines), 0)
        for line in lines:
            line = line.split("#", 1)[0].strip()          # drop trailing comment
            line = re.sub(r"\[[^\]]*\]", "", line)          # drop [optional] groups
            argv = [a for a in line.split() if "|" not in a]
            script = argv[1].split("/")[-1]
            rest = argv[2:]
            if script == "debugger.py" and rest[:1] == ["simulate"]:
                rest = ["simulate", "network"]
            if script == "recovery.py" and rest[:1] == ["heal"]:
                rest = ["heal", "test error"]
            with self.subTest(cmd=" ".join([script] + rest)):
                r = self._cli(script, *rest)
                stderr = (r.stderr or "").lower()
                self.assertNotIn("invalid choice", stderr)
                self.assertNotIn("unrecognized arguments", stderr)
                self.assertNotIn("traceback", stderr)

    def test_simulate_accepts_all_documented_kinds(self) -> None:
        for kind in ("network", "timeout", "validation", "permission"):
            with self.subTest(kind=kind):
                r = self._cli("debugger.py", "simulate", kind)
                self.assertNotIn("invalid choice", (r.stderr or "").lower())


class DocumentedBehaviourTest(unittest.TestCase):
    """SKILL.md makes two behavioural promises that used to be false."""

    def setUp(self) -> None:
        sys.path.insert(0, str(ROOT))

    def test_retry_is_jittered_as_documented(self) -> None:
        """Docs promise full jitter. v1.0.6 had none: gaps were identical runs."""
        from debug_enhancement import RetryPolicy
        p = RetryPolicy(initial_delay=1.0, max_delay=60.0, backoff_multiplier=2.0)
        samples = [p.compute_delay(3) for _ in range(200)]
        self.assertGreater(len(set(samples)), 100, "delays are not randomised")
        cap = min(1.0 * 2 ** 2, 60.0)
        self.assertTrue(all(0.0 <= d <= cap for d in samples))

    def test_seeded_jitter_is_a_reproducible_sequence_not_a_constant(self) -> None:
        """Review catch: a fresh Random(seed) per call returned one value forever."""
        from debug_enhancement import RetryPolicy
        a = RetryPolicy(initial_delay=1.0, jitter_seed=7)
        b = RetryPolicy(initial_delay=1.0, jitter_seed=7)
        sa = [a.compute_delay(1) for _ in range(5)]
        sb = [b.compute_delay(1) for _ in range(5)]
        self.assertGreater(len(set(sa)), 1, "seeded jitter returned a constant")
        self.assertEqual(sa, sb, "same seed must reproduce the same sequence")

    def test_jitter_can_be_disabled_and_seeded(self) -> None:
        from debug_enhancement import RetryPolicy
        fixed = RetryPolicy(initial_delay=1.0, jitter=False)
        self.assertEqual([fixed.compute_delay(a) for a in (1, 2, 3)], [1.0, 2.0, 4.0])

    def test_retry_respects_max_delay_cap(self) -> None:
        from debug_enhancement import RetryPolicy
        p = RetryPolicy(initial_delay=1.0, max_delay=5.0)
        self.assertTrue(all(p.compute_delay(20) <= 5.0 for _ in range(200)))

    def test_shell_retry_is_not_lock_step(self) -> None:
        """dbg_retry was linear with no jitter while the docs claimed exponential."""
        runs = []
        for _ in range(3):
            r = sh('dbg_retry 4 1 "false" 2>&1 | grep -o "retrying in [0-9.]*s"')
            runs.append(r.stdout.strip())
        self.assertGreater(len(set(runs)), 1, "shell retry delays are identical across runs")


class WithHealingTest(unittest.TestCase):
    """v1.0.6: `with_healing` used @wraps without importing it, so this
    documented decorator raised NameError on first use. No test covered it;
    static analysis (ruff F821) found what 16 passing tests missed."""

    def setUp(self) -> None:
        sys.path.insert(0, str(ROOT))

    def test_decorator_does_not_raise_nameerror(self) -> None:
        from debug_enhancement import AutoHealer, with_healing

        @with_healing(AutoHealer("test"))
        def ok():
            return "worked"

        self.assertEqual(ok(), "worked")

    def test_wraps_preserves_metadata(self) -> None:
        from debug_enhancement import AutoHealer, with_healing

        @with_healing(AutoHealer("test"))
        def named_function():
            """docstring"""
            return 1

        self.assertEqual(named_function.__name__, "named_function")
        self.assertEqual(named_function.__doc__, "docstring")

    def test_heals_then_retries(self) -> None:
        from debug_enhancement import AutoHealer, with_healing
        state = {"n": 0}

        @with_healing(AutoHealer("test"))
        def flaky():
            state["n"] += 1
            if state["n"] == 1:
                raise ConnectionError("network failed")
            return "recovered"

        self.assertEqual(flaky(), "recovered")


class CleanupSafetyTest(unittest.TestCase):
    """v1.0.6: `recovery.py cleanup` with no arguments deleted *.tmp, *.cache and
    __pycache__ from bare /tmp - files belonging to every other process on the
    machine - with no confirmation and no dry run."""

    def test_cleanup_is_dry_run_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            victim = Path(td) / "precious.tmp"
            victim.write_text("do not delete", encoding="utf-8")
            r = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "recovery.py"), "cleanup"],
                capture_output=True, text=True, timeout=300)
            payload = json.loads(r.stdout)
            self.assertTrue(payload["dry_run"], "cleanup must default to a dry run")
            self.assertTrue(victim.exists())

    def test_cleanup_never_defaults_to_slash_tmp(self) -> None:
        r = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "recovery.py"), "cleanup"],
            capture_output=True, text=True, timeout=300)
        target = json.loads(r.stdout)["target"]
        self.assertNotEqual(Path(target), Path("/tmp"))

    def test_cleanup_does_not_escape_its_target(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from recovery import RecoveryStrategies
        with tempfile.TemporaryDirectory() as td:
            outside = Path(td) / "outside.tmp"
            outside.write_text("x", encoding="utf-8")
            inside = Path(td) / "sub"
            inside.mkdir()
            (inside / "a.tmp").write_text("y", encoding="utf-8")
            RecoveryStrategies.cleanup_temp_files(["**/*.tmp"], [str(inside)],
                                                  dry_run=False)
            self.assertTrue(outside.exists(), "cleanup escaped its target directory")


class DestructiveCapabilityGateTest(unittest.TestCase):
    """The registry scan flagged undisclosed install/kill/delete powers. Each is
    now refused unless the operator opts in - assert they stay that way."""

    def setUp(self) -> None:
        sys.path.insert(0, str(ROOT))
        import os
        os.environ.pop("DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE", None)

    def test_restart_service_refused_by_default(self) -> None:
        from debug_enhancement import RecoveryStrategies
        r = RecoveryStrategies.restart_service("some-service", ["true"])
        self.assertFalse(r.success)
        self.assertEqual(r.action_taken, "restart_refused")

    def test_pip_install_refused_by_default(self) -> None:
        from debug_enhancement import AutoHealer
        healer = AutoHealer("test")
        try:
            raise ImportError("No module named 'somepkg'")
        except ImportError as exc:
            r = healer.heal(exc)
        self.assertEqual(r.action_taken, "reinstall_refused")

    def test_unsafe_package_name_rejected_even_when_enabled(self) -> None:
        """The name is parsed out of an error message: untrusted input."""
        import os
        from debug_enhancement import AutoHealer
        os.environ["DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE"] = "1"
        try:
            healer = AutoHealer("test")
            try:
                raise ImportError("No module named 'evil; rm -rf /'")
            except ImportError as exc:
                r = healer.heal(exc)
            self.assertEqual(r.action_taken, "reinstall_rejected")
        finally:
            os.environ.pop("DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE", None)

    def test_capabilities_are_disclosed_in_frontmatter(self) -> None:
        fm = SKILL_MD.read_text(encoding="utf-8").split("---")[1]
        for key in ("capabilities:", "process:", "install:", "network:"):
            self.assertIn(key, fm, f"frontmatter must disclose {key}")


class NoSilentEgressTest(unittest.TestCase):
    """v2.1.1 and earlier curled clawhub.ai on every dbg_diagnose run, while the
    docs claimed no network access."""

    def test_no_hardcoded_remote_host(self) -> None:
        sh_src = DEBUGGER_SH.read_text(encoding="utf-8")
        self.assertNotIn("https://clawhub.ai", sh_src,
                         "diagnose must not contact a hardcoded remote host")

    def test_diagnose_makes_no_request_by_default(self) -> None:
        r = sh("dbg_diagnose 2>/dev/null | grep -A2 '=== Network ==='")
        self.assertIn("skipped", r.stdout,
                      "connectivity probe must be opt-in")

    def test_network_capability_is_declared_honestly(self) -> None:
        fm = SKILL_MD.read_text(encoding="utf-8").split("---")[1]
        net = re.search(r"network:\s*\"(.*?)\"", fm, re.S)
        self.assertIsNotNone(net, "frontmatter must declare network behaviour")
        text = net.group(1).lower()
        self.assertNotIn("none -", text,
                         "declaring 'none' is false: network_fallback performs HTTP")


class LibraryLevelGateTest(unittest.TestCase):
    """v2.1.4: the gate lived only in the CLI, so a DIRECT library call still
    deleted or replaced arbitrary paths. Reproduced before the fix."""

    def setUp(self) -> None:
        import os
        sys.path.insert(0, str(ROOT))
        os.environ.pop("DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE", None)

    def test_cleanup_library_call_is_gated(self) -> None:
        from debug_enhancement import RecoveryStrategies
        with tempfile.TemporaryDirectory() as td:
            victim = Path(td) / "victim.tmp"
            victim.write_text("data", encoding="utf-8")
            r = RecoveryStrategies.cleanup_temp_files(["**/*.tmp"], [td], dry_run=False)
            self.assertEqual(r.action_taken, "cleanup_refused")
            self.assertTrue(victim.exists())

    def test_recreate_directory_is_gated(self) -> None:
        from debug_enhancement import RecoveryStrategies
        with tempfile.TemporaryDirectory() as td:
            sub = Path(td) / "sub"; sub.mkdir()
            keep = sub / "keep.txt"; keep.write_text("x", encoding="utf-8")
            r = RecoveryStrategies.recreate_directory(str(sub))
            self.assertEqual(r.action_taken, "recreate_directory_refused")
            self.assertTrue(keep.exists())

    def test_rollback_to_backup_is_gated(self) -> None:
        from debug_enhancement import RecoveryStrategies
        with tempfile.TemporaryDirectory() as td:
            backup = Path(td) / "bk"; backup.write_text("backup", encoding="utf-8")
            target = Path(td) / "tg"; target.write_text("target", encoding="utf-8")
            r = RecoveryStrategies.rollback_to_backup(str(backup), str(target))
            self.assertEqual(r.action_taken, "rollback_refused")
            self.assertEqual(target.read_text(encoding="utf-8"), "target")

    def test_gate_open_still_permits_the_action(self) -> None:
        import os
        from debug_enhancement import RecoveryStrategies
        os.environ["DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE"] = "1"
        try:
            with tempfile.TemporaryDirectory() as td:
                victim = Path(td) / "x.tmp"; victim.write_text("d", encoding="utf-8")
                r = RecoveryStrategies.cleanup_temp_files(["**/*.tmp"], [td], dry_run=False)
                self.assertEqual(r.action_taken, "cleanup")
                self.assertFalse(victim.exists())
        finally:
            os.environ.pop("DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE", None)


class ScopingTest(unittest.TestCase):
    """v2.1.3: narrow the two remaining broad-by-default write paths."""

    def test_cleanup_apply_is_gated(self) -> None:
        import os
        env = dict(os.environ); env.pop("DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE", None)
        r = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "recovery.py"), "cleanup", "--apply"],
            capture_output=True, text=True, timeout=300, env=env)
        payload = json.loads(r.stdout)
        self.assertTrue(payload["gated"], "--apply must be gated")
        self.assertTrue(payload["dry_run"], "gated --apply must stay a dry run")

    def test_dbg_fix_refuses_outside_cwd(self) -> None:
        with tempfile.TemporaryDirectory() as outside:
            victim = Path(outside) / "elsewhere.txt"
            victim.write_text("original\n", encoding="utf-8")
            r = sh(f"cd {ROOT} && dbg_fix {victim} 's/original/hacked/'")
            self.assertNotEqual(r.returncode, 0)
            self.assertEqual(victim.read_text(encoding="utf-8"), "original\n")

    def test_dbg_fix_still_works_inside_cwd(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "in.txt"
            target.write_text("original\n", encoding="utf-8")
            r = sh(f"cd {td} && dbg_fix in.txt 's/original/fixed/' 2>/dev/null | tail -1")
            self.assertTrue(json.loads(r.stdout)["fixed"])
            self.assertEqual(target.read_text(encoding="utf-8"), "fixed\n")


class MachineReadableOutputTest(unittest.TestCase):
    """SKILL.md promises 'All emit JSON on stdout'. v1.0.6 printed prose, and
    `simulate` printed a raw Python traceback."""

    CASES = [("debugger.py", ["diagnose"]), ("debugger.py", ["report"]),
             ("debugger.py", ["list-captures"]),
             ("debugger.py", ["simulate", "network"]),
             ("recovery.py", ["health"]), ("recovery.py", ["heal", "network failed"]),
             ("recovery.py", ["cleanup"])]

    def test_stdout_is_always_parseable_json(self) -> None:
        for script, args in self.CASES:
            with self.subTest(cmd=f"{script} {' '.join(args)}"):
                r = subprocess.run(
                    [sys.executable, str(ROOT / "scripts" / script), *args],
                    capture_output=True, text=True, timeout=300)
                try:
                    json.loads(r.stdout)
                except Exception as exc:
                    self.fail(f"stdout is not JSON: {exc}\n{r.stdout[:200]}")

    def test_simulate_signals_via_exit_code_not_traceback(self) -> None:
        r = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "debugger.py"), "simulate", "network"],
            capture_output=True, text=True, timeout=300)
        self.assertEqual(r.returncode, 2)
        self.assertNotIn("Traceback", r.stderr)
        self.assertTrue(json.loads(r.stdout)["simulated"])

    def test_bare_diagnose_succeeds(self) -> None:
        """Documented as `diagnose [SKILL]`; bare invocation used to exit 1."""
        r = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "debugger.py"), "diagnose"],
            capture_output=True, text=True, timeout=300)
        self.assertEqual(r.returncode, 0)

    def test_disk_threshold_is_proportional(self) -> None:
        """A flat 100 GB threshold flagged healthy machines as low on disk."""
        src = (ROOT / "scripts" / "debugger.py").read_text(encoding="utf-8")
        self.assertNotIn("usage.free < 100 * 1024**3", src)
        r = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "debugger.py"), "diagnose"],
            capture_output=True, text=True, timeout=300)
        disk = json.loads(r.stdout)["environment"]["disk_space"]
        self.assertIn("free_percent", disk)


class NoUndocumentedClaimsTest(unittest.TestCase):
    """Claims removed in v2.1.0 must not creep back."""

    def test_no_health_endpoint_claim(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8")
        self.assertNotIn("localhost:8080", text,
                         "a health endpoint is claimed but no server ships")

    def test_no_debug_config_json_claim(self) -> None:
        text = SKILL_MD.read_text(encoding="utf-8")
        if ".debug_config.json" in text:
            self.assertTrue((ROOT / ".debug_config.json").exists())

    def test_no_deprecated_utcnow(self) -> None:
        for py in (ROOT / "scripts").glob("*.py"):
            self.assertNotIn("datetime.utcnow()", py.read_text(encoding="utf-8"),
                             f"{py.name} uses removed-in-future datetime.utcnow()")


if __name__ == "__main__":
    unittest.main(verbosity=2)
