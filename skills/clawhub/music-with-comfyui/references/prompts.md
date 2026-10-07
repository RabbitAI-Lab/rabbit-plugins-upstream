# Prompt / Tags Reference (music-with-comfyui)

Guidance for crafting AceStep 1.5 prompts. The image-with-comfyui skill has an
analogous `prompts.md`; this one is tailored to the audio workflow.

## The two inputs

AceStep 1.5 takes two text inputs in the text-encode node:

1. **`--tags`** (required) — the music description: genre, tempo, mood,
   instrumentation, vocal style. This is the primary signal.
2. **`--lyrics`** (optional) — structured Sonic-lyrics text. Empty/instrumental
   → AceStep 1.5 generates instrumental audio.

Both are passed through the script verbatim (the ComfyUI API expects them with
ComfyUI-escaped line breaks — see below).

## Tags (music description)

Write a focused, coherent description. Think of it like a production brief:

- **Genre / style:** "Lo-fi hip hop", "80s synthwave", "orchestral trailer", "jazz piano trio"
- **Tempo / groove:** "slow and relaxed", "driving 128 BPM", "half-time 90 BPM"
- **Instrumentation:** "warm Rhodes chords", "reversed guitars", "stubby bass", "live drums"
- **Mood / atmosphere:** "melancholic", "euphoric", "smoky and intimate", "cinematic"
- **Vocal style (if any):** "female lead", "soft male falsetto", "backing harmonies", "spoken word"

Keep it natural and specific — a tight 6–12 token line usually beats a wall of
30 contradictory keywords.

### ComfyUI line-break escaping

AceStep's text node stores tags as a single-line string where real line breaks
are encoded. When you write tags through `--tags "..."`:

- Prefer a **single line** with commas/spaces separating descriptors.
- If you must include newlines, ComfyUI-escape them (`\\t` for tab, `\\n` for
  newline) — but keep line breaks to a minimum.
- The script passes the `--tags` string through as-is, so you control the
  escaping; avoid surprises by defaulting to one line.

## Lyrics (if using vocals)

- Structure them with section headers: `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Outro]`.
- Match the language to `--language` (default `en`).
- Keep length reasonable for the requested `--duration` — a 20-second clip with
  a full verse won't render cleanly; a short hook or instrumental intro will.
- The image-first mode (see image-first.md) can derive lyrics from a reference
  image's mood/content — keep them concise and on-theme.

## Image → tags

When there is no explicit `--tags`/`--lyrics` but there is an image, derive a
coherent set of tags from the image (see references/image-first.md), then pass
them through `--tags`.
