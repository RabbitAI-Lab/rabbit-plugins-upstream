#!/usr/bin/env python3
"""Whisper transcription of Teach narration audio.

Extracts the audio track from the recording to 16k mono wav, then runs local
Whisper if available. Degrades gracefully: prints WHISPER_MISSING with install
guidance when neither the `whisper` CLI nor `python -m whisper` is present, so
the teach skill can fall back to a written step list.

Usage:
    python3 transcribe.py <video.mp4> [--model base]
"""
import sys
import os
import shutil
import tempfile
import subprocess


def extract_audio(video: str, wav: str) -> None:
    subprocess.run(
        ["ffmpeg", "-y", "-i", video, "-vn", "-ac", "1", "-ar", "16000",
         "-f", "wav", wav],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def run_whisper(wav: str, model: str) -> str:
    out_dir = tempfile.mkdtemp(prefix="teach_whisper_")
    if shutil.which("whisper"):
        subprocess.run(
            ["whisper", wav, "--model", model, "--output_format", "txt",
             "--output_dir", out_dir],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    else:
        subprocess.run(
            [sys.executable, "-m", "whisper", wav, "--model", model,
             "--output_format", "txt", "--output_dir", out_dir],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    txt = os.path.join(out_dir, os.path.splitext(os.path.basename(wav))[0] + ".txt")
    return open(txt, encoding="utf-8").read()


def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit("usage: transcribe.py <video.mp4> [--model base]")
    video = args[0]
    model = "base"
    for i, a in enumerate(args):
        if a == "--model" and i + 1 < len(args):
            model = args[i + 1]

    wav = os.path.join(tempfile.mkdtemp(prefix="teach_audio_"), "narration.wav")
    try:
        extract_audio(video, wav)
    except Exception as e:
        print(f"AUDIO_EXTRACT_FAILED {e}", file=sys.stderr)
        sys.exit(1)

    if not (shutil.which("whisper") or _has_whisper_module()):
        print("WHISPER_MISSING")
        print("Install local Whisper to enable narration transcription:")
        print("  pip install openai-whisper")
        print("Then re-run, or fall back to a written step list from the user.")
        sys.exit(0)

    try:
        transcript = run_whisper(wav, model)
    except Exception as e:
        print(f"WHISPER_FAILED {e}", file=sys.stderr)
        sys.exit(1)

    print("TRANSCRIPT_START")
    print(transcript.strip())
    print("TRANSCRIPT_END")


def _has_whisper_module() -> bool:
    try:
        import importlib.util
        return importlib.util.find_spec("whisper") is not None
    except Exception:
        return False


if __name__ == "__main__":
    main()
