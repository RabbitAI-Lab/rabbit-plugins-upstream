from __future__ import annotations

import csv
import hashlib
import hmac
import io
import json
import os
import re
import stat
import unicodedata
import zipfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Any, Callable, Iterable
from uuid import UUID

import openpyxl
import openpyxl.xml
import polars as pl
import pyarrow as pa
import pyarrow.parquet as pq

from sql_data_analyst_local.contracts import (
    ExpectedTicket,
    TicketEnvelope,
)
from sql_data_analyst_local.datasets import (
    DatasetError,
    DatasetManifest,
    DatasetRepository,
    LocalColumn,
    LocalTable,
    _DatasetStage,
    _DirectoryHandle,
)
from sql_data_analyst_local.profile import bounded_profile
from sql_data_analyst_local.tickets import TicketVerifier


MAX_SOURCE_BYTES = 100 * 1024 * 1024
MAX_TABLES = 20
MAX_COLUMNS = 200
MAX_PROFILE_BYTES = 256 * 1024
MAX_ARCHIVE_ENTRIES = 1000
MAX_EXPANDED_ENTRY_BYTES = 100 * 1024 * 1024
MAX_EXPANDED_TOTAL_BYTES = 500 * 1024 * 1024
MAX_COMPRESSION_RATIO = 100
_SOURCE_FLAGS = os.O_RDONLY | os.O_NOFOLLOW
_SCALAR_TYPES = (str, int, float, bool, type(None))
_FORMATS = {
    ".csv": "csv",
    ".json": "json",
    ".jsonl": "jsonl",
    ".xlsx": "xlsx",
    ".parquet": "parquet",
}


@dataclass(frozen=True)
class ParsedTable:
    name: str
    table: pa.Table
    display_columns: list[str]


class IngestService:
    def __init__(
        self,
        repository: DatasetRepository,
        verifier: TicketVerifier,
        expected_ticket: ExpectedTicket,
        *,
        now: Callable[[], datetime],
    ) -> None:
        if not isinstance(repository, DatasetRepository):
            raise DatasetError()
        if not isinstance(verifier, TicketVerifier):
            raise DatasetError()
        if (
            not isinstance(expected_ticket, ExpectedTicket)
            or expected_ticket.operation != "dataset.ingest"
        ):
            raise DatasetError()
        self._repository = repository
        self._verifier = verifier
        self._expected_ticket = expected_ticket
        self._now = now

    def ingest(
        self,
        source: Path,
        dataset_id: UUID,
        ticket: TicketEnvelope,
        *,
        expected_source_fingerprint: str | None = None,
    ) -> DatasetManifest:
        self._verifier.verify(ticket, self._expected_ticket, self._now())
        if (
            not isinstance(source, Path)
            or not isinstance(dataset_id, UUID)
            or (
                expected_source_fingerprint is not None
                and (
                    not isinstance(expected_source_fingerprint, str)
                    or re.fullmatch(
                        r"[a-f0-9]{64}", expected_source_fingerprint
                    )
                    is None
                )
            )
        ):
            raise DatasetError()

        try:
            with self._repository._begin_staging(dataset_id) as stage:  # noqa: SLF001
                suffix_format = _FORMATS.get(source.suffix.casefold())
                if suffix_format is None:
                    raise DatasetError()
                source_name = f"source{source.suffix.casefold()}"
                source_size, source_fingerprint = _copy_source(
                    source, stage, source_name
                )
                if source_size == 0:
                    raise DatasetError()
                if expected_source_fingerprint is not None and not hmac.compare_digest(
                    source_fingerprint, expected_source_fingerprint
                ):
                    raise DatasetError()
                detected_format = detect_format(stage, source_name, suffix_format)
                if detected_format != suffix_format:
                    raise DatasetError()

                parsed = parse_source(stage, source_name, detected_format)
                if not parsed or len(parsed) > MAX_TABLES:
                    raise DatasetError("dataset_too_large")

                logical_names: set[str] = set()
                tables: list[LocalTable] = []
                with stage.create_directory("normalized") as normalized:
                    for position, parsed_table in enumerate(parsed, start=1):
                        if parsed_table.table.num_columns > MAX_COLUMNS:
                            raise DatasetError("dataset_too_large")
                        logical_name = unique_logical_name(
                            parsed_table.name, logical_names, position
                        )
                        table = normalize_columns(parsed_table.table)
                        try:
                            profile = bounded_profile(table, MAX_PROFILE_BYTES)
                        except ValueError:
                            raise DatasetError("dataset_too_large") from None
                        _write_parquet(
                            normalized,
                            f"{logical_name}.parquet",
                            table,
                        )
                        column_profiles = profile.pop("columns")
                        columns = [
                            LocalColumn(
                                name=str(column["name"]),
                                display_name=str(display_name)[:128],
                                type=str(column["type"]),
                                nullable=bool(column["nullable"]),
                                null_count=int(column["null_count"]),
                                distinct_count=column["distinct_count"],
                            )
                            for column, display_name in zip(
                                column_profiles,
                                parsed_table.display_columns,
                                strict=True,
                            )
                        ]
                        tables.append(
                            LocalTable(
                                logical_name=logical_name,
                                display_name=(
                                    parsed_table.name[:191] or f"Table {position}"
                                ),
                                parquet_path=f"normalized/{logical_name}.parquet",
                                row_count=table.num_rows,
                                columns=columns,
                                profile=profile,
                            )
                        )
                    normalized.sync()

                manifest = DatasetManifest(
                    schema_version=1,
                    dataset_id=dataset_id,
                    source_format=detected_format,
                    source_fingerprint=source_fingerprint,
                    tables=tables,
                )
                _write_manifest(stage, "manifest.json", manifest)
                stage.unlink_file(source_name)
                stage.sync()
                stage.commit()
                return manifest
        except DatasetError:
            raise
        except (OSError, UnicodeError, json.JSONDecodeError, pa.ArrowException):
            raise DatasetError() from None
        except Exception:
            raise DatasetError() from None


def _copy_source(
    source: Path, stage: _DatasetStage, destination_name: str
) -> tuple[int, str]:
    source_descriptor = -1
    destination_descriptor = -1
    try:
        source_descriptor = _open_source(source)
        metadata = os.fstat(source_descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            raise DatasetError()
        if metadata.st_size > MAX_SOURCE_BYTES:
            raise DatasetError("dataset_too_large")
        destination_descriptor = stage.create_file(destination_name)
        digest = hashlib.sha256()
        total = 0
        with os.fdopen(source_descriptor, "rb") as input_stream:
            source_descriptor = -1
            with os.fdopen(destination_descriptor, "wb") as output_stream:
                destination_descriptor = -1
                while chunk := input_stream.read(1024 * 1024):
                    total += len(chunk)
                    if total > MAX_SOURCE_BYTES:
                        raise DatasetError("dataset_too_large")
                    digest.update(chunk)
                    output_stream.write(chunk)
                output_stream.flush()
                os.fsync(output_stream.fileno())
        if total != metadata.st_size:
            raise DatasetError()
        return total, digest.hexdigest()
    except DatasetError:
        raise
    except OSError:
        raise DatasetError() from None
    finally:
        if source_descriptor >= 0:
            os.close(source_descriptor)
        if destination_descriptor >= 0:
            os.close(destination_descriptor)


def _open_source(source: Path) -> int:
    absolute = Path(os.path.abspath(os.path.expanduser(os.fspath(source))))
    if absolute == Path(absolute.anchor) or len(absolute.parts) < 2:
        raise DatasetError()
    try:
        parent = os.open(absolute.anchor, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    except OSError:
        raise DatasetError() from None
    try:
        for component in absolute.parts[1:-1]:
            try:
                child = os.open(
                    component,
                    os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                    dir_fd=parent,
                )
            except OSError:
                raise DatasetError() from None
            os.close(parent)
            parent = child
        try:
            return os.open(absolute.parts[-1], _SOURCE_FLAGS, dir_fd=parent)
        except OSError:
            raise DatasetError() from None
    finally:
        os.close(parent)


def detect_format(
    directory: _DirectoryHandle, name: str, suffix_format: str
) -> str:
    descriptor = directory.open_file(name)
    with os.fdopen(descriptor, "rb") as source:
        size = os.fstat(source.fileno()).st_size
        head = source.read(4)
        tail = b""
        if size >= 4:
            source.seek(-4, 2)
            tail = source.read(4)
    if head == b"PK\x03\x04":
        return "xlsx"
    if head == b"PAR1" and tail == b"PAR1":
        return "parquet"

    text = _decode_text(_read_bytes(directory, name))
    stripped = text.lstrip()
    if stripped.startswith("["):
        return "json"
    if stripped.startswith("{"):
        return "jsonl" if suffix_format == "jsonl" else "json"
    return "csv"


def parse_source(
    directory: _DirectoryHandle, name: str, source_format: str
) -> list[ParsedTable]:
    if source_format == "csv":
        table, display_columns = parse_csv(directory, name)
        return [ParsedTable("data", table, display_columns)]
    if source_format in {"json", "jsonl"}:
        table = parse_json(directory, name, jsonl=source_format == "jsonl")
        return [ParsedTable("data", table, table.column_names)]
    if source_format == "xlsx":
        return parse_xlsx(directory, name)
    if source_format == "parquet":
        table = parse_parquet(directory, name)
        return [ParsedTable("data", table, table.column_names)]
    raise DatasetError()


def _read_bytes(directory: _DirectoryHandle, name: str) -> bytes:
    descriptor = directory.open_file(name)
    with os.fdopen(descriptor, "rb") as stream:
        return stream.read(MAX_SOURCE_BYTES + 1)


def _decode_text(content: bytes) -> str:
    try:
        text = content.decode("utf-8-sig")
    except UnicodeDecodeError:
        try:
            text = content.decode("gb18030")
        except UnicodeDecodeError:
            raise DatasetError() from None
    if "\x00" in text:
        raise DatasetError()
    return text


def parse_csv(
    directory: _DirectoryHandle, name: str
) -> tuple[pa.Table, list[str]]:
    text = _decode_text(_read_bytes(directory, name))
    try:
        header = next(csv.reader(io.StringIO(text, newline="")))
    except (StopIteration, csv.Error):
        raise DatasetError() from None
    if len(header) > MAX_COLUMNS:
        raise DatasetError("dataset_too_large")
    display_columns = [str(value).strip() for value in header]
    frame = pl.read_csv(io.BytesIO(text.encode("utf-8")), try_parse_dates=True)
    table = frame.to_arrow()
    if table.num_columns != len(display_columns):
        raise DatasetError()
    return table.rename_columns(unique_column_names(display_columns)), display_columns


def parse_json(directory: _DirectoryHandle, name: str, *, jsonl: bool) -> pa.Table:
    text = _decode_text(_read_bytes(directory, name))
    if jsonl:
        records = [json.loads(line) for line in text.splitlines() if line.strip()]
    else:
        records = json.loads(text)
    if not isinstance(records, list):
        raise DatasetError()
    for record in records:
        if not isinstance(record, dict) or not all(
            isinstance(key, str) and isinstance(value, _SCALAR_TYPES)
            for key, value in record.items()
        ):
            raise DatasetError()
    keys: list[str] = []
    seen: set[str] = set()
    for record in records:
        for key in record:
            if key not in seen:
                seen.add(key)
                keys.append(key)
    normalized = [{key: record.get(key) for key in keys} for record in records]
    return pa.Table.from_pylist(normalized)


def parse_xlsx(directory: _DirectoryHandle, name: str) -> list[ParsedTable]:
    if not openpyxl.xml.DEFUSEDXML:
        raise DatasetError()
    validate_xlsx_archive(directory, name)
    descriptor = directory.open_file(name)
    with os.fdopen(descriptor, "rb") as stream:
        try:
            workbook = openpyxl.load_workbook(
                stream, read_only=True, data_only=True, keep_links=False
            )
        except Exception:
            raise DatasetError() from None
        try:
            if not workbook.worksheets or len(workbook.worksheets) > MAX_TABLES:
                raise DatasetError("dataset_too_large")
            parsed: list[ParsedTable] = []
            for worksheet in workbook.worksheets:
                rows = worksheet.iter_rows(values_only=True)
                header = next(rows, None)
                if header is None:
                    names: list[str] = []
                    display_columns: list[str] = []
                    table = pa.table({})
                else:
                    if len(header) > MAX_COLUMNS:
                        raise DatasetError("dataset_too_large")
                    display_columns = [
                        str(value).strip() if value is not None else ""
                        for value in header
                    ]
                    names = unique_column_names(header)
                    values = [dict(zip(names, row, strict=False)) for row in rows]
                    table = (
                        pa.Table.from_pylist(values)
                        if values
                        else pa.table({column: [] for column in names})
                    )
                parsed.append(ParsedTable(worksheet.title, table, display_columns))
            return parsed
        finally:
            workbook.close()


def validate_xlsx_archive(directory: _DirectoryHandle, name: str) -> None:
    descriptor = directory.open_file(name)
    try:
        with os.fdopen(descriptor, "rb") as stream, zipfile.ZipFile(stream) as archive:
            entries = archive.infolist()
            if len(entries) > MAX_ARCHIVE_ENTRIES:
                raise DatasetError("dataset_too_large")
            total = 0
            for entry in entries:
                member = PurePosixPath(entry.filename)
                unix_mode = entry.external_attr >> 16
                if (
                    member.is_absolute()
                    or not member.parts
                    or any(part in {"", ".", ".."} for part in member.parts)
                    or entry.flag_bits & 0x1
                    or stat.S_ISLNK(unix_mode)
                ):
                    raise DatasetError()
                total += entry.file_size
                compressed = max(entry.compress_size, 1)
                if (
                    entry.file_size > MAX_EXPANDED_ENTRY_BYTES
                    or total > MAX_EXPANDED_TOTAL_BYTES
                    or entry.file_size / compressed > MAX_COMPRESSION_RATIO
                ):
                    raise DatasetError("dataset_too_large")
    except DatasetError:
        raise
    except (OSError, zipfile.BadZipFile, zipfile.LargeZipFile):
        raise DatasetError() from None


def parse_parquet(directory: _DirectoryHandle, name: str) -> pa.Table:
    descriptor = directory.open_file(name)
    with os.fdopen(descriptor, "rb") as source:
        if os.fstat(source.fileno()).st_size < 8:
            raise DatasetError()
        if source.read(4) != b"PAR1":
            raise DatasetError()
        source.seek(-4, 2)
        if source.read(4) != b"PAR1":
            raise DatasetError()
        source.seek(0)
        try:
            parquet = pq.ParquetFile(source)
            if len(parquet.schema_arrow) > MAX_COLUMNS:
                raise DatasetError("dataset_too_large")
            return parquet.read()
        except DatasetError:
            raise
        except (OSError, pa.ArrowException):
            raise DatasetError() from None


def normalize_columns(table: pa.Table) -> pa.Table:
    return table.rename_columns(unique_column_names(table.column_names))


def unique_column_names(values: Iterable[Any]) -> list[str]:
    names: list[str] = []
    used: set[str] = set()
    for index, value in enumerate(values, start=1):
        base = str(value).strip() if value is not None else ""
        base = base[:128] or f"column_{index}"
        candidate = base
        suffix = 2
        while candidate.casefold() in used:
            candidate = f"{base[:120]}_{suffix}"
            suffix += 1
        used.add(candidate.casefold())
        names.append(candidate)
    return names


def unique_logical_name(name: str, used: set[str], position: int) -> str:
    normalized = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    base = re.sub(r"[^a-z0-9]+", "_", normalized.lower()).strip("_")[:48]
    base = base or f"table_{position}"
    candidate = base
    suffix = 2
    while candidate in used:
        candidate = f"{base[:45]}_{suffix}"
        suffix += 1
    used.add(candidate)
    return candidate


def _write_parquet(
    directory: _DirectoryHandle, name: str, table: pa.Table
) -> None:
    descriptor = directory.create_file(name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            descriptor = -1
            pq.write_table(table, stream, compression="zstd")
            stream.flush()
            os.fsync(stream.fileno())
    finally:
        if descriptor >= 0:
            os.close(descriptor)


def _write_manifest(
    directory: _DirectoryHandle, name: str, manifest: DatasetManifest
) -> None:
    encoded = manifest.model_dump_json().encode("utf-8") + b"\n"
    descriptor = directory.create_file(name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            descriptor = -1
            stream.write(encoded)
            stream.flush()
            os.fsync(stream.fileno())
    finally:
        if descriptor >= 0:
            os.close(descriptor)
