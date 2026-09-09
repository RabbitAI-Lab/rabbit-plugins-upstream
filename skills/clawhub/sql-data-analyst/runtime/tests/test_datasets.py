from __future__ import annotations

import json
from pathlib import Path
from uuid import uuid4

import pyarrow as pa
import pyarrow.parquet as pq
import pytest

from sql_data_analyst_local.datasets import DatasetError, DatasetRepository


def permissions(path: Path) -> int:
    return path.stat().st_mode & 0o777


def test_repository_rejects_arbitrary_identifiers_and_paths(tmp_path):
    repository = DatasetRepository(tmp_path / "workspace")

    for value in ("../outside", "/tmp/outside", tmp_path / "outside"):
        with pytest.raises(DatasetError, match="^dataset_invalid$"):
            repository.inspect(value)  # type: ignore[arg-type]
        with pytest.raises(DatasetError, match="^dataset_invalid$"):
            repository.delete(value)  # type: ignore[arg-type]


def test_delete_removes_only_the_exact_uuid_owned_directory(tmp_path):
    repository = DatasetRepository(tmp_path / "workspace")
    target_id = uuid4()
    sibling_id = uuid4()
    target = repository.dataset_path(target_id)
    sibling = repository.dataset_path(sibling_id)
    target.mkdir(mode=0o700)
    sibling.mkdir(mode=0o700)
    (target / "manifest.json").write_text("{}")
    (sibling / "keep.txt").write_text("keep")
    outside = tmp_path / "outside.txt"
    outside.write_text("untouched")

    repository.delete(target_id)

    assert not target.exists()
    assert (sibling / "keep.txt").read_text() == "keep"
    assert outside.read_text() == "untouched"


def test_delete_refuses_symlinked_dataset_directory(tmp_path):
    repository = DatasetRepository(tmp_path / "workspace")
    dataset_id = uuid4()
    outside = tmp_path / "outside"
    outside.mkdir()
    (outside / "keep.txt").write_text("keep")
    repository.dataset_path(dataset_id).symlink_to(outside, target_is_directory=True)

    with pytest.raises(DatasetError, match="^dataset_invalid$"):
        repository.delete(dataset_id)

    assert (outside / "keep.txt").read_text() == "keep"


def test_delete_refuses_symlink_inside_dataset_before_removing_regular_files(tmp_path):
    repository = DatasetRepository(tmp_path / "workspace")
    dataset_id = uuid4()
    dataset = repository.dataset_path(dataset_id)
    dataset.mkdir(mode=0o700)
    keep = dataset / "keep.txt"
    keep.write_text("keep")
    outside = tmp_path / "outside.txt"
    outside.write_text("outside")
    (dataset / "linked.txt").symlink_to(outside)

    with pytest.raises(DatasetError, match="^dataset_invalid$"):
        repository.delete(dataset_id)

    assert keep.read_text() == "keep"
    assert outside.read_text() == "outside"


def test_inspect_rejects_invalid_or_sample_bearing_manifest(tmp_path):
    repository = DatasetRepository(tmp_path / "workspace")
    dataset_id = uuid4()
    dataset = repository.dataset_path(dataset_id)
    dataset.mkdir(mode=0o700)
    (dataset / "manifest.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "dataset_id": str(dataset_id),
                "source_format": "csv",
                "source_fingerprint": "a" * 64,
                "tables": [],
                "rows": [{"secret": "must-not-load"}],
            }
        )
    )

    with pytest.raises(DatasetError, match="^dataset_invalid$") as caught:
        repository.inspect(dataset_id)

    assert "must-not-load" not in str(caught.value)


def test_inspect_refuses_symlink_manifest(tmp_path):
    repository = DatasetRepository(tmp_path / "workspace")
    dataset_id = uuid4()
    dataset = repository.dataset_path(dataset_id)
    dataset.mkdir(mode=0o700)
    outside = tmp_path / "outside.json"
    outside.write_text("{}")
    (dataset / "manifest.json").symlink_to(outside)

    with pytest.raises(DatasetError, match="^dataset_invalid$"):
        repository.inspect(dataset_id)


def test_inspect_rejects_row_samples_hidden_inside_profile(tmp_path):
    repository = DatasetRepository(tmp_path / "workspace")
    dataset_id = uuid4()
    dataset = repository.dataset_path(dataset_id)
    normalized = dataset / "normalized"
    normalized.mkdir(parents=True, mode=0o700)
    pq.write_table(pa.table({"amount": [1]}), normalized / "data.parquet")
    secret = "profile-secret-must-not-load"
    (dataset / "manifest.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "dataset_id": str(dataset_id),
                "source_format": "csv",
                "source_fingerprint": "a" * 64,
                "tables": [
                    {
                        "logical_name": "data",
                        "display_name": "data",
                        "parquet_path": "normalized/data.parquet",
                        "row_count": 1,
                        "columns": [
                            {
                                "name": "amount",
                                "display_name": "amount",
                                "type": "int64",
                                "nullable": True,
                                "null_count": 0,
                                "distinct_count": 1,
                            }
                        ],
                        "profile": {
                            "row_count": 1,
                            "column_count": 1,
                            "rows": [{"amount": secret}],
                        },
                    }
                ],
            }
        )
    )

    with pytest.raises(DatasetError, match="^dataset_invalid$") as caught:
        repository.inspect(dataset_id)

    assert secret not in str(caught.value)


def test_repository_creates_private_dataset_root(tmp_path):
    repository = DatasetRepository(tmp_path / "workspace")

    assert permissions(repository.workspace_root) == 0o700
    assert permissions(repository.datasets_root) == 0o700


def test_repository_rechecks_workspace_root_before_operations(tmp_path):
    workspace = tmp_path / "workspace"
    repository = DatasetRepository(workspace)
    original = tmp_path / "original"
    workspace.rename(original)
    outside = tmp_path / "outside"
    outside.mkdir()
    workspace.symlink_to(outside, target_is_directory=True)

    with pytest.raises(DatasetError, match="^dataset_invalid$"):
        repository.delete(uuid4())

    assert list(outside.iterdir()) == []
