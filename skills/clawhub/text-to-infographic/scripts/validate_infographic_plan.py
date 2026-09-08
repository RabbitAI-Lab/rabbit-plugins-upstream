#!/usr/bin/env python3
"""Validate infographic plan JSON with schema-subset rules and business checks."""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Tuple


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SCHEMA_PATH = ROOT / "schemas" / "infographic-plan.schema.json"
DEFAULT_LAYOUTS: Dict[str, Dict[str, str]] = {
    "flywheel": {
        "layout_mode": "radial",
        "coordinate_system": "polar",
        "reading_order": "clockwise",
    },
    "fishbone": {
        "layout_mode": "spine-branch",
        "coordinate_system": "cartesian",
        "reading_order": "left-to-right",
    },
    "pyramid": {
        "layout_mode": "pyramid",
        "coordinate_system": "cartesian",
        "reading_order": "top-to-bottom",
    },
    "roadmap": {
        "layout_mode": "timeline",
        "coordinate_system": "cartesian",
        "reading_order": "left-to-right",
    },
    "dashboard": {
        "layout_mode": "dashboard",
        "coordinate_system": "cartesian",
        "reading_order": "left-to-right",
    },
}
DEFAULT_DELIVERY: Dict[str, Any] = {
    "primary_target": "html",
    "secondary_targets": ["svg", "doc"],
    "doc_mode": "companion-detail",
}
MESSAGE_LIMITS = {
    "title": 40,
    "subtitle": 80,
    "core_takeaway": 120,
    "cta": 60,
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def apply_defaults(plan: Dict[str, Any]) -> Dict[str, Any]:
    normalized = copy.deepcopy(plan)
    chart_family = normalized.get("chart_family")

    layout = normalized.setdefault("layout", {})
    if isinstance(layout, dict):
        for key, value in DEFAULT_LAYOUTS.get(chart_family, {}).items():
            layout.setdefault(key, value)

    delivery = normalized.setdefault("delivery", {})
    if isinstance(delivery, dict):
        for key, value in DEFAULT_DELIVERY.items():
            delivery.setdefault(key, copy.deepcopy(value))

    return normalized


def _type_matches(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return (isinstance(value, (int, float)) and not isinstance(value, bool))
    return True


def _validate_schema_subset(value: Any, schema: Dict[str, Any], path: str, errors: List[str]) -> None:
    schema_type = schema.get("type")
    if schema_type and not _type_matches(value, schema_type):
        errors.append(f"{path} should be {schema_type}")
        return

    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path} should be one of {schema['enum']}, got {value!r}")
        return

    if isinstance(value, str) and "pattern" in schema:
        if re.fullmatch(schema["pattern"], value) is None:
            errors.append(f"{path} does not match pattern {schema['pattern']}")

    if isinstance(value, list):
        min_items = schema.get("minItems")
        max_items = schema.get("maxItems")
        if isinstance(min_items, int) and len(value) < min_items:
            errors.append(f"{path} should contain at least {min_items} items")
        if isinstance(max_items, int) and len(value) > max_items:
            errors.append(f"{path} should contain at most {max_items} items")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for idx, item in enumerate(value):
                _validate_schema_subset(item, item_schema, f"{path}[{idx}]", errors)
        return

    if isinstance(value, dict):
        properties = schema.get("properties", {})
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                errors.append(f"{path}.{key} is required")

        if schema.get("additionalProperties") is False:
            unknown_keys = sorted(set(value.keys()) - set(properties.keys()))
            for key in unknown_keys:
                errors.append(f"{path}.{key} is not allowed")

        for key, prop_schema in properties.items():
            if key in value:
                _validate_schema_subset(value[key], prop_schema, f"{path}.{key}", errors)
        return

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        minimum = schema.get("minimum")
        if minimum is not None and value < minimum:
            errors.append(f"{path} should be >= {minimum}")


def text_units(*parts: str) -> int:
    return sum(len((part or "").strip()) for part in parts)


def validate_business_rules(original: Dict[str, Any], normalized: Dict[str, Any]) -> Tuple[List[str], List[str]]:
    errors: List[str] = []
    warnings: List[str] = []

    message = normalized.get("message", {})
    if isinstance(message, dict):
        for field, limit in MESSAGE_LIMITS.items():
            value = message.get(field)
            if isinstance(value, str) and len(value.strip()) > limit:
                errors.append(f"message.{field} looks too dense (chars={len(value.strip())}, limit={limit})")

    blocks = normalized.get("blocks", [])
    block_ids = set()
    primary_count = 0
    if isinstance(blocks, list):
        for index, block in enumerate(blocks):
            block_path = f"blocks[{index}]"
            if not isinstance(block, dict):
                continue
            block_id = block.get("block_id")
            if isinstance(block_id, str):
                if block_id in block_ids:
                    errors.append(f"duplicate block_id: {block_id}")
                block_ids.add(block_id)
            if block.get("visual_role") == "primary":
                primary_count += 1

            text_budget = block.get("text_budget")
            if text_budget is not None and isinstance(text_budget, int):
                usage = text_units(block.get("title", ""), block.get("content", ""))
                if usage > text_budget * 3:
                    errors.append(
                        f"{block_path} text looks too long for text_budget={text_budget} (chars={usage})"
                    )

            for list_field in ("must_include", "avoid"):
                value = block.get(list_field)
                if value is not None and not isinstance(value, list):
                    errors.append(f"{block_path}.{list_field} should be an array")

    if blocks and primary_count == 0:
        errors.append("blocks should include at least one visual_role=primary item")

    relations = normalized.get("relations", [])
    if not isinstance(relations, list):
        relations = []
    for index, relation in enumerate(relations):
        rel_path = f"relations[{index}]"
        if not isinstance(relation, dict):
            continue
        start = relation.get("from")
        end = relation.get("to")
        if start not in block_ids:
            errors.append(f"{rel_path}.from references unknown block_id: {start}")
        if end not in block_ids:
            errors.append(f"{rel_path}.to references unknown block_id: {end}")

    chart_family = normalized.get("chart_family")
    if chart_family == "sankey":
        if not relations:
            errors.append("chart_family=sankey should include at least one relation")
        for index, relation in enumerate(relations):
            if "weight" not in relation:
                errors.append(f"relations[{index}].weight is required when chart_family=sankey")

    if chart_family in DEFAULT_LAYOUTS:
        expected = DEFAULT_LAYOUTS[chart_family]
        actual_layout = normalized.get("layout", {}) if isinstance(normalized.get("layout"), dict) else {}
        raw_layout = original.get("layout", {}) if isinstance(original.get("layout"), dict) else {}
        for key, expected_value in expected.items():
            actual_value = actual_layout.get(key)
            if actual_value != expected_value:
                warnings.append(
                    f"chart_family={chart_family} overrides default {key}={expected_value} with {actual_value}"
                )
            elif key not in raw_layout:
                warnings.append(
                    f"chart_family={chart_family} filled missing default {key}={expected_value}"
                )

    delivery = normalized.get("delivery", {}) if isinstance(normalized.get("delivery"), dict) else {}
    primary_target = delivery.get("primary_target")
    secondary_targets = delivery.get("secondary_targets", [])
    if isinstance(secondary_targets, list):
        if len(secondary_targets) != len(set(secondary_targets)):
            errors.append("delivery.secondary_targets should not contain duplicates")
        if primary_target in secondary_targets:
            errors.append("delivery.secondary_targets should not repeat delivery.primary_target")

    return errors, warnings


def block_shape(block_type: str) -> str:
    mapping = {
        "title": "header",
        "summary": "summary-card",
        "stage": "step-card",
        "cause": "cause-branch",
        "effect": "headline-node",
        "metric": "metric-card",
        "node": "node-card",
        "callout": "callout-card",
        "legend": "legend",
        "note": "note-card",
        "cta": "cta-banner",
        "custom": "custom-shape",
    }
    return mapping.get(block_type, "custom-shape")


def build_svg_preview(plan: Dict[str, Any]) -> Dict[str, Any]:
    groups = []
    for block in plan.get("blocks", []):
        groups.append(
            {
                "group_id": block.get("block_id"),
                "group_type": block.get("block_type"),
                "label": block.get("title"),
                "text_nodes": [block.get("title"), block.get("content")],
            }
        )
    connectors = [
        {
            "from": relation.get("from"),
            "to": relation.get("to"),
            "relation_type": relation.get("relation_type"),
            "label": relation.get("label"),
        }
        for relation in plan.get("relations", [])
    ]
    return {
        "ok": True,
        "group_count": len(groups),
        "connector_count": len(connectors),
        "sample_groups": groups[:2],
        "sample_connectors": connectors[:2],
    }


def build_whiteboard_preview(plan: Dict[str, Any]) -> Dict[str, Any]:
    blocks = []
    for block in plan.get("blocks", []):
        blocks.append(
            {
                "block_id": block.get("block_id"),
                "shape": block_shape(str(block.get("block_type", "custom"))),
                "text": f"{block.get('title', '')}\n{block.get('content', '')}".strip(),
                "group_id": block.get("group_id"),
            }
        )
    connectors = [
        {
            "from": relation.get("from"),
            "to": relation.get("to"),
            "connector_type": relation.get("relation_type"),
            "label": relation.get("label"),
        }
        for relation in plan.get("relations", [])
    ]
    return {
        "ok": True,
        "block_count": len(blocks),
        "connector_count": len(connectors),
        "sample_blocks": blocks[:2],
        "sample_connectors": connectors[:2],
    }


def build_doc_preview(plan: Dict[str, Any]) -> Dict[str, Any]:
    message = plan.get("message", {}) if isinstance(plan.get("message"), dict) else {}
    paragraphs = [message.get("title", "")]
    if message.get("subtitle"):
        paragraphs.append(message["subtitle"])
    if message.get("core_takeaway"):
        paragraphs.append(f"核心结论：{message['core_takeaway']}")

    primary_blocks = [
        block for block in plan.get("blocks", []) if isinstance(block, dict) and block.get("visual_role") == "primary"
    ]
    for block in primary_blocks[:3]:
        paragraphs.append(f"- {block.get('title', '')}：{block.get('content', '')}")

    delivery = plan.get("delivery", {}) if isinstance(plan.get("delivery"), dict) else {}
    if delivery.get("doc_mode") == "companion-detail" and message.get("cta"):
        paragraphs.append(f"后续文档展开：{message['cta']}")

    return {
        "ok": True,
        "paragraph_count": len([p for p in paragraphs if p]),
        "sample_paragraphs": [p for p in paragraphs if p][:4],
    }


def validate_file(path: Path, schema: Dict[str, Any], include_plan: bool) -> Dict[str, Any]:
    raw = load_json(path)
    normalized = apply_defaults(raw)

    errors: List[str] = []
    _validate_schema_subset(normalized, schema, "$", errors)
    business_errors, warnings = validate_business_rules(raw, normalized)
    errors.extend(business_errors)

    svg_preview = build_svg_preview(normalized)
    whiteboard_preview = build_whiteboard_preview(normalized)
    doc_preview = build_doc_preview(normalized)

    result: Dict[str, Any] = {
        "file": str(path),
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "chart_family": normalized.get("chart_family"),
        "block_count": len(normalized.get("blocks", [])),
        "relation_count": len(normalized.get("relations", [])),
        "adapter_smoke": {
            "svg": svg_preview,
            "whiteboard": whiteboard_preview,
            "doc": doc_preview,
        },
    }
    if include_plan:
        result["normalized_plan"] = normalized
    return result


def summarize(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    passed = sum(1 for item in results if item["ok"])
    by_family = Counter((item.get("chart_family") or "unknown") for item in results)
    return {
        "total": len(results),
        "passed": passed,
        "failed": len(results) - passed,
        "by_chart_family": dict(sorted(by_family.items(), key=lambda kv: kv[0])),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate infographic plan JSON files.")
    parser.add_argument("infographic_plans", nargs="+", help="Path(s) to infographic plan JSON")
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA_PATH), help="Path to infographic-plan schema")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    parser.add_argument("--include-plan", action="store_true", help="Include normalized plans in output")
    args = parser.parse_args()

    schema = load_json(Path(args.schema))
    results = [validate_file(Path(path), schema, args.include_plan) for path in args.infographic_plans]
    payload = {
        "ok": all(item["ok"] for item in results),
        "summary": summarize(results),
        "results": results,
    }

    if args.pretty:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(payload, ensure_ascii=False))
    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
