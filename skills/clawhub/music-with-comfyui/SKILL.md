---
name: music-with-comfyui
description: 'Use to generate music and audio through a user-defined ComfyUI server (COMFYUI_URL env var or comfyui_url in config.json; if no server is reachable the script exits with configuration instructions) — trigger with requests like "make me a song", "make up a song", "compose", "write a song", "compose a track", "arrange a song", "编一个歌", "写歌", "作曲", "编个曲", "做首歌", or any similar instruction to write/compose/arrange a song or melody (in any language). **Important disambiguation: in Chinese, "写歌" / "写一个歌" / "来个歌" here means *generate an actual audio song through ComfyUI* (AceStep 1.5 → MP3), NOT merely writing lyrics text.** If you only want lyrics written down (words, no audio), that is plain text writing and NOT this skill. Not for simple audio file conversion, volume adjustment, or transcribing/normalizing an existing audio file (that is plain audio processing, not generation). The model is **AceStep Audio 1.5** — it turns a music-description (style/genre tags) plus optional lyrics into a generated MP3. You may specify any of theme, music length, style, lyrics — one or more; if the user gives an image, the style and/or lyrics can be derived from it.'
version: "0.3.1"
license: BSD-3-Clause
compatibility: 'ComfyUI with the AceStep 1.5 audio nodes installed; requires python3; the endpoint is user-defined (COMFYUI_URL or config.json) — point it at a server you control and trust.'
allowed-tools: Read, Write, Edit, Exec
metadata:
  openclaw:
    emoji: "🎵"
    requires:
      anyBins: ["python3"]
    config:
      path: "config.json"
---

# Music with ComfyUI

Call a user-defined ComfyUI server (local or remote) to generate **music / audio** with **AceStep Audio 1.5** (text + optional lyrics → MP3). The user may specify any of **theme, music length, style, and lyrics** (one or more). If no style or lyrics are given explicitly, the agent derives them from the user's request — and from any image the user provides (see [Image → Music](#image--music-deriving-style-and-lyrics)).

- **T2M (Text → Music)** → **AceStep Audio 1.5** (the only model here). A music description (style/genre tags) plus optional lyrics → an MP3.

The workflow expects several model files on the server (see [Models](#models-and-custom-nodes) and [`MODEL_URL.txt`](MODEL_URL.txt)):

- Diffusion model: `acestep_v1.5_xl_turbo_bf16.safetensors`
- CLIP (dual): `qwen_0.6b_ace15.safetensors` + `qwen_4b_ace15.safetensors`
- VAE: `ace_1.5_vae.safetensors`

`config.json` at the skill root holds every default; any value can be overridden by an env var (see the Data & Privacy table there).

## Image → Music — Deriving Style and Lyrics

The **agent** reads the image; the workflow reads **only text**. AceStep 1.5's
graph has no image input — the sole text node is `TextEncodeAceStepAudio1.5`
(tags + lyrics). When the user sends an image and does **not** also specify a
full style prompt and/or lyrics, let the **agent** derive the tags and lyrics,
then hand only that text to the script:

- Use the image to infer a suitable **style / mood / genre** for `--tags` (and, if the song has words, draft **lyrics** in the right `--language`).
- Pass the user's theme/genre on top of what the image implies; never fabricate constraints the user didn't ask for.
- **No image is ever uploaded.** The reference image is used for **vibe extraction only** — it is never uploaded to, or sent to, any external destination.

If the user *does* give explicit style and/or lyrics, honour those first and use the image only as a mood reference.

When to use this section:
- Image arrives → follow the rules in [references/image-first.md](references/image-first.md)
- User explicitly asks for a style/genre, or writes lyrics → use them verbatim (cleaned up as needed)

## When to Use (Recognizing the Request)

This skill fires whenever the user asks to **write, compose, arrange, or make a song / melody / music track**, in any language — even if no genre or length is given. Common trigger phrases include, but are not limited to:

- **English:** "make me a song", "make up a song", "compose", "compose a song/track", "write a song", "arrange a song", "write some music", "make a melody", "produce a track", "write me a tune"
- **中文:** "写歌", "作曲", "编一首歌", "编一个歌", "编个曲", "编曲", "做首歌", "帮写首歌", "生成一首歌", "来首原创"
- **其他语言:** Japanese (曲を作る、歌を歌う、作曲する), Korean (곡 만들기, 작곡), Spanish (hacer una canción, componer, escribir una canción), etc.

The signal is the *intent to create new music* (write / compose / arrange / make / generate a song/melody/track). Match it loosely across languages; if the intent is clearly "create a new song", use this skill.

- Generate music from a description / theme → **music** (`--tags`)
- The user sends an image, then asks for a song (within reason) → **image-first mode**, see [references/image-first.md](references/image-first.md)

### When NOT to use this skill

This skill is for **generation**, not post-processing of existing audio. Do **not** use it (and do not look here) for:

- Converting / transcribing / resampling / normalizing an audio file the user already has (that is plain audio processing — use an audio tool).
- Adjusting volume, trimming, splicing, or remixing an existing file.
- Adding lyrics/subtitles to a pre-existing recording (unless the user wants a *new* song sung).

## Data & Privacy (read before running)

- **What is transmitted:** the music tags/lyrics and the workflow JSON go to the configured endpoint for **every** run. No image is ever sent — AceStep 1.5 has no image input; if the user provides one, the agent visual-reads it and turns it into tags/lyrics before calling the script.
- **Endpoint** is user-defined (`COMFYUI_URL` env var > `comfyui_url` in `config.json`; bundled default `http://127.0.0.1:8188`). A non-local host prints a data-flow warning on every run; if no server answers, the script exits with configuration instructions instead of a raw timeout.
- **Written to disk:** generated audio is saved under `output_dir` (`config.json` or `COMFYUI_OUTPUT_DIR`). Don't submit sensitive content if the endpoint or disk is a concern.
- **Secrets:** never put credentials in the URL or logs.

## Workflow Files

| Mode | Workflow | File |
|---|---|---|
| Music (AceStep 1.5) | AceStep Audio 1.5 (text/lyrics → audio) | `workflows/acestep_audio_api.json` |

The workflow is an **adapted** version of a real ComfyUI graph. Original source + exactly what was changed → [references/attribution.md](references/attribution.md).

## CLI Usage

> **⚠️ The music description is MANDATORY and must be passed via `--tags` (or `--prompt`) — never as a positional word.**
>
> `python3 music_with_comfyui.py music "lo-fi track"` → `music: error: the following arguments are required: --tags`
>
> Always write the description through `--tags "..."` on the **first** attempt. A positional word wastes a whole turn before the command ever reaches ComfyUI.

Full commands and the timeout table → [references/cli-reference.md](references/cli-reference.md)

### What each knob controls

- **`--tags`** *(required)* — the music description: genre, tempo, instrumentation, mood, vocal style. This is the primary prompt. ComfyUI-escaped (line breaks as `\t`/`\n`); keep it clean.
- **`--lyrics`** *(optional)* — structured Sonic-lyrics text. Omit (or pass empty) for an instrumental; AceStep 1.5 generates instrumental audio.
- **`--duration`** *(optional)* — seconds (default: config `default_duration`, 120). The audio latent's `seconds` is set to match, so keep them consistent.
- **`--seed`** *(optional)* — **not sent by default.** If omitted, the script uses no seed (random per run). Pass `--seed <n>` only to lock/reproduce a specific output.
- **Style/tuning flags** (`--bpm`, `--keyscale`, `--language`, `--timesignature`, `--cfg-scale`, `--temperature`, `--top-p`, `--top-k`, `--min-p`) — optional overrides of the defaults in `config.json` `music.default_params`; each omits cleanly if unset.
- **`--tags-image`** *(removed)* — AceStep 1.5 takes no image. If the user gives a reference image, the agent reads it and derives tags/lyrics itself (see [Image → Music](#image--music-deriving-style-and-lyrics)).
- **`--format` / `--output-dir`** — output format (jpg/png for the image skill; here audio format is whatever the server's `SaveAudioAdvanced` writes).

## Prompt / Tags Formatting

Guidance for crafting AceStep prompts lives in [references/prompts.md](references/prompts.md). Key points:

- Write **`--tags`** as a comma/space-separated description of **genre, tempo, instrumentation, mood, and vocal style**. Keep it clean and natural.
- ComfyUI-escape any line breaks in the description: `\\t` (tab) / `\\n` (newline). If you write the tags through `--tags "..."` the script passes the string through, so keep line breaks to a minimum or escape them.
- **Lyrics**, if any, should be structured (sections like `[Verse 1]`, `[Chorus]`, ...). Keep to the language set via `--language`.
- If the agent picks the style itself, it should still produce a concise, coherent tag line — not a wall of contradictory keywords.

## Error Handling

The script auto-detects the same categories as the image skill and reports them with install/source guidance (see [references/error-handling.md](references/error-handling.md)):

1. **Missing nodes** — reports which node, its package, and a pinned GitHub install hint (the script never runs `git clone` itself).
2. **Missing models** — reports the missing model file(s); the AceStep workflow has no blind model substitution (there is only one model), so it aborts with the install hint instead of degrading.
3. **Non-critical utility nodes** (e.g. `UnloadAllModels`) — bypassed automatically without interrupting generation.

## Output Delivery

**Send the generated file — do not just describe it.** Deliver in the **user's original session**, never raw paths/URLs. Per-channel prefixes and the staging/cleanup routine → [references/delivery.md](references/delivery.md)

- Generated audio is saved under `output_dir/music/` (prefix `amusic_<timestamp>`, e.g. `amusic_20261006_153000.mp3`).
- **Attach the file** — send it as an audio attachment in the user's session (e.g. a `MEDIA:` line for WhatsApp, a native attachment elsewhere). Do not send the raw file path to the group unless asked.
- **WhatsApp → transcode to 44.1kHz. Always.** AceStep 1.5 writes 48 kHz MP3, which does not play on WhatsApp. Before delivering on WhatsApp, transcode to 44.1 kHz with ffmpeg first:
  `ffmpeg -y -i <src> -c:a aac -b:a 128k -ar 44100 -ac 1 -movflags +faststart <out>.m4a`
  then send the `.m4a` via `MEDIA:` as a plain line. (mp3 also works if 44.1 kHz; 44.1 kHz is the key.)
- **Explicit original-request:** if the user asks for the original/unmodified file, do NOT transcode. Instead package the original audio as a `.zip` (e.g. `zip -j out/<name>.zip <src>.mp3`) and send the zip as a document attachment (`MEDIA:<path>.zip`, or `message(action="send", channel=..., asDocument=true, media=<path>.zip)`).
- Never send raw local file paths, ComfyUI URLs, or host info unless asked.

### Delivering the Result — Title + Lyrics

A generated song is not just an audio clip: hand it over as a complete package, and do it all in one message.

- **Song title.** If the user did not request a specific title, give the song one. Derive it from the track's mood, the `--tags`, and the lyrics — keep it short and evocative. State it clearly as the song's name.
- **Lyrics.** If the song has lyrics, return them to the user, **cleanly formatted** (each section on its own line, section headers such as `[Verse]` / `[Chorus]` intact, no stray control characters or unescaped line breaks).
- **The audio file**, attached in the user's session (channel prefixes in [references/delivery.md](references/delivery.md)).

Deliver all three together — title, lyrics, and audio — not in separate hand-offs:

```
🎵  **<Song Title>**
<style note — one line>

[Verse 1]
...

[Chorus]
...

MEDIA:/…/amusic_<timestamp>.mp3
```

Never omit the title or the lyrics: a finished song should arrive with its name and, when it has words, its lyrics, in the same message as the audio. If the user supplied a title, use theirs; if the song is instrumental, skip the lyrics but still give it a title.

## Execution Discipline — Fast Path

The measured GPU sampling time is model-dependent (short, looped clips are fast; long durations cost seconds-to-tens-of-seconds of sampling). When a run stretches well beyond the configured `timeout_seconds`, the delay is almost always **agent-side overhead** before the run, not inference. Kill the waste:

1. **Skip re-reads on repeat.** For a known config / repeat / same-job, the defaults are already baked in — no need to re-open `SKILL.md`, `config.json`, or the script.
2. **At most one pre-check merge.** Gather any needed info (requested style/lyrics) in a single batched command, or skip it for a trivial repeat.
3. **Run immediately after one check.** Don't inspect, second-guess, or add tool calls between knowing the tags and running.
4. **Verify only the minimum.** After the run, check only what the user asked (duration / format / file exists).
5. **Golden rule:** sampling is bounded by `timeout_seconds` in config; anything past that is overhead. Never pile on tool calls before the audio exists.

## References (index)

- [references/image-first.md](references/image-first.md) — image-then-music detection rules
- [references/attribution.md](references/attribution.md) — original source + modifications per workflow
- [references/cli-reference.md](references/cli-reference.md) — full commands + timeout reference
- [references/prompts.md](references/prompts.md) — per-model prompt / tags guidance
- [references/error-handling.md](references/error-handling.md) — auto-handled error categories
- [references/delivery.md](references/delivery.md) — per-channel delivery + staging
