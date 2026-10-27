from __future__ import annotations

import json
import hashlib
import os
import random
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import Any, Callable

from notebook_sync_core import NotebookSyncError, normalize_markdown


NOTION_API_VERSION = "2026-03-11"
FLOWUS_API_VERSION = "v2"


class ProviderError(NotebookSyncError):
    def __init__(self, message: str, status: int | None = None, code: str | None = None):
        super().__init__(message)
        self.status = status
        self.code = code


@dataclass
class RemotePage:
    page_id: str
    markdown: str
    etag: str | None = None
    last_edited_time: str | None = None
    truncated: bool = False
    unknown_block_ids: list[str] | None = None


@dataclass
class Lease:
    page_id: str
    lease_id: str
    owner: str
    expires_at: str
    compare_token: str | None = None
    raw_content: str | None = None


class LeaseGuard:
    """Renew a lease from the provider's serial request checkpoints."""

    def __init__(self, provider: "HttpProvider", lease: Lease, renew_every: float = 30.0):
        self.provider = provider
        self.lease = lease
        self.renew_every = renew_every
        self.last_renewed = time.monotonic()

    def checkpoint(self, force: bool = False) -> None:
        now = time.monotonic()
        if not force and now - self.last_renewed < self.renew_every:
            return
        self.provider.renew_lease(self.lease)
        self.last_renewed = time.monotonic()


def _parse_json_body(raw: bytes) -> dict[str, Any]:
    if not raw:
        return {}
    try:
        payload = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ProviderError(f"在线笔记返回了无法解析的 JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise ProviderError("在线笔记返回的 JSON 顶层不是对象。")
    return payload


def _markdown_digest(markdown: str) -> str:
    return hashlib.sha256(normalize_markdown(markdown).encode("utf-8")).hexdigest()


def keychain_token(service: str, account: str) -> str:
    try:
        result = subprocess.run(
            ["security", "find-generic-password", "-s", service, "-a", account, "-w"],
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError as exc:
        raise ProviderError("当前系统没有 macOS security 命令，无法读取钥匙串凭据。") from exc
    if result.returncode != 0 or not result.stdout.strip():
        raise ProviderError(f"无法从 macOS 钥匙串读取凭据: service={service}, account={account}")
    return result.stdout.strip()


def resolve_token(config: dict[str, Any]) -> str:
    credential = config.get("credential") or {}
    kind = credential.get("type", "env")
    if kind == "env":
        name = credential.get("name")
        token = os.environ.get(str(name), "")
        if not token:
            raise ProviderError(f"缺少环境变量凭据: {name}")
        return token
    if kind == "keychain":
        return keychain_token(str(credential.get("service")), str(credential.get("account")))
    raise ProviderError(f"不支持的凭据类型: {kind}")


def store_keychain_token(service: str, account: str, token: str) -> None:
    try:
        result = subprocess.run(
            ["security", "add-generic-password", "-U", "-s", service, "-a", account, "-w", token],
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError as exc:
        raise ProviderError("当前系统没有 macOS security 命令，无法写入钥匙串凭据。") from exc
    if result.returncode != 0:
        raise ProviderError(f"写入 macOS 钥匙串失败: {result.stderr.strip()}")


class HttpProvider:
    base_url = ""
    min_interval = 0.0

    def __init__(self, token: str):
        self.token = token
        self._last_request_at = 0.0
        self._request_guard: Callable[[], None] | None = None
        self._inside_request_guard = False

    def set_request_guard(self, guard: Callable[[], None] | None) -> None:
        self._request_guard = guard

    def _checkpoint(self) -> None:
        if self._request_guard is None or self._inside_request_guard:
            return
        self._inside_request_guard = True
        try:
            self._request_guard()
        finally:
            self._inside_request_guard = False

    def _guarded_sleep(self, seconds: float) -> None:
        remaining = max(0.0, seconds)
        while remaining > 0:
            interval = min(remaining, 5.0)
            time.sleep(interval)
            remaining -= interval
            self._checkpoint()

    def headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}

    def _request(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
        extra_headers: dict[str, str] | None = None,
        max_attempts: int = 6,
        safe_to_retry: bool | None = None,
    ) -> tuple[dict[str, Any], dict[str, str]]:
        url = path if path.startswith("https://") else f"{self.base_url}{path}"
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8") if payload is not None else None
        headers = self.headers()
        if extra_headers:
            headers.update(extra_headers)
        safe = method.upper() == "GET" if safe_to_retry is None else safe_to_retry

        for attempt in range(max_attempts):
            self._checkpoint()
            wait = self.min_interval - (time.monotonic() - self._last_request_at)
            if wait > 0:
                self._guarded_sleep(wait)
            request = urllib.request.Request(url, data=body, headers=headers, method=method.upper())
            try:
                with urllib.request.urlopen(request, timeout=45) as response:
                    self._last_request_at = time.monotonic()
                    response_headers = {key.lower(): value for key, value in response.headers.items()}
                    result = _parse_json_body(response.read())
                    self._checkpoint()
                    return result, response_headers
            except urllib.error.HTTPError as exc:
                self._last_request_at = time.monotonic()
                raw = exc.read()
                try:
                    error = _parse_json_body(raw)
                except ProviderError:
                    error = {}
                code = str(error.get("code") or error.get("error") or "") or None
                message = str(error.get("message") or error.get("error_description") or exc.reason)
                retryable = exc.code == 429 or (safe and exc.code in {500, 502, 503, 504, 529})
                if retryable and attempt < max_attempts - 1:
                    retry_after = exc.headers.get("Retry-After")
                    delay = float(retry_after) if retry_after and retry_after.isdigit() else min(2**attempt, 30)
                    self._guarded_sleep(delay + random.uniform(0, 0.25))
                    continue
                raise ProviderError(f"在线笔记 API 请求失败 ({exc.code} {code or ''}): {message}", exc.code, code) from exc
            except urllib.error.URLError as exc:
                if safe and attempt < max_attempts - 1:
                    self._guarded_sleep(min(2**attempt, 15) + random.uniform(0, 0.25))
                    continue
                raise ProviderError(f"无法连接在线笔记 API: {exc.reason}") from exc
        raise ProviderError("在线笔记 API 请求重试耗尽。")

    def verify(self) -> dict[str, Any]:
        raise NotImplementedError

    def create_page(
        self,
        parent_id: str,
        title: str,
        markdown: str,
        on_created: Callable[[str], None] | None = None,
    ) -> str:
        raise NotImplementedError

    def read_page(self, page_id: str) -> RemotePage:
        raise NotImplementedError

    def replace_page(self, page_id: str, markdown: str) -> RemotePage:
        raise NotImplementedError

    def list_child_pages(self, parent_id: str) -> dict[str, str]:
        raise NotImplementedError

    def archive_page(self, page_id: str) -> None:
        raise NotImplementedError

    def restore_page(self, page_id: str) -> None:
        raise NotImplementedError

    def acquire_lease(self, page_id: str, owner: str, lease_seconds: int = 120) -> Lease:
        raise NotImplementedError

    def renew_lease(self, lease: Lease, lease_seconds: int = 120) -> Lease:
        raise NotImplementedError

    def release_lease(self, lease: Lease) -> None:
        raise NotImplementedError


def _iso_after(seconds: int) -> str:
    return (datetime.now(UTC) + timedelta(seconds=seconds)).isoformat(timespec="seconds").replace("+00:00", "Z")


def _is_expired(raw: str | None) -> bool:
    if not raw:
        return True
    try:
        parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return True
    return parsed <= datetime.now(UTC)


class NotionProvider(HttpProvider):
    base_url = "https://api.notion.com"
    min_interval = 0.36

    def headers(self) -> dict[str, str]:
        headers = super().headers()
        headers["Notion-Version"] = NOTION_API_VERSION
        return headers

    def verify(self) -> dict[str, Any]:
        payload, _ = self._request("GET", "/v1/users/me")
        return payload

    def create_page(
        self,
        parent_id: str,
        title: str,
        markdown: str,
        on_created: Callable[[str], None] | None = None,
    ) -> str:
        payload = {
            "parent": {"page_id": parent_id},
            "properties": {"title": {"title": [{"type": "text", "text": {"content": title}}]}},
            "markdown": normalize_markdown(markdown),
        }
        try:
            result, _ = self._request("POST", "/v1/pages", payload, safe_to_retry=False)
        except ProviderError as exc:
            if exc.status not in {None, 500, 502, 503, 504, 529}:
                raise
            try:
                existing = self.list_child_pages(parent_id).get(title)
            except ProviderError:
                raise exc
            if existing:
                page = self.read_page(existing)
                if not page.truncated and not page.unknown_block_ids and _markdown_digest(page.markdown) == _markdown_digest(markdown):
                    if on_created:
                        on_created(str(existing))
                    return existing
                raise ProviderError("同名 Notion 页面与本次创建内容不匹配，拒绝误认领。") from exc
            raise
        page_id = result.get("id")
        if not page_id:
            raise ProviderError("Notion 创建页面成功但没有返回页面 ID。")
        if on_created:
            on_created(str(page_id))
        return str(page_id)

    def read_page(self, page_id: str) -> RemotePage:
        markdown_result, _ = self._request("GET", f"/v1/pages/{page_id}/markdown")
        metadata, _ = self._request("GET", f"/v1/pages/{page_id}")
        return RemotePage(
            page_id=page_id,
            markdown=normalize_markdown(str(markdown_result.get("markdown", ""))),
            last_edited_time=metadata.get("last_edited_time"),
            truncated=bool(markdown_result.get("truncated")),
            unknown_block_ids=[str(item) for item in markdown_result.get("unknown_block_ids", [])],
        )

    def replace_page(self, page_id: str, markdown: str) -> RemotePage:
        payload = {"type": "replace_content", "replace_content": {"new_str": normalize_markdown(markdown)}}
        result, _ = self._request("PATCH", f"/v1/pages/{page_id}/markdown", payload, safe_to_retry=True)
        return RemotePage(
            page_id=page_id,
            markdown=normalize_markdown(str(result.get("markdown", markdown))),
            truncated=bool(result.get("truncated")),
            unknown_block_ids=[str(item) for item in result.get("unknown_block_ids", [])],
        )

    def list_child_pages(self, parent_id: str) -> dict[str, str]:
        pages: dict[str, str] = {}
        cursor: str | None = None
        while True:
            query = "?page_size=100"
            if cursor:
                query += "&start_cursor=" + urllib.parse.quote(cursor)
            payload, _ = self._request("GET", f"/v1/blocks/{parent_id}/children{query}")
            for item in payload.get("results", []):
                if not isinstance(item, dict) or item.get("type") != "child_page":
                    continue
                title = str(item.get("child_page", {}).get("title") or "")
                page_id = item.get("id")
                if title and page_id:
                    pages[title] = str(page_id)
            if not payload.get("has_more"):
                break
            cursor = payload.get("next_cursor")
            if not cursor:
                break
        return pages

    def archive_page(self, page_id: str) -> None:
        self._request("PATCH", f"/v1/pages/{page_id}", {"in_trash": True}, safe_to_retry=True)

    def restore_page(self, page_id: str) -> None:
        self._request("PATCH", f"/v1/pages/{page_id}", {"in_trash": False}, safe_to_retry=True)

    @staticmethod
    def _lock_markdown(owner: str | None, lease_id: str | None, expires_at: str | None) -> str:
        payload = {"kind": "team-memory-lease-v1", "owner": owner, "lease-id": lease_id, "expires-at": expires_at}
        return normalize_markdown("# Team Memory 同步锁\n\n```json\n" + json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n```\n")

    @staticmethod
    def _parse_lock(markdown: str) -> dict[str, Any]:
        match = re.search(r"```json\s*\n(.*?)\n```", markdown, flags=re.DOTALL)
        if not match:
            return {}
        try:
            payload = json.loads(match.group(1))
        except json.JSONDecodeError:
            return {}
        return payload if isinstance(payload, dict) else {}

    def _cas_lock(self, page_id: str, old: str, new: str) -> str:
        payload = {
            "type": "update_content",
            "update_content": {"content_updates": [{"old_str": old.rstrip("\n"), "new_str": new.rstrip("\n")}]},
        }
        result, _ = self._request("PATCH", f"/v1/pages/{page_id}/markdown", payload)
        return normalize_markdown(str(result.get("markdown", new)))

    def acquire_lease(self, page_id: str, owner: str, lease_seconds: int = 120) -> Lease:
        current = self.read_page(page_id).markdown
        record = self._parse_lock(current)
        if record.get("lease-id") and not _is_expired(record.get("expires-at")):
            raise ProviderError(f"远端同步锁正由 {record.get('owner')} 持有，至 {record.get('expires-at')}。", 409, "lease_busy")
        lease_id = str(uuid.uuid4())
        expires = _iso_after(lease_seconds)
        new = self._lock_markdown(owner, lease_id, expires)
        self._cas_lock(page_id, current, new)
        stored = self.read_page(page_id).markdown
        confirmed = self._parse_lock(stored)
        if confirmed.get("lease-id") != lease_id or confirmed.get("owner") != owner:
            raise ProviderError("Notion 远端租约写后确认失败。", 409, "lease_lost")
        return Lease(page_id, lease_id, owner, expires, raw_content=stored)

    def renew_lease(self, lease: Lease, lease_seconds: int = 120) -> Lease:
        current = self.read_page(lease.page_id).markdown
        record = self._parse_lock(current)
        if record.get("lease-id") != lease.lease_id:
            raise ProviderError("远端同步锁已被其他写入者接管。", 409, "lease_lost")
        expires = _iso_after(lease_seconds)
        self._cas_lock(lease.page_id, current, self._lock_markdown(lease.owner, lease.lease_id, expires))
        stored = self.read_page(lease.page_id).markdown
        confirmed = self._parse_lock(stored)
        if confirmed.get("lease-id") != lease.lease_id or confirmed.get("owner") != lease.owner:
            raise ProviderError("Notion 远端租约续期确认失败。", 409, "lease_lost")
        lease.expires_at = expires
        lease.raw_content = stored
        return lease

    def release_lease(self, lease: Lease) -> None:
        current = self.read_page(lease.page_id).markdown
        record = self._parse_lock(current)
        if record.get("lease-id") == lease.lease_id:
            self._cas_lock(lease.page_id, current, self._lock_markdown(None, None, None))


def _plain_text(rich_text: list[dict[str, Any]]) -> str:
    return "".join(str(item.get("plain_text") or item.get("text", {}).get("content") or "") for item in rich_text)


def _flowus_title(page: dict[str, Any]) -> str:
    properties = page.get("properties") or {}
    title = properties.get("title") or properties.get("Name") or {}
    items = title.get("title") or []
    return _plain_text(items)


INLINE_MARKDOWN_RE = re.compile(r"(\*\*[^*\n]+\*\*|`[^`\n]+`|\[[^\]\n]+\]\(https?://[^)\n]+\)|(?<!\*)\*[^*\n]+\*(?!\*))")


def _text_chunks(
    content: str,
    *,
    bold: bool = False,
    italic: bool = False,
    code: bool = False,
    url: str | None = None,
) -> list[dict[str, Any]]:
    chunks = [content[idx : idx + 1900] for idx in range(0, len(content), 1900)] or [""]
    result: list[dict[str, Any]] = []
    for chunk in chunks:
        text: dict[str, Any] = {"content": chunk}
        if url:
            text["link"] = {"url": url}
        item: dict[str, Any] = {"type": "text", "text": text}
        if bold or italic or code:
            item["annotations"] = {
                "bold": bold,
                "italic": italic,
                "strikethrough": False,
                "underline": False,
                "code": code,
                "color": "default",
            }
        result.append(item)
    return result


def _rich_text(content: str) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    cursor = 0
    for match in INLINE_MARKDOWN_RE.finditer(content):
        if match.start() > cursor:
            result.extend(_text_chunks(content[cursor : match.start()]))
        token = match.group(0)
        if token.startswith("**"):
            result.extend(_text_chunks(token[2:-2], bold=True))
        elif token.startswith("`"):
            result.extend(_text_chunks(token[1:-1], code=True))
        elif token.startswith("["):
            label, url = re.match(r"^\[([^]]+)\]\((https?://[^)]+)\)$", token).groups()  # type: ignore[union-attr]
            result.extend(_text_chunks(label, url=url))
        else:
            result.extend(_text_chunks(token[1:-1], italic=True))
        cursor = match.end()
    if cursor < len(content):
        result.extend(_text_chunks(content[cursor:]))
    return result or _text_chunks("")


def _table_cells(line: str) -> list[str]:
    stripped = line.strip().strip("|")
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", stripped)]


def markdown_to_flowus_blocks(markdown: str) -> list[dict[str, Any]]:
    lines = normalize_markdown(markdown).splitlines()
    blocks: list[dict[str, Any]] = []
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if (
            "|" in line
            and idx + 1 < len(lines)
            and re.match(r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$", lines[idx + 1])
        ):
            rows = [_table_cells(line)]
            idx += 2
            while idx < len(lines) and "|" in lines[idx] and lines[idx].strip():
                rows.append(_table_cells(lines[idx]))
                idx += 1
            width = max(len(row) for row in rows)
            table_rows = []
            for row in rows:
                cells = [_rich_text(cell) for cell in row + [""] * (width - len(row))]
                table_rows.append({"object": "block", "type": "table_row", "table_row": {"cells": cells}})
            blocks.append(
                {
                    "object": "block",
                    "type": "table",
                    "table": {
                        "table_width": width,
                        "has_column_header": True,
                        "has_row_header": False,
                        "children": table_rows,
                    },
                }
            )
            continue
        if fence_match := re.match(r"^(`{3,})([^`]*)$", line):
            fence = fence_match.group(1)
            language = fence_match.group(2).strip() or "plain text"
            body: list[str] = []
            idx += 1
            while idx < len(lines) and not re.match(r"^`{" + str(len(fence)) + r",}\s*$", lines[idx]):
                body.append(lines[idx])
                idx += 1
            blocks.append({"object": "block", "type": "code", "code": {"rich_text": _text_chunks("\n".join(body)), "language": language}})
        elif match := re.match(r"^(#{1,3})\s+(.*)$", line):
            kind = f"heading_{len(match.group(1))}"
            blocks.append({"object": "block", "type": kind, kind: {"rich_text": _rich_text(match.group(2))}})
        elif match := re.match(r"^- \[([ xX])\]\s+(.*)$", line):
            blocks.append({"object": "block", "type": "to_do", "to_do": {"rich_text": _rich_text(match.group(2)), "checked": match.group(1).lower() == "x"}})
        elif match := re.match(r"^[-*]\s+(.*)$", line):
            blocks.append({"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": _rich_text(match.group(1))}})
        elif match := re.match(r"^\d+[.)]\s+(.*)$", line):
            blocks.append({"object": "block", "type": "numbered_list_item", "numbered_list_item": {"rich_text": _rich_text(match.group(1))}})
        elif line.startswith("> "):
            blocks.append({"object": "block", "type": "quote", "quote": {"rich_text": _rich_text(line[2:])}})
        elif re.match(r"^---+$", line):
            blocks.append({"object": "block", "type": "divider", "divider": {}})
        else:
            blocks.append({"object": "block", "type": "paragraph", "paragraph": {"rich_text": _rich_text(line)}})
        idx += 1
    return blocks


class FlowUsProvider(HttpProvider):
    base_url = "https://api.flowus.cn"
    min_interval = 0.55

    def verify(self) -> dict[str, Any]:
        try:
            payload, _ = self._request("GET", "/v2/users/me")
        except ProviderError as exc:
            if exc.status == 403:
                raise ProviderError("FlowUs V2 API 拒绝访问：请确认空间不是免费版，并检查 pages/blocks scopes。", exc.status, exc.code) from exc
            raise
        return payload

    def create_page(
        self,
        parent_id: str,
        title: str,
        markdown: str,
        on_created: Callable[[str], None] | None = None,
    ) -> str:
        blocks = markdown_to_flowus_blocks(markdown)
        first, rest = blocks[:100], blocks[100:]
        payload = {
            "parent": {"page_id": parent_id},
            "properties": {"title": {"type": "title", "title": [{"type": "text", "text": {"content": title}}]}},
            "children": first,
        }
        result, _ = self._request(
            "POST",
            "/v2/pages",
            payload,
            {"Idempotency-Key": str(uuid.uuid4())},
            safe_to_retry=True,
        )
        page_id = result.get("id")
        if not page_id:
            raise ProviderError("FlowUs 创建页面成功但没有返回页面 ID。")
        if on_created:
            on_created(str(page_id))
        page: dict[str, Any] = {}
        etag: str | None = None
        if rest:
            page, etag = self._page_metadata(str(page_id))
            etag = self._cas_page(str(page_id), page, etag)
        for idx in range(0, len(rest), 100):
            self._request(
                "PATCH",
                f"/v2/blocks/{page_id}/children",
                {"children": rest[idx : idx + 100]},
                safe_to_retry=False,
            )
            if idx + 100 < len(rest):
                page, etag = self._page_metadata(str(page_id))
                etag = self._cas_page(str(page_id), page, etag)
        return str(page_id)

    def _page_metadata(self, page_id: str) -> tuple[dict[str, Any], str | None]:
        payload, headers = self._request("GET", f"/v2/pages/{page_id}")
        return payload, headers.get("etag")

    def _cas_page(self, page_id: str, page: dict[str, Any], etag: str | None) -> str:
        if not etag:
            raise ProviderError("FlowUs 页面未返回 ETag，拒绝执行非条件写入。", 409, "etag_required")
        _, headers = self._request(
            "PATCH",
            f"/v2/pages/{page_id}",
            {"in_trash": bool(page.get("in_trash", False))},
            {"If-Match": etag},
            safe_to_retry=False,
        )
        if headers.get("etag"):
            return str(headers["etag"])
        _, confirmed_etag = self._page_metadata(page_id)
        if not confirmed_etag:
            raise ProviderError("FlowUs 页面 CAS 成功后仍缺少 ETag。", 409, "etag_required")
        return confirmed_etag

    def read_page(self, page_id: str) -> RemotePage:
        result, _ = self._request("GET", f"/v2/pages/{page_id}/content/markdown")
        metadata, etag = self._page_metadata(page_id)
        supported = {
            "paragraph",
            "heading_1",
            "heading_2",
            "heading_3",
            "bulleted_list_item",
            "numbered_list_item",
            "to_do",
            "quote",
            "divider",
            "code",
            "table",
            "table_row",
            "child_page",
            "child_database",
        }
        unknown = [str(item.get("id")) for item in self._children(page_id) if item.get("type") not in supported]
        return RemotePage(
            page_id=page_id,
            markdown=normalize_markdown(str(result.get("markdown") or result.get("content") or "")),
            etag=etag,
            last_edited_time=metadata.get("last_edited_time"),
            unknown_block_ids=unknown,
        )

    def _children(self, page_id: str) -> list[dict[str, Any]]:
        results: list[dict[str, Any]] = []
        cursor: str | None = None
        while True:
            query = "?page_size=100"
            if cursor:
                query += "&start_cursor=" + urllib.parse.quote(cursor)
            payload, _ = self._request("GET", f"/v2/blocks/{page_id}/children{query}")
            results.extend(item for item in payload.get("results", []) if isinstance(item, dict))
            if not payload.get("has_more"):
                break
            cursor = payload.get("next_cursor")
            if not cursor:
                break
        return results

    def replace_page(self, page_id: str, markdown: str) -> RemotePage:
        initial_page, initial_etag = self._page_metadata(page_id)
        if not initial_etag:
            raise ProviderError("FlowUs 页面未返回 ETag，拒绝整页替换。", 409, "etag_required")
        children = self._children(page_id)
        observed_page, observed_etag = self._page_metadata(page_id)
        if not observed_etag or initial_etag != observed_etag:
            raise ProviderError("FlowUs 页面在读取分块期间已变化，拒绝覆盖。", 409, "etag_changed")
        etag = self._cas_page(page_id, observed_page or initial_page, observed_etag)
        protected = [item for item in children if item.get("type") in {"child_page", "child_database"}]
        if protected:
            raise ProviderError("FlowUs 页面包含子页面或子数据库，拒绝整页替换。")
        for item in children:
            block_id = item.get("id")
            if block_id:
                self._request("DELETE", f"/v2/blocks/{block_id}")
                page, etag = self._page_metadata(page_id)
                etag = self._cas_page(page_id, page, etag)
        blocks = markdown_to_flowus_blocks(markdown)
        for idx in range(0, len(blocks), 100):
            self._request(
                "PATCH",
                f"/v2/blocks/{page_id}/children",
                {"children": blocks[idx : idx + 100]},
                safe_to_retry=False,
            )
            if idx + 100 < len(blocks):
                page, etag = self._page_metadata(page_id)
                etag = self._cas_page(page_id, page, etag)
        return self.read_page(page_id)

    def list_child_pages(self, parent_id: str) -> dict[str, str]:
        pages: dict[str, str] = {}
        for item in self._children(parent_id):
            if item.get("type") != "child_page":
                continue
            title = str(item.get("child_page", {}).get("title") or item.get("title") or "")
            page_id = item.get("id")
            if title and page_id:
                pages[title] = str(page_id)
        return pages

    def archive_page(self, page_id: str) -> None:
        page, etag = self._page_metadata(page_id)
        if not etag:
            raise ProviderError("FlowUs 页面未返回 ETag，拒绝归档。", 409, "etag_required")
        self._request("PATCH", f"/v2/pages/{page_id}", {"in_trash": True}, {"If-Match": etag}, safe_to_retry=True)

    def restore_page(self, page_id: str) -> None:
        page, etag = self._page_metadata(page_id)
        if not etag:
            raise ProviderError("FlowUs 页面未返回 ETag，拒绝恢复。", 409, "etag_required")
        self._request("PATCH", f"/v2/pages/{page_id}", {"in_trash": False}, {"If-Match": etag}, safe_to_retry=True)

    @staticmethod
    def _lease_title(owner: str | None, lease_id: str | None, expires_at: str | None) -> str:
        if not lease_id:
            return "90 系统锁 · 空闲"
        return f"90 系统锁 · {owner} · {expires_at} · {lease_id}"

    @staticmethod
    def _parse_lease_title(title: str) -> dict[str, str | None]:
        if title.endswith("· 空闲"):
            return {"owner": None, "expires-at": None, "lease-id": None}
        parts = [part.strip() for part in title.split("·")]
        if len(parts) < 4:
            return {"owner": None, "expires-at": None, "lease-id": None}
        return {"owner": parts[-3], "expires-at": parts[-2], "lease-id": parts[-1]}

    def _set_title(self, page_id: str, title: str, etag: str | None) -> str | None:
        if not etag:
            raise ProviderError("FlowUs 页面未返回 ETag，无法安全执行乐观锁写入。", 409, "etag_required")
        headers = {"If-Match": etag}
        payload = {"properties": {"title": {"type": "title", "title": [{"type": "text", "text": {"content": title}}]}}}
        _, response_headers = self._request("PATCH", f"/v2/pages/{page_id}", payload, headers)
        return response_headers.get("etag")

    def acquire_lease(self, page_id: str, owner: str, lease_seconds: int = 120) -> Lease:
        page, etag = self._page_metadata(page_id)
        current = self._parse_lease_title(_flowus_title(page))
        if current.get("lease-id") and not _is_expired(current.get("expires-at")):
            raise ProviderError(f"远端同步锁正由 {current.get('owner')} 持有，至 {current.get('expires-at')}。", 409, "lease_busy")
        lease_id = str(uuid.uuid4())
        expires = _iso_after(lease_seconds)
        new_etag = self._set_title(page_id, self._lease_title(owner, lease_id, expires), etag)
        confirmed_page, confirmed_etag = self._page_metadata(page_id)
        confirmed = self._parse_lease_title(_flowus_title(confirmed_page))
        if confirmed.get("lease-id") != lease_id or confirmed.get("owner") != owner:
            raise ProviderError("FlowUs 远端租约写后确认失败。", 409, "lease_lost")
        compare_token = confirmed_etag or new_etag
        if not compare_token:
            raise ProviderError("FlowUs 远端租约确认后缺少 ETag。", 409, "etag_required")
        return Lease(page_id, lease_id, owner, expires, compare_token=compare_token)

    def renew_lease(self, lease: Lease, lease_seconds: int = 120) -> Lease:
        page, etag = self._page_metadata(lease.page_id)
        current = self._parse_lease_title(_flowus_title(page))
        if current.get("lease-id") != lease.lease_id:
            raise ProviderError("远端同步锁已被其他写入者接管。", 409, "lease_lost")
        expires = _iso_after(lease_seconds)
        lease.compare_token = self._set_title(lease.page_id, self._lease_title(lease.owner, lease.lease_id, expires), etag)
        lease.expires_at = expires
        return lease

    def release_lease(self, lease: Lease) -> None:
        page, etag = self._page_metadata(lease.page_id)
        current = self._parse_lease_title(_flowus_title(page))
        if current.get("lease-id") == lease.lease_id:
            self._set_title(lease.page_id, self._lease_title(None, None, None), etag)


def provider_from_config(config: dict[str, Any]) -> HttpProvider:
    token = resolve_token(config)
    provider = config.get("provider")
    if provider == "notion":
        return NotionProvider(token)
    if provider == "flowus":
        return FlowUsProvider(token)
    raise ProviderError(f"不支持的在线笔记平台: {provider}")
