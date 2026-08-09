---
name: youtube-transcript
description: Fetch and save YouTube video transcripts as clean plain text. Use when the user provides a YouTube URL or wants to extract a transcript from a podcast, interview, or talk.
---

# YouTube Transcript

Extracts clean, deduplicated plain-text transcripts from YouTube videos using `yt-dlp`.

## Dependencies

- `yt-dlp` (must be installed and on PATH)
- Python 3.10+

## Usage

Fetch a transcript and save it to a file:

```bash
python3 .pi/skills/youtube-transcript/yt_transcript.py "YOUTUBE_URL" -o transcript.txt
```

Options:
- `-l LANG` — subtitle language code (default: `en`)
- `-o FILE` — output file path (default: stdout)

## Workflow

When the user gives a YouTube URL:

1. **Fetch transcript** — Run the script, optionally with `-o <path>` to save to a file.
2. **Review** — Read through the transcript and summarise the key points if the user asks.
