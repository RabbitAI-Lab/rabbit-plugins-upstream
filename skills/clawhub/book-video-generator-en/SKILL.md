---
name: book-video-generator-en
slug: book-video-generator-en
version: 1.0.0
displayName: 三分钟精读一本书英文版
description: English 3-minute book digest video generator. Input a book title + author, one-click generate a 3-minute book review video (review script → storyboard → AI illustrations → English TTS narration → subtitles → final MP4). Trigger words: book video, 3 minute book summary, read a book in 3 minutes, book digest, make a book video. Cross-platform compatible with WorkBuddy / OpenClaw / Codex CLI / TRAE Work.
---

# 3-Minute Book Digest — English Version

## Overview

Automatically turn any book into a 3-minute explainer video: from writing the
review script, splitting it into storyboards, AI illustration, English TTS
narration, to subtitle compositing — fully automated.

Derived from the Coze workflow "Pipadushu_video_1". This Skill follows the
[Agent Skills open standard](https://agentskills.io) and is cross-platform
compatible with WorkBuddy, OpenClaw, Codex CLI, and TRAE Work.

It replaces Coze plugins with local open-source tools: 剪映小助手 (Jianying
assistant) → ffmpeg, Coze image generation → multi-model image generation
(default ImageGen + alternatives Volcano Seedream / Gemini / Agnes), Coze TTS →
Volcano Engine TTS (default) / edge-tts (fallback). All script, narration,
on-screen text, and prompts are **fully in English**.

## Platform Tool Mapping

This Skill's workflow involves 3 platform-related tools. Pick the matching tool
for the platform you are running on.

### Web Search (Stage 1 — search for book info)

| Platform | Tool | Notes |
|----------|------|-------|
| WorkBuddy | `WebSearch` | Built-in tool, call directly |
| OpenClaw | built-in web search | Auto-available |
| Codex CLI | `shell: curl` or search MCP | Use shell commands or install a search MCP |
| TRAE Work | built-in web search | Auto-available |

### Image Generation (Stage 4a — storyboard illustrations)

Provides **1 default + 3 alternatives**. Switch via the `IMAGE_API` env var:

| Plan | Tool | Model | Env var | Notes |
|------|------|-------|---------|-------|
| 🏠 **Default** | `ImageGen` | Tencent Hunyuan (WorkBuddy built-in) | none | Call `DeferExecuteTool` directly in WorkBuddy |
| 🏔️ Alt | `volcengine` | Volcano Seedream 5.0 lite (ByteDance) | `ARK_API_KEY` (recommended) or `VOLCENGINE_AK` + `VOLCENGINE_SK` | Original Coze image model; best for flat Chinese/English style, supports watermark removal |
| 🤖 Alt | `gemini` | Google Gemini 3 Pro Image | `GEMINI_API_KEY` | Rich detail, strong semantic understanding |
| ✨ Alt | `agnes` | Agnes AI (completely free) | `AGNES_API_KEY` | Free registration, OpenAI-compatible API |

**Switching**:
- **WorkBuddy**: uses `ImageGen` by default. To switch, set `IMAGE_API=volcengine|gemini|agnes`, the script auto-calls `scripts/generate_image.py`.
- **CLI platforms** (Codex CLI / OpenClaw): run `scripts/generate_image.py --api <plan>` directly.

> On every platform, the image prompt uses the `desc_promopt` field from the storyboard.

### LLM Calls (Stages 1-3 — script & storyboard)

Every platform has built-in LLM chat. Simply send the System Prompts from
`references/prompts.md` to the current platform's LLM.

## Input

| Param | Description | Required |
|-------|-------------|----------|
| `book_name` | Book title | Yes |
| `author_name` | Author name | Yes |
| `ip_name` | Account name (bottom watermark on cover) | No, hidden by default |

## Environment Setup

Ensure these Python dependencies are installed before running:

```bash
pip install edge-tts imageio-ffmpeg pillow
```

> Scripts auto-install missing dependencies on first run, but pre-installing avoids interruptions.

`ffmpeg` is provided automatically by the `imageio-ffmpeg` package — no separate system ffmpeg needed.

### TTS Engine Config (optional)

| Engine | Credential | Timestamps | Notes |
|--------|-----------|-----------|-------|
| Volcano Engine TTS (default) | `VOLC_TTS_API_KEY` | Estimated from audio duration | Doubao Speech 2.0, best English naturalness, commercial use, get API Key from [Volcano console](https://console.volcengine.com/speech/new) |
| edge-tts (fallback) | none | Native WordBoundary | Microsoft free TTS, works out of the box, auto-fallback when no credential |

Set the Volcano credential:
```bash
export VOLC_TTS_API_KEY="your-api-key"
```

> When `VOLC_TTS_API_KEY` is not set, the script auto-uses edge-tts — fully functional.
> Default English voice: `en-US-AriaNeural` (edge-tts) / `en_us_amy` (Volcano). See `scripts/generate_audio.py --list-voices`.

## Full Workflow (5 stages)

### Stage 1: Generate the review script

**Goal**: From book title + author, use the LLM to produce a ~1000-word, 3-minute video script.

**Steps**:
1. Use the platform's **web search tool** to find real book info (summary, interpretations, publication year).
2. Use the system prompt (see `references/prompts.md` §1) and ask the LLM to output JSON:

```json
{
  "book_name": "...",
  "author_name": "...",
  "year": "yyyy-MM",
  "content": "1000+ word book review script (hook intro + core content + key insights)",
  "category": "Book category"
}
```

**Notes**:
- Script should fit ~3 minutes of spoken narration (~450-650 words).
- The opening hook must be highly compelling.
- Source info via search to ensure accuracy.

### Stage 2: Generate the storyboard

**Goal**: Split the review script into 8-50 storyboard shots, each with subtitle text, visual description, and an AI image prompt.

**Steps**:
Use the system prompt (`references/prompts.md` §2), feed in Stage 1's `content`, output:
```json
{
  "list": [
    {
      "story_name": "Shot name",
      "desc": "Visual description",
      "cap": "Subtitle text (one sentence)",
      "desc_promopt": "Image generation prompt (English)"
    }
  ],
  "keywords": ["keyword1", "keyword2"]
}
```

Then insert the intro shot at the beginning of `list` (mirrors the original workflow node 150774):
```python
list.insert(0, {
    "story_name": "Intro",
    "desc": "Read one book every day",
    "cap": f"Read a book in 3 minutes. Today we're reading {book_name} by {author_name}.",
    "desc_promopt": "A person reading a book, flat illustration style"
})
```

**Style constraints**: flat illustration, cartoon character with clean lines, flat symbolic background, soft bright low-saturation palette.

### Stage 3: Generate the title progress bar

**Goal**: Split the script into 4 sections, each with a title of ≤6 words, shown as a progress bar at the top of the video.

**Steps**:
Use the system prompt (`references/prompts.md` §3), output 4 titles (title1-title4).

**Usage**: The 4 titles are passed to `compose_video.py` via the `chapter_titles` field in `segments.json`, rendered as a top progress bar (current section highlighted in orange + bottom progress line). Also need `segment_chapters` specifying each shot's section index (0-3); auto-distributed evenly if omitted.

Example: `["Introduction", "Core Ideas", "Practical Tips", "Conclusion"]`

### Stage 4: Generate assets (in parallel)

This stage generates all assets the video needs:

#### 4a. AI illustration generation

For each shot's `desc_promopt`, call the image generation tool. **Defaults to WorkBuddy's built-in `ImageGen` (Tencent Hunyuan); switch via `IMAGE_API` env var.**

**Unified style params** (from the original workflow's image node):
- Size: 1024x768
- Style: flat illustration
- Protagonist top #FF7F72, pants #243139
- 30% transparent glass effect background
- Negative prompt: none

**Plan selection & invocation**:

| Plan | `IMAGE_API` value | Invocation | Config needed |
|------|-------------------|-----------|---------------|
| 🏠 Tencent Hunyuan (default) | unset or `imagegen` | WorkBuddy built-in `ImageGen` tool | none |
| 🏔️ Volcano Seedream | `volcengine` | `python3 scripts/generate_image.py --api volcengine` | `ARK_API_KEY` (recommended) or `VOLCENGINE_AK` + `VOLCENGINE_SK` |
| 🤖 Google Gemini | `gemini` | `python3 scripts/generate_image.py --api gemini` | `GEMINI_API_KEY` |
| ✨ Agnes AI | `agnes` | `python3 scripts/generate_image.py --api agnes` | `AGNES_API_KEY` |

**Execution logic**:
1. If running in **WorkBuddy** and `IMAGE_API` is unset: call the `ImageGen` tool (DeferExecuteTool) directly, `prompt` = desc_promopt, `size` = "1024x768".
2. If `IMAGE_API=volcengine|gemini|agnes`: call `scripts/generate_image.py`, auto-install deps and generate via API.
3. If running on a **CLI platform** (Codex CLI, etc.): default `scripts/generate_image.py --api gemini`.

> Generated images are named `scene_000.png` ~ `scene_NNN.png`, stored in `output/{book_name}/images/`.

#### 4b. TTS voice synthesis

For each shot's `cap` (subtitle text), use the TTS engine to generate MP3 audio plus word-level timestamps (saved as a sibling `.words.json` for precise per-line subtitle sync in Stage 5).

**Dual-engine architecture**:
- **Volcano Engine TTS** (default): V1 API + X-Api-Key auth, Doubao Speech 2.0 voice, best English naturalness, commercial use, requires `VOLC_TTS_API_KEY`.
- **edge-tts** (fallback): free, no config, native WordBoundary word timestamps, auto-fallback when no Volcano credential.

**Default voices**:
- Volcano: `en_us_amy` (English female, warm — good for book narration)
- edge-tts: `en-US-AriaNeural` (Aria, female)

List all available voices: `python3 scripts/generate_audio.py --list-voices`

Run (all platforms, auto engine selection):
```bash
python3 scripts/generate_audio.py --text "<subtitle>" --output "audio_001.mp3"
```

Specify engine or voice:
```bash
# Force Volcano
python3 scripts/generate_audio.py --text "<subtitle>" --output "audio_001.mp3" --engine volcano --voice en_us_amy

# Force edge-tts
python3 scripts/generate_audio.py --text "<subtitle>" --output "audio_001.mp3" --engine edge --voice en-US-AriaNeural
```

Batch mode:
```bash
python3 scripts/generate_audio.py --batch captions.json --output-dir audio/ --voice "en-US-AriaNeural"
```

#### 4c. Opening cover image

Generate a dedicated cover image (1920x1080) for the first frame, with book title, author, and brand text.

**Steps**: run `python3 scripts/generate_cover.py`

```bash
# Use first storyboard image as blurred background (recommended, consistent style)
python3 scripts/generate_cover.py \
  --book-name "Atomic Habits" \
  --author "James Clear" \
  --output output/Atomic_Habits/images/cover.png \
  --bg output/Atomic_Habits/images/scene_000.png

# No background image, use deep-blue gradient
python3 scripts/generate_cover.py \
  --book-name "Atomic Habits" \
  --author "James Clear" \
  --output output/Atomic_Habits/images/cover.png
```

**Cover layout**:
- Top: "3-MINUTE BOOK DIGEST" brand text + orange divider line (#FF7F72, matches protagonist's top)
- Middle: book title (large, auto-wrapped, centered, 80pt)
- Lower-middle: author name (42pt)
- Bottom: account-name watermark (**optional**, via `--ip-name`; hidden if omitted)

**Fonts**: auto-detects a system English font (Windows: Arial / macOS: Helvetica / Linux: DejaVu Sans) — no manual change needed.

> The cover image is specified via the `cover` field in `segments.json` at Stage 5; it shows for `cover_duration` seconds (default 5) before the first shot, then switches back to the original shot image (narration continues uninterrupted).
>
> ```json
> {
>   "output": "output/BookName_3min_digest.mp4",
>   "cover": "output/BookName/images/cover.png",
>   "chapter_titles": ["Introduction", "Core Ideas", "Practical Tips", "Conclusion"],
>   "segment_chapters": [0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3],
>   "keywords": ["Atomic Habits", "tiny changes", "compound effect"],
>   "bgm": "assets/bgm_reading.mp3",
>   "bgm_volume": 0.15,
>   "transition_sound": "assets/transition_page_flip.mp3",
>   "transition_interval": 3,
>   "transition_volume": 0.3,
>   "segments": [
>     {"image": "images/scene_000.png", "audio": "audio/audio_000.mp3", "caption": "Subtitle text"},
>     ...
>   ]
> }
> ```
> - `cover`: optional, cover image path, shown for `cover_duration` seconds before the first shot
> - `cover_duration`: optional, cover display time (seconds), default 5.0
> - `chapter_titles`: optional, section titles for the top progress bar
> - `segment_chapters`: optional, each shot's section index (0-based); auto-distributed evenly if omitted
> - `keywords`: optional, keyword list; matched keywords in subtitles show in orange
> - `bgm`: optional, background music path; auto-looks for `assets/bgm_reading.mp3`; pass empty string to disable
> - `bgm_volume`: optional, BGM volume (0.0-1.0), default 0.15
> - `transition_sound`: optional, transition sound path; auto-looks for `assets/transition_page_flip.mp3`; pass empty string to disable
> - `transition_interval`: optional, add a transition sound every N shots, default 3
> - `transition_volume`: optional, transition sound volume (0.0-1.0), default 0.3

### Stage 5: Video composition

**Goal**: Compose all assets into the final MP4 video.

**Steps**: run `python3 scripts/compose_video.py`, which:
1. Computes each shot's duration (based on TTS audio duration + gap interval)
2. Scales/crops images to 1920x1080 (16:9)
3. Adds a **0.3s fade in/out transition** (dip-to-black) per shot
4. Uses ffmpeg to compose image + audio into video clips
5. **Progress bar overlay**: top shows section titles (current section orange highlight + filled dot, others gray + hollow dot), bottom progress line shows overall playback progress
6. Generates **per-line single-line ASS subtitles** (precise sync via TTS word timestamps, split into short single lines by punctuation + word count, white bold text + black outline, **orange keyword highlight**, **fade-in + slide-up entrance / fade-out exit animation**)
7. Concatenates all clips into the full video
8. **Audio mix**: blends background music (BGM) at low volume throughout + a page-flip transition sound every 3 shots at the boundary

**Subtitle params** (corresponds to original workflow add_captions_1 node):
- Font color: white (#FFFFFF)
- Keyword highlight: orange (#FF7F72), via ASS inline color tag `{\c&H727FFF&}`
- Outline color: black (#000000)
- Font size: 64pt (bold)
- Position: bottom center (MarginV=30)
- Font: **auto-detected** system English font (Windows: Arial / macOS: Helvetica / Linux: DejaVu Sans), no manual change
- Subtitle format: **ASS** (Advanced SubStation Alpha), supports inline color + animation tags
- **Per-line single-line display**: uses TTS word timestamps to split long subtitles into short single lines synced to speech
- **Entrance animation**: fade in 200ms + slide up 20px from below (ASS `\fad` + `\move`)
- **Exit animation**: fade out 150ms (ASS `\fad`)

**Progress bar params**:
- Position: top of frame (80px height)
- Background: semi-transparent dark (alpha=130)
- Current section: orange (#FF7F72) text + filled dot
- Other sections: gray (#AAAAAA) text + hollow dot
- Bottom progress line: orange fill + dark-gray base, shows overall progress
- Font: auto-detected system English font, 44pt

**Dynamic effect params**:
- Transition fade duration: 0.3s (auto-halved for shots shorter than 0.6s)

**Audio mix params**:
- Background music: `assets/bgm_reading.mp3` (3:56 reading BGM, auto-loop), volume 0.15
- Transition sound: `assets/transition_page_flip.mp3` (0.71s page-flip), triggered 0.5s before the end of every 3rd shot, volume 0.3
- Mix method: ffmpeg `amix` filter, BGM loop + transition sounds overlaid at time points via `adelay`

> **📌 Audio assets are optional**: Because SkillHub does not support uploading .mp3 files, audio assets are not bundled. If these files are missing from `assets/`, the video still generates fine (just without BGM and transition sounds). To add them, see `assets/README.md`.

### Output

Final output: `output/{book_name}_3min_digest.mp4`

## Cross-Platform Installation

### WorkBuddy

The skill is installed at `~/.workbuddy/skills/book-video-generator-en/`, ready to use.

### OpenClaw

```bash
# Copy to OpenClaw skills dir
cp -r ~/.workbuddy/skills/book-video-generator-en ~/.openclaw/skills/

# Or install via ClawHub (if published)
openclaw skills install book-video-generator-en
```

### Codex CLI

```bash
# 1. Enable Skills (if not yet)
echo '[features]\nskills = true' >> ~/.codex/config.toml

# 2. Copy skill dir
cp -r ~/.workbuddy/skills/book-video-generator-en ~/.codex/skills/

# 3. Restart Codex CLI
# 4. Type /skills to confirm the skill loaded
```

### TRAE Work

```
1. Open TRAE Work → Rules & Skills → Skills → Create → Import files
2. Upload SKILL.md
3. Copy scripts/ and references/ into the skill dir
```

## Original Workflow Reference

The original Coze workflow file is at `references/workflow-original.yaml`, a full chain of 30+ nodes:
```
Start → LLM (DeepSeek V3.2) generate review → Title summary → Storyboard visual description
→ Code concat intro → Batch image gen + cutout → TTS voice synthesis
→ Create Jianying draft → Batch add images/subtitles/audio → Save draft → End
```

The original flow relied on the **Jianying assistant plugin** (video composition core) and Coze's built-in **image generation + cutout** and **TTS** plugins.
This Skill replaces them with ffmpeg, edge-tts, and the platform's image generation tools.

## Quick Usage Example

User says: "Generate a 3-minute digest video of Atomic Habits by James Clear"

Execution flow:
1. Search "Atomic Habits James Clear summary review"
2. Generate review script with Stage 1 prompt
3. Generate storyboard with Stage 2 prompt
4. Generate title progress bar with Stage 3 prompt
5. For each shot: image generation tool creates illustration + TTS generates English narration (Volcano default / edge-tts fallback)
6. compose_video.py composes the final video
7. Output `output/Atomic_Habits_3min_digest.mp4`

## Resource Files

- `references/prompts.md` — all LLM prompt sources (platform-independent, reusable)
- `references/workflow-original.yaml` — original Coze workflow (full YAML backup)
- `scripts/compose_video.py` — video composition script (pure Python + ffmpeg, cross-platform, with fade transitions + auto font detection + cover support + per-line single-line ASS subtitles with precise sync + keyword highlight + entrance/exit animations + top progress bar + BGM mix + transition sounds)
- `scripts/generate_audio.py` — TTS voice script (pure Python, dual engine: Volcano TTS V1 API + X-Api-Key default / edge-tts fallback, with word timestamps, auto engine switch by credential)
- `scripts/generate_cover.py` — cover image script (pure Python + Pillow, auto-wrap + blurred background + auto font detection)
- `scripts/generate_image.py` — image generation script (Volcano / Gemini / Agnes / OpenAI / Stability / local SD)
