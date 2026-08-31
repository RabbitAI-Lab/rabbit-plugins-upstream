from __future__ import annotations

from dataclasses import dataclass
from typing import Any


_FAILURE_CODES = {
    "dataset_invalid",
    "query_failed",
    "query_resource_limit",
    "query_timeout",
    "sql_rejected",
    "unknown_table",
}


class QueryFailure(RuntimeError):
    """A stable query failure without SQL, data, traceback, or local paths."""

    def __init__(self, code: str = "query_failed") -> None:
        self.code = code if code in _FAILURE_CODES else "query_failed"
        super().__init__(self.code)


@dataclass(frozen=True)
class QueryResult:
    columns: list[dict[str, str]]
    rows: list[list[Any]]
    truncated: bool
    elapsed_ms: int
    byte_count: int
