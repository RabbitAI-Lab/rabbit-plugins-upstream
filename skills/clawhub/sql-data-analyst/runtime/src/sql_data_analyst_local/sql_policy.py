from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass

import sqlglot
from sqlglot import exp
from sqlglot.errors import ParseError
from sqlglot.optimizer.scope import traverse_scope

from sql_data_analyst_local.datasets import LocalTable


MAX_SQL_CHARACTERS = 20_000
FORBIDDEN_NODE_NAMES = {
    "alter",
    "analyze",
    "attach",
    "call",
    "command",
    "commit",
    "copy",
    "create",
    "delete",
    "detach",
    "drop",
    "export",
    "grant",
    "import",
    "insert",
    "install",
    "load",
    "merge",
    "pragma",
    "rollback",
    "transaction",
    "update",
    "use",
}
EXTERNAL_FUNCTIONS = {
    "delta_scan",
    "excel_scan",
    "glob",
    "httpfs",
    "iceberg_scan",
    "parquet_scan",
    "read_blob",
    "read_csv",
    "read_csv_auto",
    "read_json",
    "read_json_auto",
    "read_json_objects",
    "read_ndjson",
    "read_parquet",
    "read_text",
    "read_xlsx",
    "sqlite_scan",
}
NONDETERMINISTIC_NODE_NAMES = {
    "currentdate",
    "currenttime",
    "currenttimestamp",
    "currentuser",
    "rand",
    "uuid",
    "version",
}
NONDETERMINISTIC_FUNCTIONS = {
    "current_date",
    "current_time",
    "current_timestamp",
    "gen_random_uuid",
    "now",
    "random",
    "setseed",
    "today",
    "uuid",
}
SENSITIVE_FUNCTIONS = {
    "current_setting",
    "getenv",
    "query",
    "query_table",
    "set_config",
}
SENSITIVE_PSEUDO_IDENTIFIERS = {"current_role", "current_schema", "user"}
SAFE_TABLE_FUNCTIONS = {"generate_series", "range", "unnest"}
ALLOWED_FUNCTIONS = {
    # Aggregates.
    "approx_count_distinct",
    "array_agg",
    "avg",
    "count",
    "count_if",
    "first",
    "last",
    "max",
    "median",
    "min",
    "product",
    "stddev",
    "stddev_pop",
    "stddev_samp",
    "string_agg",
    "sum",
    "variance",
    "var_pop",
    "var_samp",
    # Window functions.
    "cume_dist",
    "dense_rank",
    "first_value",
    "lag",
    "last_value",
    "lead",
    "nth_value",
    "ntile",
    "percent_rank",
    "rank",
    "row_number",
    # Date and time.
    "date_add",
    "date_diff",
    "date_part",
    "date_sub",
    "date_trunc",
    "day",
    "dayofweek",
    "dayofyear",
    "epoch",
    "extract",
    "hour",
    "minute",
    "month",
    "quarter",
    "second",
    "strftime",
    "strptime",
    "week",
    "year",
    # Numeric, conditional, and conversion helpers.
    "abs",
    "acos",
    "asin",
    "atan",
    "atan2",
    "cast",
    "ceil",
    "ceiling",
    "case",
    "coalesce",
    "cos",
    "degrees",
    "exp",
    "floor",
    "greatest",
    "if",
    "isnan",
    "least",
    "ln",
    "log",
    "log10",
    "mod",
    "nullif",
    "pi",
    "power",
    "radians",
    "round",
    "sign",
    "sin",
    "sqrt",
    "tan",
    "try_cast",
    # String, list, and safe table helpers.
    "concat",
    "concat_ws",
    "contains",
    "ends_with",
    "generate_series",
    "left",
    "length",
    "lower",
    "lpad",
    "ltrim",
    "range",
    "regexp_extract",
    "regexp_matches",
    "regexp_replace",
    "repeat",
    "replace",
    "reverse",
    "right",
    "rpad",
    "rtrim",
    "starts_with",
    "substr",
    "substring",
    "trim",
    "unnest",
    "upper",
}
SUSPICIOUS_COMMENT = re.compile(
    r";|\b(?:attach|call|copy|create|delete|detach|drop|export|import|insert|"
    r"install|load|pragma|update)\b",
    re.IGNORECASE,
)


class SqlRejected(ValueError):
    """A stable policy failure that never includes submitted SQL."""

    def __init__(self, code: str = "sql_rejected") -> None:
        self.code = code if code in {"sql_rejected", "unknown_table"} else "sql_rejected"
        super().__init__(self.code)


@dataclass(frozen=True)
class ValidatedQuery:
    sql: str


def validate_sql(sql: str, tables: Mapping[str, LocalTable]) -> ValidatedQuery:
    if (
        not isinstance(sql, str)
        or not sql.strip()
        or len(sql) > MAX_SQL_CHARACTERS
        or not isinstance(tables, Mapping)
    ):
        raise SqlRejected()
    allowed = _validated_table_names(tables)
    _reject_suspicious_comments(sql)

    try:
        statements = sqlglot.parse(sql, read="duckdb")
    except (ParseError, ValueError, TypeError):
        raise SqlRejected() from None
    if len(statements) != 1 or not isinstance(statements[0], exp.Select):
        raise SqlRejected()
    statement = statements[0]

    for node in statement.walk():
        node_name = type(node).__name__.casefold()
        if node_name in FORBIDDEN_NODE_NAMES:
            raise SqlRejected()

        if isinstance(node, exp.Into):
            raise SqlRejected()

        if isinstance(node, exp.With) and node.args.get("recursive") is True:
            raise SqlRejected()

        if (
            isinstance(node, exp.Column)
            and not node.table
            and node.name.casefold() in SENSITIVE_PSEUDO_IDENTIFIERS
        ):
            raise SqlRejected()

        if (
            isinstance(node, exp.Literal)
            and node.is_string
            and ".parquet" in str(node.this).casefold()
        ):
            raise SqlRejected()

        if isinstance(node, exp.Func):
            function_name = _function_name(node)
            if (
                function_name not in ALLOWED_FUNCTIONS
                or node_name in NONDETERMINISTIC_NODE_NAMES
                or function_name in NONDETERMINISTIC_FUNCTIONS
                or function_name in EXTERNAL_FUNCTIONS
                or function_name in SENSITIVE_FUNCTIONS
                or function_name.startswith(
                    ("http", "s3", "azure", "shell", "system")
                )
            ):
                raise SqlRejected()

        if isinstance(node, exp.Table):
            if node.args.get("catalog") is not None or node.args.get("db") is not None:
                raise SqlRejected()
            if not isinstance(node.this, exp.Identifier):
                if _function_name(node.this) not in SAFE_TABLE_FUNCTIONS:
                    raise SqlRejected()

    _validate_table_scopes(statement, allowed)

    normalized = statement.sql(dialect="duckdb", pretty=False, comments=False)
    return ValidatedQuery(sql=normalized)


def _validated_table_names(tables: Mapping[str, LocalTable]) -> set[str]:
    allowed: set[str] = set()
    for name, table in tables.items():
        if (
            not isinstance(name, str)
            or not isinstance(table, LocalTable)
            or name != table.logical_name
            or name.casefold() in allowed
        ):
            raise SqlRejected()
        allowed.add(name.casefold())
    return allowed


def _validate_table_scopes(statement: exp.Select, allowed: set[str]) -> None:
    validated_nodes: set[int] = set()
    for scope in traverse_scope(statement):
        visible_ctes = {name.casefold() for name in scope.cte_sources}
        for table in scope.tables:
            if not isinstance(table.this, exp.Identifier):
                continue
            validated_nodes.add(id(table))
            table_name = table.name.casefold()
            if table_name not in visible_ctes and table_name not in allowed:
                raise SqlRejected("unknown_table")

    for table in statement.find_all(exp.Table):
        if isinstance(table.this, exp.Identifier) and id(table) not in validated_nodes:
            raise SqlRejected("unknown_table")


def _function_name(node: exp.Expression) -> str:
    if isinstance(node, exp.Anonymous):
        return node.name.casefold()
    try:
        return node.sql_name().casefold()
    except (AttributeError, TypeError):
        return type(node).__name__.casefold()


def _reject_suspicious_comments(sql: str) -> None:
    comments = re.findall(r"--[^\r\n]*|/\*.*?\*/", sql, flags=re.DOTALL)
    if any(SUSPICIOUS_COMMENT.search(comment) for comment in comments):
        raise SqlRejected()
