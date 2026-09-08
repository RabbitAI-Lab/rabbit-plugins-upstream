#!/usr/bin/env python3
"""Normalize AIDSO get-result responses and parse embedded structured cards."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


CARD_PATTERN = re.compile(
    r"render_ecom_card_widget_(?P<kind>[a-zA-Z0-9_]+)_start:\s*"
    r"(?P<payload>\[.*?\])\s*"
    r"render_ecom_card_widget_(?P=kind)_end:",
    re.DOTALL,
)


def is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def workspace_path(
    path: Path,
    label: str,
    *,
    allowed_roots: tuple[Path, ...],
    must_exist: bool = False,
) -> Path:
    workspace = Path.cwd().resolve()
    candidate = path if path.is_absolute() else workspace / path
    try:
        resolved = candidate.resolve(strict=must_exist)
    except OSError as exc:
        raise ValueError(f"{label}无法解析：{exc}") from exc
    if not is_within(resolved, workspace):
        raise ValueError(f"{label}必须位于当前工作区内")
    resolved_roots = []
    for relative_root in allowed_roots:
        root = (workspace / relative_root).resolve()
        if not is_within(root, workspace):
            raise ValueError(f"{label}的规定目录不得通过符号链接逃逸工作区")
        resolved_roots.append(root)
    if not any(is_within(resolved, root) for root in resolved_roots):
        roots = " 或 ".join(f"{root.as_posix()}/" for root in allowed_roots)
        raise ValueError(f"{label}必须位于当前工作区 {roots} 下")
    return resolved


def write_new_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("x", encoding="utf-8") as stream:
            json.dump(payload, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
    except FileExistsError as exc:
        raise ValueError(f"拒绝覆盖已有文件：{path}") from exc


def decode_jsonish(value: Any, default: Any) -> Any:
    if value is None or value == "":
        return default
    current = value
    for _ in range(2):
        if not isinstance(current, str):
            return current
        text = current.strip()
        if not text:
            return default
        try:
            current = json.loads(text)
        except json.JSONDecodeError:
            return value
    return current


def first_nonempty(mapping: dict, names: list[str]) -> Any:
    for name in names:
        value = mapping.get(name)
        if value not in (None, ""):
            return value
    return None


def normalize_card(kind: str, item: dict, position: int) -> dict:
    title = first_nonempty(item, ["text", "title", "sku_name", "name", "poi_name", "query"])
    card_id = first_nonempty(item, ["pid", "item_id", "sku", "id", "poi_id", "wx_app_id", "source_seq_id"])
    url = first_nonempty(item, ["jump_url", "auctionURL", "pc_url", "webURL", "poi_url"])
    image = first_nonempty(item, ["image_url", "pic_path", "verticalPic", "photos", "icon"])
    shop = first_nonempty(item, ["seller_name", "shop_name", "venueName", "source"])
    price = first_nonempty(item, ["price", "priceShowText", "priceLow", "minPrice", "priceStr"])
    return {
        "kind": kind,
        "position": position,
        "id": str(card_id) if card_id is not None else None,
        "title": str(title) if title is not None else None,
        "shop": str(shop) if shop is not None else None,
        "price": price,
        "image_url": str(image) if image is not None else None,
        "url": str(url) if url is not None else None,
        "raw": item,
    }


def extract_cards(context: str) -> tuple[str, list[dict], list[dict]]:
    cards: list[dict] = []
    errors: list[dict] = []
    position = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal position
        kind = match.group("kind")
        payload = match.group("payload")
        try:
            decoded = json.loads(payload)
            if not isinstance(decoded, list):
                raise ValueError("payload 不是数组")
            for raw in decoded:
                position += 1
                if isinstance(raw, dict):
                    cards.append(normalize_card(kind, raw, position))
                else:
                    errors.append({"kind": kind, "error": "卡片项不是对象", "value": raw})
        except (json.JSONDecodeError, ValueError) as exc:
            errors.append({"kind": kind, "error": str(exc), "payload": payload[:500]})
        return "\n"

    clean = CARD_PATTERN.sub(replace, context)
    clean = re.sub(r"\n{3,}", "\n\n", clean).strip()
    return clean, cards, errors


def flatten_result(result: Any) -> dict:
    fields: dict[str, list[Any]] = {}
    if not isinstance(result, list):
        return fields
    for entry in result:
        if not isinstance(entry, dict):
            continue
        for key, value in entry.items():
            fields.setdefault(str(key), []).append(value)
    return fields


def join_text(values: list[Any]) -> str:
    cleaned = []
    for value in values:
        if value in (None, ""):
            continue
        text = str(value)
        # Some API adapters preserve a second JSON-escape layer in context strings.
        # Decode only the common escapes needed for text/card parsing, without using
        # unicode_escape (which would corrupt non-ASCII text).
        if "\\n" in text and "\n" not in text:
            text = (
                text.replace("\\r\\n", "\n")
                .replace("\\n", "\n")
                .replace("\\t", "\t")
                .replace('\\"', '"')
                .replace("\\/", "/")
            )
        cleaned.append(text)
    return "\n".join(cleaned).strip()


def collect_decoded(values: list[Any]) -> list[Any]:
    output: list[Any] = []
    for value in values:
        decoded = decode_jsonish(value, [])
        if isinstance(decoded, list):
            output.extend(decoded)
        elif decoded not in (None, ""):
            output.append(decoded)
    return output


def normalize_response(raw: dict, meta: dict) -> dict:
    data = raw.get("data") if isinstance(raw.get("data"), dict) else raw
    fields = flatten_result(data.get("result"))
    context_raw = join_text(fields.get("context", []))
    context_text, cards, card_errors = extract_cards(context_raw)
    quotes = collect_decoded(fields.get("quote", []))
    search_words = collect_decoded(fields.get("search_word", []))
    rich_media = collect_decoded(fields.get("rich_media_block", []))
    suggestions = join_text(fields.get("suggestions", []))

    return {
        "job_id": meta.get("job_id"),
        "request_id": (
            meta.get("request_id")
            or meta.get("reqId")
            or raw.get("request_id")
            or data.get("reqId")
        ),
        "question_index": meta.get("question_index"),
        "prompt": meta.get("prompt") or data.get("prompt"),
        "platform_code": meta.get("platform_code") or meta.get("platform"),
        "platform_name": meta.get("platform_name"),
        "mode": meta.get("mode"),
        "repetition": meta.get("repetition"),
        "status": str(data.get("status") or "UNKNOWN").upper(),
        "fetch_time": data.get("fetch_time"),
        "context_raw": context_raw,
        "context_text": context_text,
        "search_words": search_words,
        "quotes": [item for item in quotes if isinstance(item, dict)],
        "cards": cards,
        "card_parse_errors": card_errors,
        "suggestions": suggestions,
        "rich_media": rich_media,
    }


def expand_input(payload: Any, base_dir: Path) -> list[tuple[dict, dict]]:
    pairs: list[tuple[dict, dict]] = []
    if isinstance(payload, dict) and isinstance(payload.get("jobs"), list):
        for job in payload["jobs"]:
            if not isinstance(job, dict):
                continue
            response = job.get("response") or job.get("raw_response") or job.get("result_response")
            if response is None and job.get("raw_file"):
                raw_path = workspace_path(
                    base_dir / str(job["raw_file"]),
                    "manifest raw_file",
                    allowed_roots=(Path(".aidso-geo/raw"),),
                    must_exist=True,
                )
                response = json.loads(raw_path.read_text(encoding="utf-8"))
            if isinstance(response, dict):
                meta = {key: value for key, value in job.items() if key not in {"response", "raw_response", "result_response"}}
                pairs.append((response, meta))
        return pairs
    if isinstance(payload, list):
        for index, item in enumerate(payload, start=1):
            if isinstance(item, dict):
                response = item.get("response") if isinstance(item.get("response"), dict) else item
                meta = item.get("meta") if isinstance(item.get("meta"), dict) else {"job_id": f"j{index:05d}"}
                pairs.append((response, meta))
        return pairs
    if isinstance(payload, dict):
        return [(payload, {})]
    raise ValueError("输入必须是原始响应对象、响应数组或包含 jobs 的对象")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        input_path = workspace_path(
            args.input,
            "原始响应或 manifest 输入",
            allowed_roots=(Path(".aidso-geo/raw"), Path(".aidso-geo/tasks")),
            must_exist=True,
        )
        output_path = workspace_path(
            args.output,
            "规范化输出",
            allowed_roots=(Path(".aidso-geo/normalized"),),
        )
        payload = json.loads(input_path.read_text(encoding="utf-8"))
        pairs = expand_input(payload, input_path.parent)
        conversations = [normalize_response(raw, meta) for raw, meta in pairs]
        counts: dict[str, int] = {}
        for item in conversations:
            counts[item["status"]] = counts.get(item["status"], 0) + 1
        output = {
            "schema_version": 1,
            "source": str(input_path),
            "counts": counts,
            "conversations": conversations,
        }
        write_new_json(output_path, output)
        print(json.dumps({"output": str(output_path), "conversations": len(conversations), "counts": counts}, ensure_ascii=False))
        return 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
