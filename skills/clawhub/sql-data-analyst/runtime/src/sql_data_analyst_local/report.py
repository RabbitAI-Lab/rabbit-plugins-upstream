from __future__ import annotations

import html
import io
import json
import math
import os
import re
import secrets
import stat
from dataclasses import dataclass
from pathlib import Path
from typing import Literal
from uuid import UUID

import plotly.graph_objects as go
import plotly.offline
import xlsxwriter
from pydantic import Field, JsonValue, ValidationError, model_validator

from sql_data_analyst_local.contracts import StrictContract
from sql_data_analyst_local.state import LocalState, StateError


MAX_REPORT_BYTES = 25 * 1024 * 1024
_DIRECTORY_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
_WRITE_FLAGS = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW
_FORMULA_PREFIXES = ("=", "+", "-", "@", "\t", "\r")
_SURROGATES = re.compile(r"[\ud800-\udfff]")
_REMOTE_ASSIGNMENT = re.compile(
    r"(?P<prefix>\.(?P<attribute>src|href)\s*=\s*)"
    r"(?P<quote>['\"])https?://[^'\"]*(?P=quote)",
    re.IGNORECASE,
)
_MAX_EXCEL_STRING_LENGTH = 32767


class ReportError(RuntimeError):
    """A stable report failure without report content or filesystem paths."""

    def __init__(self, code: str = "report_failed") -> None:
        self.code = "report_failed" if code != "report_invalid" else code
        super().__init__(self.code)


class ReportTable(StrictContract):
    title: str = Field(min_length=1, max_length=128)
    columns: list[str] = Field(min_length=1, max_length=200)
    rows: list[list[JsonValue]] = Field(max_length=1000)

    @model_validator(mode="after")
    def valid_shape(self) -> "ReportTable":
        if len({column.casefold() for column in self.columns}) != len(self.columns):
            raise ValueError("duplicate columns")
        if any(not column or len(column) > 128 for column in self.columns):
            raise ValueError("invalid column")
        if any(len(row) != len(self.columns) for row in self.rows):
            raise ValueError("invalid row")
        if any(not _safe_cell(cell) for row in self.rows for cell in row):
            raise ValueError("invalid cell")
        return self


class ChartSpec(StrictContract):
    title: str = Field(min_length=1, max_length=128)
    kind: Literal["bar", "line"]
    table: int = Field(ge=0, le=9)
    x: str = Field(min_length=1, max_length=128)
    y: str = Field(min_length=1, max_length=128)


class ReportSummary(StrictContract):
    schema_version: Literal[1]
    title: str = Field(min_length=1, max_length=191)
    findings: list[str] = Field(max_length=50)
    limitations: list[str] = Field(max_length=50)
    tables: list[ReportTable] = Field(min_length=1, max_length=10)
    charts: list[ChartSpec] = Field(max_length=8)

    @model_validator(mode="after")
    def valid_content(self) -> "ReportSummary":
        for text in [self.title, *self.findings, *self.limitations]:
            if not text or len(text) > 2000:
                raise ValueError("invalid text")
        for chart in self.charts:
            if chart.table >= len(self.tables):
                raise ValueError("unknown chart table")
            columns = self.tables[chart.table].columns
            if chart.x not in columns or chart.y not in columns:
                raise ValueError("unknown chart column")
        return self


@dataclass(frozen=True)
class ReportArtifacts:
    xlsx_path: Path
    html_path: Path


class ReportWriter:
    def __init__(self, workspace_root: Path) -> None:
        try:
            self._state = LocalState(workspace_root)
        except StateError:
            raise ReportError() from None
        self.workspace_root = self._state.root

    def create(self, execution_id: UUID, summary: ReportSummary) -> ReportArtifacts:
        if not isinstance(execution_id, UUID) or not isinstance(summary, ReportSummary):
            raise ReportError("report_invalid")
        root = reports = execution = -1
        try:
            root = self._state._open_root(create=False)  # noqa: SLF001
            reports = _open_or_create_directory(root, "reports")
            execution = _open_or_create_directory(reports, str(execution_id))
            xlsx = _xlsx_bytes(summary)
            html_document = _html_document(summary).encode("utf-8")
            _atomic_write(execution, "analysis-report.xlsx", xlsx)
            _atomic_write(execution, "analysis-report.html", html_document)
            os.fsync(execution)
            os.fsync(reports)
            output = self.workspace_root / "reports" / str(execution_id)
            return ReportArtifacts(
                xlsx_path=output / "analysis-report.xlsx",
                html_path=output / "analysis-report.html",
            )
        except ReportError:
            raise
        except (
            OSError,
            UnicodeError,
            ValueError,
            TypeError,
            xlsxwriter.exceptions.XlsxWriterException,
        ):
            raise ReportError() from None
        finally:
            for descriptor in (execution, reports, root):
                if descriptor >= 0:
                    try:
                        os.close(descriptor)
                    except OSError:
                        pass


def parse_summary(value: object) -> ReportSummary:
    try:
        return ReportSummary.model_validate(value)
    except (ValidationError, TypeError, ValueError):
        raise ReportError() from None


def _safe_cell(value: JsonValue) -> bool:
    if value is None or isinstance(value, (bool, int)):
        return True
    if isinstance(value, float):
        return math.isfinite(value)
    if isinstance(value, str):
        return len(value) <= _MAX_EXCEL_STRING_LENGTH
    return False


def _open_or_create_directory(parent: int, name: str) -> int:
    try:
        descriptor = os.open(name, _DIRECTORY_FLAGS, dir_fd=parent)
    except FileNotFoundError:
        try:
            os.mkdir(name, 0o700, dir_fd=parent)
            descriptor = os.open(name, _DIRECTORY_FLAGS, dir_fd=parent)
        except OSError:
            raise ReportError() from None
    except OSError:
        raise ReportError() from None
    try:
        os.fchmod(descriptor, 0o700)
        if not stat.S_ISDIR(os.fstat(descriptor).st_mode):
            raise ReportError()
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _atomic_write(directory: int, name: str, content: bytes) -> None:
    if len(content) > MAX_REPORT_BYTES:
        raise ReportError()
    descriptor = -1
    temporary: str | None = None
    try:
        for _ in range(16):
            temporary = f".{name}.{secrets.token_hex(8)}.tmp"
            try:
                descriptor = os.open(
                    temporary,
                    _WRITE_FLAGS,
                    0o600,
                    dir_fd=directory,
                )
                break
            except FileExistsError:
                continue
        if descriptor < 0 or temporary is None:
            raise ReportError()
        os.fchmod(descriptor, 0o600)
        with os.fdopen(descriptor, "wb") as stream:
            descriptor = -1
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        try:
            target = os.stat(name, dir_fd=directory, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            if not stat.S_ISREG(target.st_mode):
                raise ReportError()
        os.replace(temporary, name, src_dir_fd=directory, dst_dir_fd=directory)
        temporary = None
        os.fsync(directory)
    except ReportError:
        raise
    except OSError:
        raise ReportError() from None
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        if temporary is not None:
            try:
                os.unlink(temporary, dir_fd=directory)
            except OSError:
                pass


def _clean_text(value: object) -> str:
    text = value if isinstance(value, str) else str(value)
    return _SURROGATES.sub("\ufffd", text)


def _cell(value: JsonValue) -> JsonValue | str:
    if not isinstance(value, str):
        return value
    cleaned = _clean_text(value)
    if cleaned.startswith(_FORMULA_PREFIXES):
        return "'" + cleaned
    return cleaned


def _xlsx_bytes(summary: ReportSummary) -> bytes:
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(
        output,
        {
            "in_memory": True,
            "constant_memory": False,
            "strings_to_formulas": False,
            "strings_to_urls": False,
        },
    )
    try:
        heading = workbook.add_format({"bold": True, "bg_color": "#E2E8F0"})
        overview = workbook.add_worksheet("Summary")
        overview.write(0, 0, _cell(summary.title), heading)
        row_number = 2
        for label, values in (("Findings", summary.findings), ("Limitations", summary.limitations)):
            overview.write(row_number, 0, label, heading)
            row_number += 1
            for value in values:
                overview.write(row_number, 0, _cell(value))
                row_number += 1
            row_number += 1

        used_sheet_names = {"summary"}
        for position, table in enumerate(summary.tables, start=1):
            sheet_name = _unique_sheet_name(
                table.title, position, used_sheet_names
            )
            used_sheet_names.add(sheet_name.casefold())
            worksheet = workbook.add_worksheet(sheet_name)
            for column_number, column in enumerate(table.columns):
                worksheet.write(0, column_number, _cell(column), heading)
            for row_index, row in enumerate(table.rows, start=1):
                for column_number, value in enumerate(row):
                    worksheet.write(row_index, column_number, _cell(value))
            worksheet.autofilter(0, 0, max(0, len(table.rows)), len(table.columns) - 1)
            worksheet.freeze_panes(1, 0)
    finally:
        workbook.close()
    return output.getvalue()


def _unique_sheet_name(
    value: str, position: int, used_names: set[str]
) -> str:
    cleaned = re.sub(r"[\[\]:*?/\\]", "_", _clean_text(value)).strip("'")[:31]
    base = cleaned or f"Table {position}"
    candidate = base
    suffix = 2
    while candidate.casefold() in used_names:
        marker = f" ({suffix})"
        candidate = base[: 31 - len(marker)] + marker
        suffix += 1
    return candidate


def _html_document(summary: ReportSummary) -> str:
    plotly_js = plotly.offline.get_plotlyjs()
    # Reports never need Plotly's optional remote loaders. Removing the callable
    # network primitives makes the artifact safe even outside its CSP sandbox.
    plotly_js = plotly_js.replace("fetch(", "blockedRequest(")
    plotly_js = plotly_js.replace("XMLHttpRequest", "BlockedRequest")
    plotly_js = plotly_js.replace("WebSocket", "BlockedSocket")
    plotly_js = plotly_js.replace("importScripts", "BlockedLoader")
    plotly_js = plotly_js.replace("Worker(", "BlockedThread(")
    plotly_js = _REMOTE_ASSIGNMENT.sub(_local_assignment, plotly_js)
    sections = [f"<h1>{html.escape(_clean_text(summary.title))}</h1>"]
    sections.append(_text_list("Findings", summary.findings))
    sections.append(_text_list("Limitations", summary.limitations))
    for table in summary.tables:
        head = "".join(f"<th>{html.escape(_clean_text(column))}</th>" for column in table.columns)
        body = "".join(
            "<tr>"
            + "".join(
                f"<td>{html.escape(_clean_text(value))}</td>" for value in row
            )
            + "</tr>"
            for row in table.rows
        )
        sections.append(
            f"<section><h2>{html.escape(_clean_text(table.title))}</h2>"
            f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></section>"
        )
    chart_scripts: list[str] = []
    for index, chart in enumerate(summary.charts):
        table = summary.tables[chart.table]
        x_index = table.columns.index(chart.x)
        y_index = table.columns.index(chart.y)
        figure = go.Figure()
        trace = go.Bar if chart.kind == "bar" else go.Scatter
        kwargs: dict[str, object] = {
            "x": [_clean_text(row[x_index]) for row in table.rows],
            "y": [row[y_index] for row in table.rows],
        }
        if chart.kind == "line":
            kwargs["mode"] = "lines+markers"
        figure.add_trace(trace(**kwargs))
        figure.update_layout(title=_clean_text(chart.title))
        chart_id = f"chart-{index}"
        sections.append(f'<section><div id="{chart_id}" class="chart"></div></section>')
        payload = (
            figure.to_json()
            .replace("<", "\\u003c")
            .replace(">", "\\u003e")
            .replace("&", "\\u0026")
        )
        chart_scripts.append(
            f"const figure{index}={payload};Plotly.newPlot('{chart_id}',"
            f"figure{index}.data,figure{index}.layout,"
            "{displayModeBar:false,responsive:true});"
        )
    csp = (
        "default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; "
        "img-src data:; font-src data:; connect-src 'none'; object-src 'none'; "
        "base-uri 'none'; form-action 'none'"
    )
    return (
        "<!doctype html><html><head><meta charset=\"utf-8\">"
        f'<meta http-equiv="Content-Security-Policy" content="{csp}">'
        "<meta name=\"referrer\" content=\"no-referrer\"><title>Analysis report</title>"
        "<style>body{font-family:system-ui,sans-serif;max-width:1200px;"
        "margin:2rem auto;padding:0 1rem;color:#172033}"
        "table{border-collapse:collapse;width:100%;margin-bottom:2rem}"
        "th,td{border:1px solid #cbd5e1;padding:.5rem;text-align:left}"
        "th{background:#e2e8f0}.chart{min-height:360px}</style></head><body>"
        + "".join(sections)
        + "<script>"
        + plotly_js
        + "\n"
        + "".join(chart_scripts)
        + "</script></body></html>"
    )


def _text_list(title: str, values: list[str]) -> str:
    items = "".join(f"<li>{html.escape(_clean_text(value))}</li>" for value in values)
    return f"<section><h2>{title}</h2><ul>{items}</ul></section>"


def _local_assignment(match: re.Match[str]) -> str:
    target = "data:," if match.group("attribute").casefold() == "src" else "#"
    quote = match.group("quote")
    return f"{match.group('prefix')}{quote}{target}{quote}"
