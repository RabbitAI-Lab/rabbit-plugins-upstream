from __future__ import annotations

import base64
import datetime as dt
import decimal
import json
import math
import multiprocessing as mp
import os
import signal
import sys
import tempfile
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from sql_data_analyst_local.datasets import (
    DatasetError,
    DatasetManifest,
    DatasetRepository,
)
from sql_data_analyst_local.results import QueryFailure, QueryResult


MIB = 1024 * 1024


@dataclass(frozen=True)
class QueryLimits:
    max_rows: int = 1_000
    max_result_bytes: int = 10 * MIB
    timeout_seconds: float = 30
    address_space_bytes: int = 1024 * MIB
    duckdb_memory_limit_bytes: int = 512 * MIB
    threads: int = 2

    def __post_init__(self) -> None:
        integer_values = (
            self.max_rows,
            self.max_result_bytes,
            self.address_space_bytes,
            self.duckdb_memory_limit_bytes,
            self.threads,
        )
        if (
            any(type(value) is not int for value in integer_values)
            or type(self.timeout_seconds) not in {int, float}
            or not math.isfinite(self.timeout_seconds)
            or not (
                1 <= self.max_rows <= 1_000
                and 256 <= self.max_result_bytes <= 10 * MIB
                and 0.01 <= self.timeout_seconds <= 30
                and 16 * MIB <= self.address_space_bytes <= 1024 * MIB
                and MIB <= self.duckdb_memory_limit_bytes <= 512 * MIB
                and self.duckdb_memory_limit_bytes <= self.address_space_bytes
                and 1 <= self.threads <= 2
            )
        ):
            raise ValueError("query_limits_invalid")


def run_isolated_query(
    *,
    workspace_root: Path,
    manifest: dict[str, object],
    sql: str,
    limits: QueryLimits,
    temporary_parent: Path | None = None,
) -> QueryResult:
    context = mp.get_context("spawn")
    receiver = None
    sender = None
    process = None
    process_started = False
    payload: dict[str, object] | None = None
    try:
        receiver, sender = context.Pipe(duplex=False)
        with tempfile.TemporaryDirectory(
            prefix="sql-data-analyst-query-",
            dir=temporary_parent,
        ) as temporary:
            process = context.Process(
                target=_execute_child,
                args=(
                    str(workspace_root),
                    manifest,
                    sql,
                    asdict(limits),
                    temporary,
                    sender,
                ),
                daemon=True,
            )
            process.start()
            process_started = True
            sender.close()
            deadline = time.monotonic() + limits.timeout_seconds
            while time.monotonic() < deadline:
                if _rss_limit_exceeded(process.pid, limits.address_space_bytes):
                    _terminate_and_reap(process)
                    raise QueryFailure("query_resource_limit")
                wait = min(0.05, max(0.0, deadline - time.monotonic()))
                if receiver.poll(wait):
                    try:
                        payload = receiver.recv()
                    except (EOFError, OSError):
                        payload = None
                    break
                if not process.is_alive():
                    if receiver.poll(0.1):
                        try:
                            payload = receiver.recv()
                        except (EOFError, OSError):
                            payload = None
                    break

            if payload is None and process.is_alive():
                _terminate_and_reap(process)
                raise QueryFailure("query_timeout")

            process.join(2)
            if process.is_alive():
                _terminate_and_reap(process)
            if payload is None:
                code = (
                    "query_resource_limit"
                    if _resource_exit(process.exitcode)
                    else "query_failed"
                )
                raise QueryFailure(code)
    except QueryFailure:
        raise
    except (OSError, ValueError):
        if process is not None and process_started and process.is_alive():
            _terminate_and_reap(process)
        raise QueryFailure() from None
    finally:
        if sender is not None:
            try:
                sender.close()
            except OSError:
                pass
        if receiver is not None:
            receiver.close()
        if process is not None and process_started and not process.is_alive():
            process.join()
            process.close()

    if not isinstance(payload, dict) or payload.get("ok") is not True:
        code = payload.get("code") if isinstance(payload, dict) else "query_failed"
        raise QueryFailure(code if isinstance(code, str) else "query_failed")
    result = payload.get("result")
    if not isinstance(result, dict):
        raise QueryFailure()
    try:
        return QueryResult(**result)
    except (TypeError, ValueError):
        raise QueryFailure() from None


def _execute_child(
    workspace_root: str,
    manifest_value: dict[str, object],
    sql: str,
    limits: dict[str, int | float],
    temporary: str,
    sender: Any,
) -> None:
    connection = None
    descriptors: list[int] = []
    try:
        _apply_os_limits(limits)
        import duckdb

        started = time.monotonic()
        manifest = DatasetManifest.model_validate(manifest_value)
        repository = DatasetRepository(Path(workspace_root))
        owned_manifest = repository.inspect(manifest.dataset_id)
        if owned_manifest != manifest:
            raise DatasetError()

        memory_limit = max(1, int(limits["duckdb_memory_limit_bytes"]) // MIB)
        connection = duckdb.connect(
            ":memory:",
            config={
                "threads": str(int(limits["threads"])),
                "memory_limit": f"{memory_limit}MB",
                "temp_directory": temporary,
                "autoinstall_known_extensions": "false",
                "autoload_known_extensions": "false",
                "allow_unsigned_extensions": "false",
            },
        )
        for index, table in enumerate(owned_manifest.tables):
            descriptor = repository._open_table_file(  # noqa: SLF001
                owned_manifest.dataset_id, table
            )
            descriptors.append(descriptor)
            internal_name = f"_dataset_table_{index}"
            connection.from_parquet(f"/dev/fd/{descriptor}").create(internal_name)
            connection.execute(
                f'CREATE VIEW "{table.logical_name}" AS SELECT * FROM "{internal_name}"'
            )
        for descriptor in descriptors:
            os.close(descriptor)
        descriptors.clear()

        # Files are loaded through validated descriptors before this switch.
        # Submitted SQL executes only after DuckDB external access is disabled.
        connection.execute("SET enable_external_access=false")
        row_limit = int(limits["max_rows"]) + 1
        cursor = connection.execute(
            f"SELECT * FROM ({sql}) AS _bounded_query_result LIMIT {row_limit}"
        )
        columns = [
            {"name": str(column[0]), "type": str(column[1])}
            for column in (cursor.description or [])
        ]
        rows: list[list[Any]] = []
        truncated = False
        max_bytes = int(limits["max_result_bytes"])
        max_rows = int(limits["max_rows"])
        conservative_size = _conservative_wire_size(columns, [])
        while True:
            raw_row = cursor.fetchone()
            if raw_row is None:
                break
            if len(rows) == max_rows:
                truncated = True
                break
            row = [_serialize_value(value) for value in raw_row]
            row_size = len(
                json.dumps(
                    row,
                    ensure_ascii=False,
                    separators=(",", ":"),
                    allow_nan=False,
                ).encode("utf-8")
            )
            candidate_size = conservative_size + (1 if rows else 0) + row_size
            if candidate_size > max_bytes:
                truncated = True
                break
            rows.append(row)
            conservative_size = candidate_size

        elapsed_ms = max(0, int((time.monotonic() - started) * 1000))
        byte_count = _exact_wire_size(columns, rows, truncated, elapsed_ms)
        if byte_count > max_bytes:
            raise MemoryError("result envelope exceeded limit")
        sender.send(
            {
                "ok": True,
                "result": {
                    "columns": columns,
                    "rows": rows,
                    "truncated": truncated,
                    "elapsed_ms": elapsed_ms,
                    "byte_count": byte_count,
                },
            }
        )
    except (DatasetError, ValidationError):
        try:
            sender.send({"ok": False, "code": "dataset_invalid"})
        except (BrokenPipeError, EOFError, OSError):
            pass
    except BaseException as exception:
        resource_limited = _is_resource_error(exception)
        try:
            sender.send(
                {
                    "ok": False,
                    "code": (
                        "query_resource_limit" if resource_limited else "query_failed"
                    ),
                }
            )
        except (BrokenPipeError, EOFError, OSError):
            pass
    finally:
        for descriptor in descriptors:
            try:
                os.close(descriptor)
            except OSError:
                pass
        if connection is not None:
            try:
                connection.close()
            except BaseException:
                pass
        sender.close()


def _apply_os_limits(limits: dict[str, int | float]) -> None:
    if not sys.platform.startswith("linux"):
        return
    import resource

    address_space = int(limits["address_space_bytes"])
    cpu_seconds = max(1, math.ceil(float(limits["timeout_seconds"])) + 1)
    resource.setrlimit(resource.RLIMIT_AS, (address_space, address_space))
    resource.setrlimit(resource.RLIMIT_CPU, (cpu_seconds, cpu_seconds))
    resource.setrlimit(resource.RLIMIT_NOFILE, (64, 64))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))


def _rss_limit_exceeded(pid: int | None, limit: int) -> bool:
    if not sys.platform.startswith("darwin") or pid is None:
        return False
    import psutil

    try:
        return psutil.Process(pid).memory_info().rss > limit
    except psutil.NoSuchProcess:
        return False
    except psutil.Error:
        # The parent must fail closed when it cannot enforce the macOS cap.
        return True


def _terminate_and_reap(process: mp.Process) -> None:
    if process.is_alive():
        process.terminate()
    process.join(2)
    if process.is_alive():
        process.kill()
        process.join()


def _resource_exit(exitcode: int | None) -> bool:
    return exitcode in {
        -getattr(signal, "SIGKILL", 9),
        -getattr(signal, "SIGSEGV", 11),
        -getattr(signal, "SIGXCPU", 24),
    }


def _is_resource_error(exception: BaseException) -> bool:
    try:
        import duckdb

        resource_types = (MemoryError, duckdb.OutOfMemoryException)
    except ImportError:
        resource_types = (MemoryError,)
    if isinstance(exception, resource_types):
        return True
    message = str(exception).casefold()
    return any(
        marker in message
        for marker in (
            "out of memory",
            "failed to allocate",
            "temp directory",
            "disk space",
        )
    )


def _serialize_value(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, bool)):
        return value
    if isinstance(value, float):
        return value if math.isfinite(value) else None
    if isinstance(value, decimal.Decimal):
        return str(value)
    if isinstance(value, (dt.datetime, dt.date, dt.time)):
        return value.isoformat()
    if isinstance(value, bytes):
        return base64.b64encode(value).decode("ascii")
    if isinstance(value, (list, tuple)):
        return [_serialize_value(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _serialize_value(item) for key, item in value.items()}
    return str(value)


def _wire_payload(
    columns: list[dict[str, str]],
    rows: list[list[Any]],
    truncated: bool,
    elapsed_ms: int,
    byte_count: int,
) -> bytes:
    return json.dumps(
        {
            "columns": columns,
            "rows": rows,
            "truncated": truncated,
            "elapsed_ms": elapsed_ms,
            "byte_count": byte_count,
        },
        ensure_ascii=False,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def _conservative_wire_size(
    columns: list[dict[str, str]], rows: list[list[Any]]
) -> int:
    return len(
        _wire_payload(
            columns,
            rows,
            True,
            9_999_999_999_999,
            9_999_999_999_999,
        )
    )


def _exact_wire_size(
    columns: list[dict[str, str]],
    rows: list[list[Any]],
    truncated: bool,
    elapsed_ms: int,
) -> int:
    size = 0
    for _ in range(8):
        measured = len(_wire_payload(columns, rows, truncated, elapsed_ms, size))
        if measured == size:
            return size
        size = measured
    return len(_wire_payload(columns, rows, truncated, elapsed_ms, size))
