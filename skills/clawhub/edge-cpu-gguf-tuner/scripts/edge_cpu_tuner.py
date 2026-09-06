#!/usr/bin/env python3
"""Safe, evidence-first llama.cpp CPU/GGUF tuning helper.

The program is intentionally stdlib-only and offline by default. It does not
install llama.cpp, download models, call a cloud API, execute a shell, or edit
source files. A benchmark is run only when the user explicitly supplies a
local llama-bench executable and a local model path. Every recommendation is a
measured result or an explicitly labelled plan; host-specific observations are
never promoted to universal defaults.
"""
from __future__ import annotations

import argparse
import csv
import datetime as _dt
import hashlib
import json
import math
import os
import platform
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Iterable, Sequence

TOOL_VERSION = "1.2.0"
SCHEMA = "edge-cpu-gguf-tuner.report.v1"
PLAN_SCHEMA = "edge-cpu-gguf-tuner.plan.v1"

# Only variables needed for a normal local binary invocation are inherited.
# Dynamic-loader injection and Python startup hooks are deliberately excluded.
SAFE_ENV_KEYS = {
    "PATH", "HOME", "USER", "LOGNAME", "LANG", "LC_ALL", "LC_CTYPE",
    "TMPDIR", "TEMP", "TMP", "TERM", "COLORTERM",
}
DANGEROUS_ENV_KEYS = {
    "LD_PRELOAD", "LD_AUDIT", "DYLD_INSERT_LIBRARIES", "DYLD_LIBRARY_PATH",
    "PYTHONPATH", "PYTHONHOME", "PYTHONINSPECT", "PYTHONSTARTUP", "BASH_ENV",
    "ENV", "CDPATH",
}


def utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def json_dump(value: Any, compact: bool = False) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":") if compact else (",", ": "))


def die(message: str, code: int = 2) -> None:
    raise TunerError(message, code)


class TunerError(Exception):
    def __init__(self, message: str, code: int = 2):
        super().__init__(message)
        self.code = code


def safe_env() -> dict[str, str]:
    env = {k: v for k, v in os.environ.items() if k in SAFE_ENV_KEYS and k not in DANGEROUS_ENV_KEYS}
    env.setdefault("PATH", os.defpath)
    env["LC_ALL"] = "C"
    return env


def redact_text(text: str, limit: int = 2000) -> str:
    """Keep diagnostics useful while not echoing credential-shaped values."""
    text = text or ""
    patterns = [
        (r"(?i)(api[_-]?key|access[_-]?token|secret|password|authorization)(\s*[=:]\s*)[^\s,;]+", r"\1\2[REDACTED]"),
        (r"(?i)bearer\s+[A-Za-z0-9._~+/=-]+", "Bearer [REDACTED]"),
    ]
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)
    return text[-limit:]


def resolve_file(value: str, label: str, executable: bool = False, suffix: str | None = None) -> Path:
    if not value:
        die(f"{label} is required")
    raw = Path(value).expanduser()
    try:
        path = raw.resolve(strict=True)
    except FileNotFoundError:
        die(f"{label} does not exist: {value}")
    except OSError as exc:
        die(f"cannot resolve {label}: {exc}")
    if not path.is_file():
        die(f"{label} is not a regular file: {path}")
    if executable and not os.access(path, os.X_OK):
        die(f"{label} is not executable: {path}")
    if suffix and path.suffix.lower() != suffix.lower():
        die(f"{label} must end in {suffix}: {path}")
    if not os.access(path, os.R_OK):
        die(f"{label} is not readable: {path}")
    return path


def check_allowed_root(path: Path, root_value: str | None, label: str) -> None:
    if not root_value:
        return
    root = Path(root_value).expanduser().resolve(strict=True)
    try:
        path.relative_to(root)
    except ValueError:
        die(f"{label} is outside --allowed-root: {path}")


def resolve_directory(value: str | None, label: str) -> str | None:
    if not value:
        return None
    try:
        path = Path(value).expanduser().resolve(strict=True)
    except FileNotFoundError:
        die(f"{label} does not exist: {value}")
    except OSError as exc:
        die(f"cannot resolve {label}: {exc}")
    if not path.is_dir():
        die(f"{label} is not a directory: {path}")
    return str(path)


def resolve_executable(value: str | None, candidates: Sequence[str], label: str) -> Path | None:
    if value:
        path = Path(value).expanduser()
        if path.parent != Path('.') or os.sep in value:
            return resolve_file(value, label, executable=True)
        found = shutil.which(value)
        if found:
            return resolve_file(found, label, executable=True)
        die(f"{label} not found on PATH: {value}")
    for candidate in candidates:
        found = shutil.which(candidate)
        if found:
            try:
                return resolve_file(found, label, executable=True)
            except TunerError:
                continue
    return None


def run_process(argv: Sequence[str], timeout: float, cwd: str | None = None,
                max_output_bytes: int = 8 * 1024 * 1024) -> subprocess.CompletedProcess[str]:
    if not argv or any(not isinstance(x, str) or "\x00" in x for x in argv):
        die("invalid process arguments")
    if max_output_bytes < 1:
        die("max_output_bytes must be positive")
    timeout_value = float(timeout)
    if not math.isfinite(timeout_value) or timeout_value <= 0:
        die("timeout must be a finite positive number")
    try:
        proc = subprocess.run(
            list(argv), shell=False, cwd=cwd, env=safe_env(), text=True,
            encoding="utf-8", errors="replace",
            stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=timeout_value, check=False,
        )
        output_size = len(proc.stdout.encode("utf-8", "replace")) + len(proc.stderr.encode("utf-8", "replace"))
        if output_size > max_output_bytes:
            raise TunerError(f"process output exceeded {max_output_bytes} bytes: {argv[0]}", 1)
        return proc
    except subprocess.TimeoutExpired as exc:
        raise TunerError(f"process timed out after {timeout:g}s: {argv[0]}", 124) from exc
    except OSError as exc:
        raise TunerError(f"could not execute {argv[0]}: {exc}", 127) from exc


def read_meminfo() -> dict[str, int]:
    values: dict[str, int] = {}
    try:
        for line in Path("/proc/meminfo").read_text(errors="replace").splitlines():
            match = re.match(r"^(\w+):\s+(\d+)\s+kB", line)
            if match:
                values[match.group(1)] = int(match.group(2)) * 1024
    except OSError:
        pass
    return values


def cpu_runtime_state() -> dict[str, Any]:
    governors: dict[str, int] = {}
    for path in Path("/sys/devices/system/cpu").glob("cpu[0-9]*/cpufreq/scaling_governor"):
        try:
            value = path.read_text().strip()
        except OSError:
            continue
        if value:
            governors[value] = governors.get(value, 0) + 1
    temperatures: list[dict[str, Any]] = []
    for path in Path("/sys/class/thermal").glob("thermal_zone*/temp"):
        try:
            raw = int(path.read_text().strip())
        except (OSError, ValueError):
            continue
        # Linux thermal-zone temperatures are commonly millidegrees Celsius;
        # keep the raw value too because firmware/OS conventions can differ.
        temperatures.append({"zone": path.parent.name, "raw": raw,
                             "celsius": round(raw / 1000.0, 3) if abs(raw) > 200 else raw})
    return {"cpu_governors": governors, "thermal_zones": temperatures}


def physical_cpu_count(logical: int | None = None) -> tuple[int, str]:
    pairs: set[tuple[str, str]] = set()
    topology = Path("/sys/devices/system/cpu")
    try:
        for cpu in topology.glob("cpu[0-9]*"):
            core = (cpu / "topology/core_id").read_text().strip()
            package_file = cpu / "topology/physical_package_id"
            package = package_file.read_text().strip() if package_file.exists() else "0"
            if core:
                pairs.add((package, core))
    except OSError:
        pairs.clear()
    if pairs:
        return max(1, len(pairs)), "sysfs topology"
    # Linux /proc fallback; useful in containers where sysfs is masked.
    try:
        current: dict[str, str] = {}
        for line in Path("/proc/cpuinfo").read_text(errors="replace").splitlines() + [""]:
            if not line.strip():
                if "core id" in current:
                    pairs.add((current.get("physical id", "0"), current["core id"]))
                current = {}
                continue
            if ":" in line:
                key, value = line.split(":", 1)
                current[key.strip()] = value.strip()
        if pairs:
            return max(1, len(pairs)), "/proc/cpuinfo"
    except OSError:
        pass
    return max(1, logical or os.cpu_count() or 1), "logical CPU fallback"


def inspect_host() -> dict[str, Any]:
    logical = max(1, os.cpu_count() or 1)
    physical, physical_source = physical_cpu_count(logical)
    physical = min(physical, logical)
    mem = read_meminfo()
    result: dict[str, Any] = {
        "schema": "edge-cpu-gguf-tuner.host.v1",
        "platform": platform.platform(),
        "system": platform.system(),
        "machine": platform.machine(),
        "python": platform.python_version(),
        "logical_cpus": logical,
        "physical_cpus": physical,
        "physical_cpu_source": physical_source,
        "memory_bytes": {k: mem[k] for k in ("MemTotal", "MemAvailable", "SwapTotal", "SwapFree") if k in mem},
        "load_average": list(os.getloadavg()) if hasattr(os, "getloadavg") else None,
        "binaries": {},
        "runtime_state": cpu_runtime_state(),
        "observed_at": utc_now(),
    }
    candidates = {
        "llama_bench": ("llama-bench", "llama_bench"),
        "llama_cli": ("llama-cli", "llama", "llama-completion"),
        "cmake": ("cmake",),
    }
    for key, names in candidates.items():
        found = None
        for name in names:
            path = shutil.which(name)
            if path:
                found = str(Path(path).resolve())
                break
        result["binaries"][key] = found
    return result


def thread_candidates(host: dict[str, Any]) -> list[int]:
    logical = max(1, int(host.get("logical_cpus") or 1))
    physical = max(1, min(logical, int(host.get("physical_cpus") or logical)))
    values: list[int] = []
    n = 1
    while n < physical:
        values.append(n)
        n *= 2
    values.append(physical)
    if logical != physical:
        values.append(logical)
    return sorted({max(1, min(logical, int(v))) for v in values})


def parse_int_list(value: str, label: str, minimum: int = 0) -> list[int]:
    values: list[int] = []
    for item in value.split(","):
        item = item.strip()
        if not re.fullmatch(r"\d+", item):
            die(f"{label} must be a comma-separated list of integers: {value}")
        number = int(item)
        if number < minimum:
            die(f"{label} values must be >= {minimum}")
        values.append(number)
    if not values:
        die(f"{label} cannot be empty")
    return sorted(set(values))


def plan_configs(host: dict[str, Any], sweep: str = "threads", threads: list[int] | None = None,
                 batches: list[int] | None = None, flash: list[str] | None = None,
                 cache: list[tuple[str, str]] | None = None, depths: list[int] | None = None,
                 max_configs: int = 24) -> list[dict[str, Any]]:
    threads = threads or thread_candidates(host)
    physical = max(1, min(int(host.get("logical_cpus") or 1), int(host.get("physical_cpus") or 1)))
    base = {"threads": physical, "batch_size": 2048, "ubatch_size": 512,
            "flash_attn": "auto", "cache_type_k": "f16", "cache_type_v": "f16", "context_depth": 0}
    configs: list[dict[str, Any]] = []

    def add(**changes: Any) -> None:
        item = dict(base)
        item.update(changes)
        if item not in configs:
            configs.append(item)

    if sweep in ("threads", "all"):
        for value in threads:
            add(threads=value)
    if sweep in ("batch", "all"):
        for value in (batches or [512, 1024, 2048]):
            add(batch_size=value)
    if sweep in ("flash", "all"):
        for value in (flash or ["off", "auto", "on"]):
            add(flash_attn=value)
    if sweep in ("kv", "all"):
        pairs = cache or [("f16", "f16"), ("q8_0", "f16"), ("f16", "q8_0"), ("q8_0", "q8_0")]
        for key, value in pairs:
            add(cache_type_k=key, cache_type_v=value)
    if sweep in ("context", "all"):
        for value in (depths or [0, 512, 2048]):
            add(context_depth=value)
    if sweep == "baseline":
        add()
    if not configs:
        die(f"unknown or empty sweep: {sweep}")
    if len(configs) > max_configs:
        die(f"sweep would run {len(configs)} configurations; raise --max-configs only deliberately")
    return configs


def benchmark_argv(binary: str, model: str, config: dict[str, Any], prompt_tokens: int,
                   gen_tokens: int, repetitions: int) -> list[str]:
    # These are current llama-bench short options documented upstream. Use argv,
    # not shell text, so model paths cannot become shell syntax.
    return [binary, "-m", model, "-p", str(prompt_tokens), "-n", str(gen_tokens),
            "-t", str(config["threads"]), "-b", str(config["batch_size"]),
            "-ub", str(config["ubatch_size"]), "-fa", str(config["flash_attn"]),
            "-ctk", str(config["cache_type_k"]), "-ctv", str(config["cache_type_v"]),
            "-d", str(config["context_depth"]), "-r", str(repetitions), "-o", "json"]


def numeric(value: Any) -> float | None:
    if value is None or isinstance(value, bool):
        return None
    try:
        number = float(str(value).strip())
        return number if math.isfinite(number) else None
    except (TypeError, ValueError):
        return None


def extract_json_records(text: str) -> list[dict[str, Any]]:
    text = text.strip()
    if not text:
        return []
    candidates: list[Any] = []
    try:
        candidates.append(json.loads(text))
    except json.JSONDecodeError:
        # Some builds may print a short diagnostic before JSON. Search only for
        # a JSON array/object; do not execute or evaluate the diagnostic.
        for marker in ("[", "{"):
            start = text.find(marker)
            if start >= 0:
                try:
                    candidates.append(json.loads(text[start:]))
                    break
                except json.JSONDecodeError:
                    pass
        if not candidates:
            for line in text.splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    candidates.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    records: list[dict[str, Any]] = []
    for value in candidates:
        if isinstance(value, list):
            records.extend(x for x in value if isinstance(x, dict))
        elif isinstance(value, dict):
            nested = value.get("results") or value.get("benchmarks") or value.get("data")
            if isinstance(nested, list):
                records.extend(x for x in nested if isinstance(x, dict))
            else:
                records.append(value)
    return records


def csv_records(text: str) -> list[dict[str, Any]]:
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines or "avg_ts" not in lines[0]:
        return []
    try:
        return list(csv.DictReader(lines))
    except csv.Error:
        return []


def normalize_record(record: dict[str, Any]) -> dict[str, Any] | None:
    # Current llama-bench JSON/CSV names are kept first; aliases make reports
    # useful with a few older builds without pretending the outputs are equal.
    avg = next((numeric(record.get(k)) for k in ("avg_ts", "avg_t_s", "tokens_per_second", "tps") if record.get(k) is not None), None)
    if avg is None or avg < 0:
        return None
    std = next((numeric(record.get(k)) for k in ("stddev_ts", "stddev_t_s", "stddev", "tps_stddev") if record.get(k) is not None), 0.0) or 0.0
    test_raw = str(record.get("test", record.get("type", "unknown"))).strip().lower()
    match = re.search(r"\b(pp|tg|pg)\b", test_raw)
    test_type = match.group(1) if match else ("pp" if test_raw.startswith("pp") else "tg" if test_raw.startswith("tg") else "unknown")
    def first(keys: Sequence[str]) -> Any:
        for key in keys:
            if key in record and record[key] not in (None, ""):
                return record[key]
        return None
    result: dict[str, Any] = {
        "test": test_raw,
        "test_type": test_type,
        "avg_tokens_per_second": avg,
        "stddev_tokens_per_second": std,
    }
    field_aliases = {
        "threads": ("n_threads", "threads"),
        "batch_size": ("n_batch", "batch_size"),
        "ubatch_size": ("n_ubatch", "ubatch_size"),
        "flash_attn": ("flash_attn", "flash-attn"),
        "cache_type_k": ("type_k", "cache_type_k"),
        "cache_type_v": ("type_v", "cache_type_v"),
        "context_depth": ("n_depth", "context_depth"),
        "prompt_tokens": ("n_prompt", "prompt_tokens"),
        "generation_tokens": ("n_gen", "generation_tokens"),
        "model": ("model_filename", "model"),
        "backend": ("backends", "backend"),
        "build_commit": ("build_commit",),
    }
    for output_key, keys in field_aliases.items():
        value = first(keys)
        if value is not None:
            result[output_key] = value
    return result


def parse_bench_output(text: str) -> list[dict[str, Any]]:
    records = extract_json_records(text)
    if not records:
        records = csv_records(text)
    normalized = []
    for record in records:
        item = normalize_record(record)
        if item:
            normalized.append(item)
    return normalized


def record_configuration(record: dict[str, Any]) -> dict[str, Any]:
    keys = ("threads", "batch_size", "ubatch_size", "flash_attn", "cache_type_k", "cache_type_v", "context_depth")
    return {key: record[key] for key in keys if key in record}


def rank_records(records: Iterable[dict[str, Any]], metric: str = "tg", repetitions: int | None = None) -> dict[str, Any]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    invalid_records = 0
    for record in records:
        test_type = record.get("test_type", "unknown")
        avg = numeric(record.get("avg_tokens_per_second"))
        std = numeric(record.get("stddev_tokens_per_second", 0.0))
        if test_type in ("pp", "tg", "pg") and avg is not None and avg >= 0 and std is not None and std >= 0:
            grouped.setdefault(test_type, []).append(record)
        else:
            invalid_records += 1
    ranked: dict[str, list[dict[str, Any]]] = {}
    for test_type, rows in grouped.items():
        def key(row: dict[str, Any]) -> float:
            avg = float(row["avg_tokens_per_second"])
            std = abs(float(row.get("stddev_tokens_per_second", 0.0)))
            cv = std / avg if avg else float("inf")
            # Penalize noisy observations only modestly; primary ordering stays
            # tokens/sec so the report remains interpretable.
            return avg * max(0.0, 1.0 - min(cv, 0.25))
        ordered = sorted(rows, key=key, reverse=True)
        output = []
        for row in ordered:
            avg = float(row["avg_tokens_per_second"])
            std = abs(float(row.get("stddev_tokens_per_second", 0.0)))
            output.append({
                "configuration": record_configuration(row),
                "tokens_per_second": avg,
                "stddev_tokens_per_second": std,
                "coefficient_variation": (std / avg if avg else None),
                "test": row.get("test"),
                "model": row.get("model"),
                "build_commit": row.get("build_commit"),
            })
        ranked[test_type] = output
    target = ranked.get(metric, [])
    recommendation: dict[str, Any] = {"metric": metric, "status": "no_data", "confidence": "none"}
    if target:
        best = target[0]
        second = target[1] if len(target) > 1 else None
        margin = None
        if second and second["tokens_per_second"] > 0:
            margin = (best["tokens_per_second"] - second["tokens_per_second"]) / second["tokens_per_second"]
        cv = best.get("coefficient_variation")
        reps = repetitions or 0
        if len(target) == 1:
            status, confidence = "single_observation", "low"
        elif margin is not None and margin >= 0.05 and (cv is None or cv <= 0.05) and reps >= 3:
            status, confidence = "winner", "high"
        elif margin is not None and margin >= 0.02:
            status, confidence = "provisional_winner", "medium"
        else:
            status, confidence = "no_clear_winner", "low"
        recommendation = {
            "metric": metric, "status": status, "confidence": confidence,
            "configuration": best["configuration"],
            "tokens_per_second": best["tokens_per_second"],
            "stddev_tokens_per_second": best["stddev_tokens_per_second"],
            "coefficient_variation": cv, "margin_vs_second": margin,
            "reason": "local measurement only; re-run after changing model, binary, build, or host",
        }
    return {"ranked": ranked, "recommendation": recommendation, "invalid_records": invalid_records}


def model_metadata(model: Path, hash_model: bool = False) -> dict[str, Any]:
    stat = model.stat()
    data: dict[str, Any] = {"path": str(model), "size_bytes": stat.st_size, "mtime_ns": stat.st_mtime_ns}
    if hash_model:
        digest = hashlib.sha256()
        with model.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        data["sha256"] = digest.hexdigest()
    return data


def verify_gguf_magic(model: Path) -> bool:
    try:
        with model.open("rb") as handle:
            return handle.read(4) == b"GGUF"
    except OSError as exc:
        die(f"could not read GGUF header: {exc}")
    return False


def version_probe(binary: Path) -> str | None:
    try:
        proc = run_process([str(binary), "--version"], 8)
    except TunerError:
        return None
    text = (proc.stdout or proc.stderr).strip()
    return redact_text(text, 500) if text else None


def make_plan(args: argparse.Namespace) -> dict[str, Any]:
    host = inspect_host()
    sweep = args.sweep
    threads = parse_int_list(args.threads, "--threads", 1) if args.threads else None
    batches = parse_int_list(args.batches, "--batches", 1) if args.batches else None
    depths = parse_int_list(args.depths, "--depths", 0) if args.depths else None
    flash = [x.strip() for x in args.flash.split(",")] if args.flash else None
    if flash and any(x not in {"on", "off", "auto"} for x in flash):
        die("--flash values must be on, off, or auto")
    if args.binary:
        candidate = shutil.which(args.binary) if os.sep not in args.binary else args.binary
        binary = str(Path(candidate).expanduser().resolve()) if candidate else args.binary
    else:
        binary = host["binaries"].get("llama_bench")
    model = str(Path(args.model).expanduser().resolve()) if args.model else None
    configs = plan_configs(host, sweep, threads, batches, flash, None, depths, args.max_configs)
    commands = []
    for config in configs:
        if binary and model:
            argv = benchmark_argv(binary, model, config, args.prompt_tokens, args.gen_tokens, args.repetitions)
            rendered = {"argv": argv, "shell": shlex.join(argv)}
        else:
            rendered = {"argv": None, "shell": None}
        commands.append({"configuration": config, **rendered, "runs": args.repetitions})
    return {
        "schema": PLAN_SCHEMA, "tool_version": TOOL_VERSION, "created_at": utc_now(),
        "offline": True, "sweep": sweep, "host": host,
        "model": model, "binary": binary,
        "prompt_tokens": args.prompt_tokens, "generation_tokens": args.gen_tokens,
        "repetitions": args.repetitions, "commands": commands,
        "notes": [
            "One variable changes per configuration; this is a plan, not a universal default.",
            "llama-bench throughput excludes tokenization and sampling; compare end-to-end latency separately.",
            "Use an updated llama.cpp binary and a non-privileged account. No model or binary is downloaded by this tool.",
        ],
    }


def do_bench(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    host = inspect_host()
    if not args.binary:
        die("--binary is required for bench; inspect/plan may discover PATH candidates, but execution requires an explicit local binary")
    binary = resolve_executable(args.binary, ("llama-bench", "llama_bench"), "llama-bench")
    if binary is None:
        die("llama-bench was not found; pass --binary /path/to/llama-bench")
    model = resolve_file(args.model, "model", suffix=None)
    check_allowed_root(model, args.allowed_root, "model")
    if model.suffix.lower() != ".gguf" and not args.allow_non_gguf:
        die("model must have a .gguf suffix; use --allow-non-gguf only for a deliberate compatibility test")
    if args.verify_gguf_magic and not verify_gguf_magic(model):
        die("model does not start with GGUF magic; use a valid GGUF or omit --verify-gguf-magic for a deliberate parser test")
    if args.repetitions < 1 or args.repetitions > 100:
        die("--repetitions must be between 1 and 100")
    if not math.isfinite(args.timeout) or args.timeout <= 0:
        die("--timeout must be a finite positive number")
    threads = parse_int_list(args.threads, "--threads", 1) if args.threads else None
    batches = parse_int_list(args.batches, "--batches", 1) if args.batches else None
    depths = parse_int_list(args.depths, "--depths", 0) if args.depths else None
    flash = [x.strip() for x in args.flash.split(",")] if args.flash else None
    if flash and any(x not in {"on", "off", "auto"} for x in flash):
        die("--flash values must be on, off, or auto")
    configs = plan_configs(host, args.sweep, threads, batches, flash, None, depths, args.max_configs)
    cwd = resolve_directory(args.cwd, "--cwd")
    report: dict[str, Any] = {
        "schema": SCHEMA, "tool_version": TOOL_VERSION, "started_at": utc_now(),
        "offline": True, "host": host, "model": model_metadata(model, args.hash_model),
        "binary": {"path": str(binary), "version": version_probe(binary)},
        "benchmark": {"sweep": args.sweep, "prompt_tokens": args.prompt_tokens,
                       "generation_tokens": args.gen_tokens, "repetitions": args.repetitions,
                       "timeout_seconds": args.timeout, "configs_requested": len(configs),
                       "verify_gguf_magic": args.verify_gguf_magic},
        "policy": {"shell": False, "network": False, "downloads": False,
                    "inherited_environment": sorted(SAFE_ENV_KEYS),
                    "warning": "A local llama.cpp binary parses the supplied model; run it as a non-privileged user and keep it updated.",
                    "confidence_note": "confidence is a transparent heuristic, not a p-value or scientific confidence interval"},
        "attempts": [], "records": [], "warnings": [],
    }
    available = host.get("memory_bytes", {}).get("MemAvailable")
    if isinstance(available, int) and report["model"]["size_bytes"] > available:
        report["warnings"].append({"message": "model file is larger than reported available memory; expect page faults, swap, or failure", "model_bytes": report["model"]["size_bytes"], "available_bytes": available})
    if not host.get("runtime_state", {}).get("cpu_governors"):
        report["warnings"].append({"message": "CPU frequency governor was not readable; record power/thermal conditions separately"})
    status_code = 0
    for index, config in enumerate(configs, 1):
        argv = benchmark_argv(str(binary), str(model), config, args.prompt_tokens, args.gen_tokens, args.repetitions)
        started = time.monotonic()
        attempt: dict[str, Any] = {"index": index, "configuration": config, "argv": argv}
        try:
            proc = run_process(argv, args.timeout, cwd, args.max_output_bytes)
            attempt.update({"returncode": proc.returncode, "duration_seconds": round(time.monotonic() - started, 3),
                            "stderr_tail": redact_text(proc.stderr, 2000)})
            parsed = parse_bench_output(proc.stdout)
            attempt["records_parsed"] = len(parsed)
            report["attempts"].append(attempt)
            report["records"].extend(parsed)
            if proc.returncode != 0 or not parsed:
                status_code = max(status_code, 1)
                report["warnings"].append({"configuration": config, "message": "benchmark failed or returned no structured records", "returncode": proc.returncode})
                if not args.keep_going:
                    break
        except TunerError as exc:
            attempt.update({"error": str(exc), "duration_seconds": round(time.monotonic() - started, 3)})
            report["attempts"].append(attempt)
            status_code = max(status_code, exc.code)
            if not args.keep_going:
                break
    report["finished_at"] = utc_now()
    if report["records"]:
        ranked = rank_records(report["records"], args.metric, args.repetitions)
        report.update(ranked)
    else:
        report.update({"ranked": {}, "recommendation": {"metric": args.metric, "status": "no_data", "confidence": "none"}})
        status_code = max(status_code, 1)
    return report, status_code


def human_summary(report: dict[str, Any]) -> str:
    lines = [f"{report.get('schema', 'edge-cpu-gguf-tuner')} — {report.get('tool_version', '?')}"]
    if "recommendation" in report:
        rec = report["recommendation"]
        lines.append(f"recommendation[{rec.get('metric')}]: {rec.get('status')} / confidence={rec.get('confidence')}")
        if rec.get("configuration"):
            lines.append("configuration: " + json_dump(rec["configuration"], compact=True))
        if rec.get("tokens_per_second") is not None:
            lines.append(f"throughput: {rec['tokens_per_second']:.3f} tokens/s ± {float(rec.get('stddev_tokens_per_second') or 0):.3f}")
    if report.get("attempts"):
        lines.append(f"attempts: {len(report['attempts'])}; structured records: {len(report.get('records', []))}")
    for warning in report.get("warnings", []):
        lines.append("warning: " + str(warning.get("message", warning)))
    return "\n".join(lines)


def save_json(path_value: str | None, data: dict[str, Any], max_bytes: int | None = None) -> None:
    payload = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if max_bytes is not None and len(payload.encode("utf-8")) > max_bytes:
        die(f"report exceeds --max-report-bytes {max_bytes}")
    if not path_value:
        return
    path = Path(path_value).expanduser()
    if path.exists() and path.is_dir():
        die(f"output is a directory: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: str | None = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent,
                                        prefix=f".{path.name}.", suffix=".tmp", delete=False) as handle:
            temporary = handle.name
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary:
            try:
                os.unlink(temporary)
            except OSError:
                pass


def load_json(path_value: str) -> dict[str, Any]:
    path = resolve_file(path_value, "report")
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        die(f"invalid report JSON: {exc}")
    if not isinstance(data, dict):
        die("report must be a JSON object")
    return data


def do_recommend(args: argparse.Namespace) -> dict[str, Any]:
    report = load_json(args.report)
    records = report.get("records")
    if not isinstance(records, list):
        die("report has no records array")
    ranked = rank_records((x for x in records if isinstance(x, dict)), args.metric, report.get("benchmark", {}).get("repetitions"))
    return {"schema": SCHEMA, "tool_version": TOOL_VERSION, "source_report": str(Path(args.report).expanduser().resolve()),
            "generated_at": utc_now(), **ranked}


def detect_cli(cli_value: str | None) -> tuple[Path, str]:
    binary = resolve_executable(cli_value, ("llama-cli", "llama", "llama-completion"), "llama CLI")
    if binary is None:
        die("no llama CLI found; pass --cli /path/to/llama-cli")
    name = binary.name.lower()
    if name == "llama":
        return binary, "unified"
    if "completion" in name:
        return binary, "legacy-completion"
    return binary, "direct"


def do_deploy(args: argparse.Namespace) -> dict[str, Any]:
    report = load_json(args.report)
    rec = report.get("recommendation")
    if not isinstance(rec, dict) or not rec.get("configuration"):
        die("report has no measured configuration to deploy")
    config = rec["configuration"]
    if args.model:
        model = resolve_file(args.model, "model", suffix=None)
    else:
        recorded = str(report.get("model", {}).get("path", ""))
        if not recorded:
            die("pass --model because the report does not contain a model path")
        model = resolve_file(recorded, "recorded model", suffix=None)
    cli, mode = detect_cli(args.cli)
    argv: list[str] = [str(cli)]
    if mode == "unified":
        argv.append("cli")
    argv.extend(["-m", str(model)])
    for key, flag in (("threads", "-t"), ("batch_size", "-b"), ("ubatch_size", "-ub"),
                      ("flash_attn", "-fa"), ("cache_type_k", "-ctk"), ("cache_type_v", "-ctv")):
        if key in config:
            argv.extend([flag, str(config[key])])
    if args.prompt:
        argv.extend(["-p", args.prompt])
    if args.tokens is not None:
        argv.extend(["-n", str(args.tokens)])
    return {
        "schema": "edge-cpu-gguf-tuner.command.v1", "tool_version": TOOL_VERSION,
        "generated_at": utc_now(), "executed": False, "requires_user_review": True,
        "cli_mode": mode, "argv": argv, "shell": shlex.join(argv),
        "notes": [
            "This command is rendered only; the tool never launches inference here.",
            "Confirm `-h` on this exact binary accepts every flag before running; legacy and unified builds differ.",
            "A benchmark winner optimizes the selected metric, not response quality, latency, or memory safety by itself.",
        ],
    }


def do_verify_output(args: argparse.Namespace) -> dict[str, Any]:
    left = resolve_file(args.baseline, "baseline output")
    right = resolve_file(args.candidate, "candidate output")
    if left.stat().st_size > args.max_bytes or right.stat().st_size > args.max_bytes:
        die(f"output exceeds --max-bytes {args.max_bytes}")
    left_bytes, right_bytes = left.read_bytes(), right.read_bytes()
    if args.mode == "bytes":
        identical = left_bytes == right_bytes
    else:
        identical = left_bytes.decode("utf-8", "replace") == right_bytes.decode("utf-8", "replace")
    return {
        "schema": "edge-cpu-gguf-tuner.quality-gate.v1", "tool_version": TOOL_VERSION,
        "generated_at": utc_now(), "mode": args.mode, "identical": identical,
        "baseline": {"path": str(left), "bytes": len(left_bytes), "sha256": hashlib.sha256(left_bytes).hexdigest()},
        "candidate": {"path": str(right), "bytes": len(right_bytes), "sha256": hashlib.sha256(right_bytes).hexdigest()},
        "decision": "pass" if identical else "reject_candidate",
        "note": "Byte/text identity is a reproducibility gate, not proof of semantic quality.",
    }


def add_json_flag(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument("--compact", action="store_true", help="compact JSON formatting")


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="edge-cpu-tuner", description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    inspect_p = sub.add_parser("inspect", help="inspect host and discover compatible binaries")
    add_json_flag(inspect_p)
    plan_p = sub.add_parser("plan", help="render an offline benchmark plan without running it")
    plan_p.add_argument("--sweep", choices=("baseline", "threads", "batch", "flash", "kv", "context", "all"), default="threads")
    plan_p.add_argument("--model")
    plan_p.add_argument("--binary")
    plan_p.add_argument("--threads")
    plan_p.add_argument("--batches")
    plan_p.add_argument("--flash")
    plan_p.add_argument("--depths")
    plan_p.add_argument("--prompt-tokens", type=int, default=512)
    plan_p.add_argument("--gen-tokens", type=int, default=128)
    plan_p.add_argument("--repetitions", type=int, default=3)
    plan_p.add_argument("--max-configs", type=int, default=24)
    add_json_flag(plan_p)
    bench_p = sub.add_parser("bench", help="run explicit local llama-bench configurations")
    bench_p.add_argument("--model", required=True)
    bench_p.add_argument("--binary")
    bench_p.add_argument("--allowed-root")
    bench_p.add_argument("--allow-non-gguf", action="store_true")
    bench_p.add_argument("--verify-gguf-magic", action="store_true", help="read and require GGUF magic before launching the benchmark")
    bench_p.add_argument("--hash-model", action="store_true")
    bench_p.add_argument("--sweep", choices=("baseline", "threads", "batch", "flash", "kv", "context", "all"), default="threads")
    bench_p.add_argument("--threads")
    bench_p.add_argument("--batches")
    bench_p.add_argument("--flash")
    bench_p.add_argument("--depths")
    bench_p.add_argument("--prompt-tokens", type=int, default=512)
    bench_p.add_argument("--gen-tokens", type=int, default=128)
    bench_p.add_argument("--repetitions", type=int, default=3)
    bench_p.add_argument("--timeout", type=float, default=300)
    bench_p.add_argument("--max-output-bytes", type=int, default=8 * 1024 * 1024)
    bench_p.add_argument("--max-report-bytes", type=int, default=10 * 1024 * 1024)
    bench_p.add_argument("--max-configs", type=int, default=24)
    bench_p.add_argument("--keep-going", action="store_true")
    bench_p.add_argument("--cwd")
    bench_p.add_argument("--metric", choices=("pp", "tg", "pg"), default="tg")
    bench_p.add_argument("--out")
    add_json_flag(bench_p)
    rec_p = sub.add_parser("recommend", help="re-rank measured records from a report")
    rec_p.add_argument("--report", required=True)
    rec_p.add_argument("--metric", choices=("pp", "tg", "pg"), default="tg")
    rec_p.add_argument("--out")
    add_json_flag(rec_p)
    dep_p = sub.add_parser("deploy", help="render, but never execute, a measured command")
    dep_p.add_argument("--report", required=True)
    dep_p.add_argument("--model")
    dep_p.add_argument("--cli")
    dep_p.add_argument("--prompt")
    dep_p.add_argument("--tokens", type=int)
    add_json_flag(dep_p)
    ver_p = sub.add_parser("verify-output", help="compare two user-produced output files")
    ver_p.add_argument("--baseline", required=True)
    ver_p.add_argument("--candidate", required=True)
    ver_p.add_argument("--mode", choices=("bytes", "text"), default="bytes")
    ver_p.add_argument("--max-bytes", type=int, default=10 * 1024 * 1024)
    add_json_flag(ver_p)
    return p


def main(argv: Sequence[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if args.command == "inspect":
            result = inspect_host()
        elif args.command == "plan":
            if args.prompt_tokens < 0 or args.gen_tokens < 0 or args.repetitions < 1:
                die("token counts must be non-negative and repetitions must be positive")
            result = make_plan(args)
        elif args.command == "bench":
            result, status = do_bench(args)
            save_json(None, result, args.max_report_bytes)
            save_json(args.out, result, args.max_report_bytes)
            if args.json:
                print(json_dump(result, args.compact))
            else:
                print(human_summary(result))
            return status
        elif args.command == "recommend":
            result = do_recommend(args)
            save_json(args.out, result)
        elif args.command == "deploy":
            result = do_deploy(args)
        elif args.command == "verify-output":
            if args.max_bytes < 0:
                die("--max-bytes must be non-negative")
            result = do_verify_output(args)
        else:
            die(f"unknown command: {args.command}")
        if args.json:
            print(json_dump(result, args.compact))
        else:
            print(human_summary(result) if isinstance(result, dict) and result.get("schema") == SCHEMA else json_dump(result, compact=True))
        return 0
    except TunerError as exc:
        if getattr(args, "json", False):
            print(json_dump({"schema": "edge-cpu-gguf-tuner.error.v1", "tool_version": TOOL_VERSION,
                             "error": str(exc), "exit_code": exc.code}, getattr(args, "compact", False)))
        else:
            print(f"error: {exc}", file=sys.stderr)
        return exc.code
    except KeyboardInterrupt:
        print("error: interrupted; no subprocess was left running", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
