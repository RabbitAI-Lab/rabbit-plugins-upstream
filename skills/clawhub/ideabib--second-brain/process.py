#!/usr/bin/env python3
"""
Second Brain Content Processor - Knowledge Ingestion & Security Screening Engine.
Usage: python3 process.py <url_or_text> [--type auto|article|video|note]
"""

import sys
import json
import uuid
import re
import os
import shutil
import tempfile
import subprocess
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

KNOWLEDGE_DIR = Path(__file__).resolve().parent.parent
ENTRIES_DIR = KNOWLEDGE_DIR / "entries"
INDEX_FILE = KNOWLEDGE_DIR / "index.json"
MEDIA_DIR = KNOWLEDGE_DIR / "media"

ENTRIES_DIR.mkdir(parents=True, exist_ok=True)
MEDIA_DIR.mkdir(parents=True, exist_ok=True)

CATEGORIES = [
    "work-career",
    "learning-tech",
    "health-fitness",
    "entertainment",
    "ideas-projects",
    "uncategorized"
]

# Patterns for Step 2.5 Security Screening
SUSPICIOUS_PATTERNS = [
    (r"(?i)tell\s+your\s+agent", "Agent-directed instruction detected"),
    (r"(?i)have\s+it\s+(run|fetch|install|execute|list)", "Agent directive to execute external command"),
    (r"(?i)bypass\s+(rate\s*limit|quota|auth|restriction|paywall)", "Attempt to bypass rate limits/auth restrictions"),
    (r"(?i)(reset\s*credit|share\s*api\s*key|pool\s*credentials)", "Credential pooling or credit exploitation pattern"),
    (r"(?i)(exfiltrate|send\s+tokens?|dump\s+env|paste\s+credentials?)", "Data or credential exfiltration request"),
    (r"(?i)disable\s+safety\s+checks?", "Request to disable security controls"),
    (r"(?i)(one-shot\s*only|before\s*they\s*expire|act\s*now)", "Urgency/scarcity manipulation pattern"),
]


def clean_url(url: str) -> str:
    """Clean trailing punctuation and brackets from extracted URL."""
    return url.strip().rstrip(".,;:!?)])>\"'")


def detect_type(text: str) -> str:
    """Detect content type from input."""
    text = text.strip()
    url_pattern = re.compile(r'https?://\S+')
    match = url_pattern.search(text)
    if not match:
        return "note"
    url = clean_url(match.group(0))
    try:
        domain = urlparse(url).netloc.lower()
    except Exception:
        return "note"
    video_domains = ["youtube.com", "youtu.be", "twitter.com", "x.com", "tiktok.com", "instagram.com", "vimeo.com"]
    if any(d in domain for d in video_domains):
        return "video"
    return "article"


def extract_url(text: str) -> str:
    match = re.search(r'https?://\S+', text.strip())
    return clean_url(match.group(0)) if match else ""


def security_screen(text: str, url: str = "") -> str:
    """Scan content for agent manipulation or security bypass patterns (Step 2.5)."""
    flags = []
    combined = f"{text} {url}"
    for pattern, reason in SUSPICIOUS_PATTERNS:
        if re.search(pattern, combined):
            flags.append(reason)
    if flags:
        return "Flagged during ingestion screening: " + "; ".join(flags)
    return ""


def ensure_index_exists():
    """Ensure index.json exists with valid structure."""
    if not INDEX_FILE.exists() or INDEX_FILE.stat().st_size == 0:
        with open(INDEX_FILE, 'w', encoding='utf-8') as f:
            json.dump({"entries": []}, f, indent=2)


def sanitize_uuid(raw_id: str) -> str:
    """Ensure ID is a safe canonical UUID string to prevent path traversal."""
    try:
        return str(uuid.UUID(raw_id))
    except Exception:
        return str(uuid.uuid4())


def save_entry(entry: dict) -> Path:
    """Safely save entry JSON and atomically update index.json."""
    entry_id = sanitize_uuid(entry.get('id', ''))
    entry['id'] = entry_id

    raw_title = str(entry.get('title', 'untitled'))
    slug = re.sub(r'[^a-z0-9]+', '-', raw_title.lower()).strip('-')
    if not slug:
        slug = "entry"
    slug = slug[:50].strip('-')

    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    filename = f"{date_str}-{slug}-{entry_id[:8]}.json"
    entry_path = (ENTRIES_DIR / filename).resolve()

    # Prevent path traversal outside ENTRIES_DIR
    if not str(entry_path).startswith(str(ENTRIES_DIR.resolve())):
        raise ValueError(f"Path traversal detected in entry path: {filename}")

    # Write entry file
    with open(entry_path, 'w', encoding='utf-8') as f:
        json.dump(entry, f, indent=2, ensure_ascii=False)

    # Atomic update of index.json
    ensure_index_exists()
    try:
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
    except Exception:
        index_data = {"entries": []}

    if not isinstance(index_data, dict) or "entries" not in index_data:
        index_data = {"entries": []}

    index_record = {
        "id": entry['id'],
        "title": entry['title'],
        "type": entry['type'],
        "category": entry.get('category', 'uncategorized'),
        "tags": entry.get('tags', []),
        "url": entry.get('url', ''),
        "saved_at": entry.get('saved_at', datetime.utcnow().isoformat() + "Z"),
        "file": str(filename)
    }

    if entry.get('safety_note'):
        index_record['safety_note'] = entry['safety_note']

    # Avoid duplicate index entries
    index_data['entries'] = [e for e in index_data['entries'] if e.get('id') != entry['id']]
    index_data['entries'].append(index_record)

    # Atomic temp write + replace
    temp_dir = KNOWLEDGE_DIR
    with tempfile.NamedTemporaryFile('w', dir=temp_dir, delete=False, encoding='utf-8') as tf:
        json.dump(index_data, tf, indent=2, ensure_ascii=False)
        temp_name = tf.name

    os.replace(temp_name, INDEX_FILE)

    # Restrict permissions (defense-in-depth)
    try:
        os.chmod(entry_path, 0o600)
        os.chmod(INDEX_FILE, 0o600)
    except Exception:
        pass

    return entry_path


def extract_video_frames(url: str, entry_id: str) -> tuple:
    """Download video safely and extract frames for AI analysis."""
    safe_id = sanitize_uuid(entry_id)
    frame_dir = (MEDIA_DIR / safe_id).resolve()
    if not str(frame_dir).startswith(str(MEDIA_DIR.resolve())):
        return [], "Invalid media output directory"

    frame_dir.mkdir(parents=True, exist_ok=True)
    ffmpeg_path = os.path.expanduser("~/.local/bin/ffmpeg")
    if not os.path.exists(ffmpeg_path):
        ffmpeg_path = shutil.which("ffmpeg") or "ffmpeg"

    ytdlp = shutil.which("yt-dlp") or str(Path(sys.executable).parent / "yt-dlp")

    video_file = frame_dir / "video.mp4"
    try:
        # Use '--' to prevent URL option injection attacks
        subprocess.run([
            ytdlp,
            "--format", "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]/best[height<=720]",
            "--output", str(video_file),
            "--no-playlist",
            "--quiet",
            "--",
            url
        ], timeout=120, check=True)
    except Exception as e:
        return [], str(e)

    frames = []
    try:
        subprocess.run([
            ffmpeg_path, "-i", str(video_file),
            "-vf", "fps=1/10,scale=640:-1",
            "-frames:v", "6",
            str(frame_dir / "frame_%02d.jpg"),
            "-y", "-loglevel", "quiet"
        ], timeout=60, capture_output=True)
        frames = sorted([str(f) for f in frame_dir.glob("frame_*.jpg")])
    except Exception:
        pass

    return frames, None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No input provided"}))
        sys.exit(1)

    input_text = " ".join(sys.argv[1:])
    content_type = detect_type(input_text)
    url = extract_url(input_text)
    entry_id = str(uuid.uuid4())
    safety_note = security_screen(input_text, url)

    result = {
        "input": input_text,
        "detected_type": content_type,
        "url": url,
        "entry_id": entry_id,
        "safety_note": safety_note
    }

    if content_type == "video" and url:
        frames, err = extract_video_frames(url, entry_id)
        result["frames"] = frames
        result["frame_error"] = err

    print(json.dumps(result, indent=2, ensure_ascii=False))
