---
name: video-analyzer
description: "Analyze video files by extracting keyframes with ffmpeg and using vision to understand content. Supports single and batch processing."
---

# Video Analyzer

Analyze video content using ffmpeg frame extraction + vision AI. Supports single files, batch processing, and structured reports.

## Prerequisites

- `ffmpeg` installed (`pkg install ffmpeg` in Termux, or `apt install ffmpeg`)

## Scripts

### extract_frames.sh
Single video frame extraction.

```bash
bash scripts/extract_frames.sh <video_path> <output_dir>
```

Outputs frame file paths (one per line). Density adapts to duration:
- < 30 s → 1 frame/s, max 30
- 30 s – 5 min → 1 frame / 5 s, max 60
- > 5 min → 1 frame / 15 s, max 40

### analyze_batch.sh
Batch video processing with metadata extraction.

```bash
bash scripts/analyze_batch.sh <video_file_or_directory> [output_dir]
```

For each video, outputs:
- `metadata.txt` — duration, resolution, codec, size
- `frame_XXX.jpg` — extracted keyframes

## Workflow

1. **Extract** — Run the appropriate script
2. **Analyze** — Pick 3–5 evenly spaced frames, pass to `image` tool with prompt: "Describe this video's content based on these keyframes"
3. **Report** — Summarize findings in structured format

## Report Template

```markdown
## Video Analysis Report

**File:** <filename>
**Duration:** <duration> | **Resolution:** <WxH> | **Size:** <size>

### Content Summary
<concise description of what happens in the video>

### Key Observations
- <observation 1>
- <observation 2>
- <observation 3>
```

## Tips

- Clean up frames after analysis: `rm -rf <output_dir>`
- Common Android video locations: `/sdcard/Movies/`, `/sdcard/DCIM/Camera/`, `/sdcard/Pictures/WeiXin/`, `/sdcard/Pictures/QQ/`
- For audio transcription: `ffmpeg -i <video> -vn -acodec pcm_s16le -ar 16000 output.wav`
