#!/usr/bin/env python3
"""Reject stale phrase cards and missing scene-topic metadata before rendering."""

import argparse
import json
import re
from pathlib import Path


def visible_copy(data: dict) -> list[str]:
    copy: list[str] = []
    for scene in data.get("scenes", []):
        copy.extend(str(scene.get("caption", {}).get(key, "")) for key in ("title", "subtitle"))
    for row in data.get("narration", []):
        copy.extend(str(row.get(key, "")) for key in ("text", "caption"))
    for cards in data.get("phrase_cards", {}).values():
        if isinstance(cards, list):
            copy.extend(str(card) for card in cards)
    return copy


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("script", type=Path)
    parser.add_argument("--video-source", type=Path)
    args = parser.parse_args()
    data = json.loads(args.script.read_text(encoding="utf-8"))
    contract = data.get("semantic_contract")
    errors: list[str] = []
    if not isinstance(contract, dict):
        errors.append("semantic_contract is required for topic-to-visual validation")
        contract = {}
    for key in ("topic", "setting", "scene_visual_brief"):
        if not str(contract.get(key, "")).strip():
            errors.append(f"semantic_contract.{key} must be non-empty")
    required_tags = contract.get("required_scene_tags")
    if not isinstance(required_tags, list) or not all(str(tag).strip() for tag in required_tags):
        errors.append("semantic_contract.required_scene_tags must be a non-empty tag list")
        required_tags = []
    required = {str(tag).strip().lower() for tag in required_tags}
    for scene in data.get("scenes", []):
        tags = {str(tag).strip().lower() for tag in scene.get("semantic_tags", [])}
        if not tags:
            errors.append(f"scene {scene.get('id', '<unknown>')}: semantic_tags are required")
        elif required and not tags.intersection(required):
            errors.append(f"scene {scene.get('id', '<unknown>')}: no tag matches the topic contract")

    narrator_ids = {str(row.get("id")) for row in data.get("narration", []) if row.get("speaker") == "narrator"}
    phrase_cards = data.get("phrase_cards", {})
    if not isinstance(phrase_cards, dict):
        errors.append("phrase_cards must be an object keyed by narrator segment id")
    else:
        for segment_id, cards in phrase_cards.items():
            if segment_id not in narrator_ids:
                errors.append(f"phrase_cards.{segment_id}: must belong to a narrator segment")
            if not isinstance(cards, list) or not cards or not all(str(card).strip() for card in cards):
                errors.append(f"phrase_cards.{segment_id}: must be a non-empty string list")

    haystack = "\n".join(visible_copy(data)).lower()
    for term in contract.get("prohibited_terms", []):
        normalized = str(term).strip().lower()
        if normalized and normalized in haystack:
            errors.append(f"prohibited stale term appears in visible copy: {term}")

    if args.video_source and args.video_source.exists():
        source = args.video_source.read_text(encoding="utf-8")
        if "phrase_cards" not in source:
            errors.append("video renderer must read phrase_cards from script.json")
        if re.search(r"const words\s*=\s*segment\.id", source):
            errors.append("video renderer contains hard-coded segment-id phrase-card logic")

    if errors:
        raise SystemExit("\n".join(errors))
    print("semantic topic, scene tags, and data-driven phrase cards are valid")


if __name__ == "__main__":
    main()
