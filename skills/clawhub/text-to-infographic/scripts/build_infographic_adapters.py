#!/usr/bin/env python3
"""Build minimal SVG / whiteboard / doc adapter drafts from an infographic plan."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

from validate_infographic_plan import (  # type: ignore
    DEFAULT_SCHEMA_PATH,
    _validate_schema_subset,
    apply_defaults,
    block_shape,
    load_json,
    validate_business_rules,
)


def build_svg_adapter(plan: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "format": "svg-draft",
        "metadata": {
            "infographic_id": plan.get("infographic_id"),
            "chart_family": plan.get("chart_family"),
            "aspect_ratio": plan.get("layout", {}).get("aspect_ratio"),
        },
        "layout": plan.get("layout", {}),
        "groups": [
            {
                "id": block.get("block_id"),
                "type": block.get("block_type"),
                "role": block.get("visual_role"),
                "group_id": block.get("group_id"),
                "label": block.get("title"),
                "body": block.get("content"),
                "icon_hint": block.get("icon_hint"),
                "payload": block.get("payload", {}),
            }
            for block in plan.get("blocks", [])
        ],
        "connectors": [
            {
                "id": f"{relation.get('from')}->{relation.get('to')}",
                "from": relation.get("from"),
                "to": relation.get("to"),
                "type": relation.get("relation_type"),
                "label": relation.get("label"),
                "weight": relation.get("weight"),
            }
            for relation in plan.get("relations", [])
        ],
    }


def build_whiteboard_adapter(plan: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "format": "whiteboard-draft",
        "board": {
            "infographic_id": plan.get("infographic_id"),
            "chart_family": plan.get("chart_family"),
            "aspect_ratio": plan.get("layout", {}).get("aspect_ratio"),
            "primary_target": plan.get("delivery", {}).get("primary_target"),
        },
        "blocks": [
            {
                "id": block.get("block_id"),
                "shape": block_shape(str(block.get("block_type", "custom"))),
                "role": block.get("visual_role"),
                "group_id": block.get("group_id"),
                "title": block.get("title"),
                "content": block.get("content"),
                "icon_hint": block.get("icon_hint"),
                "payload": block.get("payload", {}),
            }
            for block in plan.get("blocks", [])
        ],
        "connectors": [
            {
                "from": relation.get("from"),
                "to": relation.get("to"),
                "type": relation.get("relation_type"),
                "label": relation.get("label"),
                "weight": relation.get("weight"),
            }
            for relation in plan.get("relations", [])
        ],
    }


def build_doc_outline(plan: Dict[str, Any]) -> Dict[str, Any]:
    message = plan.get("message", {})
    sections: List[Dict[str, Any]] = [
        {"type": "title", "text": message.get("title", "")},
    ]
    if message.get("subtitle"):
        sections.append({"type": "subtitle", "text": message["subtitle"]})
    if message.get("core_takeaway"):
        sections.append({"type": "summary", "text": message["core_takeaway"]})

    primary_blocks = [
        block for block in plan.get("blocks", []) if block.get("visual_role") == "primary"
    ]
    secondary_blocks = [
        block for block in plan.get("blocks", []) if block.get("visual_role") == "secondary"
    ]

    if primary_blocks:
        sections.append(
            {
                "type": "section",
                "title": "Primary blocks",
                "items": [
                    {"title": block.get("title"), "content": block.get("content")}
                    for block in primary_blocks
                ],
            }
        )
    if secondary_blocks:
        sections.append(
            {
                "type": "section",
                "title": "Secondary blocks",
                "items": [
                    {"title": block.get("title"), "content": block.get("content")}
                    for block in secondary_blocks[:6]
                ],
            }
        )

    cta = message.get("cta")
    if cta:
        sections.append({"type": "cta", "text": cta})

    return {
        "format": "doc-outline",
        "infographic_id": plan.get("infographic_id"),
        "sections": sections,
    }


def build_doc_summary_markdown(plan: Dict[str, Any]) -> str:
    message = plan.get("message", {})
    lines = [f"# {message.get('title', '').strip()}", ""]
    subtitle = message.get("subtitle", "").strip()
    if subtitle:
        lines.extend([subtitle, ""])
    takeaway = message.get("core_takeaway", "").strip()
    if takeaway:
        lines.extend([f"> {takeaway}", ""])

    lines.extend([
        "## Overview blocks",
        "",
    ])
    for block in plan.get("blocks", []):
        role = block.get("visual_role", "supporting")
        title = block.get("title", "")
        content = block.get("content", "")
        lines.append(f"- [{role}] {title}: {content}")
    lines.append("")

    if plan.get("relations"):
        lines.extend(["## Relations", ""])
        for relation in plan.get("relations", []):
            label = relation.get("label") or relation.get("relation_type")
            weight = relation.get("weight")
            if weight is None:
                lines.append(f"- {relation.get('from')} -> {relation.get('to')}: {label}")
            else:
                lines.append(f"- {relation.get('from')} -> {relation.get('to')}: {label} (weight={weight})")
        lines.append("")

    cta = message.get("cta", "").strip()
    if cta:
        lines.extend(["## Next action", "", cta, ""])

    return "\n".join(lines).strip() + "\n"


def write_json(path: Path, payload: Dict[str, Any], pretty: bool) -> None:
    with path.open("w", encoding="utf-8") as f:
        if pretty:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        else:
            json.dump(payload, f, ensure_ascii=False)
            f.write("\n")


def validate_or_raise(plan_path: Path, schema_path: Path) -> Dict[str, Any]:
    raw = load_json(plan_path)
    schema = load_json(schema_path)
    normalized = apply_defaults(raw)

    errors: List[str] = []
    _validate_schema_subset(normalized, schema, "$", errors)
    business_errors, warnings = validate_business_rules(raw, normalized)
    errors.extend(business_errors)
    if errors:
        raise SystemExit(
            json.dumps(
                {
                    "ok": False,
                    "file": str(plan_path),
                    "errors": errors,
                    "warnings": warnings,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    return normalized


def default_output_dir(plan_path: Path) -> Path:
    return Path("/tmp") / "text-to-infographic-adapters" / plan_path.stem


def main() -> int:
    parser = argparse.ArgumentParser(description="Build infographic adapter drafts.")
    parser.add_argument("infographic_plan", help="Path to infographic plan JSON")
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA_PATH), help="Path to schema JSON")
    parser.add_argument("--out", help="Output directory for generated drafts")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON outputs")
    args = parser.parse_args()

    plan_path = Path(args.infographic_plan)
    schema_path = Path(args.schema)
    out_dir = Path(args.out) if args.out else default_output_dir(plan_path)
    out_dir.mkdir(parents=True, exist_ok=True)

    normalized = validate_or_raise(plan_path, schema_path)
    svg_adapter = build_svg_adapter(normalized)
    whiteboard_adapter = build_whiteboard_adapter(normalized)
    doc_outline = build_doc_outline(normalized)
    doc_summary = build_doc_summary_markdown(normalized)

    normalized_path = out_dir / "normalized-plan.json"
    svg_path = out_dir / "svg-draft.json"
    whiteboard_path = out_dir / "whiteboard-draft.json"
    outline_path = out_dir / "doc-outline.json"
    summary_md_path = out_dir / "doc-summary.md"

    write_json(normalized_path, normalized, args.pretty)
    write_json(svg_path, svg_adapter, args.pretty)
    write_json(whiteboard_path, whiteboard_adapter, args.pretty)
    write_json(outline_path, doc_outline, args.pretty)
    summary_md_path.write_text(doc_summary, encoding="utf-8")

    payload = {
        "ok": True,
        "infographic_id": normalized.get("infographic_id"),
        "out_dir": str(out_dir),
        "files": {
            "normalized_plan": str(normalized_path),
            "svg_draft": str(svg_path),
            "whiteboard_draft": str(whiteboard_path),
            "doc_outline": str(outline_path),
            "doc_summary": str(summary_md_path),
        },
    }
    if args.pretty:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(payload, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
