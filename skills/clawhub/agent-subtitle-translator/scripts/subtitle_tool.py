#!/usr/bin/env python3
"""Deterministic subtitle preparation, response validation, and composition.

The translation itself is deliberately external: an agent sends the generated
batch prompts to an LLM, stores each response, validates it, then composes the
validated JSON files without ever asking an LLM to handle timestamps.
"""

from __future__ import annotations

import argparse
import codecs
import json
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


MAX_BATCH_SIZE = 32
MANIFEST_VERSION = 1
WRAPPER_RE = re.compile(
    r"⟦ID:(?P<id>\d{6})⟧(?P<body>.*?)⟦/ID:(?P=id)⟧", re.DOTALL
)
MARKER_RE = re.compile(r"⟦(?P<close>/)?(?P<kind>S|BR|F)(?P<num>\d+)⟧")
NEUTRAL_TOKEN_RE = re.compile(r"⟦[^⟧]*⟧")
ASS_TAG_RE = re.compile(r"\{[^{}]*\}")
KARAOKE_RE = re.compile(r"\\(?:k|K|kf|ko)\s*\d+", re.IGNORECASE)
ASS_SAFE_COMMAND_RE = re.compile(
    r"\\(?:pos\([^)]*\)|org\([^)]*\)|an\d+|q\d+|pbo-?\d+)", re.IGNORECASE
)
ASS_DRAWING_RE = re.compile(r"\\p\s*(\d+)", re.IGNORECASE)


class SubtitleError(RuntimeError):
    """Raised when deterministic mapping cannot be guaranteed."""


@dataclass
class DecodeResult:
    text: str
    encoding: str
    confidence: float
    bom: str | None


def normalize_bcp47(value: str) -> str:
    """Normalize the casing and separators of a practical BCP 47 tag."""
    raw = value.strip().replace("_", "-")
    if not raw or not re.fullmatch(r"[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*", raw):
        raise SubtitleError(f"Invalid BCP 47 language tag: {value!r}")
    parts = raw.split("-")
    if not re.fullmatch(r"[A-Za-z]{2,8}", parts[0]):
        raise SubtitleError(f"Invalid BCP 47 primary language subtag: {parts[0]!r}")
    normalized = [parts[0].lower()]
    for part in parts[1:]:
        if len(part) == 4 and part.isalpha():
            normalized.append(part.title())
        elif (len(part) == 2 and part.isalpha()) or (len(part) == 3 and part.isdigit()):
            normalized.append(part.upper())
        else:
            normalized.append(part.lower())
    return "-".join(normalized)


def decode_subtitle(path: Path) -> DecodeResult:
    data = path.read_bytes()
    if not data:
        raise SubtitleError("Input file is empty")

    boms: list[tuple[bytes, str, str]] = [
        (codecs.BOM_UTF8, "utf-8-sig", "UTF-8"),
        (codecs.BOM_UTF32_LE, "utf-32", "UTF-32-LE"),
        (codecs.BOM_UTF32_BE, "utf-32", "UTF-32-BE"),
        (codecs.BOM_UTF16_LE, "utf-16", "UTF-16-LE"),
        (codecs.BOM_UTF16_BE, "utf-16", "UTF-16-BE"),
    ]
    for prefix, encoding, label in boms:
        if data.startswith(prefix):
            try:
                return DecodeResult(data.decode(encoding), encoding, 1.0, label)
            except UnicodeDecodeError as exc:
                raise SubtitleError(f"Declared {label} BOM could not be decoded: {exc}") from exc

    try:
        return DecodeResult(data.decode("utf-8"), "utf-8", 1.0, None)
    except UnicodeDecodeError:
        pass

    try:
        from charset_normalizer import from_bytes
    except ImportError as exc:
        raise SubtitleError(
            "Input is not UTF-8 and charset-normalizer is unavailable. "
            "Install dependencies with: python3 -m pip install -r requirements.txt"
        ) from exc

    match = from_bytes(data).best()
    if match is None or not match.encoding:
        raise SubtitleError("Unable to detect a reliable subtitle encoding")
    confidence = max(0.0, min(1.0, 1.0 - float(match.percent_chaos) / 100.0))
    # Very short legacy-encoded samples are intrinsically ambiguous. Refuse them.
    if confidence < 0.75 or (len(data) < 24 and any(byte >= 0x80 for byte in data)):
        raise SubtitleError(
            f"Encoding detection confidence is too low ({confidence:.2f}, {match.encoding}); "
            "convert the input to UTF-8 explicitly"
        )
    try:
        text = str(match)
    except Exception as exc:  # pragma: no cover - defensive library boundary
        raise SubtitleError(f"Detected {match.encoding} but decoding failed: {exc}") from exc
    if "\ufffd" in text:
        raise SubtitleError("Decoded text contains replacement characters; refusing unsafe input")
    return DecodeResult(text, match.encoding, confidence, None)


def parse_timestamp(value: str, *, vtt: bool = False) -> int:
    value = value.strip().replace(".", ",") if vtt else value.strip()
    match = re.fullmatch(r"(?:(\d{1,2}):)?(\d{2}):(\d{2}),(\d{3})", value)
    if not match:
        raise SubtitleError(f"Invalid timestamp: {value!r}")
    hours = int(match.group(1) or 0)
    minutes, seconds, millis = map(int, match.groups()[1:])
    if minutes > 59 or seconds > 59:
        raise SubtitleError(f"Out-of-range timestamp: {value!r}")
    return ((hours * 60 + minutes) * 60 + seconds) * 1000 + millis


def format_timestamp(ms: int) -> str:
    if ms < 0:
        raise SubtitleError("Negative timestamps are not supported")
    hours, rem = divmod(ms, 3_600_000)
    minutes, rem = divmod(rem, 60_000)
    seconds, millis = divmod(rem, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}"


def _timeline_report(entries: list[dict[str, Any]]) -> dict[str, Any]:
    timed = [e for e in entries if "start_ms" in e]
    unsorted: list[str] = []
    for previous, current in zip(timed, timed[1:]):
        if (current["start_ms"], current["end_ms"]) < (
            previous["start_ms"],
            previous["end_ms"],
        ):
            unsorted.append(current["id"])
    return {
        "entry_count": len(entries),
        "time_range_ms": (
            [min(e["start_ms"] for e in timed), max(e["end_ms"] for e in timed)]
            if timed
            else None
        ),
        "sorted": not unsorted,
        "out_of_order_ids": unsorted,
        "empty_text_ids": [e["id"] for e in entries if not e.get("source_text", "").strip()],
    }


def parse_srt(text: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n").strip("\n")
    blocks = re.split(r"\n[ \t]*\n", normalized) if normalized else []
    entries: list[dict[str, Any]] = []
    original_indices: list[str] = []
    for position, block in enumerate(blocks, 1):
        lines = block.split("\n")
        if len(lines) < 3:
            raise SubtitleError(f"SRT block {position} has no complete index, timeline, and text")
        index = lines[0].strip()
        if not re.fullmatch(r"\d+", index):
            raise SubtitleError(f"SRT block {position} has invalid index {index!r}")
        original_indices.append(index)
        timing = re.fullmatch(r"\s*(.*?)\s*-->\s*(.*?)\s*", lines[1])
        if not timing:
            raise SubtitleError(f"SRT block {position} has an invalid timeline")
        start_ms = parse_timestamp(timing.group(1))
        end_ms = parse_timestamp(timing.group(2))
        if end_ms <= start_ms:
            raise SubtitleError(f"SRT block {position} ends at or before its start")
        content = "\n".join(lines[2:]).strip()
        if not content:
            raise SubtitleError(f"SRT block {position} has empty text")
        stable_id = f"{position:06d}"
        entries.append(
            {
                "id": stable_id,
                "order": position,
                "start_ms": start_ms,
                "end_ms": end_ms,
                "source_text": content,
                "payload_text": content,
                "kind": "srt",
            }
        )
    if not entries:
        raise SubtitleError("No SRT subtitle entries found")
    before = _timeline_report(entries)
    # SRT normalization uses a stable timeline sort and contiguous output indices.
    entries.sort(key=lambda item: (item["start_ms"], item["end_ms"], item["order"]))
    for order, entry in enumerate(entries, 1):
        entry["order"] = order
        entry["id"] = f"{order:06d}"
    after = _timeline_report(entries)
    return entries, {
        "original_entry_count": len(blocks),
        "normalized_entry_count": len(entries),
        "indices_were_contiguous": original_indices == [str(i) for i in range(1, len(entries) + 1)],
        "before": before,
        "after": after,
    }


def parse_vtt(text: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff")
    if not normalized.startswith("WEBVTT"):
        raise SubtitleError("VTT input must begin with WEBVTT")
    lines = normalized.split("\n")
    entries: list[dict[str, Any]] = []
    index = 1
    while index < len(lines):
        line = lines[index].strip()
        if not line:
            index += 1
            continue
        if line.startswith(("NOTE", "STYLE", "REGION")):
            index += 1
            while index < len(lines) and lines[index].strip():
                index += 1
            continue
        cue_identifier: str | None = None
        if "-->" not in line:
            cue_identifier = line
            index += 1
            if index >= len(lines):
                raise SubtitleError(f"VTT cue {cue_identifier!r} has no timeline")
            line = lines[index].strip()
        if "-->" not in line:
            raise SubtitleError(f"Invalid VTT cue timeline near line {index + 1}")
        left, right = [part.strip() for part in line.split("-->", 1)]
        right_time = right.split()[0]
        start_ms = parse_timestamp(left, vtt=True)
        end_ms = parse_timestamp(right_time, vtt=True)
        if end_ms <= start_ms:
            raise SubtitleError(f"VTT cue near line {index + 1} ends at or before its start")
        index += 1
        content_lines: list[str] = []
        while index < len(lines) and lines[index].strip():
            content_lines.append(lines[index])
            index += 1
        content = "\n".join(content_lines).strip()
        if not content:
            raise SubtitleError(f"VTT cue near line {index + 1} has empty text")
        order = len(entries) + 1
        entries.append(
            {
                "id": f"{order:06d}",
                "order": order,
                "start_ms": start_ms,
                "end_ms": end_ms,
                "source_text": content,
                "payload_text": content,
                "kind": "srt",
                "vtt_identifier": cue_identifier,
            }
        )
    if not entries:
        raise SubtitleError("No VTT cues found")
    before = _timeline_report(entries)
    entries.sort(key=lambda item: (item["start_ms"], item["end_ms"], item["order"]))
    for order, entry in enumerate(entries, 1):
        entry["order"] = order
        entry["id"] = f"{order:06d}"
    return entries, {
        "original_entry_count": len(entries),
        "normalized_entry_count": len(entries),
        "before": before,
        "after": _timeline_report(entries),
        "conversion": "WebVTT to normalized SRT",
    }


def ass_split_fields(line: str, field_count: int) -> list[str]:
    payload = line.split(":", 1)[1].lstrip()
    fields = payload.split(",", field_count - 1)
    if len(fields) != field_count:
        raise SubtitleError(f"ASS event has {len(fields)} fields; expected {field_count}")
    return fields


def parse_ass_time(value: str) -> int:
    match = re.fullmatch(r"\s*(\d+):(\d{2}):(\d{2})[.](\d{2})\s*", value)
    if not match:
        raise SubtitleError(f"Invalid ASS timestamp: {value!r}")
    hours, minutes, seconds, centis = map(int, match.groups())
    if minutes > 59 or seconds > 59:
        raise SubtitleError(f"Out-of-range ASS timestamp: {value!r}")
    return ((hours * 60 + minutes) * 60 + seconds) * 1000 + centis * 10


def _ass_tokens(text: str) -> list[tuple[str, str]]:
    tokens: list[tuple[str, str]] = []
    position = 0
    for match in ASS_TAG_RE.finditer(text):
        if match.start() > position:
            tokens.append(("text", text[position : match.start()]))
        tokens.append(("tag", match.group(0)))
        position = match.end()
    if position < len(text):
        tokens.append(("text", text[position:]))
    return tokens


def ass_visible_text(text: str) -> str:
    drawing_mode = 0
    visible: list[str] = []
    for kind, value in _ass_tokens(text):
        if kind == "tag":
            drawing = ASS_DRAWING_RE.findall(value)
            if drawing:
                drawing_mode = int(drawing[-1])
            continue
        if drawing_mode == 0:
            visible.append(value.replace(r"\N", "\n").replace(r"\n", "\n").replace(r"\h", " "))
    return "".join(visible)


def _split_safe_position_commands(tag: str) -> tuple[str, str]:
    """Extract safe whole-line positioning commands from an override block."""
    inner = tag[1:-1]
    matches = list(ASS_SAFE_COMMAND_RE.finditer(inner))
    if not matches:
        return "", tag
    safe = "".join(match.group(0) for match in matches)
    pieces: list[str] = []
    cursor = 0
    for match in matches:
        pieces.append(inner[cursor : match.start()])
        cursor = match.end()
    pieces.append(inner[cursor:])
    remainder = "".join(pieces).strip()
    return "{" + safe + "}", ("{" + remainder + "}" if remainder else "")


def _karaoke_safe_prefix(text: str) -> str:
    commands: list[str] = []
    for tag in ASS_TAG_RE.findall(text):
        commands.extend(ASS_SAFE_COMMAND_RE.findall(tag[1:-1]))
    return "{" + "".join(commands) + "}" if commands else ""


def _neutralize_karaoke_visible_text(
    text: str,
) -> tuple[str, dict[str, str], dict[str, str]]:
    """Drop karaoke/drawing syntax while retaining movable hard-break markers."""
    drawing_mode = 0
    output: list[str] = []
    breaks: dict[str, str] = {}
    fixed: dict[str, str] = {}
    for kind, value in _ass_tokens(text):
        if kind == "tag":
            drawing_values = ASS_DRAWING_RE.findall(value)
            if drawing_values:
                drawing_mode = int(drawing_values[-1])
            continue
        if drawing_mode:
            continue
        for part in re.split(r"(\\N|\\n|\\h)", value):
            if part in (r"\N", r"\n"):
                marker = f"BR{len(breaks) + 1}"
                breaks[marker] = part
                output.append(f"⟦{marker}⟧")
            elif part == r"\h":
                marker = f"F{len(fixed) + 1}"
                fixed[marker] = part
                output.append(f"⟦{marker}⟧")
            elif part:
                output.append(part)
    return "".join(output).strip(), breaks, fixed


def neutralize_ass_text(text: str) -> dict[str, Any]:
    """Replace ASS inline structure with movable, strictly validated markers."""
    karaoke = bool(KARAOKE_RE.search(text))
    if karaoke:
        payload, breaks, fixed = _neutralize_karaoke_visible_text(text)
        return {
            "payload_text": payload,
            "style_spans": {},
            "break_markers": breaks,
            "fixed_markers": fixed,
            "ass_prefix": _karaoke_safe_prefix(text),
            "degradation": "karaoke",
        }

    output: list[str] = []
    style_spans: dict[str, dict[str, str]] = {}
    break_markers: dict[str, str] = {}
    fixed_markers: dict[str, str] = {}
    stack: list[str] = []
    leading_prefix: list[str] = []
    drawing_mode = 0

    def close_styles(close_tag: str = "") -> None:
        while stack:
            marker = stack.pop()
            output.append(f"⟦/{marker}⟧")
            if close_tag and not stack:
                style_spans[marker]["close_tag"] = close_tag

    for kind, value in _ass_tokens(text):
        if kind == "tag":
            drawing_values = ASS_DRAWING_RE.findall(value)
            if drawing_values:
                new_mode = int(drawing_values[-1])
                if new_mode != drawing_mode:
                    marker = f"F{len(fixed_markers) + 1}"
                    fixed_markers[marker] = value
                    output.append(f"⟦{marker}⟧")
                drawing_mode = new_mode
                continue
            safe_tag, value = _split_safe_position_commands(value)
            if safe_tag:
                leading_prefix.append(safe_tag)
            if not value:
                continue
            inner = value[1:-1]
            reset = re.search(r"\\r[^\\}]*", inner, re.IGNORECASE)
            if reset:
                reset_tag = "{" + reset.group(0) + "}"
                had_styles = bool(stack)
                close_styles(reset_tag)
                if not had_styles:
                    marker = f"F{len(fixed_markers) + 1}"
                    fixed_markers[marker] = reset_tag
                    output.append(f"⟦{marker}⟧")
                remainder = inner[: reset.start()] + inner[reset.end() :]
                value = "{" + remainder + "}" if remainder.strip() else ""
                if not value:
                    continue
            marker = f"S{len(style_spans) + 1}"
            style_spans[marker] = {"open_tag": value, "close_tag": ""}
            output.append(f"⟦{marker}⟧")
            stack.append(marker)
            continue

        if drawing_mode:
            if value:
                marker = f"F{len(fixed_markers) + 1}"
                fixed_markers[marker] = value
                output.append(f"⟦{marker}⟧")
            continue
        parts = re.split(r"(\\N|\\n|\\h)", value)
        for part in parts:
            if part in (r"\N", r"\n"):
                marker = f"BR{len(break_markers) + 1}"
                break_markers[marker] = part
                output.append(f"⟦{marker}⟧")
            elif part == r"\h":
                marker = f"F{len(fixed_markers) + 1}"
                fixed_markers[marker] = part
                output.append(f"⟦{marker}⟧")
            elif part:
                output.append(part)
    close_styles()
    return {
        "payload_text": "".join(output).strip(),
        "style_spans": style_spans,
        "break_markers": break_markers,
        "fixed_markers": fixed_markers,
        "ass_prefix": "".join(leading_prefix),
        "degradation": None,
    }


def parse_ass(text: str) -> tuple[list[dict[str, Any]], dict[str, Any], dict[str, Any]]:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff")
    lines = normalized.split("\n")
    section = ""
    event_format: list[str] | None = None
    format_line_index: int | None = None
    entries: list[dict[str, Any]] = []
    dialogue_count = 0
    comment_count = 0
    pure_drawing_count = 0
    empty_dialogue_numbers: list[int] = []
    dialogue_timeline_entries: list[dict[str, Any]] = []
    for line_index, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("[") and stripped.endswith("]"):
            section = stripped.casefold()
            continue
        if section != "[events]":
            continue
        if stripped.casefold().startswith("format:"):
            event_format = [part.strip() for part in stripped.split(":", 1)[1].split(",")]
            format_line_index = line_index
            continue
        if stripped.casefold().startswith("comment:"):
            comment_count += 1
            continue
        if not stripped.casefold().startswith("dialogue:"):
            continue
        dialogue_count += 1
        if not event_format or format_line_index is None:
            raise SubtitleError("ASS Dialogue appears before an Events Format line")
        fields = ass_split_fields(line, len(event_format))
        lookup = {name.casefold(): pos for pos, name in enumerate(event_format)}
        required = {"start", "end", "text"}
        if not required.issubset(lookup):
            raise SubtitleError("ASS Events Format must contain Start, End, and Text")
        start_ms = parse_ass_time(fields[lookup["start"]])
        end_ms = parse_ass_time(fields[lookup["end"]])
        if end_ms <= start_ms:
            raise SubtitleError(f"ASS Dialogue {dialogue_count} ends at or before its start")
        ass_text = fields[lookup["text"]]
        visible = ass_visible_text(ass_text).strip()
        dialogue_timeline_entries.append(
            {
                "id": f"D{dialogue_count:06d}",
                "start_ms": start_ms,
                "end_ms": end_ms,
                "source_text": visible or "<non-text-event>",
            }
        )
        if not visible:
            if ASS_DRAWING_RE.search(ass_text) and ASS_TAG_RE.sub("", ass_text).strip():
                pure_drawing_count += 1
            else:
                empty_dialogue_numbers.append(dialogue_count)
            continue
        neutral = neutralize_ass_text(ass_text)
        order = len(entries) + 1
        entry = {
            "id": f"{order:06d}",
            "order": order,
            "start_ms": start_ms,
            "end_ms": end_ms,
            "source_text": visible,
            "payload_text": neutral["payload_text"],
            "kind": "ass",
            "ass_line_index": line_index,
            "ass_fields": fields,
            "ass_text_field": lookup["text"],
            **neutral,
        }
        entries.append(entry)
    if not event_format:
        raise SubtitleError("ASS input has no [Events] Format line")
    report = {
        "original_dialogue_count": dialogue_count,
        "translatable_entry_count": len(entries),
        "comment_count_preserved": comment_count,
        "pure_drawing_count_preserved": pure_drawing_count,
        "empty_dialogue_numbers_preserved": empty_dialogue_numbers,
        "karaoke_degraded_ids": [e["id"] for e in entries if e["degradation"] == "karaoke"],
        "before": _timeline_report(dialogue_timeline_entries),
        "after": _timeline_report(dialogue_timeline_entries),
        "event_order_preserved": True,
    }
    template = {"lines": lines, "event_format": event_format}
    return entries, report, template


def build_prompt(entries: list[dict[str, Any]], source_language: str, target_language: str) -> str:
    payload = "\n\n".join(
        f"⟦ID:{entry['id']}⟧\n{entry['payload_text']}\n⟦/ID:{entry['id']}⟧"
        for entry in entries
    )
    return f"""# 角色
你是一位字幕翻译专家，擅长翻译电影与视频对白。

# 任务
将以下字幕从{source_language}翻译成{target_language}。

# 翻译要求
1. 使用自然、流畅、简洁的口语，根据上下文合理意译，避免翻译腔；若来源语言与目标语言相同，返回原文内容。
2. 只翻译，不解释、不说明、不添加原文没有的信息。
3. 可理解批次上下文，但必须逐条翻译，不跨条目合并、拆分或借用相邻条目的译文。
4. 原样保留每个 ⟦ID:nnnnnn⟧ 与对应的 ⟦/ID:nnnnnn⟧，ID、顺序和条数不得改变。
5. 原样保留正文中的全部中性标记。⟦Sx⟧...⟦/Sx⟧ 必须继续包裹同一语义，可随目标语言语序成对移动；⟦BRx⟧ 和 ⟦Fx⟧ 可随语义移动，但不得增删、复制或改名。
6. 不要输出 Markdown 代码块或任何批次外文字。

# 待翻译文本
{payload}
"""


def _ensure_clean_work_dir(path: Path, overwrite: bool) -> None:
    if path.exists():
        if not overwrite:
            raise SubtitleError(f"Work directory already exists: {path}")
        if path.is_file():
            raise SubtitleError(f"Work path is a file: {path}")
        shutil.rmtree(path)
    path.mkdir(parents=True)
    (path / "batches").mkdir()
    (path / "validated").mkdir()


def command_prepare(args: argparse.Namespace) -> int:
    input_path = Path(args.input).expanduser().resolve()
    if not input_path.is_file():
        raise SubtitleError(f"Input file does not exist: {input_path}")
    extension = input_path.suffix.lower()
    if extension not in {".srt", ".vtt", ".ass"}:
        raise SubtitleError("Supported input formats are .srt, .vtt, and .ass")
    target = normalize_bcp47(args.target_language)
    source = normalize_bcp47(args.source_language) if args.source_language else "自动检测语言"
    batch_size = args.batch_size
    if not 1 <= batch_size <= MAX_BATCH_SIZE:
        raise SubtitleError(f"Batch size must be between 1 and {MAX_BATCH_SIZE}")
    decoded = decode_subtitle(input_path)

    ass_template: dict[str, Any] | None = None
    if extension == ".srt":
        entries, checks = parse_srt(decoded.text)
        output_extension = ".srt"
    elif extension == ".vtt":
        entries, checks = parse_vtt(decoded.text)
        output_extension = ".srt"
    else:
        entries, checks, ass_template = parse_ass(decoded.text)
        output_extension = ".ass"

    for entry in entries:
        if NEUTRAL_TOKEN_RE.search(entry["source_text"]):
            raise SubtitleError(
                f"Subtitle {entry['id']} contains reserved neutral-marker syntax"
            )
    default_work = input_path.parent / f".{input_path.stem}.{target}.subtitle-work"
    work_dir = Path(args.work_dir).expanduser().resolve() if args.work_dir else default_work
    _ensure_clean_work_dir(work_dir, args.overwrite_work)

    output_path = input_path.with_name(f"{input_path.stem}.{target}{output_extension}")
    manifest = {
        "version": MANIFEST_VERSION,
        "input_path": str(input_path),
        "input_format": extension[1:],
        "output_format": output_extension[1:],
        "default_output_path": str(output_path),
        "target_language": target,
        "source_language": source,
        "encoding": {
            "name": decoded.encoding,
            "confidence": decoded.confidence,
            "bom": decoded.bom,
        },
        "batch_size": batch_size,
        "entry_count": len(entries),
        "entries": entries,
        "checks": checks,
    }
    if ass_template is not None:
        manifest["ass_template"] = ass_template
    batch_records: list[dict[str, Any]] = []
    for batch_index, offset in enumerate(range(0, len(entries), batch_size), 1):
        batch_entries = entries[offset : offset + batch_size]
        filename = f"batch-{batch_index:04d}.txt"
        (work_dir / "batches" / filename).write_text(
            build_prompt(batch_entries, source, target), encoding="utf-8"
        )
        batch_records.append(
            {"batch": batch_index, "file": filename, "ids": [e["id"] for e in batch_entries]}
        )
    manifest["batches"] = batch_records
    (work_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    report = {
        "status": "prepared",
        "work_dir": str(work_dir),
        "manifest": str(work_dir / "manifest.json"),
        "input_format": extension[1:],
        "output_format": output_extension[1:],
        "entry_count": len(entries),
        "batch_count": len(batch_records),
        "batch_size": batch_size,
        "target_language": target,
        "encoding": manifest["encoding"],
        "checks": checks,
    }
    (work_dir / "report.prepare.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SubtitleError(f"Cannot read manifest {path}: {exc}") from exc
    if manifest.get("version") != MANIFEST_VERSION:
        raise SubtitleError("Unsupported manifest version")
    return manifest


def expected_markers(entry: dict[str, Any]) -> dict[str, set[str]]:
    return {
        "S": set(entry.get("style_spans", {})),
        "BR": set(entry.get("break_markers", {})),
        "F": set(entry.get("fixed_markers", {})),
    }


def validate_markers(text: str, entry: dict[str, Any], allow_style_fallback: bool) -> tuple[str, bool]:
    expected = expected_markers(entry)
    reserved_tokens = re.findall(r"⟦[^⟧]*⟧", text)
    recognized_tokens = [match.group(0) for match in MARKER_RE.finditer(text)]
    unrecognized = list(reserved_tokens)
    for token in recognized_tokens:
        if token in unrecognized:
            unrecognized.remove(token)
    style_like_unknown = [token for token in unrecognized if re.fullmatch(r"⟦/?S[^⟧]*⟧", token)]
    other_unknown = [token for token in unrecognized if token not in style_like_unknown]
    if other_unknown:
        raise SubtitleError(f"Subtitle {entry['id']} contains unknown neutral markers: {other_unknown}")
    seen: dict[str, list[str]] = {"S": [], "BR": [], "F": []}
    style_stack: list[str] = []
    style_error: str | None = None
    for match in MARKER_RE.finditer(text):
        kind = match.group("kind")
        marker = f"{kind}{match.group('num')}"
        closing = bool(match.group("close"))
        seen[kind].append(("/" if closing else "") + marker)
        if kind == "S":
            if closing:
                if not style_stack or style_stack[-1] != marker:
                    style_error = f"mis-nested closing marker {marker}"
                else:
                    style_stack.pop()
            else:
                style_stack.append(marker)
        elif closing:
            raise SubtitleError(f"Subtitle {entry['id']} has invalid closing marker {marker}")
    if style_stack and not style_error:
        style_error = f"unclosed markers: {', '.join(style_stack)}"

    for kind in ("BR", "F"):
        actual = seen[kind]
        wanted = expected[kind]
        if len(actual) != len(wanted) or set(actual) != wanted:
            raise SubtitleError(
                f"Subtitle {entry['id']} {kind} markers mismatch: expected {sorted(wanted)}, got {actual}"
            )

    actual_style_tokens = seen["S"]
    wanted_style_tokens = {token for marker in expected["S"] for token in (marker, f"/{marker}")}
    style_ok = (
        not style_error
        and len(actual_style_tokens) == len(wanted_style_tokens)
        and set(actual_style_tokens) == wanted_style_tokens
    )
    if style_ok:
        return text, False
    if expected["S"] and allow_style_fallback:
        # Strip only neutral style markers. BR/F integrity remains mandatory.
        stripped = re.sub(r"⟦/?S[^⟧]*⟧", "", text)
        return stripped, True
    if style_like_unknown:
        raise SubtitleError(
            f"Subtitle {entry['id']} contains invalid style markers: {style_like_unknown}"
        )
    if expected["S"]:
        detail = style_error or f"expected {sorted(wanted_style_tokens)}, got {actual_style_tokens}"
        raise SubtitleError(f"Subtitle {entry['id']} style markers mismatch: {detail}")
    if actual_style_tokens:
        raise SubtitleError(f"Subtitle {entry['id']} contains unexpected style markers")
    return text, False


def parse_response(response: str, expected_ids: list[str]) -> dict[str, str]:
    matches = list(WRAPPER_RE.finditer(response))
    if len(matches) != len(expected_ids):
        raise SubtitleError(
            f"Response entry count mismatch: expected {len(expected_ids)}, got {len(matches)}"
        )
    residue = WRAPPER_RE.sub("", response).strip()
    if residue:
        raise SubtitleError("Response contains text outside the required ID wrappers")
    actual_ids = [match.group("id") for match in matches]
    if actual_ids != expected_ids:
        raise SubtitleError(f"Response IDs/order mismatch: expected {expected_ids}, got {actual_ids}")
    result: dict[str, str] = {}
    for match in matches:
        body = match.group("body").strip("\r\n")
        if not body.strip():
            raise SubtitleError(f"Subtitle {match.group('id')} has an empty translation")
        result[match.group("id")] = body
    return result


def command_validate_response(args: argparse.Namespace) -> int:
    manifest_path = Path(args.manifest).expanduser().resolve()
    manifest = load_manifest(manifest_path)
    try:
        batch_number = int(args.batch)
    except ValueError as exc:
        raise SubtitleError("Batch must be an integer") from exc
    record = next((b for b in manifest["batches"] if b["batch"] == batch_number), None)
    if record is None:
        raise SubtitleError(f"Batch {batch_number} is not present in the manifest")
    response_path = Path(args.response).expanduser().resolve()
    try:
        response = response_path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        raise SubtitleError(f"Cannot read UTF-8 response {response_path}: {exc}") from exc
    translated = parse_response(response, record["ids"])
    entry_by_id = {entry["id"]: entry for entry in manifest["entries"]}
    rows: list[dict[str, Any]] = []
    fallback_ids: list[str] = []
    for stable_id in record["ids"]:
        checked, fallback = validate_markers(
            translated[stable_id], entry_by_id[stable_id], args.allow_style_fallback
        )
        if fallback:
            fallback_ids.append(stable_id)
        rows.append({"id": stable_id, "text": checked, "style_fallback": fallback})
    output_path = (
        Path(args.output).expanduser().resolve()
        if args.output
        else manifest_path.parent / "validated" / f"batch-{batch_number:04d}.json"
    )
    if output_path.exists() and not args.overwrite:
        raise SubtitleError(f"Validated output already exists: {output_path}")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "manifest": str(manifest_path),
        "batch": batch_number,
        "ids": record["ids"],
        "translations": rows,
        "style_fallback_ids": fallback_ids,
    }
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "validated",
                "batch": batch_number,
                "output": str(output_path),
                "entry_count": len(rows),
                "style_fallback_ids": fallback_ids,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def restore_ass_text(text: str, entry: dict[str, Any], style_fallback: bool) -> str:
    if style_fallback or entry.get("degradation") == "karaoke":
        # The validated translation contains no style markers in this path.
        static = re.sub(r"⟦/?S\d+⟧", "", text)
        for marker, original in entry.get("break_markers", {}).items():
            static = static.replace(f"⟦{marker}⟧", original)
        for marker, original in entry.get("fixed_markers", {}).items():
            static = static.replace(f"⟦{marker}⟧", original)
        return entry.get("ass_prefix", "") + static
    restored = text
    for marker, mapping in entry.get("style_spans", {}).items():
        restored = restored.replace(f"⟦{marker}⟧", mapping["open_tag"])
        restored = restored.replace(f"⟦/{marker}⟧", mapping["close_tag"])
    for marker, original in entry.get("break_markers", {}).items():
        restored = restored.replace(f"⟦{marker}⟧", original)
    for marker, original in entry.get("fixed_markers", {}).items():
        restored = restored.replace(f"⟦{marker}⟧", original)
    if MARKER_RE.search(restored):
        raise SubtitleError(f"Subtitle {entry['id']} still contains unresolved markers")
    return entry.get("ass_prefix", "") + restored


def render_srt(entries: list[dict[str, Any]], translations: dict[str, dict[str, Any]]) -> str:
    blocks = []
    for index, entry in enumerate(entries, 1):
        translated = translations[entry["id"]]["text"]
        blocks.append(
            f"{index}\n{format_timestamp(entry['start_ms'])} --> {format_timestamp(entry['end_ms'])}\n{translated}"
        )
    return "\n\n".join(blocks) + "\n"


def render_ass(
    manifest: dict[str, Any], translations: dict[str, dict[str, Any]]
) -> str:
    lines = list(manifest["ass_template"]["lines"])
    for entry in manifest["entries"]:
        translation = translations[entry["id"]]
        rendered = restore_ass_text(translation["text"], entry, translation["style_fallback"])
        fields = list(entry["ass_fields"])
        fields[entry["ass_text_field"]] = rendered
        original_line = lines[entry["ass_line_index"]]
        prefix = original_line.split(":", 1)[0]
        lines[entry["ass_line_index"]] = f"{prefix}: " + ",".join(fields)
    return "\n".join(lines).rstrip("\n") + "\n"


def command_compose(args: argparse.Namespace) -> int:
    manifest_path = Path(args.manifest).expanduser().resolve()
    manifest = load_manifest(manifest_path)
    validated_dir = (
        Path(args.validated_dir).expanduser().resolve()
        if args.validated_dir
        else manifest_path.parent / "validated"
    )
    translations: dict[str, dict[str, Any]] = {}
    fallback_ids: list[str] = []
    entry_by_id = {entry["id"]: entry for entry in manifest["entries"]}
    for batch in manifest["batches"]:
        path = validated_dir / f"batch-{batch['batch']:04d}.json"
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise SubtitleError(f"Missing or invalid validated batch {path}: {exc}") from exc
        if payload.get("ids") != batch["ids"]:
            raise SubtitleError(f"Validated batch {path.name} IDs do not match the manifest")
        rows = payload.get("translations", [])
        if not isinstance(rows, list) or not all(
            isinstance(row, dict) and isinstance(row.get("id"), str) for row in rows
        ):
            raise SubtitleError(f"Validated batch {path.name} has malformed translation rows")
        row_ids = [row["id"] for row in rows]
        if len(row_ids) != len(batch["ids"]) or sorted(row_ids) != sorted(batch["ids"]):
            raise SubtitleError(f"Validated batch {path.name} translation rows do not match its IDs")
        for row in rows:
            stable_id = row.get("id")
            if stable_id in translations:
                raise SubtitleError(f"Duplicate translation ID {stable_id}")
            if not isinstance(row.get("text"), str) or not row["text"].strip():
                raise SubtitleError(f"Validated batch {path.name} has invalid text for {stable_id}")
            declared_fallback = row.get("style_fallback") is True
            checked, effective_fallback = validate_markers(
                row["text"], entry_by_id[stable_id], declared_fallback
            )
            if checked != row["text"] or effective_fallback != declared_fallback:
                raise SubtitleError(f"Validated batch {path.name} has inconsistent fallback data for {stable_id}")
            translations[stable_id] = {
                "id": stable_id,
                "text": checked,
                "style_fallback": effective_fallback,
            }
            if effective_fallback:
                fallback_ids.append(stable_id)
    expected_ids = [entry["id"] for entry in manifest["entries"]]
    actual_ids = sorted(translations)
    if actual_ids != sorted(expected_ids):
        missing = sorted(set(expected_ids) - set(actual_ids))
        extra = sorted(set(actual_ids) - set(expected_ids))
        raise SubtitleError(f"Translation mapping mismatch; missing={missing}, extra={extra}")
    # Always merge by stable ID/order, regardless of batch execution order.
    ordered_entries = sorted(manifest["entries"], key=lambda entry: entry["id"])
    if manifest["output_format"] == "ass":
        output_text = render_ass(manifest, translations)
    else:
        output_text = render_srt(ordered_entries, translations)
    output_path = (
        Path(args.output).expanduser().resolve()
        if args.output
        else Path(manifest["default_output_path"])
    )
    if output_path.exists() and not args.overwrite:
        raise SubtitleError(f"Output already exists (use --overwrite explicitly): {output_path}")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output_text, encoding="utf-8-sig", newline="")
    karaoke_ids = [
        entry["id"] for entry in manifest["entries"] if entry.get("degradation") == "karaoke"
    ]
    report = {
        "status": "composed",
        "output": str(output_path),
        "output_format": manifest["output_format"],
        "encoding": "utf-8-sig",
        "entry_count": len(ordered_entries),
        "time_range_ms": manifest["checks"]["after"]["time_range_ms"],
        "karaoke_degraded_count": len(karaoke_ids),
        "karaoke_degraded_ids": karaoke_ids,
        "style_fallback_count": len(fallback_ids),
        "style_fallback_ids": sorted(fallback_ids),
    }
    report_path = output_path.with_suffix(output_path.suffix + ".report.json")
    if report_path.exists() and not args.overwrite:
        output_path.unlink(missing_ok=True)
        raise SubtitleError(f"Report already exists (use --overwrite explicitly): {report_path}")
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Prepare, validate, and compose one SRT, VTT, or ASS subtitle translation safely."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser(
        "prepare", help="Decode and validate one subtitle, then create LLM-free timeline batches."
    )
    prepare.add_argument("input", help="Path to one .srt, .vtt, or .ass file")
    prepare.add_argument("--target-language", required=True, help="Required BCP 47 target tag")
    prepare.add_argument("--source-language", help="Optional BCP 47 source tag; omitted means auto-detect")
    prepare.add_argument("--batch-size", type=int, default=MAX_BATCH_SIZE, help="1-32 (default: 32)")
    prepare.add_argument("--work-dir", help="Work package directory")
    prepare.add_argument("--overwrite-work", action="store_true", help="Replace an existing work directory")
    prepare.set_defaults(func=command_prepare)

    validate = subparsers.add_parser(
        "validate-response", help="Strictly map and validate one LLM batch response."
    )
    validate.add_argument("--manifest", required=True, help="Prepared manifest.json")
    validate.add_argument("--batch", required=True, help="1-based batch number")
    validate.add_argument("--response", required=True, help="UTF-8 LLM response file")
    validate.add_argument("--output", help="Validated JSON path")
    validate.add_argument("--overwrite", action="store_true", help="Replace validated output")
    validate.add_argument(
        "--allow-style-fallback",
        action="store_true",
        help="After an agent retry, downgrade only entries with invalid ASS style markers",
    )
    validate.set_defaults(func=command_validate_response)

    compose = subparsers.add_parser(
        "compose", help="Merge all validated batches by stable ID and write the subtitle."
    )
    compose.add_argument("--manifest", required=True, help="Prepared manifest.json")
    compose.add_argument("--validated-dir", help="Directory containing validated batch JSON files")
    compose.add_argument("--output", help="Output path (default: <stem>.<BCP47>.<ext>)")
    compose.add_argument("--overwrite", action="store_true", help="Explicitly replace output and report")
    compose.set_defaults(func=command_compose)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        return int(args.func(args))
    except SubtitleError as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
