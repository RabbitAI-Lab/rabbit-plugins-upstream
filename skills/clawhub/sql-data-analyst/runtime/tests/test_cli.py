from __future__ import annotations

import hashlib
import json
import multiprocessing
from threading import BrokenBarrierError
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from uuid import UUID

import pytest

from sql_data_analyst_local.cli import Cli
from sql_data_analyst_local.contracts import (
    AuthorizationReceipt,
    TicketClaims,
    TicketEnvelope,
)
from sql_data_analyst_local.datasets import DatasetError, DatasetManifest, LocalColumn, LocalTable
from sql_data_analyst_local.platform import PlatformError
from sql_data_analyst_local.results import QueryResult


INSTALLATION_ID = UUID("018f47a2-7b2b-7e47-8794-c11316f5023c")
EXECUTION_ID = UUID("018f47a2-7b2b-7e47-8794-c11316f5023b")


def _idempotency_worker(
    workspace: str,
    fingerprint: str,
    barrier: object,
    worker_number: int,
    output: object,
) -> None:
    import sql_data_analyst_local.cli as cli_module

    def coordinated_uuid4() -> UUID:
        try:
            barrier.wait(timeout=2)
        except BrokenBarrierError:
            pass
        return UUID(int=worker_number + 1)

    cli_module.uuid4 = coordinated_uuid4
    cli = Cli(
        workspace_root=Path(workspace),
        installation_id=INSTALLATION_ID,
    )
    output.put(cli._idempotency_key("query.execute", fingerprint))


def _two_process_idempotency_keys(workspace: Path, fingerprint: str) -> list[str]:
    context = multiprocessing.get_context("spawn")
    barrier = context.Barrier(2)
    output = context.Queue()
    processes = [
        context.Process(
            target=_idempotency_worker,
            args=(str(workspace), fingerprint, barrier, number, output),
        )
        for number in range(2)
    ]
    for process in processes:
        process.start()
    for process in processes:
        process.join(timeout=10)
        assert process.exitcode == 0
    return [output.get(timeout=2), output.get(timeout=2)]


@dataclass
class Event:
    name: str


class FakePlatform:
    def __init__(self, events: list[Event], *, fail_once: bool = False) -> None:
        self.events = events
        self.fail_once = fail_once
        self.keys: list[str] = []
        self.fingerprints: list[str] = []

    def authorize(
        self,
        operation: str,
        installation_id: UUID,
        input_fingerprint: str,
        idempotency_key: str,
    ) -> AuthorizationReceipt:
        self.events.append(Event("authorize"))
        self.keys.append(idempotency_key)
        self.fingerprints.append(input_fingerprint)
        if self.fail_once and len(self.keys) == 1:
            raise PlatformError()
        return AuthorizationReceipt(
            execution_id=EXECUTION_ID,
            operation=operation,
            ticket=TicketEnvelope(key_id="test", signed_payload="e30=", signature="sig"),
            currency="CNY",
            charged_amount="0.080000",
            balance_after="99.920000",
        )


class RejectingPlatform:
    def __init__(self) -> None:
        self.calls: list[object] = []

    def authorize(self, *args: object) -> AuthorizationReceipt:
        self.calls.append(args)
        raise AssertionError("offline commands must not authorize")


class FakeVerifier:
    def __init__(self, events: list[Event]) -> None:
        self.events = events

    def verify(self, envelope: TicketEnvelope, expected: object, now: datetime) -> TicketClaims:
        self.events.append(Event("verify"))
        return TicketClaims(
            schema_version=1,
            execution_id=EXECUTION_ID,
            operation=expected.operation,
            installation_id=expected.installation_id,
            input_fingerprint=expected.input_fingerprint,
            billing_units=1,
            charged_amount="0.080000",
            currency="CNY",
            runner_min_version="1.0.0",
            issued_at="2026-08-24T00:00:00Z",
            expires_at="2026-08-24T00:05:00Z",
        )


class FakeRepository:
    def __init__(self, events: list[Event], manifest: DatasetManifest) -> None:
        self.events = events
        self.manifest = manifest
        self.deleted = False

    def inspect(self, dataset_id: UUID) -> DatasetManifest:
        self.events.append(Event("open_dataset"))
        return self.manifest

    def delete(self, dataset_id: UUID) -> None:
        self.events.append(Event("delete_dataset"))
        self.deleted = True


@pytest.fixture
def manifest() -> DatasetManifest:
    return DatasetManifest(
        schema_version=1,
        dataset_id=UUID("018f47a2-7b2b-7e47-8794-c11316f5023d"),
        source_format="csv",
        source_fingerprint="a" * 64,
        tables=[
            LocalTable(
                logical_name="data",
                display_name="Data",
                parquet_path="normalized/data.parquet",
                row_count=1,
                columns=[
                    LocalColumn(
                        name="value",
                        display_name="value",
                        type="int64",
                        nullable=False,
                        null_count=0,
                        distinct_count=1,
                    )
                ],
                profile={"row_count": 1, "column_count": 1},
            )
        ],
    )


def build_cli(
    tmp_path: Path,
    platform: object,
    verifier: FakeVerifier,
    repository: FakeRepository,
    *,
    execute=lambda *_args, **_kwargs: QueryResult(
        columns=[{"name": "value", "type": "BIGINT"}],
        rows=[[1]],
        truncated=False,
        elapsed_ms=1,
        byte_count=3,
    ),
) -> Cli:
    return Cli(
        workspace_root=tmp_path / "workspace",
        platform=platform,
        verifier=verifier,
        repository=repository,
        installation_id=INSTALLATION_ID,
        now=lambda: datetime(2026, 8, 24, tzinfo=timezone.utc),
        query_executor=execute,
        release_validator=lambda: None,
    )


def manifest_digest(manifest: DatasetManifest) -> str:
    canonical = json.dumps(
        manifest.model_dump(mode="json"),
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def query_argv(
    manifest: DatasetManifest,
    sql_file: Path,
    *,
    command: str = "query",
    sql_sha256: str | None = None,
    manifest_sha256: str | None = None,
) -> list[str]:
    return [
        command,
        "--dataset",
        str(manifest.dataset_id),
        "--sql-file",
        str(sql_file),
        "--sql-sha256",
        sql_sha256 or hashlib.sha256(sql_file.read_bytes()).hexdigest(),
        "--manifest-sha256",
        manifest_sha256 or manifest_digest(manifest),
    ]


def test_query_authorizes_and_verifies_before_opening_inputs(
    tmp_path: Path, manifest: DatasetManifest
) -> None:
    events: list[Event] = []
    sql_file = tmp_path / "query.sql"
    sql_file.write_text("SELECT value FROM data", encoding="utf-8")
    cli = build_cli(
        tmp_path,
        FakePlatform(events),
        FakeVerifier(events),
        FakeRepository(events, manifest),
    )

    result = cli.invoke(query_argv(manifest, sql_file))

    assert result.exit_code == 0
    assert [event.name for event in events[:3]] == ["authorize", "verify", "open_dataset"]
    envelope = json.loads(result.stdout)
    assert envelope["schema_version"] == 1
    assert envelope["operation"] == "query.execute"
    assert envelope["charged_amount"] == "0.080000"
    assert result.stdout.count("\n") == 1


def test_authorization_failure_does_not_open_dataset_or_sql(
    tmp_path: Path, manifest: DatasetManifest
) -> None:
    events: list[Event] = []
    sql_file = tmp_path / "secret.sql"
    sql_file.write_text("SECRET SQL", encoding="utf-8")
    cli = build_cli(
        tmp_path,
        FakePlatform(events, fail_once=True),
        FakeVerifier(events),
        FakeRepository(events, manifest),
    )

    result = cli.invoke(query_argv(manifest, sql_file))

    assert result.exit_code == 1
    assert [event.name for event in events] == ["authorize"]
    assert json.loads(result.stdout)["error"]["code"] == "license_unavailable"
    assert "SECRET SQL" not in result.stdout + result.stderr
    assert "Traceback" not in result.stdout + result.stderr


def test_retry_reuses_idempotency_key_persisted_before_request(
    tmp_path: Path, manifest: DatasetManifest
) -> None:
    events: list[Event] = []
    sql_file = tmp_path / "query.sql"
    sql_file.write_text("SELECT value FROM data", encoding="utf-8")
    platform = FakePlatform(events, fail_once=True)
    cli = build_cli(
        tmp_path,
        platform,
        FakeVerifier(events),
        FakeRepository(events, manifest),
    )
    argv = query_argv(manifest, sql_file)

    assert cli.invoke(argv).exit_code == 1
    assert list((tmp_path / "workspace" / "state" / "idempotency").iterdir())
    assert cli.invoke(argv).exit_code == 0
    assert platform.keys[0] == platform.keys[1]


def test_new_successful_invocation_uses_a_new_idempotency_key(
    tmp_path: Path, manifest: DatasetManifest
) -> None:
    events: list[Event] = []
    sql_file = tmp_path / "query.sql"
    sql_file.write_text("SELECT value FROM data", encoding="utf-8")
    platform = FakePlatform(events)
    cli = build_cli(
        tmp_path,
        platform,
        FakeVerifier(events),
        FakeRepository(events, manifest),
    )
    argv = query_argv(manifest, sql_file)

    assert cli.invoke(argv).exit_code == 0
    assert cli.invoke(argv).exit_code == 0
    assert platform.keys[0] != platform.keys[1]


def test_concurrent_clients_select_one_pending_idempotency_key(tmp_path: Path) -> None:
    keys = _two_process_idempotency_keys(tmp_path / "workspace", "c" * 64)

    assert len(set(keys)) == 1


def test_concurrent_clients_serialize_completed_to_one_new_key(tmp_path: Path) -> None:
    workspace = tmp_path / "workspace"
    fingerprint = "d" * 64
    cli = Cli(workspace_root=workspace, installation_id=INSTALLATION_ID)
    completed_key = cli._idempotency_key("query.execute", fingerprint)
    cli._complete_idempotency(
        "query.execute", fingerprint, completed_key, EXECUTION_ID
    )

    keys = _two_process_idempotency_keys(workspace, fingerprint)

    assert len(set(keys)) == 1
    assert keys[0] != completed_key


def test_local_failure_after_authorization_retains_billing(
    tmp_path: Path, manifest: DatasetManifest
) -> None:
    events: list[Event] = []
    sql_file = tmp_path / "query.sql"
    sql_file.write_text("SELECT secret FROM data", encoding="utf-8")

    def fail(*_args: object, **_kwargs: object) -> QueryResult:
        raise DatasetError("dataset_invalid")

    cli = build_cli(
        tmp_path,
        FakePlatform(events),
        FakeVerifier(events),
        FakeRepository(events, manifest),
        execute=fail,
    )
    result = cli.invoke(query_argv(manifest, sql_file))
    envelope = json.loads(result.stdout)

    assert result.exit_code == 1
    assert envelope["execution_id"] == str(EXECUTION_ID)
    assert envelope["charged_amount"] == "0.080000"
    assert envelope["currency"] == "CNY"
    assert envelope["balance_after"] == "99.920000"
    assert envelope["error"] == {"code": "dataset_invalid"}
    assert "refund" not in result.stdout.casefold()


def test_inspect_delete_and_doctor_never_call_platform(
    tmp_path: Path, manifest: DatasetManifest
) -> None:
    events: list[Event] = []
    platform = RejectingPlatform()
    repository = FakeRepository(events, manifest)
    cli = build_cli(tmp_path, platform, FakeVerifier(events), repository)

    inspected = cli.invoke(["inspect", "--dataset", str(manifest.dataset_id)])
    doctor = cli.invoke(["doctor"])
    deleted = cli.invoke(["delete", "--dataset", str(manifest.dataset_id)])

    assert inspected.exit_code == doctor.exit_code == deleted.exit_code == 0
    assert platform.calls == []
    assert json.loads(inspected.stdout)["data"]["manifest_sha256"] == manifest_digest(manifest)
    for result in (inspected, doctor, deleted):
        envelope = json.loads(result.stdout)
        assert envelope["execution_id"] is None
        assert envelope["charged_amount"] is None
        assert envelope["currency"] is None
        assert envelope["balance_after"] is None


def test_doctor_fails_closed_for_unstamped_source_runtime(
    tmp_path: Path, manifest: DatasetManifest
) -> None:
    cli = Cli(
        workspace_root=tmp_path / "workspace",
        repository=FakeRepository([], manifest),
        installation_id=INSTALLATION_ID,
    )

    result = cli.invoke(["doctor"])

    assert result.exit_code == 1
    assert json.loads(result.stdout)["error"] == {"code": "configuration_invalid"}


def test_diagnostics_never_echo_key_sql_rows_path_or_traceback(
    tmp_path: Path, manifest: DatasetManifest, monkeypatch: pytest.MonkeyPatch
) -> None:
    events: list[Event] = []
    sql_file = tmp_path / "private-query.sql"
    sql_file.write_text("SELECT 'private row'", encoding="utf-8")
    monkeypatch.setenv("SQL_DATA_ANALYST_API_KEY", "sk-sensitive")

    def explode(*_args: object, **_kwargs: object) -> QueryResult:
        raise RuntimeError(
            "sk-sensitive SELECT 'private row' " + str(sql_file) + " Traceback"
        )

    cli = build_cli(
        tmp_path,
        FakePlatform(events),
        FakeVerifier(events),
        FakeRepository(events, manifest),
        execute=explode,
    )
    result = cli.invoke(query_argv(manifest, sql_file))

    combined = result.stdout + result.stderr
    assert json.loads(result.stdout)["error"] == {"code": "internal_error"}
    for secret in ("sk-sensitive", "private row", str(sql_file), "Traceback"):
        assert secret not in combined


def test_changed_sql_cannot_execute_under_pending_authorization(
    tmp_path: Path, manifest: DatasetManifest
) -> None:
    events: list[Event] = []
    executed = False
    sql_file = tmp_path / "query.sql"
    sql_file.write_text("SELECT value FROM data", encoding="utf-8")
    authorized_digest = hashlib.sha256(sql_file.read_bytes()).hexdigest()
    platform = FakePlatform(events, fail_once=True)

    def observe_execute(*_args: object, **_kwargs: object) -> QueryResult:
        nonlocal executed
        executed = True
        raise AssertionError("changed SQL must not execute")

    cli = build_cli(
        tmp_path,
        platform,
        FakeVerifier(events),
        FakeRepository(events, manifest),
        execute=observe_execute,
    )
    argv = query_argv(manifest, sql_file, sql_sha256=authorized_digest)

    assert cli.invoke(argv).exit_code == 1
    sql_file.write_text("SELECT 999 FROM data", encoding="utf-8")
    result = cli.invoke(argv)
    envelope = json.loads(result.stdout)

    assert result.exit_code == 1
    assert platform.keys[0] == platform.keys[1]
    assert platform.fingerprints[0] == platform.fingerprints[1]
    assert executed is False
    assert envelope["error"] == {"code": "authorization_invalid"}
    assert envelope["execution_id"] == str(EXECUTION_ID)
    assert envelope["charged_amount"] == "0.080000"


def test_manifest_digest_mismatch_fails_before_sql_is_opened(
    tmp_path: Path, manifest: DatasetManifest
) -> None:
    events: list[Event] = []
    sql_file = tmp_path / "must-not-open.sql"
    sql_file.write_text("SELECT value FROM data", encoding="utf-8")
    changed = manifest.model_copy(update={"source_fingerprint": "b" * 64})
    cli = build_cli(
        tmp_path,
        FakePlatform(events),
        FakeVerifier(events),
        FakeRepository(events, changed),
    )

    result = cli.invoke(query_argv(manifest, sql_file))
    envelope = json.loads(result.stdout)

    assert result.exit_code == 1
    assert envelope["error"] == {"code": "authorization_invalid"}
    assert envelope["charged_amount"] == "0.080000"
    assert [event.name for event in events] == ["authorize", "verify", "open_dataset"]


def test_report_summary_digest_mismatch_does_not_create_artifacts(
    tmp_path: Path, manifest: DatasetManifest
) -> None:
    events: list[Event] = []
    summary_file = tmp_path / "summary.json"
    summary_file.write_text('{"changed":true}', encoding="utf-8")
    cli = build_cli(
        tmp_path,
        FakePlatform(events),
        FakeVerifier(events),
        FakeRepository(events, manifest),
    )
    argv = [
        "report",
        "--dataset",
        str(manifest.dataset_id),
        "--summary-file",
        str(summary_file),
        "--summary-sha256",
        "0" * 64,
        "--manifest-sha256",
        manifest_digest(manifest),
    ]

    result = cli.invoke(argv)
    envelope = json.loads(result.stdout)

    assert result.exit_code == 1
    assert envelope["error"] == {"code": "authorization_invalid"}
    assert envelope["charged_amount"] == "0.080000"
    assert not (tmp_path / "workspace" / "reports").exists()
