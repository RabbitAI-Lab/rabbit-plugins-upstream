from __future__ import annotations

import pytest

from sql_data_analyst_local.datasets import LocalColumn, LocalTable
from sql_data_analyst_local.sql_policy import SqlRejected, validate_sql


@pytest.fixture
def tables():
    table = LocalTable(
        logical_name="sales",
        display_name="Sales",
        parquet_path="normalized/sales.parquet",
        row_count=2,
        columns=[
            LocalColumn(
                name="amount",
                display_name="Amount",
                type="decimal128(10, 2)",
                nullable=False,
                null_count=0,
                distinct_count=2,
            )
        ],
        profile={"row_count": 2, "column_count": 1},
    )
    return {"sales": table}


@pytest.mark.parametrize(
    "sql",
    [
        "SELECT category, SUM(amount) FROM sales GROUP BY category",
        "WITH ranked AS (SELECT *, row_number() OVER (ORDER BY amount DESC) rn FROM sales) SELECT * FROM ranked WHERE rn <= 10",
        'SELECT "amount" FROM "sales"',
        "SELECT s.amount FROM sales AS s",
        "SELECT nested.total FROM (SELECT sum(amount) AS total FROM sales) AS nested",
        "SELECT CASE WHEN amount > 0 THEN round(amount, 2) ELSE 0 END FROM sales",
        "SELECT i FROM range(3) AS generated(i)",
        "SELECT amount -- harmless explanation\nFROM sales",
    ],
)
def test_read_only_queries_are_allowed(sql, tables):
    validated = validate_sql(sql, tables)

    assert validated.sql
    assert "comment" not in validated.sql


@pytest.mark.parametrize(
    "sql",
    [
        "INSERT INTO sales VALUES (1)",
        "UPDATE sales SET amount = 0",
        "DELETE FROM sales",
        "CREATE TABLE stolen AS SELECT * FROM sales",
        "DROP TABLE sales",
        "COPY sales TO '/tmp/out.csv'",
        "ATTACH '/tmp/other.db' AS x",
        "DETACH x",
        "INSTALL httpfs",
        "LOAD httpfs",
        "PRAGMA enable_external_access=true",
        "CALL checkpoint()",
        "EXPORT DATABASE '/tmp/export'",
        "IMPORT DATABASE '/tmp/export'",
        "SELECT * FROM read_csv_auto('/etc/passwd')",
        "SELECT * FROM read_parquet('/tmp/secret.parquet')",
        "SELECT * FROM parquet_scan('s3://bucket/file.parquet')",
        "SELECT * FROM glob('/tmp/*')",
        "SELECT random() FROM sales",
        "SELECT uuid() FROM sales",
        "SELECT current_timestamp FROM sales",
        "SELECT getenv('HOME')",
        "SELECT read_text('/etc/passwd')",
        "SELECT * FROM query('SELECT 1')",
        "SELECT arbitrary_future_extension(amount) FROM sales",
        "SELECT * FROM main.sales",
        "SELECT 1; SELECT 2",
        "SELECT 1 /* ; DROP TABLE sales */",
        "WITH RECURSIVE numbers AS (SELECT 1 UNION ALL SELECT * FROM numbers) SELECT * FROM numbers",
        "VALUES (1)",
        "nonsense that cannot parse",
    ],
)
def test_external_mutating_and_nondeterministic_sql_is_rejected(sql, tables):
    with pytest.raises(SqlRejected, match="^sql_rejected$") as failure:
        validate_sql(sql, tables)

    assert failure.value.code == "sql_rejected"


def test_unknown_tables_have_a_stable_error(tables):
    with pytest.raises(SqlRejected, match="^unknown_table$") as failure:
        validate_sql("SELECT * FROM missing", tables)

    assert failure.value.code == "unknown_table"


def test_cte_shadowing_does_not_hide_an_unknown_source(tables):
    with pytest.raises(SqlRejected, match="^unknown_table$"):
        validate_sql(
            "WITH sales AS (SELECT * FROM secret_table) SELECT * FROM sales",
            tables,
        )


def test_nested_cte_name_is_not_visible_in_the_outer_scope(tables):
    sql = (
        "SELECT * FROM "
        "(WITH duckdb_tables AS (SELECT 1 AS marker) "
        "SELECT marker FROM duckdb_tables) nested "
        "CROSS JOIN duckdb_tables AS system_catalog"
    )

    with pytest.raises(SqlRejected, match="^unknown_table$"):
        validate_sql(sql, tables)


@pytest.mark.parametrize(
    "sql",
    [
        "WITH outer_cte AS (SELECT * FROM sales) SELECT * FROM (WITH inner_cte AS (SELECT * FROM outer_cte) SELECT * FROM inner_cte) nested",
        "WITH shared AS (SELECT * FROM sales) SELECT * FROM (WITH shared AS (SELECT * FROM shared) SELECT * FROM shared) nested",
    ],
)
def test_nested_ctes_can_see_outer_ctes_and_shadow_them(sql, tables):
    assert validate_sql(sql, tables).sql


def test_select_into_is_rejected_even_though_the_root_is_select(tables):
    with pytest.raises(SqlRejected, match="^sql_rejected$"):
        validate_sql("SELECT * INTO sales_copy FROM sales", tables)


def test_recursive_with_is_rejected_inside_a_nested_subquery(tables):
    sql = (
        "SELECT * FROM (WITH RECURSIVE n AS "
        "(SELECT 1 UNION ALL SELECT * FROM n) SELECT * FROM n) nested"
    )

    with pytest.raises(SqlRejected, match="^sql_rejected$"):
        validate_sql(sql, tables)


@pytest.mark.parametrize("pseudo_identifier", ["user", "current_role", "current_schema"])
def test_environment_sensitive_bare_identifiers_are_rejected(
    pseudo_identifier, tables
):
    with pytest.raises(SqlRejected, match="^sql_rejected$"):
        validate_sql(f"SELECT {pseudo_identifier}", tables)


@pytest.mark.parametrize(
    "sql",
    [
        "SELECT * FROM '/tmp/secret.parquet'",
        "SELECT * FROM 'normalized/sales.parquet'",
        "SELECT * FROM read_parquet('normalized/sales.parquet')",
        "SELECT 'normalized/sales.parquet' AS path",
    ],
)
def test_sql_cannot_reference_parquet_paths(sql, tables):
    with pytest.raises(SqlRejected):
        validate_sql(sql, tables)


def test_empty_non_string_and_oversized_sql_are_rejected(tables):
    for sql in [None, "", " " * 10, "SELECT 1 " + (" " * 20_001)]:
        with pytest.raises(SqlRejected, match="^sql_rejected$"):
            validate_sql(sql, tables)  # type: ignore[arg-type]
