from __future__ import annotations

from pathlib import Path

from sql_data_analyst_local.datasets import (
    DatasetError,
    DatasetManifest,
    DatasetRepository,
)
from sql_data_analyst_local.isolation import QueryLimits, run_isolated_query
from sql_data_analyst_local.results import QueryFailure, QueryResult
from sql_data_analyst_local.settings import default_workspace_root
from sql_data_analyst_local.sql_policy import SqlRejected, validate_sql


def execute_query(
    manifest: DatasetManifest,
    sql: str,
    limits: QueryLimits = QueryLimits(),
    *,
    repository: DatasetRepository | None = None,
    temporary_parent: Path | None = None,
) -> QueryResult:
    if not isinstance(manifest, DatasetManifest) or not isinstance(limits, QueryLimits):
        raise QueryFailure("dataset_invalid")
    try:
        owned_repository = repository or DatasetRepository(default_workspace_root())
        if not isinstance(owned_repository, DatasetRepository):
            raise DatasetError()
        owned_manifest = owned_repository.inspect(manifest.dataset_id)
        if owned_manifest != manifest:
            raise DatasetError()
    except DatasetError:
        raise QueryFailure("dataset_invalid") from None

    try:
        validated = validate_sql(sql, owned_manifest.table_map)
    except SqlRejected as exception:
        raise QueryFailure(exception.code) from None

    return run_isolated_query(
        workspace_root=owned_repository.workspace_root,
        manifest=owned_manifest.model_dump(mode="json"),
        sql=validated.sql,
        limits=limits,
        temporary_parent=temporary_parent,
    )
