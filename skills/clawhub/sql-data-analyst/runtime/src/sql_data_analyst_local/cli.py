from __future__ import annotations

import argparse
import fcntl
import hashlib
import hmac
import json
import os
import re
import stat
import sys
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Protocol, Sequence
from uuid import UUID, uuid4

from pydantic import ValidationError

from sql_data_analyst_local.contracts import AuthorizationReceipt, ExpectedTicket, TicketClaims
from sql_data_analyst_local.datasets import DatasetError, DatasetRepository
from sql_data_analyst_local.executor import execute_query
from sql_data_analyst_local.ingest import IngestService
from sql_data_analyst_local.isolation import QueryLimits
from sql_data_analyst_local.platform import PlatformClient, PlatformError
from sql_data_analyst_local.report import ReportError, ReportWriter, parse_summary
from sql_data_analyst_local.results import QueryFailure, QueryResult
from sql_data_analyst_local.settings import (
    RUNNER_VERSION,
    SettingsError,
    api_key_from_environment,
    default_workspace_root,
    validate_release_settings,
)
from sql_data_analyst_local.state import LocalState, StateError
from sql_data_analyst_local.tickets import TicketError, TicketVerifier


MAX_INPUT_BYTES = 10 * 1024 * 1024
_SHA256 = re.compile(r"^[a-f0-9]{64}$")
_DIRECTORY_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
_READ_FLAGS = os.O_RDONLY | os.O_NOFOLLOW
_LOCK_CREATE_FLAGS = os.O_RDWR | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW
_LOCK_OPEN_FLAGS = os.O_RDWR | os.O_NOFOLLOW
_PAID_OPERATIONS = {
    "ingest": "dataset.ingest",
    "analysis": "analysis.run",
    "query": "query.execute",
    "report": "report.create",
}
_FREE_OPERATIONS = {
    "inspect": "dataset.inspect",
    "delete": "dataset.delete",
    "doctor": "doctor",
}


class Authorizer(Protocol):
    def authorize(
        self,
        operation: str,
        installation_id: UUID,
        input_fingerprint: str,
        idempotency_key: str,
    ) -> AuthorizationReceipt: ...


class Verifier(Protocol):
    def verify(
        self, envelope: object, expected: ExpectedTicket, now: datetime
    ) -> TicketClaims: ...


@dataclass(frozen=True)
class CliResult:
    exit_code: int
    stdout: str
    stderr: str


class _UsageError(RuntimeError):
    code = "usage_invalid"


class _Parser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        del message
        raise _UsageError()


class Cli:
    def __init__(
        self,
        *,
        workspace_root: Path | None = None,
        platform: Authorizer | None = None,
        verifier: Verifier | None = None,
        repository: object | None = None,
        installation_id: UUID | None = None,
        now: Callable[[], datetime] | None = None,
        query_executor: Callable[..., QueryResult] = execute_query,
        release_validator: Callable[[], None] = validate_release_settings,
    ) -> None:
        self.workspace_root = workspace_root or default_workspace_root()
        self._state = LocalState(self.workspace_root)
        self._platform = platform
        self._verifier = verifier
        self._repository = repository
        self._installation_id = installation_id
        self._now = now or (lambda: datetime.now(timezone.utc))
        self._query_executor = query_executor
        self._release_validator = release_validator

    def invoke(self, argv: Sequence[str]) -> CliResult:
        operation = "unknown"
        receipt: AuthorizationReceipt | None = None
        fingerprint: str | None = None
        idempotency_key: str | None = None
        try:
            arguments = _parser().parse_args(list(argv))
            command = str(arguments.command)
            operation = _PAID_OPERATIONS.get(command, _FREE_OPERATIONS.get(command, "unknown"))
            if command in _PAID_OPERATIONS:
                fingerprint = _input_fingerprint(operation, arguments)
                idempotency_key = self._idempotency_key(operation, fingerprint)
                installation_id = self._installation()
                platform = self._authorizer()
                receipt = platform.authorize(
                    operation, installation_id, fingerprint, idempotency_key
                )
                expected = ExpectedTicket(
                    operation=operation,
                    installation_id=installation_id,
                    input_fingerprint=fingerprint,
                    runner_version=RUNNER_VERSION,
                )
                claims = self._ticket_verifier().verify(receipt.ticket, expected, self._now())
                _validate_receipt(receipt, claims, operation)
            data = self._dispatch(command, arguments, receipt)
            if (
                receipt is not None
                and fingerprint is not None
                and idempotency_key is not None
            ):
                self._complete_idempotency(
                    operation,
                    fingerprint,
                    idempotency_key,
                    receipt.execution_id,
                )
            return CliResult(0, _json_line(_envelope(operation, receipt, data=data)), "")
        except BaseException as exception:
            code = _error_code(exception)
            stderr = f"error:{code}\n"
            return CliResult(
                1,
                _json_line(_envelope(operation, receipt, error=code)),
                stderr,
            )

    def _dispatch(
        self, command: str, arguments: argparse.Namespace, receipt: AuthorizationReceipt | None
    ) -> dict[str, object]:
        repository = self._dataset_repository()
        if command == "inspect":
            manifest = repository.inspect(_uuid(arguments.dataset))
            return {
                "manifest": manifest.model_dump(mode="json"),
                "manifest_sha256": _manifest_digest(manifest),
            }
        if command == "delete":
            dataset_id = _uuid(arguments.dataset)
            repository.delete(dataset_id)
            return {"dataset_id": str(dataset_id), "deleted": True}
        if command == "doctor":
            self._release_validator()
            self._ticket_verifier()
            return {"runner_version": RUNNER_VERSION, "workspace_ready": True}
        if receipt is None:
            raise PlatformError()
        if command == "ingest":
            dataset_id = _uuid(arguments.dataset)
            expected = _expected_from_receipt(
                receipt,
                self._installation(),
                _input_fingerprint("dataset.ingest", arguments),
            )
            service = IngestService(
                repository,
                self._ticket_verifier(),  # type: ignore[arg-type]
                expected,
                now=self._now,
            )
            manifest = service.ingest(
                Path(arguments.source),
                dataset_id,
                receipt.ticket,
                expected_source_fingerprint=arguments.source_sha256,
            )
            return {"manifest": manifest.model_dump(mode="json")}
        if command in {"analysis", "query"}:
            dataset_id = _uuid(arguments.dataset)
            manifest = repository.inspect(dataset_id)
            _assert_digest(
                _manifest_digest(manifest), arguments.manifest_sha256
            )
            sql_bytes = _read_bytes(Path(arguments.sql_file))
            _assert_digest(hashlib.sha256(sql_bytes).hexdigest(), arguments.sql_sha256)
            sql = _decode_sql(sql_bytes)
            result = self._query_executor(
                manifest,
                sql,
                QueryLimits(),
                repository=repository,
            )
            return {"result": asdict(result)}
        if command == "report":
            dataset_id = _uuid(arguments.dataset)
            manifest = repository.inspect(dataset_id)
            _assert_digest(
                _manifest_digest(manifest), arguments.manifest_sha256
            )
            summary_bytes = _read_bytes(Path(arguments.summary_file))
            _assert_digest(
                hashlib.sha256(summary_bytes).hexdigest(), arguments.summary_sha256
            )
            summary = parse_summary(_decode_json(summary_bytes))
            artifacts = ReportWriter(self.workspace_root).create(receipt.execution_id, summary)
            return {
                "dataset_id": str(dataset_id),
                "artifacts": {
                    "xlsx": str(artifacts.xlsx_path),
                    "html": str(artifacts.html_path),
                },
            }
        raise _UsageError()

    def _dataset_repository(self) -> object:
        if self._repository is None:
            self._repository = DatasetRepository(self.workspace_root)
        return self._repository

    def _authorizer(self) -> Authorizer:
        if self._platform is None:
            self._platform = PlatformClient(api_key_from_environment())
        return self._platform

    def _ticket_verifier(self) -> Verifier:
        if self._verifier is None:
            self._verifier = TicketVerifier()
        return self._verifier

    def _installation(self) -> UUID:
        if self._installation_id is not None:
            return self._installation_id
        value = self._state.read_json("state/installation.json")
        try:
            if isinstance(value, dict):
                self._installation_id = UUID(str(value["installation_id"]))
                return self._installation_id
        except (KeyError, TypeError, ValueError):
            raise StateError("state_read_failed") from None
        self._installation_id = uuid4()
        self._state.write_json(
            "state/installation.json", {"installation_id": str(self._installation_id)}
        )
        return self._installation_id

    def _idempotency_key(self, operation: str, fingerprint: str) -> str:
        scope = hashlib.sha256(f"{operation}\0{fingerprint}".encode()).hexdigest()
        relative = f"state/idempotency/{scope}.json"
        with self._idempotency_lock(scope):
            value = self._state.read_json(relative)
            if value is not None:
                existing_key, status = _validated_idempotency(
                    value, operation, fingerprint
                )
                if status == "pending":
                    return existing_key
            key = str(uuid4())
            self._state.write_json(
                relative,
                {
                    "idempotency_key": key,
                    "input_fingerprint": fingerprint,
                    "operation": operation,
                    "status": "pending",
                },
            )
            return key

    def _complete_idempotency(
        self,
        operation: str,
        fingerprint: str,
        idempotency_key: str,
        execution_id: UUID,
    ) -> None:
        scope = hashlib.sha256(f"{operation}\0{fingerprint}".encode()).hexdigest()
        relative = f"state/idempotency/{scope}.json"
        with self._idempotency_lock(scope):
            current = self._state.read_json(relative)
            current_key, status = _validated_idempotency(
                current, operation, fingerprint
            )
            if current_key != idempotency_key or status == "completed":
                return
            self._state.write_json(
                relative,
                {
                    "execution_id": str(execution_id),
                    "idempotency_key": idempotency_key,
                    "input_fingerprint": fingerprint,
                    "operation": operation,
                    "status": "completed",
                },
            )

    @contextmanager
    def _idempotency_lock(self, scope: str):
        parent = descriptor = -1
        try:
            parent = self._state._open_parent(  # noqa: SLF001
                ("state", "idempotency-locks", ".directory"), create=True
            )
            lock_name = f"{scope}.lock"
            for _ in range(16):
                try:
                    descriptor = os.open(
                        lock_name,
                        _LOCK_CREATE_FLAGS,
                        0o600,
                        dir_fd=parent,
                    )
                    break
                except FileExistsError:
                    try:
                        descriptor = os.open(
                            lock_name, _LOCK_OPEN_FLAGS, dir_fd=parent
                        )
                        break
                    except FileNotFoundError:
                        continue
            if descriptor < 0:
                raise StateError("state_write_failed")
            metadata = os.fstat(descriptor)
            if not stat.S_ISREG(metadata.st_mode):
                raise StateError("state_path_invalid")
            os.fchmod(descriptor, 0o600)
            fcntl.flock(descriptor, fcntl.LOCK_EX)
            current = os.stat(
                lock_name, dir_fd=parent, follow_symlinks=False
            )
            if (metadata.st_dev, metadata.st_ino) != (current.st_dev, current.st_ino):
                raise StateError("state_path_invalid")
            yield
        except StateError:
            raise
        except OSError:
            raise StateError("state_write_failed") from None
        finally:
            if descriptor >= 0:
                try:
                    fcntl.flock(descriptor, fcntl.LOCK_UN)
                except OSError:
                    pass
                os.close(descriptor)
            if parent >= 0:
                os.close(parent)


def _parser() -> argparse.ArgumentParser:
    parser = _Parser(prog="sql-data-analyst", add_help=False)
    commands = parser.add_subparsers(dest="command", required=True)
    ingest = commands.add_parser("ingest", add_help=False)
    ingest.add_argument("--source", required=True)
    ingest.add_argument("--dataset", required=True)
    ingest.add_argument("--source-sha256", required=True)
    for name in ("analysis", "query"):
        query = commands.add_parser(name, add_help=False)
        query.add_argument("--dataset", required=True)
        query.add_argument("--sql-file", required=True)
        query.add_argument("--sql-sha256", required=True)
        query.add_argument("--manifest-sha256", required=True)
    report = commands.add_parser("report", add_help=False)
    report.add_argument("--dataset", required=True)
    report.add_argument("--summary-file", required=True)
    report.add_argument("--summary-sha256", required=True)
    report.add_argument("--manifest-sha256", required=True)
    for name in ("inspect", "delete"):
        local = commands.add_parser(name, add_help=False)
        local.add_argument("--dataset", required=True)
    commands.add_parser("doctor", add_help=False)
    return parser


def _input_fingerprint(operation: str, arguments: argparse.Namespace) -> str:
    dataset_id = str(_uuid(arguments.dataset))
    if operation == "dataset.ingest":
        content_digests = {"source": _declared_sha256(arguments.source_sha256)}
    elif operation in {"analysis.run", "query.execute"}:
        content_digests = {
            "manifest": _declared_sha256(arguments.manifest_sha256),
            "sql": _declared_sha256(arguments.sql_sha256),
        }
    elif operation == "report.create":
        content_digests = {
            "manifest": _declared_sha256(arguments.manifest_sha256),
            "summary": _declared_sha256(arguments.summary_sha256),
        }
    else:
        raise _UsageError()
    canonical = json.dumps(
        {
            "content_digests": content_digests,
            "dataset_id": dataset_id,
            "operation": operation,
        },
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def _expected_from_receipt(
    receipt: AuthorizationReceipt, installation_id: UUID, fingerprint: str
) -> ExpectedTicket:
    return ExpectedTicket(
        operation=receipt.operation,
        installation_id=installation_id,
        input_fingerprint=fingerprint,
        runner_version=RUNNER_VERSION,
    )


def _validate_receipt(
    receipt: AuthorizationReceipt, claims: TicketClaims, operation: str
) -> None:
    if (
        receipt.operation != operation
        or receipt.execution_id != claims.execution_id
        or receipt.currency != claims.currency
        or receipt.charged_amount != claims.charged_amount
    ):
        raise TicketError()


def _uuid(value: object) -> UUID:
    try:
        return UUID(str(value))
    except (TypeError, ValueError):
        raise DatasetError("dataset_invalid") from None


def _declared_sha256(value: object) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise _UsageError()
    return value


def _validated_idempotency(
    value: object, operation: str, fingerprint: str
) -> tuple[str, str]:
    try:
        if (
            not isinstance(value, dict)
            or value.get("operation") != operation
            or value.get("input_fingerprint") != fingerprint
            or value.get("status") not in {"pending", "completed"}
        ):
            raise StateError("state_read_failed")
        return str(UUID(str(value["idempotency_key"]))), str(value["status"])
    except (KeyError, TypeError, ValueError):
        raise StateError("state_read_failed") from None


def _assert_digest(actual: str, expected: object) -> None:
    declared = _declared_sha256(expected)
    if not hmac.compare_digest(actual, declared):
        raise TicketError()


def _manifest_digest(manifest: object) -> str:
    try:
        canonical = json.dumps(
            manifest.model_dump(mode="json"),
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
    except (AttributeError, TypeError, ValueError, UnicodeError):
        raise DatasetError() from None
    return hashlib.sha256(canonical).hexdigest()


def _decode_sql(content: bytes) -> str:
    try:
        return content.decode("utf-8-sig")
    except UnicodeError:
        raise QueryFailure("query_failed") from None


def _decode_json(content: bytes) -> object:
    try:
        return json.loads(content.decode("utf-8-sig"))
    except (UnicodeError, json.JSONDecodeError):
        raise ReportError("report_invalid") from None


def _read_bytes(path: Path) -> bytes:
    absolute = Path(os.path.abspath(os.path.expanduser(os.fspath(path))))
    if absolute == Path(absolute.anchor) or len(absolute.parts) < 2:
        raise DatasetError()
    parent = descriptor = -1
    try:
        parent = os.open(absolute.anchor, _DIRECTORY_FLAGS)
        for component in absolute.parts[1:-1]:
            child = os.open(component, _DIRECTORY_FLAGS, dir_fd=parent)
            os.close(parent)
            parent = child
        descriptor = os.open(absolute.parts[-1], _READ_FLAGS, dir_fd=parent)
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode) or metadata.st_size > MAX_INPUT_BYTES:
            raise DatasetError("dataset_too_large")
        with os.fdopen(descriptor, "rb") as stream:
            descriptor = -1
            content = stream.read(MAX_INPUT_BYTES + 1)
        if len(content) > MAX_INPUT_BYTES:
            raise DatasetError("dataset_too_large")
        return content
    except DatasetError:
        raise
    except OSError:
        raise DatasetError() from None
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        if parent >= 0:
            os.close(parent)


def _envelope(
    operation: str,
    receipt: AuthorizationReceipt | None,
    *,
    data: dict[str, object] | None = None,
    error: str | None = None,
) -> dict[str, object]:
    return {
        "schema_version": 1,
        "status": "failed" if error else "succeeded",
        "operation": operation,
        "execution_id": str(receipt.execution_id) if receipt else None,
        "charged_amount": receipt.charged_amount if receipt else None,
        "currency": receipt.currency if receipt else None,
        "balance_after": receipt.balance_after if receipt else None,
        "data": data if error is None else None,
        "error": {"code": error} if error else None,
    }


def _json_line(value: object) -> str:
    return json.dumps(value, ensure_ascii=True, separators=(",", ":"), sort_keys=True) + "\n"


def _error_code(exception: BaseException) -> str:
    if isinstance(exception, (KeyboardInterrupt, SystemExit)):
        return "interrupted"
    if isinstance(exception, _UsageError):
        return exception.code
    if isinstance(exception, ValidationError):
        return "input_invalid"
    if isinstance(
        exception,
        (
            PlatformError,
            TicketError,
            DatasetError,
            QueryFailure,
            ReportError,
            SettingsError,
            StateError,
        ),
    ):
        return str(exception.code)
    return "internal_error"


def main(argv: Sequence[str] | None = None) -> int:
    try:
        result = Cli().invoke(sys.argv[1:] if argv is None else argv)
    except BaseException as exception:
        code = _error_code(exception)
        result = CliResult(1, _json_line(_envelope("unknown", None, error=code)), f"error:{code}\n")
    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)
    return result.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
