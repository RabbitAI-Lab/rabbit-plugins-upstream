from __future__ import annotations

import json
from typing import Any

import pyarrow as pa
import pyarrow.compute as pc


def bounded_profile(table: pa.Table, maximum_bytes: int) -> dict[str, Any]:
    columns: list[dict[str, Any]] = []
    for field, column in zip(table.schema, table.columns, strict=True):
        try:
            distinct_count: int | None = int(pc.count_distinct(column).as_py())
        except (pa.ArrowException, TypeError, ValueError):
            distinct_count = None
        columns.append(
            {
                "name": field.name,
                "type": str(field.type),
                "nullable": field.nullable,
                "null_count": column.null_count,
                "distinct_count": distinct_count,
            }
        )

    profile = {
        "row_count": table.num_rows,
        "column_count": table.num_columns,
        "columns": columns,
    }
    encoded = json.dumps(
        profile, ensure_ascii=False, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")
    if len(encoded) > maximum_bytes:
        raise ValueError("profile exceeds limit")
    return profile
