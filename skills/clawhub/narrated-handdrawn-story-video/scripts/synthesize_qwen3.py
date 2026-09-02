#!/usr/bin/env python3
"""Synthesize a multi-role local Qwen3-TTS voice plan into audio clips.

The input plan intentionally keeps each clip's text identical to its subtitle.
Use `mode: voice-design` for custom narrator/character voices, or
`mode: custom-voice` with a built-in Qwen speaker in each voice definition.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import soundfile as sf
import torch
from huggingface_hub import snapshot_download
from qwen_tts import Qwen3TTSModel

VOICE_DESIGN = "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign"
CUSTOM_VOICE = "Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice"


def device_for(value: str) -> str:
    if value != "auto":
        return value
    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def require_plan(plan: dict) -> None:
    if plan.get("mode", "voice-design") not in {"voice-design", "custom-voice"}:
        raise ValueError("mode must be voice-design or custom-voice")
    if not isinstance(plan.get("voices"), dict) or not plan["voices"]:
        raise ValueError("voices must be a non-empty object")
    if not isinstance(plan.get("segments"), list) or not plan["segments"]:
        raise ValueError("segments must be a non-empty array")
    seen: set[str] = set()
    for segment in plan["segments"]:
        identifier = segment.get("id")
        if not identifier or identifier in seen:
            raise ValueError("each segment needs a unique id")
        seen.add(identifier)
        if segment.get("speaker") not in plan["voices"]:
            raise ValueError(f"{identifier}: speaker must be defined in voices")
        if not segment.get("text") or not segment.get("output"):
            raise ValueError(f"{identifier}: text and output are required")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("plan", type=Path)
    parser.add_argument("public_dir", type=Path)
    parser.add_argument("--device", choices=["auto", "cpu", "cuda", "mps"], default="auto")
    parser.add_argument("--allow-download", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    require_plan(plan)
    mode = plan.get("mode", "voice-design")
    model_id = plan.get("model", VOICE_DESIGN if mode == "voice-design" else CUSTOM_VOICE)
    model_path = plan.get("model_path") or snapshot_download(model_id, local_files_only=not args.allow_download)
    device = device_for(args.device)
    model = Qwen3TTSModel.from_pretrained(
        model_path, device_map=device,
        dtype=torch.float16 if device in {"cuda", "mps"} else torch.float32,
        attn_implementation="eager",
    )
    language = plan.get("language", "Chinese")
    for segment in plan["segments"]:
        output = args.public_dir / segment["output"]
        if output.exists() and not args.overwrite:
            print(f"Skip {output}")
            continue
        voice = plan["voices"][segment["speaker"]]
        instruction = "。".join(part for part in [voice.get("instruct", "").strip(), segment.get("instruct", "").strip()] if part)
        kwargs = {"text": segment["text"], "language": segment.get("language", language), "instruct": instruction or None}
        if mode == "voice-design":
            wavs, rate = model.generate_voice_design(**kwargs)
        else:
            speaker = voice.get("speaker")
            if not speaker:
                raise ValueError(f"{segment['speaker']}: custom-voice requires speaker")
            wavs, rate = model.generate_custom_voice(**kwargs, speaker=speaker)
        output.parent.mkdir(parents=True, exist_ok=True)
        sf.write(output, wavs[0], rate)
        print(f"Wrote {output}")
        if device == "mps":
            torch.mps.empty_cache()


if __name__ == "__main__":
    main()
