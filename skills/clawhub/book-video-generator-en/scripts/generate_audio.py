#!/usr/bin/env python3
"""
3-Minute Book Digest — English TTS generation script
Default engine: Volcano Engine TTS (Doubao Speech 2.0, requires API Key),
fallback: edge-tts (Microsoft free TTS).

Volcano: V1 API + X-Api-Key auth, TTS 2.0 voice, word timestamps estimated
         from returned audio duration.
edge-tts: native WordBoundary word timestamps, precise sync.

Environment variables:
  VOLC_TTS_API_KEY  Volcano Engine API Key (from the new console)

Usage:
  # Single clip (auto engine selection)
  python generate_audio.py --text "Hello world" --output audio.mp3

  # Specify engine
  python generate_audio.py --text "Hello world" --output audio.mp3 --engine edge

  # Batch
  python generate_audio.py --batch captions.json --output-dir audio/

  # List available voices
  python generate_audio.py --list-voices
"""

import asyncio
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request
import uuid


# ── Volcano Engine TTS (V1 API + X-Api-Key) ──────────────────────

VOLC_TTS_URL = "https://openspeech.bytedance.com/api/v1/tts"
VOLC_TTS_RESOURCE_ID = "seed-tts-2.0"

# Volcano Engine TTS 2.0 English voices (suitable for book narration)
# NOTE: verify exact voice_type IDs against the current Volcano console.
VOLC_DEFAULT_VOICE = "en_us_amy"

VOLC_VOICES = {
    "en_us_amy": "Amy (female, warm — recommended for books)",
    "en_us_emma": "Emma (female, soft)",
    "en_us_helen": "Helen (female, clear)",
    "en_us_brian": "Brian (male, deep)",
    "en_us_harry": "Harry (male, energetic)",
    "en_us_ryan": "Ryan (male, neutral)",
}

# Natural English narration speed (1.0 = native pace; Chinese workflow used 1.2x)
VOLC_SPEED_RATIO = 1.0


def _volc_tts(text: str, output_path: str, speaker: str,
              api_key: str) -> tuple:
    """Call Volcano Engine V1 API to generate TTS audio.

    Uses X-Api-Key auth + seed-tts-2.0 resource ID + TTS 2.0 voice.
    Word timestamps are estimated from the returned audio duration
    (TTS 2.0 does not natively return timestamps).

    Returns: (audio_path, words_path)
    """
    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": api_key,
        "X-Api-Resource-Id": VOLC_TTS_RESOURCE_ID,
    }

    body = json.dumps({
        "app": {
            "appid": "api_key",
            "token": "api_key",
            "cluster": "volcano_tts",
        },
        "user": {"uid": "book-video-generator-en"},
        "audio": {
            "voice_type": speaker,
            "encoding": "mp3",
            "speed_ratio": VOLC_SPEED_RATIO,
        },
        "request": {
            "reqid": str(uuid.uuid4()),
            "text": text,
            "text_type": "plain",
            "operation": "query",
            "with_timestamp": 1,
        },
    }).encode("utf-8")

    req = urllib.request.Request(
        VOLC_TTS_URL, data=body, headers=headers, method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Volcano TTS HTTP error {e.code}: {err_body}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Volcano TTS network error: {e.reason}") from e

    result = json.loads(raw)

    code = result.get("code", -1)
    if code != 3000:
        message = result.get("message", "unknown error")
        raise RuntimeError(f"Volcano TTS error (code={code}): {message}")

    # Decode audio data
    audio_data = base64.b64decode(result["data"])

    # Get audio duration (ms)
    addition = result.get("addition", {})
    duration_ms = int(addition.get("duration", 0))

    # Estimate word timestamps (TTS 2.0 has no native timestamps)
    words = _estimate_word_timestamps(text, duration_ms)

    # Write files
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(audio_data)

    words_path = output_path.rsplit(".", 1)[0] + ".words.json"
    with open(words_path, "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)

    return output_path, words_path


# ── Word-level timestamp estimation ──────────────────────────────

# Punctuation (occupies time but is not spoken)
_PUNCT_CHARS = set(".,!?;:…'\"()[]{} \n\t\r")


def _estimate_word_timestamps(text: str, duration_ms: int) -> list:
    """Estimate word-level timestamps from text length and audio duration.

    TTS 2.0 does not natively return word timestamps, so we distribute
    duration evenly. Punctuation gets a smaller weight (simulating natural
    pauses).

    Args:
        text: original subtitle text
        duration_ms: audio duration (milliseconds)

    Returns: [{"text": "w", "start": 0.0, "end": 0.3}, ...]
    """
    if not text or duration_ms <= 0:
        return []

    duration_s = duration_ms / 1000.0

    # Process character by character (keep punctuation to match build_phrases)
    chars = list(text)

    # Weight per character: normal = 1.0, punctuation = 0.25
    weights = []
    for c in chars:
        if c in _PUNCT_CHARS:
            weights.append(0.25)
        else:
            weights.append(1.0)

    total_weight = sum(weights)
    if total_weight <= 0:
        return []

    words = []
    current_time = 0.0
    for c, w in zip(chars, weights):
        char_duration = (w / total_weight) * duration_s
        words.append({
            "text": c,
            "start": round(current_time, 3),
            "end": round(current_time + char_duration, 3),
        })
        current_time += char_duration

    return words


# ── edge-tts (fallback, native WordBoundary) ────────────────────

EDGE_DEFAULT_VOICE = "en-US-AriaNeural"

EDGE_VOICES = {
    "en-US-AriaNeural": "Aria (female, friendly)",
    "en-US-GuyNeural": "Guy (male, warm)",
    "en-US-JennyNeural": "Jenny (female, casual)",
    "en-US-ChristopherNeural": "Christopher (male, deep)",
    "en-GB-SoniaNeural": "Sonia (female, British)",
    "en-GB-RyanNeural": "Ryan (male, British)",
}

# Slight pace-up for narration (English native pace is already brisk)
EDGE_RATE = "+10%"


async def _edge_tts(text: str, output_path: str, voice: str) -> tuple:
    """Generate TTS audio with edge-tts (fallback).

    Native WordBoundary word timestamps, precise sync.

    Returns: (audio_path, words_path)
    """
    try:
        import edge_tts
    except ImportError:
        print("Installing edge-tts...")
        os.system(f"{sys.executable} -m pip install edge-tts -q")
        import edge_tts

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    communicate = edge_tts.Communicate(text, voice, boundary="WordBoundary",
                                       rate=EDGE_RATE)

    audio_data = b""
    words = []

    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data += chunk["data"]
        elif chunk["type"] == "WordBoundary":
            offset = chunk["offset"] / 1e7
            duration = chunk["duration"] / 1e7
            words.append({
                "text": chunk["text"],
                "start": round(offset, 3),
                "end": round(offset + duration, 3),
            })

    with open(output_path, "wb") as f:
        f.write(audio_data)

    words_path = output_path.rsplit(".", 1)[0] + ".words.json"
    with open(words_path, "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)

    return output_path, words_path


# ── Unified interface ────────────────────────────────────────────

def _detect_engine(engine: str, voice: str) -> str:
    """Auto-detect which TTS engine to use.

    Priority:
    1. explicit --engine
    2. voice name match (_uranus_bigtts/_tob → volcano, *Neural → edge)
    3. VOLC_TTS_API_KEY env present → volcano
    4. fall back to edge
    """
    if engine != "auto":
        return engine

    # Infer from voice name
    if "_uranus_bigtts" in voice or "_tob" in voice:
        return "volcano"
    if "Neural" in voice:
        return "edge"

    # Infer from env
    api_key = os.environ.get("VOLC_TTS_API_KEY", "")
    if api_key:
        return "volcano"

    return "edge"


def generate_audio(text: str, output_path: str, voice: str = "",
                   engine: str = "auto") -> tuple:
    """Generate a single TTS audio clip (unified interface).

    Auto-selects engine:
    - Volcano Engine TTS (default, needs VOLC_TTS_API_KEY)
    - edge-tts (fallback, free, no config)

    Args:
        text: text to synthesize
        output_path: output MP3 path
        voice: voice name (empty → engine default)
        engine: "auto" | "volcano" | "edge"

    Returns: (audio_path, words_path)

    A .words.json word-timestamp file is generated next to output_path.
    """
    detected = _detect_engine(engine, voice)

    if detected == "volcano":
        api_key = os.environ.get("VOLC_TTS_API_KEY", "")
        if not api_key:
            print("[warn] Volcano TTS missing API Key (VOLC_TTS_API_KEY), "
                  "auto-switching to edge-tts")
            detected = "edge"
            if not voice or "_uranus_bigtts" in voice or "_tob" in voice:
                voice = EDGE_DEFAULT_VOICE
        else:
            if not voice:
                voice = VOLC_DEFAULT_VOICE

    if detected == "edge":
        if not voice or "_uranus_bigtts" in voice or "_tob" in voice:
            voice = EDGE_DEFAULT_VOICE

    if detected == "volcano":
        return _volc_tts(text, output_path, voice, api_key)
    else:
        return asyncio.run(_edge_tts(text, output_path, voice))


def batch_generate(captions: list, output_dir: str, voice: str = "",
                   engine: str = "auto") -> list:
    """Batch-generate TTS audio + word timestamps for multiple subtitles.

    Args:
        captions: list of subtitle strings
        output_dir: output directory
        voice: voice name (empty → default)
        engine: "auto" | "volcano" | "edge"

    Returns: [audio_path, ...]
    """
    detected = _detect_engine(engine, voice)
    engine_label = "Volcano" if detected == "volcano" else "edge-tts"
    print(f"TTS engine: {engine_label}")

    results = []
    for i, text in enumerate(captions):
        output = os.path.join(output_dir, f"audio_{i:03d}.mp3")
        audio_path, words_path = generate_audio(text, output, voice, detected)
        results.append(audio_path)
        print(f"[{i+1}/{len(captions)}] {os.path.basename(audio_path)} "
              f"(+ {os.path.basename(words_path)}, {len(text)} chars)")
    return results


# ── CLI ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="TTS voice generation (Volcano default / edge-tts fallback, with word timestamps)"
    )
    parser.add_argument("--text", type=str, help="Subtitle text")
    parser.add_argument("--output", type=str, default="audio.mp3", help="Output path")
    parser.add_argument("--voice", type=str, default="",
                        help="Voice (empty=default; Volcano: en_us_amy / edge: en-US-AriaNeural)")
    parser.add_argument("--engine", type=str, default="auto",
                        choices=["auto", "volcano", "edge"],
                        help="TTS engine: auto / volcano / edge")
    parser.add_argument("--batch", type=str,
                        help="Batch mode: JSON file path, format [\"text1\",\"text2\",...]")
    parser.add_argument("--output-dir", type=str, default="audio_output",
                        help="Batch output directory")
    parser.add_argument("--list-voices", action="store_true",
                        help="List available voices")

    args = parser.parse_args()

    if args.list_voices:
        print("= Volcano Engine TTS 2.0 voices (requires VOLC_TTS_API_KEY) =")
        print("  Auth: X-Api-Key (single key from new console)")
        print()
        for vid, desc in VOLC_VOICES.items():
            default = " <- default" if vid == VOLC_DEFAULT_VOICE else ""
            print(f"  {vid:24s} {desc}{default}")
        print()
        print("= edge-tts voices (free, no config) =")
        for vid, desc in EDGE_VOICES.items():
            default = " <- default" if vid == EDGE_DEFAULT_VOICE else ""
            print(f"  {vid:28s} {desc}{default}")
        sys.exit(0)

    if args.batch:
        with open(args.batch, "r", encoding="utf-8") as f:
            captions = json.load(f)
        batch_generate(captions, args.output_dir, args.voice, args.engine)
    elif args.text:
        audio_path, words_path = generate_audio(
            args.text, args.output, args.voice, args.engine
        )
        print(f"Audio: {audio_path}")
        print(f"Timestamps: {words_path}")
    else:
        print("Provide --text or --batch (or --list-voices to view voices)")
        sys.exit(1)
