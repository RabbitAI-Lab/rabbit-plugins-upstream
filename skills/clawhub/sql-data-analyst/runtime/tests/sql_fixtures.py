from __future__ import annotations

import json
import os
from datetime import date
from decimal import Decimal
from pathlib import Path
from uuid import uuid4

import pyarrow as pa
import pyarrow.parquet as pq

from sql_data_analyst_local.datasets import (
    DatasetManifest,
    DatasetRepository,
    LocalColumn,
    LocalTable,
)


def create_sales_dataset(tmp_path: Path, *, rows: int = 1_205):
    repository = DatasetRepository(tmp_path / "workspace")
    dataset_id = uuid4()
    table = pa.table(
        {
            "id": list(range(rows)),
            "category": ["books" if index % 2 == 0 else "games" for index in range(rows)],
            "amount": [Decimal("12.30")] * rows,
            "sold_on": [date(2026, 8, 24)] * rows,
            "note": pa.nulls(rows),
        }
    )
    manifest = DatasetManifest(
        schema_version=1,
        dataset_id=dataset_id,
        source_format="parquet",
        source_fingerprint="a" * 64,
        tables=[
            LocalTable(
                logical_name="sales",
                display_name="Sales",
                parquet_path="normalized/sales.parquet",
                row_count=rows,
                columns=[
                    LocalColumn(
                        name=field.name,
                        display_name=field.name,
                        type=str(field.type),
                        nullable=True,
                        null_count=rows if field.name == "note" else 0,
                        distinct_count=None,
                    )
                    for field in table.schema
                ],
                profile={"row_count": rows, "column_count": table.num_columns},
            )
        ],
    )

    with repository._begin_staging(dataset_id) as stage:  # noqa: SLF001
        with stage.create_directory("normalized") as normalized:
            with os.fdopen(normalized.create_file("sales.parquet"), "wb") as stream:
                pq.write_table(table, stream)
            normalized.sync()
        with os.fdopen(stage.create_file("manifest.json"), "w") as stream:
            json.dump(manifest.model_dump(mode="json"), stream)
            stream.flush()
            os.fsync(stream.fileno())
        stage.sync()
        stage.commit()

    return repository, manifest
