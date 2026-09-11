from __future__ import annotations

from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq
import pytest

import sql_data_analyst_local.executor as executor_module
from sql_data_analyst_local.executor import execute_query
from sql_data_analyst_local.isolation import QueryLimits
from sql_data_analyst_local.results import QueryFailure

from sql_fixtures import create_sales_dataset


@pytest.fixture
def dataset(tmp_path: Path):
    return create_sales_dataset(tmp_path)


def test_unknown_table_fails_before_the_child_or_duckdb_opens(dataset, tmp_path):
    repository, manifest = dataset
    nonexistent_temp_parent = tmp_path / "must-not-be-opened"

    with pytest.raises(QueryFailure, match="^unknown_table$") as failure:
        execute_query(
            manifest,
            "SELECT * FROM missing",
            repository=repository,
            temporary_parent=nonexistent_temp_parent,
        )

    assert failure.value.code == "unknown_table"
    assert not nonexistent_temp_parent.exists()


def test_out_of_scope_nested_cte_cannot_expose_duckdb_system_catalog(
    dataset, tmp_path
):
    repository, manifest = dataset
    nonexistent_temp_parent = tmp_path / "must-not-be-opened"
    sql = (
        "SELECT system_catalog.table_name FROM "
        "(WITH duckdb_tables AS (SELECT 1 AS marker) "
        "SELECT marker FROM duckdb_tables) nested "
        "CROSS JOIN duckdb_tables AS system_catalog LIMIT 1"
    )

    with pytest.raises(QueryFailure, match="^unknown_table$") as failure:
        execute_query(
            manifest,
            sql,
            repository=repository,
            temporary_parent=nonexistent_temp_parent,
        )

    assert failure.value.code == "unknown_table"
    assert not nonexistent_temp_parent.exists()


def test_select_into_is_rejected_before_child_or_temp_creation(dataset, tmp_path):
    repository, manifest = dataset
    nonexistent_temp_parent = tmp_path / "must-not-be-opened"

    with pytest.raises(QueryFailure, match="^sql_rejected$") as failure:
        execute_query(
            manifest,
            "SELECT * INTO sales_copy FROM sales",
            repository=repository,
            temporary_parent=nonexistent_temp_parent,
        )

    assert failure.value.code == "sql_rejected"
    assert not nonexistent_temp_parent.exists()


@pytest.mark.parametrize("pseudo_identifier", ["user", "current_role", "current_schema"])
def test_environment_sensitive_pseudo_functions_fail_before_duckdb(
    dataset, tmp_path, pseudo_identifier
):
    repository, manifest = dataset
    nonexistent_temp_parent = tmp_path / "must-not-be-opened"

    with pytest.raises(QueryFailure, match="^sql_rejected$") as failure:
        execute_query(
            manifest,
            f"SELECT {pseudo_identifier}",
            repository=repository,
            temporary_parent=nonexistent_temp_parent,
        )

    assert failure.value.code == "sql_rejected"
    assert not nonexistent_temp_parent.exists()


def test_executor_never_accepts_a_parquet_path_in_user_sql(dataset, tmp_path):
    repository, manifest = dataset
    secret_path = tmp_path / "secret.parquet"

    with pytest.raises(QueryFailure, match="^sql_rejected$") as failure:
        execute_query(
            manifest,
            f"SELECT * FROM read_parquet('{secret_path}')",
            repository=repository,
        )

    assert failure.value.code == "sql_rejected"
    assert str(secret_path) not in str(failure.value)


def test_executor_rejects_a_manifest_not_owned_by_the_repository(dataset, tmp_path):
    _, manifest = dataset
    other_repository, _ = create_sales_dataset(tmp_path / "other")

    with pytest.raises(QueryFailure, match="^dataset_invalid$") as failure:
        execute_query(manifest, "SELECT * FROM sales", repository=other_repository)

    assert failure.value.code == "dataset_invalid"


def test_child_revalidates_a_table_swapped_to_an_outside_symlink(
    dataset, tmp_path, monkeypatch
):
    repository, manifest = dataset
    outside = tmp_path / "outside.parquet"
    pq.write_table(pa.table({"secret": ["must-not-read"]}), outside)
    table_path = repository.table_path(manifest.dataset_id, manifest.tables[0])
    real_run = executor_module.run_isolated_query

    def swap_before_child(**kwargs):
        table_path.unlink()
        table_path.symlink_to(outside)
        return real_run(**kwargs)

    monkeypatch.setattr(executor_module, "run_isolated_query", swap_before_child)

    with pytest.raises(QueryFailure, match="^dataset_invalid$") as failure:
        execute_query(manifest, "SELECT * FROM sales", repository=repository)

    assert failure.value.code == "dataset_invalid"
    assert "must-not-read" not in str(failure.value)
    assert str(outside) not in str(failure.value)


def test_executor_caps_rows_and_serializes_decimal_date_and_null(dataset):
    repository, manifest = dataset

    result = execute_query(
        manifest,
        "SELECT amount, sold_on, note FROM sales ORDER BY id",
        repository=repository,
    )

    assert len(result.rows) == 1_000
    assert result.truncated is True
    assert result.rows[0] == ["12.30", "2026-08-24", None]
    assert [column["name"] for column in result.columns] == [
        "amount",
        "sold_on",
        "note",
    ]
    assert 0 < result.byte_count <= 10 * 1024 * 1024
    assert result.elapsed_ms >= 0


def test_executor_truncates_at_the_serialized_json_limit(dataset):
    repository, manifest = dataset

    result = execute_query(
        manifest,
        "SELECT repeat('x', 500) AS value FROM sales",
        QueryLimits(max_result_bytes=1_024),
        repository=repository,
    )

    assert result.truncated is True
    assert 0 < len(result.rows) < 1_000
    assert result.byte_count <= 1_024


def test_executor_caps_a_multi_megabyte_result_at_ten_mib(dataset):
    repository, manifest = dataset

    result = execute_query(
        manifest,
        "SELECT repeat('x', 12000) AS value FROM sales",
        repository=repository,
    )

    assert result.truncated is True
    assert 9_000_000 < result.byte_count <= 10 * 1024 * 1024


def test_executor_maps_duckdb_memory_errors_without_leaking_details(dataset):
    repository, manifest = dataset

    with pytest.raises(QueryFailure, match="^query_resource_limit$") as failure:
        execute_query(
            manifest,
            "SELECT * FROM sales ORDER BY repeat(cast(id AS VARCHAR), 10000)",
            QueryLimits(duckdb_memory_limit_bytes=1024 * 1024),
            repository=repository,
        )

    assert failure.value.code == "query_resource_limit"
    assert str(repository.workspace_root) not in str(failure.value)
