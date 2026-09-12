#!/usr/bin/env python3
"""Dependency-free regression tests for edge_cpu_tuner.py.

The integration test uses a deterministic fake llama-bench executable. It never
loads a model, installs a package, opens a network connection, or edits files
outside a temporary directory.
"""
from __future__ import annotations

import json
import os
import stat
import subprocess
import sys
import tempfile
import types
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import edge_cpu_tuner as tuner  # noqa: E402


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def test_host_and_plans() -> None:
    host = {"logical_cpus": 8, "physical_cpus": 4}
    check(tuner.thread_candidates(host) == [1, 2, 4, 8], "thread candidate topology")
    configs = tuner.plan_configs(host, "threads")
    check([x["threads"] for x in configs] == [1, 2, 4, 8], "thread sweep")
    all_configs = tuner.plan_configs(host, "all", max_configs=24)
    check(len(all_configs) <= 24, "all sweep cap")
    check(all(x["flash_attn"] in {"on", "off", "auto"} for x in all_configs), "flash values")
    plan_args = types.SimpleNamespace(sweep="baseline", threads=None, batches=None, depths=None,
                                      flash=None, binary=None, model=None, prompt_tokens=512,
                                      gen_tokens=128, repetitions=3, max_configs=24)
    plan = tuner.make_plan(plan_args)
    check(plan["commands"][0]["argv"] is None and plan["model"] is None, "asset-free plan")


def test_parsing_and_ranking() -> None:
    payload = json.dumps([
        {"test": "tg 128", "avg_ts": 10.0, "stddev_ts": 0.2, "n_threads": 1, "n_batch": 2048},
        {"test": "tg 128", "avg_ts": 12.0, "stddev_ts": 0.2, "n_threads": 2, "n_batch": 2048},
        {"test": "pp 512", "avg_ts": 40.0, "stddev_ts": 1.0, "n_threads": 2, "n_batch": 2048},
    ])
    records = tuner.parse_bench_output(payload)
    check(len(records) == 3, "JSON record count")
    ranked = tuner.rank_records(records, "tg", repetitions=3)
    check(ranked["recommendation"]["configuration"]["threads"] == 2, "winner configuration")
    check(ranked["recommendation"]["status"] == "winner", "high-confidence winner")
    csv_text = "test,n_threads,avg_ts,stddev_ts\ntg 128,2,12.5,0.4\n"
    check(len(tuner.parse_bench_output(csv_text)) == 1, "CSV fallback")


def test_argument_safety() -> None:
    config = {"threads": 1, "batch_size": 2, "ubatch_size": 2, "flash_attn": "auto",
              "cache_type_k": "f16", "cache_type_v": "f16", "context_depth": 0}
    argv = tuner.benchmark_argv("/bin/llama-bench", "/tmp/a; echo BAD.gguf", config, 1, 2, 1)
    check("/tmp/a; echo BAD.gguf" in argv and "echo" not in argv[1:], "argv is not shell-split")
    check("shell=True" not in Path(tuner.__file__).read_text(), "no shell execution")


def test_fake_benchmark() -> None:
    with tempfile.TemporaryDirectory(prefix="edge-cpu-tuner-test-") as raw:
        root = Path(raw)
        model = root / "tiny.gguf"
        model.write_bytes(b"not a real model; fake benchmark never opens it")
        check(not tuner.verify_gguf_magic(model), "invalid GGUF header is detectable")
        model.write_bytes(b"GGUF" + b"synthetic")
        check(tuner.verify_gguf_magic(model), "GGUF header check")
        fake = root / "llama-bench"
        fake.write_text("""#!/usr/bin/python3
import json, sys
threads = int(sys.argv[sys.argv.index('-t') + 1])
print(json.dumps([
  {'test': 'tg 128', 'avg_ts': 8.0 + threads, 'stddev_ts': 0.1,
   'n_threads': threads, 'n_batch': 2048, 'n_ubatch': 512,
   'flash_attn': 'auto', 'type_k': 'f16', 'type_v': 'f16'},
  {'test': 'pp 512', 'avg_ts': 20.0 + threads, 'stddev_ts': 0.1,
   'n_threads': threads, 'n_batch': 2048, 'n_ubatch': 512,
   'flash_attn': 'auto', 'type_k': 'f16', 'type_v': 'f16'}
]))
""")
        fake.chmod(fake.stat().st_mode | stat.S_IXUSR)
        report = root / "report.json"
        cmd = [sys.executable, str(HERE / "edge_cpu_tuner.py"), "bench",
               "--binary", str(fake), "--model", str(model), "--threads", "1,2",
               "--repetitions", "3", "--timeout", "10", "--out", str(report), "--json"]
        proc = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        check(proc.returncode == 0, f"fake bench failed: {proc.stdout} {proc.stderr}")
        data = json.loads(proc.stdout)
        check(data["recommendation"]["configuration"]["threads"] == 2, "fake bench winner")
        check(report.exists(), "report persisted")
        rec = subprocess.run([sys.executable, str(HERE / "edge_cpu_tuner.py"), "recommend",
                              "--report", str(report), "--json"], text=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        check(rec.returncode == 0, "recommend command")
        left, right = root / "left.txt", root / "right.txt"
        left.write_text("same\n")
        right.write_text("same\n")
        gate = subprocess.run([sys.executable, str(HERE / "edge_cpu_tuner.py"), "verify-output",
                               "--baseline", str(left), "--candidate", str(right), "--json"],
                              text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        check(gate.returncode == 0 and json.loads(gate.stdout)["identical"], "quality gate")


def main() -> int:
    tests = [test_host_and_plans, test_parsing_and_ranking, test_argument_safety, test_fake_benchmark]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"PASS all ({len(tests)} tests)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
