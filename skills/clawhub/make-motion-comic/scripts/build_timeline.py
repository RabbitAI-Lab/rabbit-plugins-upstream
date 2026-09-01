#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path


def probe_duration(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=nw=1:nk=1",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def srt_time(value: float) -> str:
    milliseconds = max(0, round(value * 1000))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    seconds, milliseconds = divmod(remainder, 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


def make_silence(path: Path, duration: float) -> None:
    subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono",
            "-t", str(duration), str(path),
        ],
        check=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--audio-dir", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    lines = manifest.get("lines")
    if not isinstance(lines, list) or not lines:
        parser.error("Manifest must contain a non-empty lines array.")

    audio_dir = Path(args.audio_dir).resolve()
    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)

    pause_before = float(manifest.get("pause_before", 0.65))
    initial_silence = out / "silence-initial.wav"
    make_silence(initial_silence, pause_before)

    concat_paths = [initial_silence]
    cursor = pause_before
    timed_lines = []
    shot_map: dict[int, dict] = {}
    srt_blocks = []

    for index, line in enumerate(lines, start=1):
        identifier = str(line["id"])
        shot = int(line["shot"])
        media = audio_dir / f"{identifier}.wav"
        if not media.exists():
            raise FileNotFoundError(media)

        duration = probe_duration(media)
        start = cursor
        end = start + duration
        pause_after = float(line.get("pause_after", 0.4))

        timed = dict(line)
        timed.update({"start": start, "end": end, "duration": duration})
        timed_lines.append(timed)

        if shot not in shot_map:
            shot_map[shot] = {"shot": shot, "start": start}
        shot_map[shot]["end"] = end + pause_after

        srt_blocks.append(
            f"{index}\n{srt_time(start)} --> {srt_time(end)}\n{line['text']}\n"
        )

        silence = out / f"silence-{identifier}.wav"
        make_silence(silence, pause_after)
        concat_paths.extend([media, silence])
        cursor = end + pause_after

    shots = []
    previous_end = 0.0
    for shot in sorted(shot_map.values(), key=lambda item: item["shot"]):
        shots.append({
            "shot": shot["shot"],
            "start": previous_end,
            "end": shot["end"],
            "duration": shot["end"] - previous_end,
        })
        previous_end = shot["end"]

    (out / "subtitles.srt").write_text("\n".join(srt_blocks), encoding="utf-8")
    (out / "timeline.json").write_text(
        json.dumps(
            {
                "totalDuration": cursor,
                "lineTimeline": timed_lines,
                "shotTimeline": shots,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    concat_text = "".join(
        f"file '{str(path).replace(chr(39), chr(39) + chr(92) + chr(39) + chr(39))}'\n"
        for path in concat_paths
    )
    concat_file = out / "voice-concat.txt"
    concat_file.write_text(concat_text, encoding="utf-8")
    subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-f", "concat", "-safe", "0", "-i", str(concat_file),
            "-c:a", "pcm_s16le", "-ar", "48000", "-ac", "1",
            str(out / "voice.wav"),
        ],
        check=True,
    )

    print(json.dumps({"ok": True, "duration": cursor, "shots": shots}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
