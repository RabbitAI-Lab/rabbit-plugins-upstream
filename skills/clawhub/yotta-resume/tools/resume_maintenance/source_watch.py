#!/usr/bin/env python3
"""Local-first source snapshot comparison for yotta-resume."""

import copy
import datetime as dt
import hashlib
import json
import os
import re
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlsplit


SCHEMA_VERSION = "1.0"
SKILL_VERSION = "0.2.0"
MAX_SNAPSHOT_BYTES = 2 * 1024 * 1024
DEFAULT_TIMEOUT_SECONDS = 15
_HASH_RE = re.compile(r"^[a-f0-9]{64}$")
_CANDIDATE_FILES = (
    "source-registry.candidate.json",
    "source-watch-state.candidate.json",
    "diff.json",
    "review.md",
)


class SourceWatchError(Exception):
    """A controlled source snapshot or candidate failure."""

    def __init__(self, message, exit_code=7):
        super().__init__(message)
        self.exit_code = exit_code


def _read_json(path, label):
    try:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise SourceWatchError("{}不存在：{}".format(label, path), exit_code=3) from error
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise SourceWatchError("{}无法读取：{}".format(label, error), exit_code=5) from error
    if not isinstance(payload, dict):
        raise SourceWatchError("{}格式无效：根节点必须是对象。".format(label), exit_code=5)
    return payload


def _write_text_atomic(path, text):
    _write_bytes_atomic(path, text.encode("utf-8"))


def _replace_path(source, target, attempts=4):
    last_error = None
    for attempt in range(1, attempts + 1):
        try:
            os.replace(str(source), str(target))
            return
        except OSError as error:
            retryable = isinstance(error, PermissionError) or getattr(
                error,
                "winerror",
                None,
            ) in {5, 32}
            if not retryable or attempt == attempts:
                raise
            last_error = error
            time.sleep(0.05 * attempt)
    if last_error is not None:
        raise last_error


def _write_bytes_atomic(path, payload):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=str(path.parent),
            prefix=path.name + ".",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temp_path = Path(handle.name)
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        _replace_path(temp_path, path)
        temp_path = None
    finally:
        if temp_path is not None:
            try:
                temp_path.unlink()
            except OSError:
                pass


def _write_json_atomic(path, payload):
    _write_text_atomic(
        path,
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
    )


def _sha256_bytes(payload):
    return hashlib.sha256(payload).hexdigest()


def _sha256_text(text):
    return _sha256_bytes(text.encode("utf-8"))


def _sha256_file(path):
    return _sha256_bytes(Path(path).read_bytes())


def _canonical_hash(payload):
    canonical = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return _sha256_text(canonical)


def _parse_date(value, label):
    if not isinstance(value, str):
        raise SourceWatchError("{}必须是 ISO 日期。".format(label), exit_code=5)
    try:
        return dt.date.fromisoformat(value)
    except ValueError as error:
        raise SourceWatchError("{}不是有效日期：{}".format(label, value), exit_code=5) from error


def _data_dir(root):
    base = Path(root)
    if (base / "data" / "source-registry.json").is_file():
        return base / "data"
    return base


def _load_registry(data_dir):
    registry = _read_json(data_dir / "source-registry.json", "来源注册表")
    sources = registry.get("sources")
    if not isinstance(sources, list):
        raise SourceWatchError("来源注册表缺少 sources 数组。", exit_code=5)
    by_id = {}
    for source in sources:
        if not isinstance(source, dict):
            raise SourceWatchError("来源注册表包含非对象条目。", exit_code=5)
        source_id = source.get("source_id")
        if not isinstance(source_id, str) or not source_id:
            raise SourceWatchError("来源注册表包含缺少 source_id 的条目。", exit_code=5)
        if source_id in by_id:
            raise SourceWatchError("来源 ID 重复：{}".format(source_id), exit_code=5)
        url = source.get("url")
        if not isinstance(url, str) or not url.startswith("https://"):
            raise SourceWatchError(
                "来源 {} 的 URL 必须使用 HTTPS。".format(source_id),
                exit_code=5,
            )
        by_id[source_id] = source
    return registry, by_id


def _load_state(data_dir):
    path = data_dir / "source-watch-state.json"
    if not path.is_file():
        return {
            "schema_version": SCHEMA_VERSION,
            "contract_version": "1.0",
            "generated_at": None,
            "sources": [],
        }
    state = _read_json(path, "来源指纹状态")
    if not isinstance(state.get("sources"), list):
        raise SourceWatchError("来源指纹状态缺少 sources 数组。", exit_code=5)
    return state


def _validate_snapshot(payload, source, path):
    if not isinstance(payload, dict):
        raise SourceWatchError("快照必须是 JSON 对象：{}".format(path), exit_code=5)
    source_id = payload.get("source_id")
    if source_id != source.get("source_id"):
        raise SourceWatchError(
            "快照 source_id 与文件名或来源注册表不一致：{}".format(path),
            exit_code=5,
        )
    requested_url = payload.get("requested_url")
    final_url = payload.get("final_url")
    if requested_url != source.get("url"):
        raise SourceWatchError(
            "快照 requested_url 与来源注册表不一致：{}".format(source_id),
            exit_code=5,
        )
    if not isinstance(final_url, str) or not final_url.startswith("https://"):
        raise SourceWatchError(
            "快照 final_url 必须使用 HTTPS：{}".format(source_id),
            exit_code=5,
        )
    if urlsplit(final_url).hostname != urlsplit(requested_url).hostname:
        raise SourceWatchError(
            "快照发生跨 host 重定向，需要人工处理：{}".format(source_id),
            exit_code=5,
        )
    status = payload.get("http_status")
    if not isinstance(status, int) or isinstance(status, bool) or not 200 <= status < 300:
        raise SourceWatchError(
            "快照 HTTP 状态无效：{}".format(source_id),
            exit_code=5,
        )
    content_hash = payload.get("content_sha256")
    if not isinstance(content_hash, str) or not _HASH_RE.fullmatch(content_hash):
        raise SourceWatchError(
            "快照 content_sha256 无效：{}".format(source_id),
            exit_code=5,
        )
    content_length = payload.get("content_length")
    if (
        not isinstance(content_length, int)
        or isinstance(content_length, bool)
        or content_length < 0
        or content_length > MAX_SNAPSHOT_BYTES
    ):
        raise SourceWatchError(
            "快照 content_length 超出允许范围：{}".format(source_id),
            exit_code=5,
        )
    _parse_date(payload.get("fetched_at"), "快照 fetched_at")
    for field in ("etag", "last_modified"):
        value = payload.get(field)
        if value is not None and not isinstance(value, str):
            raise SourceWatchError(
                "快照 {} 必须是字符串或 null：{}".format(field, source_id),
                exit_code=5,
            )
    return {
        "schema_version": SCHEMA_VERSION,
        "source_id": source_id,
        "requested_url": requested_url,
        "final_url": final_url,
        "fetched_at": payload["fetched_at"],
        "http_status": status,
        "content_sha256": content_hash,
        "content_length": content_length,
        "etag": payload.get("etag"),
        "last_modified": payload.get("last_modified"),
    }


def load_snapshots(snapshot_dir, sources):
    directory = Path(snapshot_dir)
    if not directory.is_dir():
        raise SourceWatchError("快照目录不存在：{}".format(directory), exit_code=3)
    paths = sorted(directory.glob("*.json"))
    if not paths:
        raise SourceWatchError("快照目录中没有 JSON 文件。", exit_code=5)

    snapshots = {}
    for path in paths:
        payload = _read_json(path, "来源快照")
        source_id = payload.get("source_id")
        if not isinstance(source_id, str) or source_id not in sources:
            raise SourceWatchError(
                "快照引用了未登记来源：{}".format(path),
                exit_code=5,
            )
        if path.stem != source_id:
            raise SourceWatchError(
                "快照文件名必须与 source_id 一致：{}".format(path.name),
                exit_code=5,
            )
        if source_id in snapshots:
            raise SourceWatchError("来源快照重复：{}".format(source_id), exit_code=5)
        snapshots[source_id] = _validate_snapshot(
            payload,
            sources[source_id],
            path,
        )
    return snapshots


def _candidate_id(registry, state, snapshots):
    payload = {
        "registry": registry,
        "state": state,
        "snapshots": snapshots,
    }
    return "source-" + _canonical_hash(payload)[:16]


def _fetch_one(source, opener, today, timeout, max_bytes):
    url = source["url"]
    if not url.startswith("https://"):
        raise SourceWatchError(
            "来源 {} 必须使用 HTTPS。".format(source["source_id"]),
            exit_code=5,
        )
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "yotta-resume-source-watch/0.2.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.1",
        },
        method="GET",
    )
    try:
        with opener.open(request, timeout=timeout) as response:
            status = getattr(response, "status", 200)
            final_url = response.geturl()
            if not isinstance(final_url, str) or not final_url.startswith("https://"):
                raise SourceWatchError(
                    "来源 {} 重定向到非 HTTPS 地址。".format(source["source_id"]),
                    exit_code=7,
                )
            if urlsplit(final_url).hostname != urlsplit(url).hostname:
                raise SourceWatchError(
                    "来源 {} 发生跨 host 重定向，需要人工快照。".format(
                        source["source_id"]
                    ),
                    exit_code=7,
                )
            if not isinstance(status, int) or not 200 <= status < 300:
                raise SourceWatchError(
                    "来源 {} 返回 HTTP {}。".format(source["source_id"], status),
                    exit_code=7,
                )
            headers = response.headers
            declared_length = headers.get("Content-Length")
            if declared_length:
                try:
                    if int(declared_length) > max_bytes:
                        raise SourceWatchError(
                            "来源 {} 声明内容超过上限。".format(source["source_id"]),
                            exit_code=7,
                        )
                except ValueError:
                    pass
            payload = response.read(max_bytes + 1)
    except SourceWatchError:
        raise
    except urllib.error.HTTPError as error:
        raise SourceWatchError(
            "来源 {} 返回 HTTP {}。".format(source["source_id"], error.code),
            exit_code=7,
        ) from error
    except (urllib.error.URLError, OSError, ValueError) as error:
        raise SourceWatchError(
            "来源 {} 抓取失败：{}".format(source["source_id"], error),
            exit_code=7,
        ) from error

    if not isinstance(payload, (bytes, bytearray)):
        raise SourceWatchError("来源响应不是字节数据。", exit_code=7)
    if len(payload) > max_bytes:
        raise SourceWatchError(
            "来源 {} 内容超过 {} 字节上限。".format(source["source_id"], max_bytes),
            exit_code=7,
        )
    return {
        "schema_version": SCHEMA_VERSION,
        "source_id": source["source_id"],
        "requested_url": url,
        "final_url": final_url,
        "fetched_at": today,
        "http_status": status,
        "content_sha256": _sha256_bytes(bytes(payload)),
        "content_length": len(payload),
        "etag": headers.get("ETag"),
        "last_modified": headers.get("Last-Modified"),
    }


def fetch_sources(
    data_root,
    out_dir,
    source_ids=None,
    today=None,
    timeout=DEFAULT_TIMEOUT_SECONDS,
    max_bytes=MAX_SNAPSHOT_BYTES,
    opener=None,
):
    current = str(today or dt.date.today().isoformat())
    _parse_date(current, "today")
    if not isinstance(timeout, (int, float)) or isinstance(timeout, bool) or timeout <= 0:
        raise SourceWatchError("timeout 必须是正数。", exit_code=5)
    if not isinstance(max_bytes, int) or isinstance(max_bytes, bool) or max_bytes < 1:
        raise SourceWatchError("max_bytes 必须是正整数。", exit_code=5)
    data_dir = _data_dir(data_root)
    _, sources = _load_registry(data_dir)
    selected = (
        [
            source_id
            for source_id, source in sources.items()
            if source.get("status") == "active"
        ]
        if source_ids is None
        else list(source_ids)
    )
    if not selected:
        raise SourceWatchError("至少选择一个来源。", exit_code=5)
    unknown = [item for item in selected if item not in sources]
    if unknown:
        raise SourceWatchError(
            "未登记来源：{}".format(", ".join(unknown)),
            exit_code=5,
        )
    selected = list(dict.fromkeys(selected))
    opener = opener or urllib.request.build_opener()

    snapshots = {}
    for source_id in selected:
        snapshots[source_id] = _fetch_one(
            sources[source_id],
            opener,
            current,
            timeout,
            max_bytes,
        )

    target = Path(out_dir)
    if target.exists():
        raise SourceWatchError(
            "快照输出目录已存在：{}".format(target),
            exit_code=7,
        )
    target.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=".source-snapshots-", dir=str(target.parent)))
    try:
        for source_id, snapshot in snapshots.items():
            _write_json_atomic(stage / "{}.json".format(source_id), snapshot)
        _replace_path(stage, target)
    except Exception:
        import shutil

        shutil.rmtree(str(stage), ignore_errors=True)
        raise
    return {
        "ok": True,
        "snapshot_dir": str(target),
        "source_count": len(snapshots),
        "source_ids": selected,
    }


def _manifest(candidate_id, created_at, files, diff):
    file_records = []
    for name in files:
        path = Path(files[name])
        file_records.append({
            "path": name,
            "size": path.stat().st_size,
            "sha256": _sha256_file(path),
        })
    return {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": candidate_id,
        "created_at": created_at,
        "base_skill_version": SKILL_VERSION,
        "target_skill_version": SKILL_VERSION,
        "base_bank_version": None,
        "target_bank_version": None,
        "source_ids": [item["source_id"] for item in diff["sources"]],
        "source_change_count": len(diff["sources"]),
        "question_change_count": len(diff["questions"]),
        "files": sorted(file_records, key=lambda item: item["path"]),
    }


def _render_review_markdown(registry, diff):
    lines = [
        "# 元简来源更新候选复核",
        "",
        "候选生成日期：{}".format(registry["generated_at"]),
        "",
        "## 来源变化",
        "",
    ]
    if not diff["sources"]:
        lines.append("- 无来源内容变化。")
    for item in diff["sources"]:
        lines.append(
            "- `{}`：{}，检查日期 {}。".format(
                item["source_id"],
                item["change_type"],
                item["current"]["checked_at"],
            )
        )
    lines.extend([
        "",
        "## 人工复核硬闸门",
        "",
        "- [ ] 来源事实已核对",
        "- [ ] 岗位族和职级适配已核对",
        "- [ ] 答案边界和安全表述已核对",
        "- [ ] 来源许可、引用方式和允许使用范围已核对",
        "",
        "本候选未修改正式题库，应用前必须运行 `bank validate`。",
        "",
    ])
    return "\n".join(lines)


def _commit_candidate(out_dir, writer):
    out_dir = Path(out_dir)
    if out_dir.exists():
        raise SourceWatchError(
            "候选目录已存在，请先检查或更换路径：{}".format(out_dir),
            exit_code=7,
        )
    out_dir.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=".source-candidate-", dir=str(out_dir.parent)))
    try:
        report = writer(stage)
        _replace_path(stage, out_dir)
        return report
    except Exception:
        shutil = __import__("shutil")
        shutil.rmtree(str(stage), ignore_errors=True)
        raise


def check_sources(data_root, snapshot_dir, out_dir, today=None):
    created_at = str(today or dt.date.today().isoformat())
    _parse_date(created_at, "today")
    data_dir = _data_dir(data_root)
    registry, sources = _load_registry(data_dir)
    state = _load_state(data_dir)
    snapshots = load_snapshots(snapshot_dir, sources)

    state_by_id = {
        item.get("source_id"): item
        for item in state.get("sources", [])
        if isinstance(item, dict) and item.get("source_id")
    }
    changes = []
    for source_id, snapshot in snapshots.items():
        previous = state_by_id.get(source_id)
        if previous is None:
            change_type = "baseline"
        else:
            fingerprint_changed = any(
                previous.get(field) != snapshot.get(field)
                for field in ("content_sha256", "etag", "last_modified")
            )
            verified_changed = (
                sources[source_id].get("last_verified_at") != snapshot["fetched_at"]
            )
            if fingerprint_changed:
                change_type = "updated"
            elif verified_changed:
                change_type = "verified"
            else:
                continue
        changes.append({
            "source_id": source_id,
            "change_type": change_type,
            "previous": previous,
            "current": {
                "content_sha256": snapshot["content_sha256"],
                "etag": snapshot["etag"],
                "last_modified": snapshot["last_modified"],
                "checked_at": snapshot["fetched_at"],
            },
        })

    if not changes:
        return {
            "ok": True,
            "changed": False,
            "candidate": None,
            "source_change_count": 0,
            "question_change_count": 0,
        }

    candidate_registry = copy.deepcopy(registry)
    candidate_registry["generated_at"] = created_at
    for item in candidate_registry["sources"]:
        snapshot = snapshots.get(item.get("source_id"))
        if snapshot is not None:
            item["retrieved_at"] = snapshot["fetched_at"]
            item["last_verified_at"] = snapshot["fetched_at"]

    candidate_state = copy.deepcopy(state)
    candidate_state["generated_at"] = created_at
    updated_sources = []
    by_id = {item.get("source_id"): copy.deepcopy(item) for item in state["sources"]}
    for source_id in sources:
        snapshot = snapshots.get(source_id)
        if snapshot is None:
            if source_id in by_id:
                updated_sources.append(by_id[source_id])
            continue
        updated_sources.append({
            "source_id": source_id,
            "content_sha256": snapshot["content_sha256"],
            "etag": snapshot["etag"],
            "last_modified": snapshot["last_modified"],
            "checked_at": snapshot["fetched_at"],
        })
    candidate_state["sources"] = updated_sources

    diff = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": created_at,
        "sources": changes,
        "questions": [],
        "risks": [],
    }
    candidate_id = _candidate_id(registry, state, snapshots)

    def writer(stage):
        paths = {
            "source-registry.candidate.json": stage / "source-registry.candidate.json",
            "source-watch-state.candidate.json": stage / "source-watch-state.candidate.json",
            "diff.json": stage / "diff.json",
            "review.md": stage / "review.md",
        }
        _write_json_atomic(paths["source-registry.candidate.json"], candidate_registry)
        _write_json_atomic(paths["source-watch-state.candidate.json"], candidate_state)
        _write_json_atomic(paths["diff.json"], diff)
        _write_text_atomic(
            paths["review.md"],
            _render_review_markdown(candidate_registry, diff),
        )
        manifest = _manifest(
            candidate_id,
            created_at,
            paths,
            diff,
        )
        _write_json_atomic(stage / "manifest.json", manifest)
        return {
            "ok": True,
            "changed": True,
            "candidate": str(out_dir),
            "candidate_id": candidate_id,
            "source_change_count": len(changes),
            "question_change_count": 0,
        }

    return _commit_candidate(out_dir, writer)

