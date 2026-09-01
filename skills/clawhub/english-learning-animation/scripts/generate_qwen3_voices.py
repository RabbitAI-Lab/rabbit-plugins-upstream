#!/usr/bin/env python3
"""Generate role-separated Qwen3-TTS VoiceDesign WAVs from a manifest."""
import argparse
import json
from pathlib import Path

import soundfile as sf
import torch
from qwen_tts import Qwen3TTSModel


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--model", required=True, help="Local Qwen3-TTS VoiceDesign checkpoint")
    parser.add_argument(
        "--device",
        default="auto",
        choices=("auto", "cuda", "mps", "cpu"),
        help="Inference device. auto prefers CUDA, then Apple MPS, then CPU.",
    )
    parser.add_argument(
        "--dtype",
        default="auto",
        choices=("auto", "bfloat16", "float32"),
    )
    args = parser.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    out_dir = Path(data["output_dir"])
    if not out_dir.is_absolute():
        out_dir = args.manifest.resolve().parent / out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    device = args.device
    if device == "auto":
        if torch.cuda.is_available():
            device = "cuda"
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            device = "mps"
        else:
            device = "cpu"
    dtype = args.dtype
    if dtype == "auto":
        dtype = "float32" if device == "cpu" else "bfloat16"
    torch_dtype = torch.float32 if dtype == "float32" else torch.bfloat16
    generation = data.get("generation", {})
    base_seed = int(generation.get("seed", 2026))
    temperature = float(generation.get("temperature", 0.72))
    top_p = float(generation.get("top_p", 0.9))
    print(f"loading Qwen3-TTS on {device} with {dtype}")
    model = Qwen3TTSModel.from_pretrained(
        args.model,
        device_map=device,
        dtype=torch_dtype,
        attn_implementation=None,
    )
    for index, segment in enumerate(data["segments"]):
        instruction = segment.get("voice_instruction")
        if not instruction:
            instruction = " ".join(
                part.strip()
                for part in (
                    segment.get("voice_profile", ""),
                    segment.get("performance", ""),
                )
                if part.strip()
            )
        seed = int(segment.get("seed", base_seed + index))
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
        wavs, sample_rate = model.generate_voice_design(
            text=segment["text"],
            language="English",
            instruct=instruction,
            temperature=temperature,
            top_p=top_p,
        )
        target = out_dir / segment["file"]
        sf.write(target, wavs[0], sample_rate)
        print(f"{target} (seed={seed})")


if __name__ == "__main__":
    main()
