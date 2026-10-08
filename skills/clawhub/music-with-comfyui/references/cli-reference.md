# CLI Usage Reference (music-with-comfyui)

Full command examples for the `music` subcommand. The SKILL.md procedure only
lists the core rule; open this file for the exact flags.

> **⚠️ The music description is MANDATORY and must be passed via `--tags` (or `--prompt`) — never as a positional argument.**
>
> `python3 music_with_comfyui.py music "lo-fi track"` → `music: error: the following arguments are required: --tags`
>
> Always write the description through `--tags "..."` on the first attempt. A positional word wastes a whole turn before the command reaches ComfyUI.

### Music (Text → Music, AceStep 1.5)

```bash
# Instrumental from a style description (default: 120s, config params)
python3 music_with_comfyui.py music --tags "Lo-fi hip hop, 80 BPM, warm, chill, rainy vibe"

# With explicit length
python3 music_with_comfyui.py music \
  --tags "Epic cinematic orchestral, building drums, brass stabs, hopeful" \
  --duration 90

# With lyrics (structured Sonic-lyrics). Instrumental if omitted.
python3 music_with_comfyui.py music \
  --tags "Indie pop, 104 BPM, bright, jangy guitars, upbeat" \
  --lyrics "[Verse 1]\nWalking down the boulevard\n..." \
  --language en

# Force a genre / key / time signature
python3 music_with_comfyui.py music \
  --tags "80s synthwave, neon, driving, arpeggiated bass" \
  --bpm 118 --keyscale "A minor" --timesignature 4 --language en

# Fixed seed (reproducible)
python3 music_with_comfyui.py music \
  --tags "Ambient pad, slow, meditative, soft textures" \
  --seed 42

# Sampling / quality overrides
python3 music_with_comfyui.py music \
  --tags "Jazz piano trio, smoky, intimate" \
  --cfg-scale 1.5 --temperature 0.9 --top-p 0.85

# Image-first mode: send the image and let the agent derive tags/lyrics.
# There is NO --tags-image flag — the agent visual-reads the image and fills
# the tags itself.
# python3 music_with_comfyui.py music --tags "..."  # agent auto-fills from image

# JPG-style format / output dir (the server decides the codec)
python3 music_with_comfyui.py music --tags "..." --output-dir /custom/out

# Health check
python3 music_with_comfyui.py test
```

### Notes on the flags

- `--tags` / `--prompt` — the music description (genre + tempo + instrumentation + mood + vocals). **Required.**
- `--lyrics` — Sonic-lyrics text. Omit or leave empty for instrumental.
- `--duration` — seconds. Also set on the audio latent; keep consistent with `--tags`.
- `--seed` — **not sent by default.** Omit it for a random run; pass a number only to reproduce a specific output.
- `--bpm`, `--keyscale`, `--language`, `--timesignature` — style metadata.
- `--cfg-scale`, `--temperature`, `--top-p`, `--top-k`, `--min-p` — sampling params (default from `config.json` → `music.default_params`).
- `--output-dir` — client-side output directory override.

### Output filename scheme

Generated files use a short mode prefix + timestamp (`YYYYMMDD_HHMMSS`) +
ComfyUI's counter, e.g. `amusic_20261006_153000_00001.mp3` (the actual extension
depends on the server's `SaveAudioAdvanced` node). See
[references/delivery.md](references/delivery.md) for how to deliver it.

### Timeout Reference

| Mode | Timeout |
|---|---|
| Music (AceStep 1.5, per config `music.default_params.duration`) | 600s (see `config.json`) |

The server-side generation time scales with the requested `duration`. Short
tracks finish in a fraction of the timeout; long tracks use more of it. The
`timeout_seconds` in `config.json` is the safety ceiling — set it generously
enough for the longest track you expect.
