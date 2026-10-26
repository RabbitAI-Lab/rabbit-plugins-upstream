#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
import zipfile
from datetime import datetime
from pathlib import Path

from notebook_sync_core import load_config as load_notebook_config, load_state as load_notebook_state
from team_memory_paths import TeamMemoryPathError, print_warnings, rel_path, resolve_paths, run_with_write_lock


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run_rebuild_index(skill_dir: Path) -> int:
    return subprocess.run(
        [sys.executable, str(skill_dir / "scripts" / "rebuild-index.py"), "--skill-dir", str(skill_dir)],
        check=False,
    ).returncode


def resolve_output(raw: str | None, skill_dir: Path) -> Path:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    if raw:
        output = Path(raw).expanduser()
        if not output.is_absolute():
            output = skill_dir / output
    else:
        output = skill_dir / "exports" / f"team-memory-export-{stamp}.zip"
    if output.suffix.lower() != ".zip":
        output = output / f"team-memory-export-{stamp}.zip"
    return output.resolve()


def main() -> int:
    parser = argparse.ArgumentParser(description="Export Team Memory Markdown data plus JSONL/SQLite machine indexes.")
    parser.add_argument("--skill-dir", default=None, help="team-memory skill directory")
    parser.add_argument("--output", default=None, help="zip file path or directory")
    parser.add_argument("--skip-index", action="store_true", help="do not rebuild indexes before export")
    args = parser.parse_args()

    try:
        paths = resolve_paths(args.skill_dir, require_lock=True)
    except TeamMemoryPathError as exc:
        print(f"ERROR: {exc}")
        return 1
    print_warnings(paths.warnings)

    if not args.skip_index:
        code = run_rebuild_index(paths.skill_dir)
        if code != 0:
            return code

    output = resolve_output(args.output, paths.skill_dir)
    output.parent.mkdir(parents=True, exist_ok=True)
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_files = sorted(
        path
        for path in paths.data_dir.rglob("*")
        if path.is_file() and ".sync" not in path.relative_to(paths.data_dir).parts
    )

    manifest = {
        "generated-at": generated_at,
        "source-of-truth": "markdown",
        "skill-dir": str(paths.skill_dir),
        "data-dir": str(paths.data_dir),
        "file-count": len(data_files),
        "contains": {
            "markdown": True,
            "jsonl": (paths.data_dir / ".index" / "events.jsonl").exists(),
            "tasks": (paths.data_dir / "tasks" / "tasks.md").exists(),
            "tasks-jsonl": (paths.data_dir / ".index" / "tasks.jsonl").exists(),
            "sqlite": (paths.data_dir / ".index" / "team-memory.sqlite").exists(),
        },
    }

    notebook_summary: dict[str, object] | None = None
    notebook_config = load_notebook_config(paths.skill_dir, required=False)
    if notebook_config:
        state = load_notebook_state(paths.data_dir)
        notebook_summary = {
            "notebook-schema-version": notebook_config.get("notebook-schema-version"),
            "provider": notebook_config.get("provider"),
            "provider-api-version": notebook_config.get("provider-api-version"),
            "mode": notebook_config.get("mode"),
            "repository-id": notebook_config.get("repository-id"),
            "remote-root-page-id": notebook_config.get("remote", {}).get("root-page-id"),
            "schedule": notebook_config.get("schedule", {"enabled": False}),
            "last-sync-at": state.get("last-sync-at"),
            "last-remote-revision": state.get("last-remote-revision", 0),
            "open-conflicts": sum(1 for item in state.get("conflicts", {}).values() if item.get("status") == "open"),
            "pending-deletions": sum(1 for item in state.get("deletions", {}).values() if item.get("status") == "pending"),
            "pending-offline-writes": len(state.get("pending-local", [])),
            "credential-exported": False,
        }
        manifest["contains"]["notebook-sync-summary"] = True

    with tempfile.TemporaryDirectory() as temp_dir_raw:
        temp_dir = Path(temp_dir_raw)
        manifest_path = temp_dir / "manifest.json"
        checksums_path = temp_dir / "checksums.sha256"
        notebook_summary_path = temp_dir / "notebook-sync-summary.json"
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if notebook_summary is not None:
            notebook_summary_path.write_text(json.dumps(notebook_summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        checksum_sources: list[tuple[Path, str]] = [
            (paths.skill_dir / ".team-memory-root.json", ".team-memory-root.json"),
            (manifest_path, "manifest.json"),
        ]
        if paths.config_path.exists():
            checksum_sources.append((paths.config_path, "skill-config.yaml"))
        if notebook_summary is not None:
            checksum_sources.append((notebook_summary_path, "notebook-sync-summary.json"))
        checksum_sources.extend((path, f"data/{rel_path(path, paths.data_dir)}") for path in data_files)
        checksums = [f"{sha256_file(path)}  {archive_path}" for path, archive_path in checksum_sources]
        checksums_path.write_text("\n".join(checksums) + "\n", encoding="utf-8")

        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.write(paths.skill_dir / ".team-memory-root.json", ".team-memory-root.json")
            if paths.config_path.exists():
                archive.write(paths.config_path, "skill-config.yaml")
            archive.write(manifest_path, "manifest.json")
            archive.write(checksums_path, "checksums.sha256")
            if notebook_summary is not None:
                archive.write(notebook_summary_path, "notebook-sync-summary.json")
            for path in data_files:
                archive.write(path, f"data/{rel_path(path, paths.data_dir)}")

    print(f"已导出: {output}")
    print(f"文件数: {len(data_files)}")
    print("包含: Markdown data、tasks.md、events.jsonl、tasks.jsonl、team-memory.sqlite、manifest、checksums")
    if notebook_summary is not None:
        print("在线同步: 已附带脱敏摘要；未导出 token、钥匙串凭据和 data/.sync")
    return 0


if __name__ == "__main__":
    raise SystemExit(run_with_write_lock(main))
