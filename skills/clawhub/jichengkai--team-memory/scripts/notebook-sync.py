#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import getpass
import json
import os
import platform
import plistlib
import re
import runpy
import shutil
import subprocess
import sys
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Callable

from notebook_providers import (
    FLOWUS_API_VERSION,
    NOTION_API_VERSION,
    HttpProvider,
    LeaseGuard,
    ProviderError,
    provider_from_config,
    store_keychain_token,
)
from notebook_sync_core import (
    CONTROL_KIND,
    LEGACY_CONTROL_KIND,
    LEGACY_MANIFEST_KIND,
    MANIFEST_KIND,
    NOTEBOOK_CONFIG,
    NOTEBOOK_SCHEMA_VERSION,
    LocalSyncLock,
    MarkdownPart,
    NotebookSyncError,
    SyncAction,
    atomic_write_json,
    config_path,
    content_hash,
    bytes_hash,
    decode_source_payload,
    decode_json_page,
    decide_action,
    deletion_id,
    discover_sync_files,
    encode_json_page,
    file_id,
    join_markdown,
    load_config,
    load_state,
    merge_append_only,
    new_manifest,
    normalize_markdown,
    read_base,
    save_bases,
    save_state,
    safe_display_markdown,
    source_payload_parts,
    split_markdown,
    sync_dir,
    unsupported_markdown,
    utc_now,
    write_conflict,
)
from team_memory_paths import (TeamMemoryPathError, read_config_data_path, resolve_data_path,
                               resolve_paths, update_config_data_path, write_root_lock)


FOLDER_TITLES = {
    "status": "00 使用说明与同步状态",
    "members": "01 成员",
    "stakeholders": "02 相关方",
    "strategy": "03 向上管理与公司战略",
    "tasks": "04 待办与复盘",
    "insights": "05 洞察与归档",
    "manager": "06 管理者思考",
    "sources": "07 对话与资料原文",
    "conflicts": "90 冲突与待确认删除",
    "system": "99 恢复索引与事务记录",
}


def resolve_team_paths(skill_dir: str | None = None):
    try:
        return resolve_paths(skill_dir, require_lock=True)
    except TeamMemoryPathError as exc:
        raise NotebookSyncError(str(exc)) from exc


def provider_name_version(provider: str) -> str:
    return NOTION_API_VERSION if provider == "notion" else FLOWUS_API_VERSION


def credential_for(provider: str, repository_id: str, token_env: str | None, store_keychain: bool) -> dict[str, str]:
    default_env = "TEAM_MEMORY_NOTION_TOKEN" if provider == "notion" else "TEAM_MEMORY_FLOWUS_TOKEN"
    env_name = token_env or default_env
    if not store_keychain:
        return {"type": "env", "name": env_name}
    token = os.environ.get(env_name)
    if not token and sys.stdin.isatty():
        token = getpass.getpass(f"请输入 {provider} token（将写入 macOS 钥匙串）: ")
    if not token:
        raise NotebookSyncError(f"缺少 {env_name}，无法写入钥匙串。")
    service = f"team-memory-notebook:{repository_id}"
    store_keychain_token(service, provider, token)
    return {"type": "keychain", "service": service, "account": provider}


def root_control_markdown(control: dict[str, Any]) -> str:
    intro = (
        "# Team Memory 在线团队记忆\n\n"
        "这是本地 Team Memory 的可读在线副本。请在文件页面中编辑正文；"
        "不要修改 `99 恢复索引与事务记录` 下的控制页面。\n\n"
    )
    return intro + encode_json_page(control, "连接控制信息")


def empty_lock_markdown() -> str:
    return normalize_markdown(
        "# Team Memory 同步锁\n\n"
        "```json\n"
        + json.dumps({"kind": "team-memory-lease-v1", "owner": None, "lease-id": None, "expires-at": None}, ensure_ascii=False, sort_keys=True)
        + "\n```\n"
    )


def category_for(path: str) -> str:
    if path == "skill-config.yaml" or path == "data/team-memory-overview.md":
        return "status"
    if path.startswith("data/members/"):
        return "members"
    if path.startswith("data/stakeholders/"):
        return "stakeholders"
    if path.startswith("data/upward/") or path.startswith("data/company/"):
        return "strategy"
    if path.startswith("data/tasks/"):
        return "tasks"
    if path.startswith("data/manager/"):
        return "manager"
    if path.startswith("data/sources/"):
        return "sources"
    return "insights"


def remote_folder_segments(path: str) -> list[str]:
    if path == "skill-config.yaml":
        return []
    raw = path.removeprefix("data/")
    parts = Path(raw).parts[:-1]
    if parts and parts[0] in {"members", "stakeholders", "upward", "company", "tasks", "insights", "archive", "manager", "sources"}:
        parts = parts[1:]
    return list(parts)


def read_manifest(provider: HttpProvider, config: dict[str, Any]) -> dict[str, Any]:
    remote = config["remote"]
    page_ids = [str(remote["manifest-page-id"])]
    if remote.get("manifest-shadow-page-id"):
        page_ids.append(str(remote["manifest-shadow-page-id"]))
    candidates: list[tuple[int, int, str, dict[str, Any]]] = []
    failures: list[str] = []
    for page_id in dict.fromkeys(page_ids):
        try:
            page = provider.read_page(page_id)
            if page.truncated or page.unknown_block_ids:
                raise NotebookSyncError("manifest 页面不完整")
            try:
                manifest = decode_json_page(page.markdown, MANIFEST_KIND)
            except NotebookSyncError:
                manifest = decode_json_page(page.markdown, LEGACY_MANIFEST_KIND)
            if manifest.get("repository-id") != config.get("repository-id"):
                raise NotebookSyncError("仓库 ID 与本地连接配置不一致")
            candidates.append(
                (
                    int(manifest.get("manifest-write-sequence", 0)),
                    int(manifest.get("revision", 0)),
                    page_id,
                    manifest,
                )
            )
        except (NotebookSyncError, ProviderError, KeyError, TypeError, ValueError) as exc:
            failures.append(f"{page_id}: {exc}")
    if not candidates:
        detail = "; ".join(failures) or "没有可读页面"
        raise NotebookSyncError(f"远端 manifest 无可用完整副本，已停止同步：{detail}")
    # An interrupted migration may leave one v1 slot. No v2 content writes are
    # permitted until both slots have been replaced and verified. If an old
    # client subsequently committed to v1, migrate that newer legacy head.
    legacy = [item for item in candidates if item[3].get("kind") == LEGACY_MANIFEST_KIND]
    if legacy:
        if any(item[3].get("kind") == MANIFEST_KIND and not item[3].get("migration-pending") for item in candidates):
            raise NotebookSyncError("新旧 manifest 混用且缺少迁移屏障，已停止以保护数据。")
        candidates = legacy
    newest_key = max((item[0], item[1]) for item in candidates)
    newest = [item for item in candidates if (item[0], item[1]) == newest_key]
    payloads = {json.dumps(item[3], ensure_ascii=False, sort_keys=True) for item in newest}
    if len(payloads) > 1:
        raise NotebookSyncError("manifest 主槽与备用槽的最新写序号相同但内容不同，拒绝猜测覆盖。")
    _, _, active_id, manifest = newest[0]
    config["_active-manifest-page-id"] = active_id
    return manifest


def write_manifest(provider: HttpProvider, config: dict[str, Any], manifest: dict[str, Any]) -> None:
    if manifest.get("kind") != MANIFEST_KIND or manifest.get("migration-pending"):
        raise NotebookSyncError("manifest 协议尚未安全升级，拒绝正文写入。")
    manifest["updated-at"] = utc_now()
    manifest["manifest-write-sequence"] = int(manifest.get("manifest-write-sequence", 0)) + 1
    remote = config["remote"]
    primary = str(remote["manifest-page-id"])
    shadow = str(remote["manifest-shadow-page-id"]) if remote.get("manifest-shadow-page-id") else None
    active = str(config.get("_active-manifest-page-id") or primary)
    target = shadow if shadow and active == primary else primary
    written = provider.replace_page(target, encode_json_page(manifest, "Team Memory 恢复清单"))
    if written.truncated or written.unknown_block_ids or decode_json_page(written.markdown, MANIFEST_KIND) != manifest:
        raise NotebookSyncError("manifest 写后校验失败，事务未确认为成功。")
    config["_active-manifest-page-id"] = target


def ensure_protocol_v2(provider: HttpProvider, config: dict[str, Any], manifest: dict[str, Any], skill_dir: Path) -> dict[str, Any]:
    """Fence old clients out of *both* slots before any v2 content mutation."""
    ensure_manifest_shadow(provider, config, manifest, skill_dir)
    remote = config["remote"]
    ids = [str(remote["manifest-page-id"]), str(remote["manifest-shadow-page-id"])]
    needs_upgrade = manifest.get("kind") != MANIFEST_KIND or manifest.get("migration-pending")
    if needs_upgrade:
        upgraded = copy.deepcopy(manifest)
        upgraded.update({"kind": MANIFEST_KIND, "notebook-schema-version": NOTEBOOK_SCHEMA_VERSION,
                         "migration-pending": True, "upgraded-at": utc_now()})
        for entry in upgraded.get("files", {}).values():
            if not entry.get("source"):
                entry["source-fidelity"] = "legacy-rendered"
            if not entry.get("previous-source"):
                entry["previous-source-fidelity"] = "legacy-rendered"
        upgraded["manifest-write-sequence"] = int(upgraded.get("manifest-write-sequence", 0)) + 1
        # Write inactive first. A crash during this barrier leaves only legacy
        # data in service; new clients repeat the barrier from the legacy head.
        active = str(config.get("_active-manifest-page-id") or ids[0])
        ordered = sorted(ids, key=lambda page_id: page_id == active)
        markdown = encode_json_page(upgraded, "Team Memory 恢复清单 · 协议升级")
        for page_id in ordered:
            provider.replace_page(page_id, markdown)
        for page_id in ids:
            page = provider.read_page(page_id)
            if page.truncated or page.unknown_block_ids or decode_json_page(page.markdown, MANIFEST_KIND) != upgraded:
                raise NotebookSyncError("manifest 双槽升级回读校验失败，未开始正文备份。")
        upgraded.pop("migration-pending", None)
        upgraded["manifest-write-sequence"] += 1
        manifest = upgraded
        # Clear the barrier in both slots; an interrupted clear is still v2-only.
        markdown = encode_json_page(manifest, "Team Memory 恢复清单")
        for page_id in ids:
            provider.replace_page(page_id, markdown)
        print("已升级为原文备份协议 v2；旧版仅有渲染副本的文件将在下一次推送时补齐。")
    for key in ("manager", "sources"):
        if not remote.setdefault("folders", {}).get(key):
            title = FOLDER_TITLES[key]
            existing = provider.list_child_pages(str(remote["root-page-id"])).get(title)
            remote["folders"][key] = existing or provider.create_page(str(remote["root-page-id"]), title, f"# {title}\n")
    if not remote.get("source-folder-id"):
        system_id = str(remote["folders"]["system"])
        title = "原文恢复载荷（请勿修改）"
        existing = provider.list_child_pages(system_id).get(title)
        remote["source-folder-id"] = existing or provider.create_page(system_id, title, "# 原文恢复载荷\n")
    config["notebook-schema-version"] = NOTEBOOK_SCHEMA_VERSION
    config["remote"]["notebook-schema-version"] = NOTEBOOK_SCHEMA_VERSION
    persisted = {key: value for key, value in config.items() if not key.startswith("_")}
    atomic_write_json(config_path(skill_dir), persisted)
    return manifest


def discover_manifest_shadow(
    provider: HttpProvider,
    config: dict[str, Any],
    skill_dir: Path | None = None,
) -> str | None:
    remote = config["remote"]
    if remote.get("manifest-shadow-page-id"):
        return str(remote["manifest-shadow-page-id"])
    folders = remote.get("folders") or {}
    if not folders.get("system"):
        return None
    title = "恢复清单 manifest.shadow.json"
    shadow_id = provider.list_child_pages(str(folders["system"])).get(title)
    if not shadow_id:
        return None
    remote["manifest-shadow-page-id"] = str(shadow_id)
    if skill_dir is not None:
        persisted = {key: value for key, value in config.items() if not key.startswith("_")}
        atomic_write_json(config_path(skill_dir), persisted)
    return str(shadow_id)


def ensure_manifest_shadow(
    provider: HttpProvider,
    config: dict[str, Any],
    manifest: dict[str, Any],
    skill_dir: Path | None = None,
) -> None:
    remote = config["remote"]
    if discover_manifest_shadow(provider, config, skill_dir):
        return
    title = "恢复清单 manifest.shadow.json"
    system_id = str(remote["folders"]["system"])
    shadow_id = provider.list_child_pages(system_id).get(title)
    if not shadow_id:
        shadow_id = provider.create_page(system_id, title, encode_json_page(manifest, "Team Memory 恢复清单备用槽"))
    remote["manifest-shadow-page-id"] = str(shadow_id)
    if skill_dir is not None:
        persisted = {key: value for key, value in config.items() if not key.startswith("_")}
        atomic_write_json(config_path(skill_dir), persisted)


def ensure_remote_folder(
    provider: HttpProvider,
    manifest: dict[str, Any],
    config: dict[str, Any],
    path: str,
    on_created: Callable[[str], None] | None = None,
) -> str:
    category = category_for(path)
    parent = str(config["remote"]["folders"][category])
    prefix = category
    folders = manifest.setdefault("folders", {})
    for segment in remote_folder_segments(path):
        prefix = f"{prefix}/{segment}"
        existing = folders.get(prefix)
        if existing:
            parent = str(existing)
            continue
        page_id = provider.create_page(
            parent,
            segment,
            f"# {segment}\n\nTeam Memory 同步目录。\n",
            on_created=on_created,
        )
        folders[prefix] = page_id
        parent = page_id
    return parent


def read_remote_entry(
    provider: HttpProvider,
    entry: dict[str, Any],
    version: str = "current",
    refresh_metadata: bool = False,
    verify_hashes: bool = False,
) -> str:
    parts: list[MarkdownPart] = []
    independent_previous = version == "previous" and bool(entry.get("previous-parts"))
    raw_parts = list(entry.get("previous-parts", [])) if independent_previous else list(entry.get("parts", []))
    names = [str(item.get("name", "main")) for item in raw_parts]
    if len(names) != len(set(names)):
        raise NotebookSyncError("在线条目存在重复分片名，拒绝重组。")
    has_order = ["order" in item for item in raw_parts]
    if any(has_order) and not all(has_order):
        raise NotebookSyncError("在线条目只有部分分片包含顺序号，拒绝重组。")
    if raw_parts and all(has_order):
        try:
            raw_parts.sort(key=lambda item: int(item["order"]))
            orders = [int(item["order"]) for item in raw_parts]
        except (TypeError, ValueError) as exc:
            raise NotebookSyncError("在线条目分片顺序号不是有效整数，拒绝重组。") from exc
        if orders != list(range(len(raw_parts))):
            raise NotebookSyncError("在线条目分片顺序不连续，拒绝重组。")
    for item in raw_parts:
        page_key = "page-id" if version == "current" or independent_previous else "previous-page-id"
        page_id = item.get(page_key)
        if not page_id:
            raise NotebookSyncError(f"在线条目缺少 {page_key}，无法恢复 {version} 版本。")
        page = provider.read_page(str(page_id))
        if page.truncated or page.unknown_block_ids:
            raise NotebookSyncError(f"在线页面 {item['page-id']} 内容被截断或含未知块，拒绝使用不完整内容。")
        content = page.markdown
        strip_key = "strip-final-newline" if version == "current" or independent_previous else "previous-strip-final-newline"
        if item.get(strip_key) and content.endswith("\n"):
            content = content[:-1]
        expected_hash = item.get("remote-hash") if version == "current" or independent_previous else None
        if verify_hashes and expected_hash and content_hash(content) != expected_hash:
            raise NotebookSyncError("旧版渲染备份分片摘要不一致，拒绝恢复。")
        if refresh_metadata and version == "current":
            item["remote-hash"] = content_hash(content)
        parts.append(MarkdownPart(str(item.get("name", "main")), content))
    combined = join_markdown(parts)
    if verify_hashes and version == "current" and entry.get("remote-hash") and content_hash(combined) != entry["remote-hash"]:
        raise NotebookSyncError("旧版渲染备份文件摘要不一致，拒绝恢复。")
    if refresh_metadata and version == "current":
        entry["remote-hash"] = content_hash(combined)
        entry["updated-at"] = utc_now()
    return combined


def read_source_entry(provider: HttpProvider, entry: dict[str, Any], version: str = "current") -> bytes:
    key = "source" if version == "current" else "previous-source"
    descriptor = entry.get(key)
    if not descriptor:
        fidelity_key = "source-fidelity" if version == "current" else "previous-source-fidelity"
        if entry.get(fidelity_key) != "legacy-rendered":
            raise NotebookSyncError(f"{entry.get('path', '文件')} 缺少 {version} 原文恢复载荷。")
        return read_remote_entry(provider, entry, version, verify_hashes=True).encode("utf-8")
    if not isinstance(descriptor, dict):
        raise NotebookSyncError("原文恢复载荷描述无效。")
    pages: list[str] = []
    for part in descriptor.get("parts", []):
        if not isinstance(part, dict) or not part.get("page-id"):
            raise NotebookSyncError("原文恢复载荷页面 ID 缺失。")
        page = provider.read_page(str(part["page-id"]))
        if page.truncated or page.unknown_block_ids:
            raise NotebookSyncError("原文恢复载荷页面被截断或包含未知块。")
        pages.append(page.markdown)
    return decode_source_payload(str(entry["path"]), descriptor, pages)


def write_source_descriptor(
    provider: HttpProvider, config: dict[str, Any], path: str, raw: bytes,
    on_created: Callable[[str], None] | None = None,
) -> dict[str, Any]:
    parent = str(config["remote"].get("source-folder-id") or config["remote"].get("folders", {}).get("system")
                 or config["remote"]["previous-folder-id"])
    parts = []
    pages = []
    for idx, part in enumerate(source_payload_parts(path, raw)):
        page_id = provider.create_page(parent, f"原文 · {path} · {part.name}", part.content, on_created=on_created)
        page = provider.read_page(page_id)
        if page.truncated or page.unknown_block_ids:
            raise NotebookSyncError("写入后的原文恢复载荷不完整，事务未提交。")
        parts.append({"name": part.name, "page-id": str(page_id), "order": idx})
        pages.append(page.markdown)
    descriptor = {"encoding": "base64-v1", "byte-length": len(raw), "sha256": bytes_hash(raw), "parts": parts}
    if decode_source_payload(path, descriptor, pages) != raw:
        raise NotebookSyncError("原文恢复载荷写后校验失败。")
    return descriptor


def source_page_ids(entry: dict[str, Any], include_current: bool = True) -> list[str]:
    keys = ("source", "previous-source") if include_current else ("previous-source",)
    return [str(part["page-id"]) for key in keys for part in (entry.get(key) or {}).get("parts", [])]


def conflict_metadata(item: dict[str, Any]) -> dict[str, Any]:
    allowed = {"id", "path", "created-at", "status", "reason", "remote-conflict-page-id", "resolved-at", "resolution"}
    return {key: value for key, value in item.items() if key in allowed}


def refresh_source_entry(
    provider: HttpProvider, config: dict[str, Any], path: str, raw: bytes, entry: dict[str, Any],
    on_created: Callable[[str], None] | None = None,
) -> list[dict[str, str]]:
    old_source = copy.deepcopy(entry.get("source"))
    if old_source:
        read_source_entry(provider, entry)
    cleanup = [{"page-id": page_id, "expected-hash": ""} for page_id in source_page_ids(entry, False)]
    entry["source"] = write_source_descriptor(provider, config, path, raw, on_created)
    entry["previous-source"] = old_source
    entry["previous-source-fidelity"] = entry.get("source-fidelity", "legacy-rendered")
    entry["source-fidelity"] = "exact-bytes"
    return cleanup


def write_remote_entry(
    provider: HttpProvider,
    config: dict[str, Any],
    manifest: dict[str, Any],
    path: str,
    content: str,
    existing: dict[str, Any] | None,
    on_created: Callable[[str], None] | None = None,
    expected_remote_content: str | None = None,
    source_bytes: bytes | None = None,
) -> tuple[dict[str, Any], str, list[dict[str, str]]]:
    parent = ensure_remote_folder(provider, manifest, config, path, on_created)
    previous_parent = str(config["remote"]["previous-folder-id"])
    old_content: str | None = None
    old_snapshots: list[tuple[dict[str, Any], str]] = []
    if existing:
        if existing.get("source"):
            read_source_entry(provider, existing)
        old_content = read_remote_entry(provider, existing)
        if expected_remote_content is not None and content_hash(old_content) != content_hash(expected_remote_content):
            raise NotebookSyncError("在写时复制前在线内容已变化，拒绝覆盖。")
        for item in existing.get("parts", []):
            page = provider.read_page(str(item["page-id"]))
            if page.truncated or page.unknown_block_ids:
                raise NotebookSyncError("旧版在线页面不完整，拒绝创建上一版。")
            old_snapshots.append((item, page.markdown))

    previous_parts: list[dict[str, Any]] = []
    if old_snapshots:
        for idx, (item, markdown) in enumerate(old_snapshots):
            name = str(item.get("name", "main"))
            previous_id = provider.create_page(
                previous_parent,
                f"上一版 · {path} · {name}",
                markdown,
                on_created=on_created,
            )
            previous_parts.append(
                {
                    "name": name,
                    "page-id": str(previous_id),
                    "remote-hash": content_hash(markdown),
                    "order": idx,
                    "strip-final-newline": bool(item.get("strip-final-newline")),
                }
            )
    else:
        previous_id = provider.create_page(
            previous_parent,
            f"上一版 · {path} · main",
            "# 尚无上一版\n",
            on_created=on_created,
        )
        previous_parts.append(
            {
                "name": "main",
                "page-id": str(previous_id),
                "remote-hash": content_hash("# 尚无上一版\n"),
                "order": 0,
                "strip-final-newline": False,
            }
        )

    new_parts: list[dict[str, Any]] = []
    rendered_parts: list[MarkdownPart] = []
    logical_parts = split_markdown(path, safe_display_markdown(content))
    title_base = Path(path).name
    for idx, part in enumerate(logical_parts):
        title = title_base if len(logical_parts) == 1 else f"{title_base} · {part.name}"
        strip_final_newline = not part.content.endswith("\n")
        page_id = provider.create_page(parent, title, part.content, on_created=on_created)
        result = provider.read_page(page_id)
        if result.truncated or result.unknown_block_ids:
            raise NotebookSyncError(f"写入后的在线页面 {page_id} 不完整，事务未提交。")
        rendered_content = result.markdown[:-1] if strip_final_newline and result.markdown.endswith("\n") else result.markdown
        rendered_parts.append(MarkdownPart(part.name, rendered_content))
        new_parts.append(
            {
                "name": part.name,
                "page-id": str(page_id),
                "remote-hash": content_hash(rendered_content),
                "order": idx,
                "strip-final-newline": strip_final_newline,
            }
        )

    if existing and old_content is not None:
        latest_old = read_remote_entry(provider, existing)
        if content_hash(latest_old) != content_hash(old_content):
            raise NotebookSyncError("在线内容在写时复制期间被修改，新页将回滚且不覆盖任一端。")

    cleanup: list[dict[str, str]] = []
    if existing:
        snapshot_hashes = {str(item["page-id"]): content_hash(markdown) for item, markdown in old_snapshots}
        for item in existing.get("parts", []):
            page_id = str(item["page-id"])
            cleanup.append({"page-id": page_id, "expected-hash": snapshot_hashes[page_id]})
        if existing.get("previous-parts"):
            for item in existing.get("previous-parts", []):
                cleanup.append({"page-id": str(item["page-id"]), "expected-hash": str(item.get("remote-hash") or "")})
        else:
            for item in existing.get("parts", []):
                if item.get("previous-page-id"):
                    cleanup.append({"page-id": str(item["previous-page-id"]), "expected-hash": ""})
        cleanup.extend({"page-id": page_id, "expected-hash": ""} for page_id in source_page_ids(existing, False))
    raw = source_bytes if source_bytes is not None else content.encode("utf-8")
    descriptor = write_source_descriptor(provider, config, path, raw, on_created)
    if existing and old_content is not None and content_hash(read_remote_entry(provider, existing)) != content_hash(old_content):
        raise NotebookSyncError("在线内容在原文备份期间变化，未提交新页面。")
    remote_content = join_markdown(rendered_parts)
    return {
        "file-id": file_id(path),
        "path": path,
        "parts": new_parts,
        "previous-parts": previous_parts,
        "source": descriptor,
        "previous-source": copy.deepcopy(existing.get("source")) if existing else None,
        "source-fidelity": "exact-bytes",
        "previous-source-fidelity": existing.get("source-fidelity", "legacy-rendered") if existing else "none",
        "remote-hash": content_hash(remote_content),
        "updated-at": utc_now(),
        "tombstone": False,
    }, remote_content, cleanup


def local_path_for(path: str, skill_dir: Path, data_dir: Path) -> Path:
    if path == "skill-config.yaml":
        return skill_dir / path
    if not path.startswith("data/"):
        raise NotebookSyncError(f"非法同步路径: {path}")
    target = (data_dir / path.removeprefix("data/")).resolve()
    try:
        target.relative_to(data_dir.resolve())
    except ValueError as exc:
        raise NotebookSyncError(f"同步路径越界: {path}") from exc
    return target


def deletion_storage_relative(path: str) -> Path:
    if path == "skill-config.yaml":
        return Path("_root") / "skill-config.yaml"
    if not path.startswith("data/"):
        raise NotebookSyncError(f"非法删除路径: {path}")
    relative = Path(path.removeprefix("data/"))
    if relative.is_absolute() or ".." in relative.parts:
        raise NotebookSyncError(f"删除路径越界: {path}")
    return relative


def pending_deletion_path(data_dir: Path, identifier: str, path: str) -> Path:
    if not re.fullmatch(r"(?:DELETE|RECOVERED)-[A-Za-z0-9-]+", identifier):
        raise NotebookSyncError("删除记录 ID 无效，拒绝生成恢复路径。")
    return data_dir / "archive" / "pending-deletions" / identifier / deletion_storage_relative(path)


def confirmed_deletion_path(data_dir: Path, identifier: str, path: str) -> Path:
    if not re.fullmatch(r"(?:DELETE|RECOVERED)-[A-Za-z0-9-]+", identifier):
        raise NotebookSyncError("删除记录 ID 无效，拒绝生成备份路径。")
    return data_dir / ".backup" / "deletions-confirmed" / identifier / deletion_storage_relative(path)


def backup_local_file(path: Path, data_dir: Path, label: str) -> None:
    if not path.exists():
        return
    try:
        relative = path.resolve().relative_to(data_dir.resolve())
    except ValueError:
        relative = Path("skill-config.yaml")
    destination = data_dir / ".backup" / label / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, destination)


def write_local(path: Path, content: str, data_dir: Path, backup_label: str) -> None:
    backup_local_file(path, data_dir, backup_label)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(normalize_markdown(content), encoding="utf-8")


def write_local_bytes(path: Path, raw: bytes, data_dir: Path, backup_label: str) -> None:
    backup_local_file(path, data_dir, backup_label)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    try:
        temporary.write_bytes(raw)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def display_changed(entry: dict[str, Any], display: str) -> bool:
    expected = entry.get("remote-hash")
    if entry.get("source") and not isinstance(expected, str):
        raise NotebookSyncError("原文载荷缺少关联的展示页摘要，无法判断在线编辑。")
    return bool(expected and content_hash(display) != expected)


def managed_conversation_source(path: str) -> bool:
    return path.startswith("data/sources/conversations/")


def prepare_pull(provider: HttpProvider, action: SyncAction, entry: dict[str, Any]) -> tuple[bytes, str, bool]:
    """Separate another client's committed bytes from uncommitted page edits."""
    latest = read_remote_entry(provider, entry)
    if action.remote_content is None or content_hash(latest) != content_hash(action.remote_content):
        raise NotebookSyncError("在线内容在同步计划后变化，未写入本地；请重新同步。")
    edited = display_changed(entry, latest)
    if edited and managed_conversation_source(action.path):
        raise NotebookSyncError("谈话原文或拆解映射被在线编辑，请通过修订来源处理，不能覆盖原文校验信息。")
    if edited:
        raw = latest.encode("utf-8")
        refresh_source = True
    else:
        raw = read_source_entry(provider, entry)
        refresh_source = not bool(entry.get("source"))
    try:
        raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise NotebookSyncError("同步原文不是有效 UTF-8，未写入本地。") from exc
    return raw, latest, refresh_source


def summarize_actions(actions: list[SyncAction]) -> None:
    counts: dict[str, int] = {}
    for action in actions:
        counts[action.action] = counts.get(action.action, 0) + 1
        print(f"- {action.path}: {action.action} ({action.reason})")
    print("汇总: " + ", ".join(f"{key}={value}" for key, value in sorted(counts.items())))


def build_actions(
    provider: HttpProvider,
    config: dict[str, Any],
    manifest: dict[str, Any],
    state: dict[str, Any],
    skill_dir: Path,
    data_dir: Path,
) -> tuple[list[SyncAction], dict[str, str], dict[str, str]]:
    local_files = discover_sync_files(skill_dir, data_dir)
    local_bytes = {path: file.read_bytes() for path, file in local_files.items()}
    try:
        local_content = {path: raw.decode("utf-8") for path, raw in local_bytes.items()}
    except UnicodeDecodeError as exc:
        raise NotebookSyncError("记忆正文必须是 UTF-8；已停止上传以保留原始文件。") from exc
    remote_content: dict[str, str] = {}
    for path, entry in manifest.get("files", {}).items():
        if entry.get("tombstone"):
            continue
        try:
            remote_content[path] = read_remote_entry(provider, entry)
        except ProviderError as exc:
            if exc.status == 404:
                remote_content[path] = None  # type: ignore[assignment]
            else:
                raise

    paths = sorted(set(local_content) | set(manifest.get("files", {})) | set(state.get("files", {})))
    actions: list[SyncAction] = []
    for path in paths:
        open_conflicts = [item for item in state.get("conflicts", {}).values() if item.get("path") == path and item.get("status") == "open"]
        if open_conflicts:
            actions.append(SyncAction(path, "noop", "已有开放冲突，等待处理"))
            continue
        manifest_entry = manifest.get("files", {}).get(path, {})
        confirmed = next(
            (
                item
                for item in manifest.get("deletions", {}).values()
                if item.get("path") == path and item.get("status") == "confirmed"
            ),
            None,
        )
        if confirmed:
            state.setdefault("deletions", {})[str(confirmed["id"])] = copy.deepcopy(confirmed)
            action = "confirmed-delete" if path in local_content or path in state.get("files", {}) else "noop"
            actions.append(SyncAction(path, action, "远端已确认删除，禁止旧副本重新上传"))
            continue
        if manifest_entry.get("tombstone"):
            pending = next(
                (
                    item
                    for item in manifest.get("deletions", {}).values()
                    if item.get("path") == path and item.get("status") == "pending"
                ),
                None,
            )
            if pending:
                state.setdefault("deletions", {})[str(pending["id"])] = copy.deepcopy(pending)
            actions.append(SyncAction(path, "noop", "远端待确认删除墓碑已阻止重新上传"))
            continue
        file_state = state.get("files", {}).get(path)
        effective_state = dict(file_state) if file_state else None
        if effective_state:
            effective_state["base-local"] = read_base(data_dir, effective_state, "local")
        action = decide_action(path, local_content.get(path), remote_content.get(path), effective_state, str(config["mode"]))
        remote_display = remote_content.get(path)
        source_hash = (manifest_entry.get("source") or {}).get("sha256")
        edited = remote_display is not None and display_changed(manifest_entry, remote_display)
        if edited and managed_conversation_source(path) and action.action != "tombstone":
            action.action = "conflict" if config["mode"] == "bidirectional" else "remote-drift"
            action.reason = "谈话来源被在线编辑，须通过原文修订流程处理"
        if path in local_bytes:
            action.source_bytes = local_bytes[path]
            current_byte_hash = bytes_hash(local_bytes[path])
            baseline_byte_hash = (file_state or {}).get("local-byte-hash")
            bytes_changed = baseline_byte_hash is not None and current_byte_hash != baseline_byte_hash
            source_baseline = (file_state or {}).get("source-byte-hash", baseline_byte_hash)
            if source_hash and remote_display is not None and not edited and action.action != "tombstone":
                if current_byte_hash == source_hash:
                    # A readable page can differ from identical canonical bytes.
                    settled = (file_state is not None and not bytes_changed
                               and file_state.get("remote-hash") == content_hash(remote_display)
                               and file_state.get("source-byte-hash") == source_hash)
                    action.action = "noop" if settled else "baseline"
                    action.reason = "本地与在线原文一致，保持原文基线"
                elif baseline_byte_hash is not None and source_baseline is not None:
                    source_changed = source_hash != source_baseline
                    if source_changed and not bytes_changed:
                        action.action = "pull" if config["mode"] == "bidirectional" else "remote-drift"
                        action.reason = "其他实例已提交新原文（包含仅换行或空白变化）"
                    elif source_changed and bytes_changed:
                        canonical = read_source_entry(provider, manifest_entry).decode("utf-8")
                        base = (effective_state or {}).get("base-local")
                        merged = (merge_append_only(str(base), local_content[path], canonical)
                                  if base is not None and not managed_conversation_source(path) else None)
                        action.action = "merge" if merged is not None else "conflict"
                        action.merged_content = merged
                        action.reason = "双方新增独立记录" if merged is not None else "双方原文均变化，拒绝覆盖"
                    else:
                        action.action = "push"
                        action.reason = "本地原文变化，或保留显式恢复的本地版本"
                elif action.action in {"baseline", "noop"}:
                    action.action = "conflict"
                    action.reason = "本地与在线原文不同，缺少字节基线，拒绝覆盖任一副本"
            elif bytes_changed and action.action in {"pull", "remote-drift"}:
                action.action = "conflict"
                action.reason = "本地原始字节与在线内容均变化，拒绝覆盖格式或原文"
            elif action.action in {"noop", "baseline"} and current_byte_hash != source_hash:
                action.action = "push"
                action.reason = "补齐或更新保真原文载荷"
        direction = str(config.get("_direction", "sync"))
        if direction == "push" and action.action in {"pull", "pull-create"}:
            action.action = "remote-drift"
            action.reason = "push 模式不拉取在线修改"
        elif direction == "pull" and action.action in {"push", "push-create"}:
            action.action = "local-drift"
            action.reason = "pull 模式不推送本地修改"
        elif direction in {"push", "pull"} and action.action == "merge":
            action.action = "conflict"
            action.reason = f"{direction} 单向命令不自动合并双方修改；请使用 sync"
        actions.append(action)
    return actions, local_content, remote_content


def update_file_state(
    state: dict[str, Any],
    data_dir: Path,
    path: str,
    local_content: str,
    remote_content: str,
    entry: dict[str, Any],
    source_bytes: bytes | None = None,
) -> None:
    bases = save_bases(data_dir, path, local_content, remote_content)
    state.setdefault("files", {})[path] = {
        "file-id": file_id(path),
        "local-hash": content_hash(local_content),
        "local-byte-hash": bytes_hash(source_bytes if source_bytes is not None else local_content.encode("utf-8")),
        "source-byte-hash": (entry.get("source") or {}).get("sha256"),
        "remote-hash": content_hash(remote_content),
        "remote-parts": entry.get("parts", []),
        "synced-at": utc_now(),
        **bases,
    }


def remote_conflict_page(
    provider: HttpProvider,
    config: dict[str, Any],
    identifier: str,
    action: SyncAction,
    on_created: Callable[[str], None] | None = None,
) -> str:
    body = normalize_markdown(
        f"# {identifier}\n\n"
        f"- 路径：`{action.path}`\n"
        f"- 原因：{action.reason}\n\n"
        "## 本地版本\n\n"
        f"```markdown\n{(action.local_content or '').rstrip()}\n```\n\n"
        "## 在线版本\n\n"
        f"```markdown\n{(action.remote_content or '').rstrip()}\n```\n"
    )
    page_id = provider.create_page(
        str(config["remote"]["folders"]["conflicts"]),
        identifier,
        body,
        on_created=on_created,
    )
    return page_id


def cleanup_page_id(item: Any) -> str:
    return str(item.get("page-id")) if isinstance(item, dict) else str(item)


def merge_cleanup_items(*groups: list[Any]) -> list[Any]:
    merged: dict[str, Any] = {}
    for group in groups:
        for item in group:
            merged[cleanup_page_id(item)] = item
    return list(merged.values())


def process_cleanup_pending(provider: HttpProvider, config: dict[str, Any], manifest: dict[str, Any]) -> None:
    pending = list(manifest.get("cleanup-pending", []))
    if not pending:
        return
    remaining: list[Any] = []
    for item in pending:
        page_id = cleanup_page_id(item)
        try:
            expected = str(item.get("expected-hash") or "") if isinstance(item, dict) else ""
            if expected:
                current = provider.read_page(page_id)
                if content_hash(current.markdown) != expected:
                    remaining.append(item)
                    print(f"WARNING: 旧页 {page_id} 在提交后被编辑，已保留并停止自动归档。", file=sys.stderr)
                    continue
            provider.archive_page(page_id)
        except ProviderError as exc:
            if exc.status != 404:
                remaining.append(item)
    manifest["cleanup-pending"] = remaining
    write_manifest(provider, config, manifest)
    if remaining:
        print(f"WARNING: 仍有 {len(remaining)} 个远端旧分片待清理。", file=sys.stderr)


def apply_actions(
    provider: HttpProvider,
    config: dict[str, Any],
    manifest: dict[str, Any],
    state: dict[str, Any],
    actions: list[SyncAction],
    skill_dir: Path,
    data_dir: Path,
    lease_guard: LeaseGuard,
) -> None:
    stamp = datetime.now().strftime("notebook-sync-%Y%m%d-%H%M%S-%f")
    # Validate all incoming source payloads before changing local business files.
    prepared_pulls: dict[str, tuple[bytes, str, bool]] = {}
    for action in actions:
        if action.action in {"pull", "pull-create"}:
            entry = manifest.get("files", {}).get(action.path)
            if not entry:
                raise NotebookSyncError("待拉取文件缺少已提交的在线条目。")
            prepared_pulls[action.path] = prepare_pull(provider, action, entry)
    transaction_id = str(uuid.uuid4())
    mutating_paths = {
        action.path
        for action in actions
        if action.action in {"push", "push-create", "merge", "pull", "pull-create", "conflict", "tombstone", "baseline"}
    }
    before_files = {path: copy.deepcopy(manifest.get("files", {}).get(path)) for path in mutating_paths}
    base_revision = int(manifest.get("revision", 0))
    manifest["transaction"] = {
        "id": transaction_id,
        "status": "prepared",
        "started-at": utc_now(),
        "machine-id": state["machine-id"],
        "base-revision": base_revision,
        "write-model": "copy-on-write-v1",
        "before-files": before_files,
        "before-conflicts": copy.deepcopy(manifest.get("conflicts", {})),
        "before-folders": copy.deepcopy(manifest.get("folders", {})),
        "created-page-ids": [],
        "post-commit-archive-page-ids": [],
    }
    write_manifest(provider, config, manifest)

    for identifier, item in state.get("conflicts", {}).items():
        if item.get("status") == "resolved" and identifier in manifest.get("conflicts", {}):
            manifest["conflicts"][identifier]["meta"] = conflict_metadata(item)

    def record_created(page_id: str) -> None:
        transaction = manifest.get("transaction")
        if not transaction or transaction.get("id") != transaction_id:
            raise NotebookSyncError("远端事务记录已丢失，拒绝继续创建页面。")
        transaction.setdefault("created-page-ids", []).append(page_id)
        write_manifest(provider, config, manifest)

    for action in actions:
        lease_guard.checkpoint()
        path = action.path
        entry = manifest.setdefault("files", {}).get(path)
        if action.action in {"noop", "remote-drift", "local-drift"}:
            continue
        if action.action == "baseline":
            assert action.local_content is not None and action.remote_content is not None and entry is not None
            latest_remote = read_remote_entry(provider, entry)
            if content_hash(latest_remote) != content_hash(action.remote_content):
                action.remote_content = latest_remote
                action.action = "conflict"
                action.reason = "在重建共同基线前在线内容再次变化"
            elif display_changed(entry, latest_remote) and managed_conversation_source(path):
                action.action = "conflict"
                action.reason = "谈话来源被在线编辑，保留原始载荷并等待处理"
            if action.action == "baseline":
                raw = action.source_bytes if action.source_bytes is not None else action.local_content.encode("utf-8")
                if (entry.get("source") and not display_changed(entry, latest_remote)
                        and entry["source"].get("sha256") == bytes_hash(raw)):
                    read_source_entry(provider, entry)
                else:
                    if content_hash(action.local_content) != content_hash(latest_remote):
                        raise NotebookSyncError("无法证明共同基线与原文一致，已停止。")
                    cleanup = refresh_source_entry(provider, config, path, raw, entry, record_created)
                    manifest["transaction"].setdefault("post-commit-archive-page-ids", []).extend(cleanup)
                    read_remote_entry(provider, entry, refresh_metadata=True)
                update_file_state(state, data_dir, path, action.local_content, latest_remote, entry, raw)
                write_manifest(provider, config, manifest)
                continue
        if action.action in {"push", "push-create", "merge"}:
            if entry is not None and action.remote_content is not None:
                latest_remote = read_remote_entry(provider, entry)
                if content_hash(latest_remote) != content_hash(action.remote_content):
                    action.action = "conflict"
                    action.reason = "在线内容在三方比较后再次变化，拒绝覆盖"
                    action.remote_content = latest_remote
            if action.action != "conflict":
                content = action.merged_content if action.action == "merge" else action.local_content
                assert content is not None
                if action.action == "merge":
                    write_local(local_path_for(path, skill_dir, data_dir), content, data_dir, stamp)
                new_entry, rendered, cleanup_ids = write_remote_entry(
                    provider,
                    config,
                    manifest,
                    path,
                    content,
                    entry,
                    record_created,
                    action.remote_content,
                    content.encode("utf-8") if action.action == "merge" else action.source_bytes,
                )
                manifest["files"][path] = new_entry
                manifest["transaction"].setdefault("post-commit-archive-page-ids", []).extend(cleanup_ids)
                write_manifest(provider, config, manifest)
                update_file_state(state, data_dir, path, content, rendered, new_entry,
                                  content.encode("utf-8") if action.action == "merge" else action.source_bytes)
                continue
        if action.action in {"pull", "pull-create"}:
            assert action.remote_content is not None and entry is not None
            raw, latest_remote, refresh_source = prepared_pulls[path]
            if content_hash(read_remote_entry(provider, entry)) != content_hash(latest_remote):
                raise NotebookSyncError("在线内容在原文校验后变化，未写入该本地文件；请重新同步。")
            target = local_path_for(path, skill_dir, data_dir)
            if refresh_source:
                cleanup = refresh_source_entry(provider, config, path, raw, entry, record_created)
                manifest["transaction"].setdefault("post-commit-archive-page-ids", []).extend(cleanup)
                read_remote_entry(provider, entry, refresh_metadata=True)
                write_manifest(provider, config, manifest)
            write_local_bytes(target, raw, data_dir, stamp)
            update_file_state(state, data_dir, path, raw.decode("utf-8"), latest_remote, entry, raw)
            continue
        if action.action == "conflict":
            base = read_base(data_dir, state.get("files", {}).get(path, {}), "local")
            identifier, root = write_conflict(data_dir, action, base)
            page_id = remote_conflict_page(provider, config, identifier, action, record_created)
            meta = json.loads((root / "meta.json").read_text(encoding="utf-8"))
            meta["remote-conflict-page-id"] = page_id
            atomic_write_json(root / "meta.json", meta)
            artifacts = {}
            for label in ("local", "remote", "base"):
                artifact_path = f"data/.sync/conflicts/{identifier}/{label}.md"
                artifacts[label] = {
                    "path": artifact_path,
                    "source": write_source_descriptor(provider, config, artifact_path, (root / f"{label}.md").read_bytes(), record_created),
                    "source-fidelity": "exact-bytes",
                }
            manifest.setdefault("conflicts", {})[identifier] = {"meta": conflict_metadata(meta), "artifacts": artifacts}
            write_manifest(provider, config, manifest)
            state.setdefault("conflicts", {})[identifier] = meta
            continue
        if action.action == "tombstone":
            identifier = deletion_id(path)
            origin = "local" if action.local_content is None else "remote"
            record = {"id": identifier, "path": path, "origin": origin, "status": "pending", "created-at": utc_now()}
            state.setdefault("deletions", {})[identifier] = record
            manifest.setdefault("deletions", {})[identifier] = record
            if entry:
                entry["tombstone"] = True
            continue

    lease_guard.checkpoint()
    remote_head = read_manifest(provider, config)
    remote_transaction = remote_head.get("transaction") or {}
    if int(remote_head.get("revision", -1)) != base_revision or remote_transaction.get("id") != transaction_id:
        raise NotebookSyncError("远端 manifest 在事务期间发生变化，拒绝提交。")
    cleanup_ids = list(manifest["transaction"].get("post-commit-archive-page-ids", []))
    manifest["cleanup-pending"] = merge_cleanup_items(list(manifest.get("cleanup-pending", [])), cleanup_ids)
    manifest["revision"] = base_revision + 1
    manifest["transaction"] = None
    write_manifest(provider, config, manifest)
    process_cleanup_pending(provider, config, manifest)
    state["last-sync-at"] = utc_now()
    state["last-remote-revision"] = manifest["revision"]
    state["pending-local"] = []
    save_state(data_dir, state)


def apply_confirmed_deletions(
    actions: list[SyncAction],
    state: dict[str, Any],
    skill_dir: Path,
    data_dir: Path,
) -> None:
    by_path = {
        str(item.get("path")): item
        for item in state.get("deletions", {}).values()
        if item.get("status") == "confirmed"
    }
    for action in actions:
        if action.action != "confirmed-delete":
            continue
        record = by_path.get(action.path)
        if not record:
            raise NotebookSyncError(f"已确认删除缺少全局记录: {action.path}")
        target = local_path_for(action.path, skill_dir, data_dir)
        backup = confirmed_deletion_path(data_dir, str(record["id"]), action.path)
        if target.exists():
            backup.parent.mkdir(parents=True, exist_ok=True)
            if backup.exists():
                backup = backup.with_name(f"{backup.stem}-{uuid.uuid4().hex[:6]}{backup.suffix}")
            shutil.move(str(target), str(backup))
            record["local-backup-path"] = str(backup)
        state.setdefault("files", {}).pop(action.path, None)
        action.action = "noop"
        action.reason = "已确认删除的本地旧副本已隔离"


def rollback_incomplete_transaction(provider: HttpProvider, config: dict[str, Any], manifest: dict[str, Any]) -> None:
    transaction = manifest.get("transaction")
    if not transaction:
        return
    restored = 0
    before_files = transaction.get("before-files")
    if isinstance(before_files, dict):
        after_files = manifest.setdefault("files", {})
        protected_ids: set[str] = set()
        for before_entry in before_files.values():
            if not isinstance(before_entry, dict):
                continue
            for part in before_entry.get("parts", []):
                protected_ids.add(str(part.get("page-id")))
                if part.get("previous-page-id"):
                    protected_ids.add(str(part.get("previous-page-id")))
            for part in before_entry.get("previous-parts", []):
                protected_ids.add(str(part.get("page-id")))
            protected_ids.update(source_page_ids(before_entry))
        for conflict in transaction.get("before-conflicts", {}).values():
            for artifact in conflict.get("artifacts", {}).values():
                protected_ids.update(source_page_ids(artifact))
        for path, before_entry in before_files.items():
            if before_entry is None:
                after_files.pop(path, None)
                continue
            if transaction.get("write-model") != "copy-on-write-v1":
                after_entry = after_files.get(path) or before_entry
                after_by_page = {str(item.get("page-id")): item for item in after_entry.get("parts", [])}
                for part in before_entry.get("parts", []):
                    page_id = str(part["page-id"])
                    current = provider.read_page(page_id)
                    expected = part.get("remote-hash")
                    if expected and content_hash(current.markdown) == expected:
                        continue
                    replacement = after_by_page.get(page_id, part)
                    previous_id = replacement.get("previous-page-id") or part.get("previous-page-id")
                    if not previous_id:
                        raise NotebookSyncError("未完成事务缺少上一版，无法自动回滚。")
                    previous = provider.read_page(str(previous_id))
                    repaired = provider.replace_page(page_id, previous.markdown)
                    if expected and content_hash(repaired.markdown) != expected:
                        raise NotebookSyncError("未完成事务自动回滚后摘要仍不一致，已停止。")
                    restored += 1
            after_files[path] = before_entry
        if isinstance(transaction.get("before-folders"), dict):
            manifest["folders"] = transaction["before-folders"]
        if isinstance(transaction.get("before-conflicts"), dict):
            manifest["conflicts"] = transaction["before-conflicts"]
        for page_id in reversed([str(item) for item in transaction.get("created-page-ids", [])]):
            if page_id in protected_ids:
                continue
            try:
                provider.archive_page(page_id)
            except ProviderError as exc:
                if exc.status != 404:
                    manifest.setdefault("cleanup-pending", []).append(page_id)
    else:
        for entry in manifest.get("files", {}).values():
            for part in entry.get("parts", []):
                current = provider.read_page(str(part["page-id"]))
                expected = part.get("remote-hash")
                if expected and content_hash(current.markdown) == expected:
                    continue
                previous_id = part.get("previous-page-id")
                if not previous_id:
                    raise NotebookSyncError("未完成事务缺少上一版，无法自动回滚。")
                previous = provider.read_page(str(previous_id))
                repaired = provider.replace_page(str(part["page-id"]), previous.markdown)
                if expected and content_hash(repaired.markdown) != expected:
                    raise NotebookSyncError("未完成事务自动回滚后摘要仍不一致，已停止。")
                restored += 1
    manifest["transaction"] = None
    manifest["recovered-at"] = utc_now()
    manifest["recovered-transaction"] = transaction
    write_manifest(provider, config, manifest)
    print(f"已回滚未完成远端事务，恢复页面数: {restored}")


def run_sync(args: argparse.Namespace, apply: bool) -> int:
    paths = resolve_team_paths(args.skill_dir)
    rebuild_needed = False
    with LocalSyncLock(paths.data_dir):
        config = load_config(paths.skill_dir)
        assert config is not None
        if getattr(args, "command", None) == "pull" and config["mode"] != "bidirectional":
            raise NotebookSyncError("单向备份模式不会拉取在线修改；请先切换为 bidirectional。")
        config = dict(config)
        config["_direction"] = getattr(args, "command", "sync")
        provider = provider_from_config(config)
        provider.verify()
        state = load_state(paths.data_dir)
        lease = None
        lease_guard = None
        if apply:
            lease = provider.acquire_lease(str(config["remote"]["lock-page-id"]), str(state["machine-id"]))
            lease_guard = LeaseGuard(provider, lease)
            if hasattr(provider, "set_request_guard"):
                provider.set_request_guard(lease_guard.checkpoint)
        try:
            discover_manifest_shadow(provider, config, paths.skill_dir if apply else None)
            manifest = read_manifest(provider, config)
            if apply:
                manifest = ensure_protocol_v2(provider, config, manifest, paths.skill_dir)
            if manifest.get("transaction"):
                if not apply:
                    raise NotebookSyncError("远端存在未完成事务；执行 sync 会先尝试安全回滚。")
                rollback_incomplete_transaction(provider, config, manifest)
            if apply:
                process_cleanup_pending(provider, config, manifest)
            actions, _, _ = build_actions(provider, config, manifest, state, paths.skill_dir, paths.data_dir)
            summarize_actions(actions)
            if apply:
                rebuild_needed = any(action.action in {"pull", "pull-create", "merge", "confirmed-delete"} for action in actions)
                apply_confirmed_deletions(actions, state, paths.skill_dir, paths.data_dir)
                assert lease is not None
                assert lease_guard is not None
                mutating = {"push", "push-create", "pull", "pull-create", "merge", "conflict", "tombstone", "baseline"}
                conflict_updates = any(item.get("status") == "resolved"
                                       and manifest.get("conflicts", {}).get(identifier, {}).get("meta", {}).get("status") == "open"
                                       for identifier, item in state.get("conflicts", {}).items())
                if any(action.action in mutating for action in actions) or conflict_updates:
                    apply_actions(provider, config, manifest, state, actions, paths.skill_dir, paths.data_dir, lease_guard)
                    print(f"同步完成，远端修订号: {manifest['revision']}")
                else:
                    for action in actions:
                        if action.action == "baseline" and action.local_content is not None and action.remote_content is not None:
                            entry = manifest.get("files", {}).get(action.path)
                            if entry:
                                update_file_state(state, paths.data_dir, action.path, action.local_content, action.remote_content, entry, action.source_bytes)
                    state["last-sync-at"] = utc_now()
                    state["last-remote-revision"] = manifest.get("revision", 0)
                    state["pending-local"] = []
                    save_state(paths.data_dir, state)
                    print(f"无需远端写入，修订号保持: {manifest.get('revision', 0)}")
        finally:
            if lease is not None:
                try:
                    if hasattr(provider, "set_request_guard"):
                        provider.set_request_guard(None)
                    provider.release_lease(lease)
                except ProviderError as exc:
                    print(f"WARNING: 释放远端锁失败: {exc}", file=sys.stderr)
    if rebuild_needed:
        # The sync lock must be released before the index command acquires it.
        try:
            indexed = subprocess.run(
                [sys.executable, str(Path(__file__).with_name("rebuild-index.py")), "--skill-dir", str(paths.skill_dir)],
                capture_output=True, text=True, check=False, timeout=60,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise NotebookSyncError("正文已同步，但本机索引未能刷新；请运行 rebuild-index.py。") from exc
        if indexed.returncode:
            raise NotebookSyncError("正文已同步，但本机索引刷新失败；请运行 rebuild-index.py 检查，未将查询缓存视为已更新。")
        print("本机查询索引已刷新。")
    return 0


def create_remote_repository(provider: HttpProvider, parent: str, repository_id: str) -> dict[str, Any]:
    stable_control = {
        "kind": CONTROL_KIND,
        "notebook-schema-version": NOTEBOOK_SCHEMA_VERSION,
        "repository-id": repository_id,
    }
    root_id = provider.create_page(parent, f"团队记忆 · {repository_id[:8]}", root_control_markdown(stable_control))
    folders: dict[str, str] = {}
    for key, title in FOLDER_TITLES.items():
        folders[key] = provider.create_page(root_id, title, f"# {title}\n")
    previous_id = provider.create_page(folders["system"], "上一版本（每个文件仅保留一份）", "# 上一版本\n")
    source_id = provider.create_page(folders["system"], "原文恢复载荷（请勿修改）", "# 原文恢复载荷\n")
    manifest = new_manifest(repository_id, {})
    manifest_id = provider.create_page(folders["system"], "恢复清单 manifest.json", encode_json_page(manifest, "Team Memory 恢复清单"))
    manifest_shadow_id = provider.create_page(
        folders["system"],
        "恢复清单 manifest.shadow.json",
        encode_json_page(manifest, "Team Memory 恢复清单备用槽"),
    )
    lock_id = provider.create_page(folders["system"], "90 系统锁 · 空闲", empty_lock_markdown())
    control = {
        "kind": CONTROL_KIND,
        "notebook-schema-version": NOTEBOOK_SCHEMA_VERSION,
        "repository-id": repository_id,
        "root-page-id": root_id,
        "manifest-page-id": manifest_id,
        "manifest-shadow-page-id": manifest_shadow_id,
        "lock-page-id": lock_id,
        "previous-folder-id": previous_id,
        "source-folder-id": source_id,
        "folders": folders,
    }
    return control


def resume_remote_repository(provider: HttpProvider, root_id: str) -> dict[str, Any]:
    page = provider.read_page(root_id)
    try:
        control = decode_json_page(page.markdown, CONTROL_KIND)
    except NotebookSyncError:
        control = decode_json_page(page.markdown, LEGACY_CONTROL_KIND)
    if control.get("root-page-id") and control.get("root-page-id") != root_id:
        raise NotebookSyncError("远端根页面 ID 与控制信息不一致。")
    root_children = provider.list_child_pages(root_id)
    folders: dict[str, str] = {}
    missing: list[str] = []
    for key, title in FOLDER_TITLES.items():
        page_id = root_children.get(title)
        if not page_id and key not in {"manager", "sources"}:
            missing.append(title)
        elif page_id:
            folders[key] = page_id
    if missing:
        raise NotebookSyncError("远端根页面缺少固定目录: " + ", ".join(missing))
    system_children = provider.list_child_pages(folders["system"])
    manifest_id = system_children.get("恢复清单 manifest.json")
    manifest_shadow_id = system_children.get("恢复清单 manifest.shadow.json")
    previous_id = system_children.get("上一版本（每个文件仅保留一份）")
    source_id = system_children.get("原文恢复载荷（请勿修改）")
    lock_id = next((page_id for title, page_id in system_children.items() if title.startswith("90 系统锁")), None)
    if not manifest_id or not previous_id or not lock_id:
        raise NotebookSyncError("远端系统目录缺少 manifest、上一版本目录或同步锁。")
    return {
        "kind": CONTROL_KIND,
        "notebook-schema-version": NOTEBOOK_SCHEMA_VERSION,
        "repository-id": str(control["repository-id"]),
        "root-page-id": root_id,
        "manifest-page-id": manifest_id,
        **({"manifest-shadow-page-id": manifest_shadow_id} if manifest_shadow_id else {}),
        "lock-page-id": lock_id,
        "previous-folder-id": previous_id,
        **({"source-folder-id": source_id} if source_id else {}),
        "folders": folders,
    }


def command_connect(args: argparse.Namespace) -> int:
    paths = resolve_team_paths(args.skill_dir)
    if config_path(paths.skill_dir).exists():
        raise NotebookSyncError("当前主库已经绑定在线笔记；请先 disconnect，不能同时连接多个笔记本。")
    provider_name = args.provider
    if not provider_name:
        candidates = []
        if os.environ.get("TEAM_MEMORY_NOTION_TOKEN"):
            candidates.append("notion")
        if os.environ.get("TEAM_MEMORY_FLOWUS_TOKEN"):
            candidates.append("flowus")
        if len(candidates) != 1:
            raise NotebookSyncError("connect --resume 时请指定 --provider notion|flowus，或只设置一个平台 token。")
        provider_name = candidates[0]
    repository_id = str(uuid.uuid4())
    credential = credential_for(provider_name, repository_id, args.token_env, False)
    provisional = {
        "notebook-schema-version": NOTEBOOK_SCHEMA_VERSION,
        "provider": provider_name,
        "provider-api-version": provider_name_version(provider_name),
        "mode": args.mode,
        "repository-id": repository_id,
        "credential": credential,
    }
    provider = provider_from_config(provisional)
    provider.verify()
    if args.resume:
        control = resume_remote_repository(provider, args.resume)
        repository_id = str(control["repository-id"])
    else:
        if not args.parent:
            raise NotebookSyncError("新建在线库必须提供 --parent 页面 ID。")
        control = create_remote_repository(provider, args.parent, repository_id)
    if args.store_keychain:
        credential = credential_for(provider_name, repository_id, args.token_env, True)
    config = {
        "notebook-schema-version": NOTEBOOK_SCHEMA_VERSION,
        "provider": provider_name,
        "provider-api-version": provider_name_version(provider_name),
        "mode": args.mode,
        "repository-id": repository_id,
        "credential": credential,
        "remote": control,
        "schedule": {"enabled": False, "type": "manual"},
        "connected-at": utc_now(),
    }
    atomic_write_json(config_path(paths.skill_dir), config)
    print(f"已连接 {provider_name}: {control['root-page-id']}")
    print(f"模式: {args.mode}；定时同步默认关闭。")
    print("连接配置已保存，尚未上传团队记忆。请先运行 plan，确认后再运行 sync。")
    return 0


def command_mode(args: argparse.Namespace) -> int:
    paths = resolve_team_paths(args.skill_dir)
    config = load_config(paths.skill_dir)
    assert config is not None
    old = config["mode"]
    config["mode"] = args.mode
    config["mode-updated-at"] = utc_now()
    atomic_write_json(config_path(paths.skill_dir), config)
    print(f"同步模式: {old} -> {args.mode}")
    print("切换后先运行 plan 检查两端差异，再运行 sync。")
    return 0


def command_offline_write(args: argparse.Namespace) -> int:
    paths = resolve_team_paths(args.skill_dir)
    config = load_config(paths.skill_dir)
    assert config is not None
    if config["mode"] != "bidirectional":
        raise NotebookSyncError("只有 bidirectional 模式需要登记离线写入。")
    state = load_state(paths.data_dir)
    record = {
        "id": f"OFFLINE-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:6]}",
        "approved-at": utc_now(),
        "note": args.note,
        "base-remote-revision": state.get("last-remote-revision", 0),
        "status": "pending-sync",
    }
    state.setdefault("pending-local", []).append(record)
    save_state(paths.data_dir, state)
    print(f"已登记离线写入许可: {record['id']}")
    print("完成本地修改后，在网络恢复时立即运行 sync；冲突仍会被隔离。")
    return 0


def command_status(args: argparse.Namespace) -> int:
    paths = resolve_team_paths(args.skill_dir)
    config = load_config(paths.skill_dir, required=False)
    if not config:
        print("在线笔记: 关闭（本地模式保持不变）")
        return 0
    state = load_state(paths.data_dir)
    print(f"平台: {config['provider']}")
    print(f"模式: {config['mode']}")
    print(f"仓库 ID: {config['repository-id']}")
    print(f"远端根页面: {config['remote']['root-page-id']}")
    print(f"上次同步: {state.get('last-sync-at') or '从未'}")
    print(f"远端修订: {state.get('last-remote-revision', 0)}")
    print(f"开放冲突: {sum(1 for item in state.get('conflicts', {}).values() if item.get('status') == 'open')}")
    print(f"待确认删除: {sum(1 for item in state.get('deletions', {}).values() if item.get('status') == 'pending')}")
    print(f"待同步离线写入: {len(state.get('pending-local', []))}")
    schedule = config.get("schedule", {})
    print(f"定时同步: {schedule if schedule.get('enabled') else '关闭'}")
    return 0


def collect_restore_snapshot(
    provider: HttpProvider,
    config: dict[str, Any],
    output: Path,
    version: str,
) -> tuple[dict[str, Any], dict[str, bytes], list[tuple[str, str, bytes]]]:
    discover_manifest_shadow(provider, config)
    manifest = read_manifest(provider, config)
    if manifest.get("transaction"):
        raise NotebookSyncError("远端 manifest 存在未完成事务，拒绝从半完成状态恢复。")
    snapshot = (
        int(manifest.get("revision", 0)),
        int(manifest.get("manifest-write-sequence", 0)),
    )
    data_dir = output / "data"
    recovered: dict[str, bytes] = {}
    pending_recovered: list[tuple[str, str, bytes]] = []
    legacy_restore = False
    for path, entry in manifest.get("files", {}).items():
        local_path_for(path, output, data_dir)
        if entry.get("path", path) != path:
            raise NotebookSyncError("恢复清单的文件键与原文路径不一致。")
        if manifest.get("kind") == LEGACY_MANIFEST_KIND:
            entry.setdefault("path", path)
            entry.setdefault("source-fidelity", "legacy-rendered")
            entry.setdefault("previous-source-fidelity", "legacy-rendered")
        if not entry.get("source" if version == "current" else "previous-source"):
            legacy_restore = True
        if entry.get("tombstone"):
            deletion = next(
                (
                    item
                    for item in manifest.get("deletions", {}).values()
                    if item.get("path") == path and item.get("status") == "pending"
                ),
                None,
            )
            identifier = str((deletion or {}).get("id") or f"RECOVERED-{file_id(path)[:12]}")
            pending_deletion_path(data_dir, identifier, path)  # Validate before any restore output is written.
            try:
                pending_recovered.append((identifier, path, read_source_entry(provider, entry, "current")))
            except ProviderError as exc:
                if exc.status != 404 or entry.get("source"):
                    raise
                print(f"WARNING: 旧版待删除文件 {path} 没有可恢复内容。", file=sys.stderr)
            continue
        content = read_source_entry(provider, entry, version)
        try:
            content.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise NotebookSyncError("原文恢复载荷不是有效 UTF-8 正文，未写入恢复目录。") from exc
        if version == "previous" and content.lstrip().startswith(b"# " + "尚无上一版".encode("utf-8")):
            raise NotebookSyncError(f"{path} 尚无上一版，已停止上一版恢复。")
        recovered[path] = content
        try:
            entry["_restore-display"] = read_remote_entry(provider, entry)
        except (ProviderError, NotebookSyncError) as exc:
            if not entry.get("source"):
                raise
            entry["_restore-display"] = content.decode("utf-8")
            print(f"WARNING: {path} 的展示页不可用，已从校验通过的原文恢复: {exc}", file=sys.stderr)
    recovered_conflicts = {}
    for identifier, conflict in manifest.get("conflicts", {}).items():
        meta = conflict.get("meta", {})
        if meta.get("status") != "open":
            continue
        if not re.fullmatch(r"CONFLICT-[A-Za-z0-9-]+", identifier) or meta.get("id") != identifier:
            raise NotebookSyncError("待恢复冲突 ID 无效。")
        local_path_for(str(meta.get("path", "")), output, data_dir)
        artifacts = {}
        for label in ("local", "remote", "base"):
            artifact = conflict.get("artifacts", {}).get(label)
            expected = f"data/.sync/conflicts/{identifier}/{label}.md"
            if not isinstance(artifact, dict) or artifact.get("path") != expected:
                raise NotebookSyncError("待恢复冲突稿缺失或路径不一致。")
            artifacts[label] = read_source_entry(provider, artifact)
            try:
                artifacts[label].decode("utf-8")
            except UnicodeDecodeError as exc:
                raise NotebookSyncError("待恢复冲突稿不是有效 UTF-8，未写入恢复目录。") from exc
        recovered_conflicts[identifier] = {"meta": conflict_metadata(meta), "artifacts": artifacts}
    head = read_manifest(provider, config)
    current = (int(head.get("revision", 0)), int(head.get("manifest-write-sequence", 0)))
    if head.get("transaction") or current != snapshot:
        raise NotebookSyncError("恢复期间远端 manifest 已变化，本次快照已丢弃。")
    if legacy_restore:
        print("WARNING: 部分文件来自旧版渲染备份，无法保证与原始文件逐字节一致。恢复后同步可补齐原文载荷。", file=sys.stderr)
    manifest["_restore-conflicts"] = recovered_conflicts
    return manifest, recovered, pending_recovered


def command_restore(args: argparse.Namespace) -> int:
    source_skill_dir = Path(args.skill_dir).expanduser().resolve() if args.skill_dir else Path(__file__).resolve().parents[1]
    config = load_config(source_skill_dir, required=False)
    if not config:
        if not args.provider or not args.remote_root:
            raise NotebookSyncError("本地连接配置已丢失时，restore 需要 --provider 和 --remote-root。")
        repository_hint = str(uuid.uuid4())
        credential = credential_for(args.provider, repository_hint, args.token_env, False)
        provisional = {
            "notebook-schema-version": NOTEBOOK_SCHEMA_VERSION,
            "provider": args.provider,
            "provider-api-version": provider_name_version(args.provider),
            "mode": args.mode,
            "repository-id": repository_hint,
            "credential": credential,
        }
        provider = provider_from_config(provisional)
        provider.verify()
        control = resume_remote_repository(provider, args.remote_root)
        config = {
            "notebook-schema-version": NOTEBOOK_SCHEMA_VERSION,
            "provider": args.provider,
            "provider-api-version": provider_name_version(args.provider),
            "mode": args.mode,
            "repository-id": str(control["repository-id"]),
            "credential": credential,
            "remote": control,
            "schedule": {"enabled": False, "type": "manual"},
            "connected-at": utc_now(),
        }
    else:
        provider = provider_from_config(config)
        provider.verify()
    output = Path(args.output).expanduser().resolve()
    if output.exists():
        if not output.is_dir():
            raise NotebookSyncError(f"恢复目标必须是空目录，不能是文件: {output}")
        if any(output.iterdir()):
            raise NotebookSyncError(f"恢复目标必须为空目录: {output}")
    owner = f"restore-{uuid.uuid4().hex[:12]}"
    lease = provider.acquire_lease(str(config["remote"]["lock-page-id"]), owner)
    guard = LeaseGuard(provider, lease)
    if hasattr(provider, "set_request_guard"):
        provider.set_request_guard(guard.checkpoint)
    try:
        manifest, recovered, pending_recovered = collect_restore_snapshot(provider, config, output, args.version)
    finally:
        if hasattr(provider, "set_request_guard"):
            provider.set_request_guard(None)
        provider.release_lease(lease)
    output.mkdir(parents=True, exist_ok=True)
    data_dir = output / "data"
    for path, content in recovered.items():
        target = local_path_for(path, output, data_dir)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    for identifier, path, content in pending_recovered:
        target = pending_deletion_path(data_dir, identifier, path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    data_dir.mkdir(parents=True, exist_ok=True)
    restored_skill_config = output / "skill-config.yaml"
    configured_data = read_config_data_path(restored_skill_config)
    if configured_data and resolve_data_path(configured_data, output) != data_dir.resolve():
        origin = data_dir / "archive" / "restore-origin" / str(manifest.get("revision", 0)) / "skill-config.original.md"
        origin.parent.mkdir(parents=True, exist_ok=True)
        origin.write_bytes(restored_skill_config.read_bytes())
        update_config_data_path(restored_skill_config, output, data_dir)
        print(f"工作配置 data-path 已重定位为 data；原始配置字节保存在 {origin}。下次 plan 将显示配置本地变更。")
    write_root_lock(output, data_dir, "从在线 Team Memory 恢复；Markdown 是本地工作源。")
    restored_config = {key: value for key, value in config.items() if not key.startswith("_")}
    restored_config["schedule"] = {"enabled": False, "type": "manual"}
    restored_config["restored-at"] = utc_now()
    atomic_write_json(config_path(output), restored_config)
    state = load_state(data_dir)
    for path, content in recovered.items():
        entry = manifest.get("files", {}).get(path)
        if entry:
            local_text = content.decode("utf-8")
            update_file_state(state, data_dir, path, local_text, str(entry.pop("_restore-display", local_text)), entry, content)
    for identifier, path, _ in pending_recovered:
        record = copy.deepcopy(manifest.get("deletions", {}).get(identifier, {}))
        record.update(
            {
                "id": identifier,
                "path": path,
                "status": "pending",
                "local-archive-path": str(pending_deletion_path(data_dir, identifier, path)),
            }
        )
        state.setdefault("deletions", {})[identifier] = record
    for identifier, conflict in manifest.pop("_restore-conflicts", {}).items():
        root = sync_dir(data_dir) / "conflicts" / identifier
        root.mkdir(parents=True, exist_ok=True)
        for label, raw in conflict["artifacts"].items():
            (root / f"{label}.md").write_bytes(raw)
        atomic_write_json(root / "meta.json", conflict["meta"])
        state.setdefault("conflicts", {})[identifier] = conflict["meta"]
    state["last-sync-at"] = utc_now()
    state["last-remote-revision"] = manifest.get("revision", 0)
    save_state(data_dir, state)
    print(f"已恢复到: {output}")
    print(f"远端修订: {manifest.get('revision', 0)}")
    print("已恢复在线连接配置；定时同步保持关闭。请先运行 doctor.py --online 和 plan。")
    # Execute the installed code, not a non-existent scripts/ directory in the
    # restored data tree. In-process execution also retains the path resolver's
    # environment and test isolation consistently.
    saved_argv = sys.argv
    index_status = 0
    try:
        sys.argv = [str(Path(__file__).with_name("rebuild-index.py")), "--skill-dir", str(output)]
        try:
            runpy.run_path(sys.argv[0], run_name="__main__")
        except SystemExit as exc:
            index_status = int(exc.code or 0)
    except Exception as exc:
        print(f"WARNING: 原文已恢复，但索引重建失败: {exc}", file=sys.stderr)
        index_status = 1
    finally:
        sys.argv = saved_argv
    from doctor import check_data_consistency
    consistency = check_data_consistency(data_dir, restored_skill_config)
    findings = [line for line in consistency if line.startswith("- ")]
    if findings:
        print("恢复后数据检查:")
        for line in findings:
            print(line)
    fatal = any(any(term in line for term in ("必须修复", "关联事件不存在", "来源事件不存在", "来源文件不存在")) for line in findings)
    if index_status or fatal:
        print("WARNING: 恢复正文已保留，索引或引用检查未通过，请按上面的信息修复。", file=sys.stderr)
        return 1
    return 0


def command_disconnect(args: argparse.Namespace) -> int:
    paths = resolve_team_paths(args.skill_dir)
    config = load_config(paths.skill_dir, required=False)
    if not config:
        print("在线笔记已经处于关闭状态。")
        return 0
    schedule_off(paths.skill_dir, config, quiet=True)
    config_path(paths.skill_dir).unlink()
    print("已解除本地在线笔记绑定；远端页面未删除。")
    return 0


def list_items(state: dict[str, Any], key: str) -> int:
    items = state.get(key, {})
    if not items:
        print("无。")
        return 0
    for identifier, item in sorted(items.items()):
        print(f"- {identifier}: {item.get('path')} [{item.get('status')}] {item.get('reason', '')}")
    return 0


def command_conflicts(args: argparse.Namespace) -> int:
    paths = resolve_team_paths(args.skill_dir)
    state = load_state(paths.data_dir)
    if args.conflict_command == "list":
        return list_items(state, "conflicts")
    item = state.get("conflicts", {}).get(args.id)
    if not item:
        raise NotebookSyncError(f"未找到冲突: {args.id}")
    root = sync_dir(paths.data_dir) / "conflicts" / args.id
    if args.conflict_command == "show":
        print((root / "meta.json").read_text(encoding="utf-8"))
        print(f"本地稿: {root / 'local.md'}")
        print(f"在线稿: {root / 'remote.md'}")
        print(f"共同基线: {root / 'base.md'}")
        return 0
    with LocalSyncLock(paths.data_dir):
        state = load_state(paths.data_dir)
        item = state.get("conflicts", {}).get(args.id)
        if not item:
            raise NotebookSyncError(f"未找到冲突: {args.id}")
        source = root / f"{args.use}.md" if args.use in {"local", "remote"} else Path(args.file).expanduser().resolve()
        if not source.is_file():
            raise NotebookSyncError(f"冲突解决稿不存在: {source}")
        path = str(item["path"])
        target = local_path_for(path, paths.skill_dir, paths.data_dir)
        chosen_raw = source.read_bytes()
        chosen = chosen_raw.decode("utf-8")
        remote_text = (root / "remote.md").read_text(encoding="utf-8")
        base_text = (root / "base.md").read_text(encoding="utf-8")
        backup_local_file(target, paths.data_dir, f"conflict-resolve-{args.id}")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(chosen_raw)
        file_state = state.setdefault("files", {}).setdefault(path, {"file-id": file_id(path)})
        if args.use == "remote":
            file_state["local-hash"] = content_hash(chosen)
            file_state["remote-hash"] = content_hash(remote_text)
            file_state.update(save_bases(paths.data_dir, path, chosen, remote_text))
        else:
            baseline = base_text if base_text.strip() else remote_text
            file_state["local-hash"] = content_hash(baseline)
            file_state["remote-hash"] = content_hash(remote_text)
            file_state.update(save_bases(paths.data_dir, path, baseline, remote_text))
        item["status"] = "resolved"
        item["resolved-at"] = utc_now()
        item["resolution"] = args.use
        atomic_write_json(root / "meta.json", item)
        save_state(paths.data_dir, state)
    print(f"已采用 {args.use} 版本写入本地；请运行 sync 提交。")
    return 0


def command_deletions(args: argparse.Namespace) -> int:
    paths = resolve_team_paths(args.skill_dir)
    state = load_state(paths.data_dir)
    if args.deletion_command == "list":
        return list_items(state, "deletions")
    with LocalSyncLock(paths.data_dir):
        config = load_config(paths.skill_dir)
        assert config is not None
        state = load_state(paths.data_dir)
        item = state.get("deletions", {}).get(args.id)
        if not item:
            raise NotebookSyncError(f"未找到待确认删除: {args.id}")
        provider = provider_from_config(config)
        provider.verify()
        lease = provider.acquire_lease(str(config["remote"]["lock-page-id"]), str(state["machine-id"]))
        guard = LeaseGuard(provider, lease)
        if hasattr(provider, "set_request_guard"):
            provider.set_request_guard(guard.checkpoint)
        try:
            discover_manifest_shadow(provider, config, paths.skill_dir)
            manifest = read_manifest(provider, config)
            manifest = ensure_protocol_v2(provider, config, manifest, paths.skill_dir)
            if manifest.get("transaction"):
                rollback_incomplete_transaction(provider, config, manifest)
            remote_item = manifest.get("deletions", {}).get(args.id)
            if remote_item:
                item.update(copy.deepcopy(remote_item))
            if item.get("status") != "pending":
                raise NotebookSyncError(f"删除事项不是待确认状态: {item.get('status')}")
            path = str(item["path"])
            entry = manifest.get("files", {}).get(path)
            base_revision = int(manifest.get("revision", 0))
            transaction_id = str(uuid.uuid4())
            manifest["transaction"] = {
                "id": transaction_id,
                "status": "prepared",
                "kind": f"deletion-{args.deletion_command}",
                "started-at": utc_now(),
                "machine-id": state["machine-id"],
                "base-revision": base_revision,
                "before-files": {path: copy.deepcopy(entry)},
                "created-page-ids": [],
                "post-commit-archive-page-ids": [],
            }
            write_manifest(provider, config, manifest)
            target = local_path_for(path, paths.skill_dir, paths.data_dir)
            pending = pending_deletion_path(paths.data_dir, args.id, path)
            cleanup_ids: list[str] = []
            if args.deletion_command == "restore":
                if not entry:
                    raise NotebookSyncError("远端 manifest 已缺少该文件，无法恢复。")
                for part in entry.get("parts", []):
                    provider.restore_page(str(part["page-id"]))
                    if part.get("previous-page-id"):
                        provider.restore_page(str(part["previous-page-id"]))
                for part in entry.get("previous-parts", []):
                    provider.restore_page(str(part["page-id"]))
                for page_id in source_page_ids(entry):
                    provider.restore_page(page_id)
                entry["tombstone"] = False
                if not target.exists():
                    if pending.exists():
                        target.parent.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(pending), str(target))
                    else:
                        content = read_source_entry(provider, entry)
                        backup_local_file(target, paths.data_dir, f"delete-restore-{args.id}")
                        target.parent.mkdir(parents=True, exist_ok=True)
                        target.write_bytes(content)
                content = target.read_bytes().decode("utf-8")
                remote_content = read_remote_entry(provider, entry)
                if content_hash(content) == content_hash(remote_content):
                    update_file_state(state, paths.data_dir, path, content, remote_content, entry, target.read_bytes())
                else:
                    bases = save_bases(paths.data_dir, path, remote_content, remote_content)
                    state.setdefault("files", {})[path] = {
                        "file-id": file_id(path),
                        "local-hash": content_hash(remote_content),
                        "remote-hash": content_hash(remote_content),
                        "remote-parts": entry.get("parts", []),
                        "synced-at": utc_now(),
                        **bases,
                    }
                item["status"] = "restored"
            else:
                backup = confirmed_deletion_path(paths.data_dir, args.id, path)
                backup.parent.mkdir(parents=True, exist_ok=True)
                source = target if target.exists() else pending
                if source.exists():
                    shutil.move(str(source), str(backup))
                elif entry:
                    try:
                        preserved = read_source_entry(provider, entry)
                    except ProviderError as exc:
                        if exc.status != 404:
                            raise
                        preserved = read_source_entry(provider, entry, "previous")
                    backup.write_bytes(preserved)
                if entry:
                    for part in entry.get("parts", []):
                        cleanup_ids.append(str(part["page-id"]))
                        if part.get("previous-page-id"):
                            cleanup_ids.append(str(part["previous-page-id"]))
                    cleanup_ids.extend(str(part["page-id"]) for part in entry.get("previous-parts", []))
                    cleanup_ids.extend(source_page_ids(entry))
                    manifest["files"].pop(path, None)
                state.setdefault("files", {}).pop(path, None)
                item["status"] = "confirmed"
                item["local-backup-path"] = str(backup)
            item[f"{item['status']}-at"] = utc_now()
            manifest.setdefault("deletions", {})[args.id] = copy.deepcopy(item)
            remote_head = read_manifest(provider, config)
            remote_transaction = remote_head.get("transaction") or {}
            if int(remote_head.get("revision", -1)) != base_revision or remote_transaction.get("id") != transaction_id:
                raise NotebookSyncError("远端 manifest 在删除事务期间发生变化，拒绝提交。")
            manifest["cleanup-pending"] = merge_cleanup_items(list(manifest.get("cleanup-pending", [])), cleanup_ids)
            manifest["revision"] = base_revision + 1
            manifest["transaction"] = None
            write_manifest(provider, config, manifest)
            process_cleanup_pending(provider, config, manifest)
            state.setdefault("deletions", {})[args.id] = item
            state["last-remote-revision"] = manifest["revision"]
            save_state(paths.data_dir, state)
        finally:
            if hasattr(provider, "set_request_guard"):
                provider.set_request_guard(None)
            provider.release_lease(lease)
    print(f"删除事项 {args.id}: {item['status']} (远端修订 {manifest['revision']})")
    return 0


def launchd_label(repository_id: str) -> str:
    return f"com.openai.team-memory-sync.{repository_id.replace('-', '')[:12]}"


def launchd_path(repository_id: str) -> Path:
    return Path.home() / "Library" / "LaunchAgents" / f"{launchd_label(repository_id)}.plist"


def schedule_off(skill_dir: Path, config: dict[str, Any], quiet: bool = False) -> None:
    path = launchd_path(str(config["repository-id"]))
    label = launchd_label(str(config["repository-id"]))
    if path.exists():
        subprocess.run(["launchctl", "bootout", f"gui/{os.getuid()}/{label}"], check=False, capture_output=True)
        path.unlink()
    config.setdefault("schedule", {}).update({"enabled": False, "type": "manual"})
    atomic_write_json(config_path(skill_dir), config)
    if not quiet:
        print("定时同步已关闭。")


def command_schedule(args: argparse.Namespace) -> int:
    paths = resolve_team_paths(args.skill_dir)
    config = load_config(paths.skill_dir)
    assert config is not None
    if args.schedule_command == "status":
        schedule = config.get("schedule", {"enabled": False})
        path = launchd_path(str(config["repository-id"]))
        label = launchd_label(str(config["repository-id"]))
        print(json.dumps(schedule, ensure_ascii=False, indent=2))
        print(f"plist 存在: {'是' if path.exists() else '否'} ({path})")
        if platform.system() != "Darwin":
            print("launchd 服务: 不可用（非 macOS）")
            return 0
        result = subprocess.run(
            ["launchctl", "print", f"gui/{os.getuid()}/{label}"],
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print("服务已加载: 否")
            print("正在运行: 否")
            print("最近退出码: 不可用")
            return 0
        state_match = re.search(r"\bstate\s*=\s*([^\n]+)", result.stdout)
        exit_match = re.search(r"\blast exit code\s*=\s*([^\n]+)", result.stdout)
        service_state = state_match.group(1).strip() if state_match else "unknown"
        print("服务已加载: 是")
        print(f"正在运行: {'是' if service_state == 'running' else '否'}")
        print(f"服务状态: {service_state}")
        print(f"最近退出码: {exit_match.group(1).strip() if exit_match else '不可用'}")
        return 0
    if args.schedule_command == "off":
        schedule_off(paths.skill_dir, config)
        return 0
    if platform.system() != "Darwin":
        raise NotebookSyncError("首版只自动安装 macOS launchd；其他系统请手动运行 sync。")
    original_config = copy.deepcopy(config)
    if config.get("credential", {}).get("type") != "keychain":
        token = os.environ.get(str(config.get("credential", {}).get("name", "")), "")
        if not token:
            raise NotebookSyncError("launchd 无法继承当前 shell 凭据；请先设置 token 环境变量后重试，脚本会转存到 macOS 钥匙串。")
        service = f"team-memory-notebook:{config['repository-id']}"
        store_keychain_token(service, str(config["provider"]), token)
        config["credential"] = {"type": "keychain", "service": service, "account": str(config["provider"])}
    interval_map = {"15m": 900, "1h": 3600, "24h": 86400}
    if args.every not in interval_map and not args.daily:
        raise NotebookSyncError("schedule set 需要 --every 15m|1h|24h 或 --daily HH:MM。")
    label = launchd_label(str(config["repository-id"]))
    script = paths.skill_dir / "scripts" / "notebook-sync.py"
    log_dir = sync_dir(paths.data_dir) / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    payload: dict[str, Any] = {
        "Label": label,
        "ProgramArguments": [sys.executable, str(script), "--skill-dir", str(paths.skill_dir), "sync"],
        "WorkingDirectory": str(paths.skill_dir),
        "StandardOutPath": str(log_dir / "launchd.out.log"),
        "StandardErrorPath": str(log_dir / "launchd.err.log"),
        "RunAtLoad": False,
    }
    if args.daily:
        try:
            hour, minute = [int(value) for value in args.daily.split(":", 1)]
        except ValueError as exc:
            raise NotebookSyncError("--daily 必须是 HH:MM。") from exc
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            raise NotebookSyncError("--daily 时间超出范围。")
        payload["StartCalendarInterval"] = {"Hour": hour, "Minute": minute}
        schedule = {"enabled": True, "type": "daily", "time": args.daily}
    else:
        payload["StartInterval"] = interval_map[args.every]
        schedule = {"enabled": True, "type": "interval", "every": args.every}
    path = launchd_path(str(config["repository-id"]))
    path.parent.mkdir(parents=True, exist_ok=True)
    previous_plist = path.read_bytes() if path.exists() else None
    path.write_bytes(plistlib.dumps(payload, sort_keys=True))
    subprocess.run(["launchctl", "bootout", f"gui/{os.getuid()}/{label}"], check=False, capture_output=True)
    result = subprocess.run(["launchctl", "bootstrap", f"gui/{os.getuid()}", str(path)], check=False, capture_output=True, text=True)
    if result.returncode != 0:
        if previous_plist is None:
            path.unlink(missing_ok=True)
        else:
            path.write_bytes(previous_plist)
            subprocess.run(
                ["launchctl", "bootstrap", f"gui/{os.getuid()}", str(path)],
                check=False,
                capture_output=True,
            )
        atomic_write_json(config_path(paths.skill_dir), original_config)
        raise NotebookSyncError(f"launchd 加载失败: {result.stderr.strip()}")
    config["schedule"] = schedule
    atomic_write_json(config_path(paths.skill_dir), config)
    print(f"已安装定时同步: {schedule}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Team Memory Notion/FlowUs backup and bidirectional sync")
    parser.add_argument("--skill-dir", default=None, help="team-memory skill directory")
    sub = parser.add_subparsers(dest="command", required=True)

    connect = sub.add_parser("connect")
    connect.add_argument("--provider", choices=["notion", "flowus"])
    connect_target = connect.add_mutually_exclusive_group(required=True)
    connect_target.add_argument("--parent", help="parent page id for a new remote repository")
    connect_target.add_argument("--resume", help="existing Team Memory remote root page id")
    connect.add_argument("--mode", choices=["backup", "bidirectional"], default="backup")
    connect.add_argument("--token-env", default=None)
    connect.add_argument("--store-keychain", action="store_true")
    connect.set_defaults(func=command_connect)

    status = sub.add_parser("status")
    status.set_defaults(func=command_status)
    mode = sub.add_parser("mode")
    mode.add_argument("mode", choices=["backup", "bidirectional"])
    mode.set_defaults(func=command_mode)
    offline = sub.add_parser("offline-write")
    offline.add_argument("--note", required=True, help="user-approved reason for writing while remote sync is unavailable")
    offline.set_defaults(func=command_offline_write)
    plan = sub.add_parser("plan")
    plan.set_defaults(func=lambda args: run_sync(args, apply=False))
    sync = sub.add_parser("sync")
    sync.set_defaults(func=lambda args: run_sync(args, apply=True))
    push = sub.add_parser("push")
    push.set_defaults(func=lambda args: run_sync(args, apply=True))
    pull = sub.add_parser("pull")
    pull.set_defaults(func=lambda args: run_sync(args, apply=True))

    restore = sub.add_parser("restore")
    restore.add_argument("--output", required=True)
    restore.add_argument("--version", choices=["current", "previous"], default="current")
    restore.add_argument("--provider", choices=["notion", "flowus"])
    restore.add_argument("--remote-root", help="remote Team Memory root page id when local connection config is lost")
    restore.add_argument("--token-env", default=None)
    restore.add_argument("--mode", choices=["backup", "bidirectional"], default="backup")
    restore.set_defaults(func=command_restore)
    disconnect = sub.add_parser("disconnect")
    disconnect.set_defaults(func=command_disconnect)

    conflicts = sub.add_parser("conflicts")
    conflict_sub = conflicts.add_subparsers(dest="conflict_command", required=True)
    conflict_sub.add_parser("list")
    show = conflict_sub.add_parser("show")
    show.add_argument("id")
    resolve = conflict_sub.add_parser("resolve")
    resolve.add_argument("id")
    resolve.add_argument("--use", choices=["local", "remote", "merged"], required=True)
    resolve.add_argument("--file", help="merged markdown file; required with --use merged")
    conflicts.set_defaults(func=command_conflicts)

    deletions = sub.add_parser("deletions")
    deletion_sub = deletions.add_subparsers(dest="deletion_command", required=True)
    deletion_sub.add_parser("list")
    for name in ["confirm", "restore"]:
        item = deletion_sub.add_parser(name)
        item.add_argument("id")
    deletions.set_defaults(func=command_deletions)

    schedule = sub.add_parser("schedule")
    schedule_sub = schedule.add_subparsers(dest="schedule_command", required=True)
    schedule_sub.add_parser("status")
    schedule_sub.add_parser("off")
    schedule_set = schedule_sub.add_parser("set")
    schedule_timing = schedule_set.add_mutually_exclusive_group(required=True)
    schedule_timing.add_argument("--every", choices=["15m", "1h", "24h"])
    schedule_timing.add_argument("--daily")
    schedule.set_defaults(func=command_schedule)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if getattr(args, "use", None) == "merged" and not getattr(args, "file", None):
        parser.error("conflicts resolve --use merged 需要 --file")
    try:
        lock_in_dispatch = args.command in {"connect", "mode", "offline-write", "disconnect"} or (
            args.command == "schedule" and args.schedule_command != "status"
        )
        if lock_in_dispatch:
            paths = resolve_team_paths(args.skill_dir)
            with LocalSyncLock(paths.data_dir):
                return int(args.func(args))
        return int(args.func(args))
    except (NotebookSyncError, ProviderError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
