from __future__ import annotations

import multiprocessing as mp
from pathlib import Path

import pytest

from sql_data_analyst_local.executor import execute_query
from sql_data_analyst_local.isolation import QueryLimits
from sql_data_analyst_local.results import QueryFailure

from sql_fixtures import create_sales_dataset


def test_default_limits_match_the_security_contract():
    limits = QueryLimits()

    assert limits.timeout_seconds == 30
    assert limits.address_space_bytes == 1024 * 1024 * 1024
    assert limits.threads <= 2
    assert limits.max_rows == 1_000
    assert limits.max_result_bytes == 10 * 1024 * 1024


@pytest.mark.parametrize(
    "limits",
    [
        {"timeout_seconds": 0},
        {"timeout_seconds": 31},
        {"address_space_bytes": 2 * 1024 * 1024 * 1024},
        {"threads": 3},
        {"max_rows": 1_001},
        {"max_result_bytes": 10 * 1024 * 1024 + 1},
        {"threads": 1.5},
    ],
)
def test_callers_cannot_raise_server_owned_limits(limits):
    with pytest.raises(ValueError):
        QueryLimits(**limits)


def test_timeout_terminates_and_reaps_child_and_cleans_temp_directory(tmp_path):
    repository, manifest = create_sales_dataset(tmp_path)
    temporary_parent = tmp_path / "query-temp"
    temporary_parent.mkdir()
    children_before = {process.pid for process in mp.active_children()}

    with pytest.raises(QueryFailure, match="^query_timeout$") as failure:
        execute_query(
            manifest,
            "SELECT sum(a.i * b.i) FROM range(1000000000) a(i), range(1000000000) b(i)",
            QueryLimits(timeout_seconds=0.05),
            repository=repository,
            temporary_parent=temporary_parent,
        )

    assert failure.value.code == "query_timeout"
    assert {process.pid for process in mp.active_children()} == children_before
    assert list(temporary_parent.iterdir()) == []


def test_low_address_space_cap_terminates_reaps_and_maps_resource_error(tmp_path):
    repository, manifest = create_sales_dataset(tmp_path)
    temporary_parent = tmp_path / "query-temp"
    temporary_parent.mkdir()
    children_before = {process.pid for process in mp.active_children()}

    with pytest.raises(QueryFailure, match="^query_resource_limit$") as failure:
        execute_query(
            manifest,
            "SELECT sum(a.i * b.i) FROM range(1000000000) a(i), range(1000000000) b(i)",
            QueryLimits(
                address_space_bytes=16 * 1024 * 1024,
                duckdb_memory_limit_bytes=1024 * 1024,
            ),
            repository=repository,
            temporary_parent=temporary_parent,
        )

    assert failure.value.code == "query_resource_limit"
    assert {process.pid for process in mp.active_children()} == children_before
    assert list(temporary_parent.iterdir()) == []


def test_success_also_cleans_the_isolated_temporary_directory(tmp_path):
    repository, manifest = create_sales_dataset(tmp_path)
    temporary_parent = tmp_path / "query-temp"
    temporary_parent.mkdir()

    result = execute_query(
        manifest,
        "SELECT count(*) AS count FROM sales",
        repository=repository,
        temporary_parent=temporary_parent,
    )

    assert result.rows == [[1_205]]
    assert list(temporary_parent.iterdir()) == []


def test_pipe_creation_failure_is_sanitized(monkeypatch, tmp_path):
    repository, manifest = create_sales_dataset(tmp_path)

    def fail_pipe(*_args, **_kwargs):
        raise OSError("sensitive fd details")

    monkeypatch.setattr(type(mp.get_context("spawn")), "Pipe", fail_pipe)

    with pytest.raises(QueryFailure, match="^query_failed$"):
        execute_query(
            manifest,
            "SELECT count(*) AS count FROM sales",
            repository=repository,
        )
