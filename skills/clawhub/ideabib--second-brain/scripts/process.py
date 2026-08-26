#!/usr/bin/env python3
"""
Second Brain Processor - Buntea's knowledge ingestion engine.
Usage: python3 process.py <url_or_text> [--type auto|article|video|note]
"""

import sys
import json
import uuid
import re
import os
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

KNOWLEDGE_DIR = Path(__file__).parent
ENTRIES_DIR = KNOWLEDGE_DIR / "entries"
INDEX_FILE = KNOWLEDGE_DIR / "index.json"
MEDIA_DIR = KNOWLEDGE_DIR / "media"
MEDIA_DIR.mkdir(exist_ok=True)

CATEGORIES = [
    "work-career",
    "learning-tech",
    "health-fitness",
    "entertainment",
    "ideas-projects",
    "uncategorized"
]

def detect_type(text: str) -> str:
    """Detect content type from input."""
    text = text.strip()
    url_pattern = re.compile(r'https?://\S+')
    match = url_pattern.search(text)
    if not match:
        return "note"
    url = match.group(0)
    domain = urlparse(url).netloc.lower()
    video_domains = ["youtube.com", "youtu.be", "twitter.com", "x.com", "tiktok.com", "instagram.com", "vimeo.com"]
    if any(d in domain for d in video_domains):
        return "video"
    return "article"

def extract_url(text: str) -> str:
    match = re.search(r'https?://\S+', text.strip())
    return match.group(0) if match else ""

def _validate_entry_path(path: Path) -> Path:
    """Ensure entry path stays within ENTRIES_DIR (path traversal shield)."""
    resolved = path.resolve()
    base = ENTRIES_DIR.resolve()
    if not str(resolved).startswith(str(base)):
        raise ValueError(f"Path traversal blocked: {resolved} escapes {base}")
    return resolved

def save_entry(entry: dict) -> Path:
    """Save entry JSON and update index atomically."""
    slug = re.sub(r'[^a-z0-9]+', '-', entry['title'].lower())[:50].strip('-') or 'untitled'
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}-{slug}-{entry['id'][:8]}.json"
    entry_path = ENTRIES_DIR / filename
    entry_path = _validate_entry_path(entry_path)

    with open(entry_path, 'w') as f:
        json.dump(entry, f, indent=2)
    os.chmod(entry_path, 0o600)  # Strict file permissions

    # Atomic index update: read → write temp → rename
    with open(INDEX_FILE, 'r') as f:
        index = json.load(f)
    index['entries'].append({
        "id": entry['id'],
        "title": entry['title'],
        "type": entry['type'],
        "category": entry['category'],
        "tags": entry['tags'],
        "url": entry.get('url', ''),
        "saved_at": entry['saved_at'],
        "file": str(filename)
    })

    # Atomic write via temp file + rename
    fd, tmp_path = tempfile.mkstemp(dir=str(KNOWLEDGE_DIR), suffix='.tmp')
    try:
        with os.fdopen(fd, 'w') as f:
            json.dump(index, f, indent=2)
        os.chmod(tmp_path, 0o600)
        os.replace(tmp_path, str(INDEX_FILE))
    except Exception:
        os.unlink(tmp_path)
        raise

    return entry_path

def extract_video_frames(url: str, entry_id: str) -> list:
    """Download video and extract frames for AI analysis."""
    frame_dir = MEDIA_DIR / entry_id
    frame_dir.mkdir(exist_ok=True)
    ffmpeg_path = os.path.expanduser("~/.local/bin/ffmpeg")

    # Find yt-dlp
    import shutil
    ytdlp = shutil.which("yt-dlp") or str(Path(sys.executable).parent / "yt-dlp")

    video_file = frame_dir / "video.mp4"
    try:
        subprocess.run([
            ytdlp, "--", url,  # positional isolation prevents option injection
            "--format", "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]/best[height<=720]",
            "--output", str(video_file),
            "--no-playlist",
            "--quiet"
        ], timeout=120, check=True)
    except Exception as e:
        return [], str(e)

    # Extract 6 evenly spaced frames
    frames = []
    try:
        result = subprocess.run([
            ffmpeg_path, "-i", str(video_file),
            "-vf", "fps=1/10,scale=640:-1",
            "-frames:v", "6",
            str(frame_dir / "frame_%02d.jpg"),
            "-y", "-loglevel", "quiet"
        ], timeout=60, capture_output=True)
        frames = sorted(frame_dir.glob("frame_*.jpg"))
    except Exception as e:
        pass

    return [str(f) for f in frames], None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No input provided"}))
        sys.exit(1)

    input_text = " ".join(sys.argv[1:])
    content_type = detect_type(input_text)
    url = extract_url(input_text)

    result = {
        "input": input_text,
        "detected_type": content_type,
        "url": url,
        "entry_id": str(uuid.uuid4())
    }

    if content_type == "video" and url:
        frames, err = extract_video_frames(url, result["entry_id"])
        result["frames"] = frames
        result["frame_error"] = err
    
    print(json.dumps(result, indent=2))
