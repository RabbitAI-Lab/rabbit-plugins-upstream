#!/usr/bin/env python3
"""Print the newest locally cached Qwen3-TTS VoiceDesign checkpoint."""

import argparse
import os
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument(
    "--cache-dir",
    type=Path,
    help="Hugging Face cache root; defaults to HF_HOME or ~/.cache/huggingface.",
)
args = parser.parse_args()

cache = args.cache_dir
if cache is None:
    cache = Path(os.environ.get("HF_HOME", Path.home() / ".cache/huggingface"))
root = (
    cache.expanduser()
    / "hub/models--Qwen--Qwen3-TTS-12Hz-1.7B-VoiceDesign/snapshots"
)
choices = [p for p in root.glob("*") if p.is_dir()]
if not choices:
    raise SystemExit(f"No local Qwen3-TTS VoiceDesign snapshot found under {root}")
print(max(choices, key=lambda p: p.stat().st_mtime))
