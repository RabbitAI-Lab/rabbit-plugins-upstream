from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

from sql_data_analyst_local.state import LocalState, StateError


def permissions(path: Path) -> int:
    return path.stat().st_mode & 0o777


def test_state_creates_private_directories_and_atomic_json_files(tmp_path):
    root = tmp_path / "workspace"
    state = LocalState(root)

    state.write_json("state/executions.json", {"execution": "ok"})
    target = root / "state" / "executions.json"

    assert permissions(root) == 0o700
    assert permissions(target.parent) == 0o700
    assert permissions(target) == 0o600
    assert json.loads(target.read_text()) == {"execution": "ok"}
    assert list(target.parent.glob(".*.tmp")) == []


def test_state_tightens_existing_permissions(tmp_path):
    root = tmp_path / "workspace"
    root.mkdir(mode=0o777)
    os.chmod(root, 0o777)

    LocalState(root)

    assert permissions(root) == 0o700


def test_atomic_failure_preserves_previous_state_and_removes_temporary_file(
    tmp_path, monkeypatch
):
    state = LocalState(tmp_path / "workspace")
    state.write_json("state/executions.json", {"version": 1})
    target = state.root / "state" / "executions.json"

    def fail_replace(source, destination, **kwargs):
        raise OSError("simulated replace failure")

    monkeypatch.setattr(os, "replace", fail_replace)

    with pytest.raises(StateError, match="^state_write_failed$"):
        state.write_json("state/executions.json", {"version": 2})

    assert json.loads(target.read_text()) == {"version": 1}
    assert list(target.parent.glob(".*.tmp")) == []


@pytest.mark.parametrize(
    "relative_path",
    ["../outside.json", "/tmp/outside.json", "state/../../outside.json"],
)
def test_state_rejects_paths_outside_private_root(tmp_path, relative_path):
    state = LocalState(tmp_path / "workspace")

    with pytest.raises(StateError, match="^state_path_invalid$"):
        state.write_json(relative_path, {"secret": True})


def test_state_refuses_symlink_targets(tmp_path):
    state = LocalState(tmp_path / "workspace")
    outside = tmp_path / "outside.json"
    outside.write_text("untouched")
    link = state.root / "linked.json"
    link.symlink_to(outside)

    with pytest.raises(StateError, match="^state_path_invalid$"):
        state.write_json("linked.json", {"changed": True})

    assert outside.read_text() == "untouched"


def test_state_rejects_symlinked_ancestor_of_nonexistent_root(tmp_path):
    outside = tmp_path / "outside"
    outside.mkdir()
    alias = tmp_path / "alias"
    alias.symlink_to(outside, target_is_directory=True)

    with pytest.raises(StateError, match="^state_path_invalid$"):
        LocalState(alias / "new-workspace")

    assert not (outside / "new-workspace").exists()


def test_state_rejects_symlinked_directory_inside_root(tmp_path):
    state = LocalState(tmp_path / "workspace")
    outside = tmp_path / "outside"
    outside.mkdir()
    (state.root / "state").symlink_to(outside, target_is_directory=True)

    with pytest.raises(StateError, match="^state_path_invalid$"):
        state.write_json("state/executions.json", {"escaped": True})

    assert not (outside / "executions.json").exists()


def test_state_rechecks_root_without_following_symlink_before_each_write(tmp_path):
    root = tmp_path / "workspace"
    state = LocalState(root)
    original = tmp_path / "original-workspace"
    root.rename(original)
    outside = tmp_path / "outside"
    outside.mkdir()
    root.symlink_to(outside, target_is_directory=True)

    with pytest.raises(StateError, match="^state_path_invalid$"):
        state.write_json("executions.json", {"escaped": True})

    assert not (outside / "executions.json").exists()


def test_state_sanitizes_root_creation_failures(tmp_path, monkeypatch):
    real_mkdir = os.mkdir

    def fail_workspace_mkdir(path, *args, **kwargs):
        if path == "workspace":
            raise PermissionError(f"must not expose {tmp_path}")
        return real_mkdir(path, *args, **kwargs)

    monkeypatch.setattr(os, "mkdir", fail_workspace_mkdir)

    with pytest.raises(StateError, match="^state_write_failed$") as caught:
        LocalState(tmp_path / "workspace")

    assert caught.value.__cause__ is None
