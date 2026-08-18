#!/usr/bin/env python3
"""Cross-platform ffmpeg screen recorder for the OpenClaw `teach` skill.

Records the primary display via ffmpeg and prints the ffmpeg PID + final
duration on stderr so the calling agent can track the capture. Audio is NOT
recorded by default (privacy). Pass --with-audio to also capture microphone
narration for later Whisper transcription. Stops on Ctrl-C or when the time cap
is reached.

Usage:
    python3 record.py <output.mp4> [max_seconds] [--with-audio] [--audio-device NAME]
"""
import sys
import os
import re
import subprocess
import platform
import signal


def pick_audio_device(system: str):
    """Best-effort default microphone device per OS."""
    if system == "Windows":
        try:
            out = subprocess.check_output(
                ["ffmpeg", "-list_devices", "true", "-f", "dshow", "-i", "dummy"],
                stderr=subprocess.STDOUT, text=True,
            )
            m = re.search(r'"([^"]+)"\s*\(audio\)', out)
            if m:
                return m.group(1)
        except Exception:
            pass
        return "Microphone"
    if system == "Darwin":
        return "0"          # avfoundation default audio device index
    if system == "Linux":
        return "default"    # pulse/alsa default source
    return None


def build_cmd(out_path: str, max_seconds: int, with_audio: bool, audio_device: str):
    system = platform.system()
    cmd = ["ffmpeg", "-y", "-framerate", "15"]

    if system == "Windows":
        video_in = ["-f", "gdigrab", "-i", "desktop"]
    elif system == "Darwin":
        video_in = ["-f", "avfoundation", "-i", "1"]
    elif system == "Linux":
        video_in = ["-f", "x11grab", "-i", os.environ.get("DISPLAY", ":0")]
    else:
        sys.exit(f"Unsupported OS: {system}")

    audio_in = []
    if with_audio:
        dev = audio_device or pick_audio_device(system)
        if system == "Windows":
            audio_in = ["-f", "dshow", "-i", f"audio={dev}"]
        elif system == "Darwin":
            # avfoundation takes "video:audio" as a single -i value
            video_in = ["-f", "avfoundation", "-i", f"1:{dev}"]
        elif system == "Linux":
            audio_in = ["-f", "pulse", "-i", dev]

    cmd += video_in + audio_in
    cmd += [
        "-t", str(max_seconds),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-preset", "ultrafast",
    ]
    if with_audio:
        cmd += ["-c:a", "aac"]
    cmd += [out_path]
    return cmd


def probe_duration(out_path: str):
    try:
        out = subprocess.check_output(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", out_path],
            stderr=subprocess.DEVNULL,
        ).decode().strip()
        return out or "unknown"
    except Exception:
        return "unknown"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("usage: record.py <output.mp4> [max_seconds] [--with-audio] [--audio-device NAME]")
    out_path = sys.argv[1]
    max_seconds = 600
    with_audio = False
    audio_device = None
    for i, a in enumerate(sys.argv[2:]):
        if a == "--with-audio":
            with_audio = True
        elif a == "--audio-device" and i + 3 <= len(sys.argv):
            audio_device = sys.argv[i + 3]
        elif a.lstrip("-").isdigit():
            max_seconds = int(a)

    cmd = build_cmd(out_path, max_seconds, with_audio, audio_device)
    print(f"RECORD_CMD {' '.join(cmd)}", file=sys.stderr)
    print(f"AUDIO {'on' if with_audio else 'off'}", file=sys.stderr)

    proc = subprocess.Popen(cmd, stderr=subprocess.DEVNULL)
    print(f"FFMPEG_PID {proc.pid}", file=sys.stderr)

    try:
        proc.wait()
    except KeyboardInterrupt:
        # Forward SIGINT so ffmpeg finalizes the file cleanly.
        try:
            proc.send_signal(signal.SIGINT)
        except Exception:
            pass
        try:
            proc.wait(timeout=30)
        except Exception:
            proc.kill()

    print(f"DURATION {probe_duration(out_path)}", file=sys.stderr)
    print(f"DONE {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
