#!/usr/bin/env python3
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--speed", type=float, default=1.0)
    parser.add_argument("--retries", type=int, default=4)
    args = parser.parse_args()

    if not 0.5 <= args.speed <= 2.0:
        parser.error("--speed must be between 0.5 and 2.0")

    for dependency in ("edge-tts", "ffmpeg"):
        if shutil.which(dependency) is None:
            print(f"Missing dependency: {dependency}", file=sys.stderr)
            return 1

    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    lines = manifest.get("lines")
    if not isinstance(lines, list) or not lines:
        print("Manifest must contain a non-empty lines array.", file=sys.stderr)
        return 1

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    for line in lines:
        required = ("id", "voice", "rate", "pitch", "text")
        if any(key not in line for key in required):
            print(f"Invalid line entry: {line}", file=sys.stderr)
            return 1

        media = out / f"{line['id']}.mp3"
        wave = out / f"{line['id']}.wav"
        metadata = out / f"{line['id']}.json"
        fingerprint_source = json.dumps(
            {
                "voice": line["voice"],
                "rate": line["rate"],
                "pitch": line["pitch"],
                "volume": line.get("volume", "+0%"),
                "text": line["text"],
                "speed": args.speed,
            },
            ensure_ascii=False,
            sort_keys=True,
        ).encode("utf-8")
        fingerprint = hashlib.sha256(fingerprint_source).hexdigest()
        previous = {}
        if metadata.exists():
            previous = json.loads(metadata.read_text(encoding="utf-8"))
        if (
            wave.exists()
            and wave.stat().st_size > 0
            and previous.get("fingerprint") == fingerprint
        ):
            continue

        command = [
            "edge-tts",
            "--voice", str(line["voice"]),
            f"--rate={line['rate']}",
            f"--pitch={line['pitch']}",
            f"--volume={line.get('volume', '+0%')}",
            "--text", str(line["text"]),
            "--write-media", str(media),
        ]

        for attempt in range(1, args.retries + 1):
            media.unlink(missing_ok=True)
            try:
                run(command)
                break
            except subprocess.CalledProcessError:
                if attempt == args.retries:
                    raise
                time.sleep(attempt * 2)

        filters = [
            f"atempo={args.speed:.4f}",
            "highpass=f=65",
            "lowpass=f=14500",
            "acompressor=threshold=-20dB:ratio=1.7:attack=18:release=140",
            "alimiter=limit=0.94",
        ]
        run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-i", str(media),
            "-af", ",".join(filters),
            "-ar", "48000", "-ac", "1", str(wave),
        ])
        metadata.write_text(
            json.dumps({"fingerprint": fingerprint}, indent=2),
            encoding="utf-8",
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
